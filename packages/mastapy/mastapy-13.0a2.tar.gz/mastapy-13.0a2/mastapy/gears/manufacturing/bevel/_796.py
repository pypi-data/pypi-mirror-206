"""_796.py

PinionBevelGeneratingModifiedRollMachineSettings
"""
from mastapy.gears.manufacturing.bevel import _801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_BEVEL_GENERATING_MODIFIED_ROLL_MACHINE_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionBevelGeneratingModifiedRollMachineSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionBevelGeneratingModifiedRollMachineSettings',)


class PinionBevelGeneratingModifiedRollMachineSettings(_801.PinionFinishMachineSettings):
    """PinionBevelGeneratingModifiedRollMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_BEVEL_GENERATING_MODIFIED_ROLL_MACHINE_SETTINGS

    class _Cast_PinionBevelGeneratingModifiedRollMachineSettings:
        """Special nested class for casting PinionBevelGeneratingModifiedRollMachineSettings to subclasses."""

        def __init__(self, parent: 'PinionBevelGeneratingModifiedRollMachineSettings'):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(self):
            return self._parent._cast(_801.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(self):
            from mastapy.gears import _316
            
            return self._parent._cast(_316.ConicalGearToothSurface)

        @property
        def pinion_bevel_generating_modified_roll_machine_settings(self) -> 'PinionBevelGeneratingModifiedRollMachineSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionBevelGeneratingModifiedRollMachineSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PinionBevelGeneratingModifiedRollMachineSettings._Cast_PinionBevelGeneratingModifiedRollMachineSettings':
        return self._Cast_PinionBevelGeneratingModifiedRollMachineSettings(self)
