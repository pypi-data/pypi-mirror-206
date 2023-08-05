"""_689.py

WormGrindingProcessCalculation
"""
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessCalculation',)


class WormGrindingProcessCalculation(_675.ProcessCalculation):
    """WormGrindingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_CALCULATION

    class _Cast_WormGrindingProcessCalculation:
        """Special nested class for casting WormGrindingProcessCalculation to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessCalculation'):
            self._parent = parent

        @property
        def process_calculation(self):
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def worm_grinding_cutter_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _687
            
            return self._parent._cast(_687.WormGrindingCutterCalculation)

        @property
        def worm_grinding_lead_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _688
            
            return self._parent._cast(_688.WormGrindingLeadCalculation)

        @property
        def worm_grinding_process_gear_shape(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _690
            
            return self._parent._cast(_690.WormGrindingProcessGearShape)

        @property
        def worm_grinding_process_mark_on_shaft(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _691
            
            return self._parent._cast(_691.WormGrindingProcessMarkOnShaft)

        @property
        def worm_grinding_process_pitch_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _692
            
            return self._parent._cast(_692.WormGrindingProcessPitchCalculation)

        @property
        def worm_grinding_process_profile_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _693
            
            return self._parent._cast(_693.WormGrindingProcessProfileCalculation)

        @property
        def worm_grinding_process_total_modification_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _697
            
            return self._parent._cast(_697.WormGrindingProcessTotalModificationCalculation)

        @property
        def worm_grinding_process_calculation(self) -> 'WormGrindingProcessCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation':
        return self._Cast_WormGrindingProcessCalculation(self)
