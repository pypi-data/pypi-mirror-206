"""_850.py

CylindricalGearFESettings
"""
from mastapy.utility import _1583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FE_SETTINGS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearFESettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFESettings',)


class CylindricalGearFESettings(_1583.PerMachineSettings):
    """CylindricalGearFESettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FE_SETTINGS

    class _Cast_CylindricalGearFESettings:
        """Special nested class for casting CylindricalGearFESettings to subclasses."""

        def __init__(self, parent: 'CylindricalGearFESettings'):
            self._parent = parent

        @property
        def per_machine_settings(self):
            return self._parent._cast(_1583.PerMachineSettings)

        @property
        def persistent_singleton(self):
            from mastapy.utility import _1584
            
            return self._parent._cast(_1584.PersistentSingleton)

        @property
        def cylindrical_gear_fe_settings(self) -> 'CylindricalGearFESettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFESettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearFESettings._Cast_CylindricalGearFESettings':
        return self._Cast_CylindricalGearFESettings(self)
