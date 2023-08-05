"""_842.py

GearStiffness
"""
from mastapy.nodal_analysis import _66
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GearStiffness',)


class GearStiffness(_66.FEStiffness):
    """GearStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_STIFFNESS

    class _Cast_GearStiffness:
        """Special nested class for casting GearStiffness to subclasses."""

        def __init__(self, parent: 'GearStiffness'):
            self._parent = parent

        @property
        def fe_stiffness(self):
            return self._parent._cast(_66.FEStiffness)

        @property
        def gear_bending_stiffness(self):
            from mastapy.gears.ltca import _828
            
            return self._parent._cast(_828.GearBendingStiffness)

        @property
        def gear_contact_stiffness(self):
            from mastapy.gears.ltca import _830
            
            return self._parent._cast(_830.GearContactStiffness)

        @property
        def cylindrical_gear_bending_stiffness(self):
            from mastapy.gears.ltca.cylindrical import _846
            
            return self._parent._cast(_846.CylindricalGearBendingStiffness)

        @property
        def cylindrical_gear_contact_stiffness(self):
            from mastapy.gears.ltca.cylindrical import _848
            
            return self._parent._cast(_848.CylindricalGearContactStiffness)

        @property
        def conical_gear_bending_stiffness(self):
            from mastapy.gears.ltca.conical import _858
            
            return self._parent._cast(_858.ConicalGearBendingStiffness)

        @property
        def conical_gear_contact_stiffness(self):
            from mastapy.gears.ltca.conical import _860
            
            return self._parent._cast(_860.ConicalGearContactStiffness)

        @property
        def gear_stiffness(self) -> 'GearStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearStiffness._Cast_GearStiffness':
        return self._Cast_GearStiffness(self)
