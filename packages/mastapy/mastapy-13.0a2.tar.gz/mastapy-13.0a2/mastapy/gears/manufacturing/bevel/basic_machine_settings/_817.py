"""_817.py

BasicConicalGearMachineSettingsFormate
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASIC_CONICAL_GEAR_MACHINE_SETTINGS_FORMATE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.BasicMachineSettings', 'BasicConicalGearMachineSettingsFormate')


__docformat__ = 'restructuredtext en'
__all__ = ('BasicConicalGearMachineSettingsFormate',)


class BasicConicalGearMachineSettingsFormate(_816.BasicConicalGearMachineSettings):
    """BasicConicalGearMachineSettingsFormate

    This is a mastapy class.
    """

    TYPE = _BASIC_CONICAL_GEAR_MACHINE_SETTINGS_FORMATE

    class _Cast_BasicConicalGearMachineSettingsFormate:
        """Special nested class for casting BasicConicalGearMachineSettingsFormate to subclasses."""

        def __init__(self, parent: 'BasicConicalGearMachineSettingsFormate'):
            self._parent = parent

        @property
        def basic_conical_gear_machine_settings(self):
            return self._parent._cast(_816.BasicConicalGearMachineSettings)

        @property
        def basic_conical_gear_machine_settings_formate(self) -> 'BasicConicalGearMachineSettingsFormate':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BasicConicalGearMachineSettingsFormate.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def horizontal_setting(self) -> 'float':
        """float: 'HorizontalSetting' is the original name of this property."""

        temp = self.wrapped.HorizontalSetting

        if temp is None:
            return 0.0

        return temp

    @horizontal_setting.setter
    def horizontal_setting(self, value: 'float'):
        self.wrapped.HorizontalSetting = float(value) if value else 0.0

    @property
    def vertical_setting(self) -> 'float':
        """float: 'VerticalSetting' is the original name of this property."""

        temp = self.wrapped.VerticalSetting

        if temp is None:
            return 0.0

        return temp

    @vertical_setting.setter
    def vertical_setting(self, value: 'float'):
        self.wrapped.VerticalSetting = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'BasicConicalGearMachineSettingsFormate._Cast_BasicConicalGearMachineSettingsFormate':
        return self._Cast_BasicConicalGearMachineSettingsFormate(self)
