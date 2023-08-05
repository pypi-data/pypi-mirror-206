"""_834.py

GearFilletNodeStressResultsRow
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _832
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_FILLET_NODE_STRESS_RESULTS_ROW = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearFilletNodeStressResultsRow')


__docformat__ = 'restructuredtext en'
__all__ = ('GearFilletNodeStressResultsRow',)


class GearFilletNodeStressResultsRow(_0.APIBase):
    """GearFilletNodeStressResultsRow

    This is a mastapy class.
    """

    TYPE = _GEAR_FILLET_NODE_STRESS_RESULTS_ROW

    class _Cast_GearFilletNodeStressResultsRow:
        """Special nested class for casting GearFilletNodeStressResultsRow to subclasses."""

        def __init__(self, parent: 'GearFilletNodeStressResultsRow'):
            self._parent = parent

        @property
        def cylindrical_gear_fillet_node_stress_results_row(self):
            from mastapy.gears.ltca import _825
            
            return self._parent._cast(_825.CylindricalGearFilletNodeStressResultsRow)

        @property
        def gear_fillet_node_stress_results_row(self) -> 'GearFilletNodeStressResultsRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearFilletNodeStressResultsRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fillet_row_index(self) -> 'int':
        """int: 'FilletRowIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilletRowIndex

        if temp is None:
            return 0

        return temp

    @property
    def node_results(self) -> 'List[_832.GearFilletNodeStressResults]':
        """List[GearFilletNodeStressResults]: 'NodeResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearFilletNodeStressResultsRow._Cast_GearFilletNodeStressResultsRow':
        return self._Cast_GearFilletNodeStressResultsRow(self)
