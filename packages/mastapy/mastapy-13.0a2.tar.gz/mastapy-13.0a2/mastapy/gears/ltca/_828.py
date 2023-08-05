"""_828.py

GearBendingStiffness
"""
from mastapy.gears.ltca import _842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_BENDING_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearBendingStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GearBendingStiffness',)


class GearBendingStiffness(_842.GearStiffness):
    """GearBendingStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_BENDING_STIFFNESS

    class _Cast_GearBendingStiffness:
        """Special nested class for casting GearBendingStiffness to subclasses."""

        def __init__(self, parent: 'GearBendingStiffness'):
            self._parent = parent

        @property
        def gear_stiffness(self):
            return self._parent._cast(_842.GearStiffness)

        @property
        def fe_stiffness(self):
            from mastapy.nodal_analysis import _66
            
            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_bending_stiffness(self):
            from mastapy.gears.ltca.cylindrical import _846
            
            return self._parent._cast(_846.CylindricalGearBendingStiffness)

        @property
        def conical_gear_bending_stiffness(self):
            from mastapy.gears.ltca.conical import _858
            
            return self._parent._cast(_858.ConicalGearBendingStiffness)

        @property
        def gear_bending_stiffness(self) -> 'GearBendingStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearBendingStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearBendingStiffness._Cast_GearBendingStiffness':
        return self._Cast_GearBendingStiffness(self)
