"""_661.py

HobbingProcessCalculation
"""
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessCalculation',)


class HobbingProcessCalculation(_675.ProcessCalculation):
    """HobbingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_CALCULATION

    class _Cast_HobbingProcessCalculation:
        """Special nested class for casting HobbingProcessCalculation to subclasses."""

        def __init__(self, parent: 'HobbingProcessCalculation'):
            self._parent = parent

        @property
        def process_calculation(self):
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def hobbing_process_gear_shape(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _662
            
            return self._parent._cast(_662.HobbingProcessGearShape)

        @property
        def hobbing_process_lead_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _663
            
            return self._parent._cast(_663.HobbingProcessLeadCalculation)

        @property
        def hobbing_process_mark_on_shaft(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _664
            
            return self._parent._cast(_664.HobbingProcessMarkOnShaft)

        @property
        def hobbing_process_pitch_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _665
            
            return self._parent._cast(_665.HobbingProcessPitchCalculation)

        @property
        def hobbing_process_profile_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _666
            
            return self._parent._cast(_666.HobbingProcessProfileCalculation)

        @property
        def hobbing_process_total_modification_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _670
            
            return self._parent._cast(_670.HobbingProcessTotalModificationCalculation)

        @property
        def hobbing_process_calculation(self) -> 'HobbingProcessCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HobbingProcessCalculation._Cast_HobbingProcessCalculation':
        return self._Cast_HobbingProcessCalculation(self)
