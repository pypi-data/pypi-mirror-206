"""_799.py

PinionConicalMachineSettingsSpecified
"""
from mastapy.gears.manufacturing.bevel import _801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_CONICAL_MACHINE_SETTINGS_SPECIFIED = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionConicalMachineSettingsSpecified')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionConicalMachineSettingsSpecified',)


class PinionConicalMachineSettingsSpecified(_801.PinionFinishMachineSettings):
    """PinionConicalMachineSettingsSpecified

    This is a mastapy class.
    """

    TYPE = _PINION_CONICAL_MACHINE_SETTINGS_SPECIFIED

    class _Cast_PinionConicalMachineSettingsSpecified:
        """Special nested class for casting PinionConicalMachineSettingsSpecified to subclasses."""

        def __init__(self, parent: 'PinionConicalMachineSettingsSpecified'):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(self):
            return self._parent._cast(_801.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(self):
            from mastapy.gears import _316
            
            return self._parent._cast(_316.ConicalGearToothSurface)

        @property
        def pinion_conical_machine_settings_specified(self) -> 'PinionConicalMachineSettingsSpecified':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionConicalMachineSettingsSpecified.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PinionConicalMachineSettingsSpecified._Cast_PinionConicalMachineSettingsSpecified':
        return self._Cast_PinionConicalMachineSettingsSpecified(self)
