"""_846.py

CylindricalGearBendingStiffness
"""
from mastapy.gears.ltca import _828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BENDING_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearBendingStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearBendingStiffness',)


class CylindricalGearBendingStiffness(_828.GearBendingStiffness):
    """CylindricalGearBendingStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BENDING_STIFFNESS

    class _Cast_CylindricalGearBendingStiffness:
        """Special nested class for casting CylindricalGearBendingStiffness to subclasses."""

        def __init__(self, parent: 'CylindricalGearBendingStiffness'):
            self._parent = parent

        @property
        def gear_bending_stiffness(self):
            return self._parent._cast(_828.GearBendingStiffness)

        @property
        def gear_stiffness(self):
            from mastapy.gears.ltca import _842
            
            return self._parent._cast(_842.GearStiffness)

        @property
        def fe_stiffness(self):
            from mastapy.nodal_analysis import _66
            
            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_bending_stiffness(self) -> 'CylindricalGearBendingStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearBendingStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness':
        return self._Cast_CylindricalGearBendingStiffness(self)
