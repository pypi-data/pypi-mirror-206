"""_2672.py

BearingDynamicElementContactPropertyWrapper
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2675
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_ELEMENT_CONTACT_PROPERTY_WRAPPER = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingDynamicElementContactPropertyWrapper')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDynamicElementContactPropertyWrapper',)


class BearingDynamicElementContactPropertyWrapper(_0.APIBase):
    """BearingDynamicElementContactPropertyWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_ELEMENT_CONTACT_PROPERTY_WRAPPER

    class _Cast_BearingDynamicElementContactPropertyWrapper:
        """Special nested class for casting BearingDynamicElementContactPropertyWrapper to subclasses."""

        def __init__(self, parent: 'BearingDynamicElementContactPropertyWrapper'):
            self._parent = parent

        @property
        def bearing_dynamic_element_contact_property_wrapper(self) -> 'BearingDynamicElementContactPropertyWrapper':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDynamicElementContactPropertyWrapper.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def contact_results(self) -> 'List[_2675.BearingDynamicResultsPropertyWrapper]':
        """List[BearingDynamicResultsPropertyWrapper]: 'ContactResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BearingDynamicElementContactPropertyWrapper._Cast_BearingDynamicElementContactPropertyWrapper':
        return self._Cast_BearingDynamicElementContactPropertyWrapper(self)
