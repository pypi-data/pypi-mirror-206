"""_5814.py

ExcitationSourceSelectionGroup
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5813
from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1517
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCITATION_SOURCE_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results', 'ExcitationSourceSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ExcitationSourceSelectionGroup',)


class ExcitationSourceSelectionGroup(_5813.ExcitationSourceSelectionBase):
    """ExcitationSourceSelectionGroup

    This is a mastapy class.
    """

    TYPE = _EXCITATION_SOURCE_SELECTION_GROUP

    class _Cast_ExcitationSourceSelectionGroup:
        """Special nested class for casting ExcitationSourceSelectionGroup to subclasses."""

        def __init__(self, parent: 'ExcitationSourceSelectionGroup'):
            self._parent = parent

        @property
        def excitation_source_selection_base(self):
            return self._parent._cast(_5813.ExcitationSourceSelectionBase)

        @property
        def excitation_source_selection_group(self) -> 'ExcitationSourceSelectionGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExcitationSourceSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def sub_items(self) -> 'List[_5813.ExcitationSourceSelectionBase]':
        """List[ExcitationSourceSelectionBase]: 'SubItems' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SubItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def selection_as_xml_string(self) -> 'str':
        """str: 'SelectionAsXmlString' is the original name of this property."""

        temp = self.wrapped.SelectionAsXmlString

        if temp is None:
            return ''

        return temp

    @selection_as_xml_string.setter
    def selection_as_xml_string(self, value: 'str'):
        self.wrapped.SelectionAsXmlString = str(value) if value else ''

    def include_only_harmonics_with_order(self, order: '_1517.RoundedOrder'):
        """ 'IncludeOnlyHarmonicsWithOrder' is the original name of this method.

        Args:
            order (mastapy.math_utility.RoundedOrder)
        """

        self.wrapped.IncludeOnlyHarmonicsWithOrder(order.wrapped if order else None)

    @property
    def cast_to(self) -> 'ExcitationSourceSelectionGroup._Cast_ExcitationSourceSelectionGroup':
        return self._Cast_ExcitationSourceSelectionGroup(self)
