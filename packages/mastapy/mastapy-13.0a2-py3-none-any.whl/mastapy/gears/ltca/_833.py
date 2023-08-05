"""_833.py

GearFilletNodeStressResultsColumn
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _832
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearFilletNodeStressResultsColumn')


__docformat__ = 'restructuredtext en'
__all__ = ('GearFilletNodeStressResultsColumn',)


class GearFilletNodeStressResultsColumn(_0.APIBase):
    """GearFilletNodeStressResultsColumn

    This is a mastapy class.
    """

    TYPE = _GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN

    class _Cast_GearFilletNodeStressResultsColumn:
        """Special nested class for casting GearFilletNodeStressResultsColumn to subclasses."""

        def __init__(self, parent: 'GearFilletNodeStressResultsColumn'):
            self._parent = parent

        @property
        def cylindrical_gear_fillet_node_stress_results_column(self):
            from mastapy.gears.ltca import _824
            
            return self._parent._cast(_824.CylindricalGearFilletNodeStressResultsColumn)

        @property
        def gear_fillet_node_stress_results_column(self) -> 'GearFilletNodeStressResultsColumn':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearFilletNodeStressResultsColumn.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fillet_column_index(self) -> 'int':
        """int: 'FilletColumnIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilletColumnIndex

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
    def cast_to(self) -> 'GearFilletNodeStressResultsColumn._Cast_GearFilletNodeStressResultsColumn':
        return self._Cast_GearFilletNodeStressResultsColumn(self)
