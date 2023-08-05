"""_848.py

CylindricalGearContactStiffness
"""
from mastapy.gears.ltca import _830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_CONTACT_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearContactStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearContactStiffness',)


class CylindricalGearContactStiffness(_830.GearContactStiffness):
    """CylindricalGearContactStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_CONTACT_STIFFNESS

    class _Cast_CylindricalGearContactStiffness:
        """Special nested class for casting CylindricalGearContactStiffness to subclasses."""

        def __init__(self, parent: 'CylindricalGearContactStiffness'):
            self._parent = parent

        @property
        def gear_contact_stiffness(self):
            return self._parent._cast(_830.GearContactStiffness)

        @property
        def gear_stiffness(self):
            from mastapy.gears.ltca import _842
            
            return self._parent._cast(_842.GearStiffness)

        @property
        def fe_stiffness(self):
            from mastapy.nodal_analysis import _66
            
            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_contact_stiffness(self) -> 'CylindricalGearContactStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearContactStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness':
        return self._Cast_CylindricalGearContactStiffness(self)
