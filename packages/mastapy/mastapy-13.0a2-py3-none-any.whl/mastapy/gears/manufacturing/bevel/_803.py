"""_803.py

PinionHypoidGeneratingTiltMachineSettings
"""
from mastapy.gears.manufacturing.bevel import _801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_HYPOID_GENERATING_TILT_MACHINE_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionHypoidGeneratingTiltMachineSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionHypoidGeneratingTiltMachineSettings',)


class PinionHypoidGeneratingTiltMachineSettings(_801.PinionFinishMachineSettings):
    """PinionHypoidGeneratingTiltMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_HYPOID_GENERATING_TILT_MACHINE_SETTINGS

    class _Cast_PinionHypoidGeneratingTiltMachineSettings:
        """Special nested class for casting PinionHypoidGeneratingTiltMachineSettings to subclasses."""

        def __init__(self, parent: 'PinionHypoidGeneratingTiltMachineSettings'):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(self):
            return self._parent._cast(_801.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(self):
            from mastapy.gears import _316
            
            return self._parent._cast(_316.ConicalGearToothSurface)

        @property
        def pinion_hypoid_generating_tilt_machine_settings(self) -> 'PinionHypoidGeneratingTiltMachineSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionHypoidGeneratingTiltMachineSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PinionHypoidGeneratingTiltMachineSettings._Cast_PinionHypoidGeneratingTiltMachineSettings':
        return self._Cast_PinionHypoidGeneratingTiltMachineSettings(self)
