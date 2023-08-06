# This file is part of pipe_base.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import annotations

__all__ = ["InMemoryDatasetHandle"]

import dataclasses
from typing import Any, Optional

from frozendict import frozendict
from lsst.daf.butler import DataCoordinate, DimensionUniverse, StorageClass, StorageClassFactory


# Use an empty dataID as a default.
def _default_dataId() -> DataCoordinate:
    return DataCoordinate.makeEmpty(DimensionUniverse())


@dataclasses.dataclass(frozen=True, init=False)
class InMemoryDatasetHandle:
    """An in-memory version of a `~lsst.daf.butler.DeferredDatasetHandle`.

    If ``dataId`` is not specified, a default empty dataId will be constructed.
    If ``kwargs`` are provided without specifying a ``dataId``, those
    parameters will be converted into a dataId-like entity.
    """

    def __init__(
        self,
        inMemoryDataset: Any,
        *,
        storageClass: StorageClass | None = None,
        parameters: dict[str, Any] | None = None,
        dataId: dict[str, Any] | DataCoordinate | None = None,
        **kwargs: Any,
    ):
        object.__setattr__(self, "inMemoryDataset", inMemoryDataset)
        object.__setattr__(self, "storageClass", storageClass)
        object.__setattr__(self, "parameters", parameters)
        # Need to be able to construct a dataId from kwargs for convenience.
        # This will not be a full DataCoordinate.
        if dataId is None:
            if kwargs:
                dataId = frozendict(kwargs)  # type: ignore
            else:
                dataId = DataCoordinate.makeEmpty(DimensionUniverse())
        elif kwargs:
            if isinstance(dataId, DataCoordinate):
                dataId = DataCoordinate.standardize(kwargs, defaults=dataId, universe=dataId.universe)
            else:
                new = dict(dataId)
                new.update(kwargs)
                dataId = frozendict(new)  # type: ignore
        object.__setattr__(self, "dataId", dataId)

    def get(
        self,
        *,
        component: Optional[str] = None,
        parameters: Optional[dict] = None,
        storageClass: str | StorageClass | None = None,
    ) -> Any:
        """Retrieves the dataset pointed to by this handle

        This handle may be used multiple times, possibly with different
        parameters.

        Parameters
        ----------
        component : `str` or None
            If the deferred object is a component dataset type, this parameter
            may specify the name of the component to use in the get operation.
        parameters : `dict` or None
            The parameters argument will be passed to the butler get method.
            It defaults to None. If the value is not None, this dict will
            be merged with the parameters dict used to construct the
            `DeferredDatasetHandle` class.
        storageClass : `StorageClass` or `str`, optional
            The storage class to be used to override the Python type
            returned by this method. By default the returned type matches
            the type stored. Specifying a read `StorageClass` can force a
            different type to be returned.
            This type must be compatible with the original type.

        Returns
        -------
        return : `object`
            The dataset pointed to by this handle. This is the actual object
            that was initially stored and not a copy. Modifying this object
            will modify the stored object. If the stored object is `None` this
            method always returns `None` regardless of any component request or
            parameters.

        Raises
        ------
        KeyError
            Raised if a component or parameters are used but no storage
            class can be found.
        """
        if self.inMemoryDataset is None:
            return None

        if self.parameters is not None:
            mergedParameters = self.parameters.copy()
            if parameters is not None:
                mergedParameters.update(parameters)
        elif parameters is not None:
            mergedParameters = parameters
        else:
            mergedParameters = {}

        returnStorageClass: StorageClass | None = None
        if storageClass:
            if isinstance(storageClass, str):
                factory = StorageClassFactory()
                returnStorageClass = factory.getStorageClass(storageClass)
            else:
                returnStorageClass = storageClass

        if component or mergedParameters:
            # This requires a storage class look up to locate the delegate
            # class.
            thisStorageClass = self._getStorageClass()
            inMemoryDataset = self.inMemoryDataset

            # Parameters for derived components are applied against the
            # composite.
            if component in thisStorageClass.derivedComponents:
                thisStorageClass.validateParameters(parameters)

                # Process the parameters (hoping this never modified the
                # original object).
                inMemoryDataset = thisStorageClass.delegate().handleParameters(
                    inMemoryDataset, mergedParameters
                )
                mergedParameters = {}  # They have now been used

                readStorageClass = thisStorageClass.derivedComponents[component]
            else:
                if component:
                    readStorageClass = thisStorageClass.components[component]
                else:
                    readStorageClass = thisStorageClass
                readStorageClass.validateParameters(mergedParameters)

            if component:
                inMemoryDataset = thisStorageClass.delegate().getComponent(inMemoryDataset, component)

            if mergedParameters:
                inMemoryDataset = readStorageClass.delegate().handleParameters(
                    inMemoryDataset, mergedParameters
                )
            if returnStorageClass:
                return returnStorageClass.coerce_type(inMemoryDataset)
            return inMemoryDataset
        else:
            # If there are no parameters or component requests the object
            # can be returned as is, but possibly with conversion.
            if returnStorageClass:
                return returnStorageClass.coerce_type(self.inMemoryDataset)
            return self.inMemoryDataset

    def _getStorageClass(self) -> StorageClass:
        """Return the relevant storage class.

        Returns
        -------
        storageClass : `StorageClass`
            The storage class associated with this handle, or one derived
            from the python type of the stored object.

        Raises
        ------
        KeyError
            Raised if the storage class could not be found.
        """
        factory = StorageClassFactory()
        if self.storageClass:
            return factory.getStorageClass(self.storageClass)

        # Need to match python type.
        pytype = type(self.inMemoryDataset)
        return factory.findStorageClass(pytype)

    inMemoryDataset: Any
    """The object to store in this dataset handle for later retrieval.
    """

    dataId: DataCoordinate | frozendict
    """The `~lsst.daf.butler.DataCoordinate` associated with this dataset
    handle.
    """

    storageClass: Optional[str] = None
    """The name of the `~lsst.daf.butler.StorageClass` associated with this
    dataset.

    If `None`, the storage class will be looked up from the factory.
    """

    parameters: Optional[dict] = None
    """Optional parameters that may be used to specify a subset of the dataset
    to be loaded (`dict` or `None`).
    """
