"""_830.py

GearContactStiffness
"""
from mastapy.gears.ltca import _842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CONTACT_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearContactStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GearContactStiffness',)


class GearContactStiffness(_842.GearStiffness):
    """GearContactStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_CONTACT_STIFFNESS

    class _Cast_GearContactStiffness:
        """Special nested class for casting GearContactStiffness to subclasses."""

        def __init__(self, parent: 'GearContactStiffness'):
            self._parent = parent

        @property
        def gear_stiffness(self):
            return self._parent._cast(_842.GearStiffness)

        @property
        def fe_stiffness(self):
            from mastapy.nodal_analysis import _66
            
            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_contact_stiffness(self):
            from mastapy.gears.ltca.cylindrical import _848
            
            return self._parent._cast(_848.CylindricalGearContactStiffness)

        @property
        def conical_gear_contact_stiffness(self):
            from mastapy.gears.ltca.conical import _860
            
            return self._parent._cast(_860.ConicalGearContactStiffness)

        @property
        def gear_contact_stiffness(self) -> 'GearContactStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearContactStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearContactStiffness._Cast_GearContactStiffness':
        return self._Cast_GearContactStiffness(self)
