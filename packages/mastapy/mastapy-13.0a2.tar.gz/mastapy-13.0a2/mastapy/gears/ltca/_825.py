"""_825.py

CylindricalGearFilletNodeStressResultsRow
"""
from mastapy._internal import constructor
from mastapy.gears.ltca import _834
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_ROW = python_net_import('SMT.MastaAPI.Gears.LTCA', 'CylindricalGearFilletNodeStressResultsRow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFilletNodeStressResultsRow',)


class CylindricalGearFilletNodeStressResultsRow(_834.GearFilletNodeStressResultsRow):
    """CylindricalGearFilletNodeStressResultsRow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_ROW

    class _Cast_CylindricalGearFilletNodeStressResultsRow:
        """Special nested class for casting CylindricalGearFilletNodeStressResultsRow to subclasses."""

        def __init__(self, parent: 'CylindricalGearFilletNodeStressResultsRow'):
            self._parent = parent

        @property
        def gear_fillet_node_stress_results_row(self):
            return self._parent._cast(_834.GearFilletNodeStressResultsRow)

        @property
        def cylindrical_gear_fillet_node_stress_results_row(self) -> 'CylindricalGearFilletNodeStressResultsRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFilletNodeStressResultsRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self) -> 'float':
        """float: 'Diameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_along_fillet(self) -> 'float':
        """float: 'DistanceAlongFillet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceAlongFillet

        if temp is None:
            return 0.0

        return temp

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'CylindricalGearFilletNodeStressResultsRow._Cast_CylindricalGearFilletNodeStressResultsRow':
        return self._Cast_CylindricalGearFilletNodeStressResultsRow(self)
