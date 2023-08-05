"""_802.py

PinionHypoidFormateTiltMachineSettings
"""
from mastapy.gears.manufacturing.bevel import _801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_HYPOID_FORMATE_TILT_MACHINE_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionHypoidFormateTiltMachineSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionHypoidFormateTiltMachineSettings',)


class PinionHypoidFormateTiltMachineSettings(_801.PinionFinishMachineSettings):
    """PinionHypoidFormateTiltMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_HYPOID_FORMATE_TILT_MACHINE_SETTINGS

    class _Cast_PinionHypoidFormateTiltMachineSettings:
        """Special nested class for casting PinionHypoidFormateTiltMachineSettings to subclasses."""

        def __init__(self, parent: 'PinionHypoidFormateTiltMachineSettings'):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(self):
            return self._parent._cast(_801.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(self):
            from mastapy.gears import _316
            
            return self._parent._cast(_316.ConicalGearToothSurface)

        @property
        def pinion_hypoid_formate_tilt_machine_settings(self) -> 'PinionHypoidFormateTiltMachineSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionHypoidFormateTiltMachineSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PinionHypoidFormateTiltMachineSettings._Cast_PinionHypoidFormateTiltMachineSettings':
        return self._Cast_PinionHypoidFormateTiltMachineSettings(self)
