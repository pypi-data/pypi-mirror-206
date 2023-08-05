"""_669.py

HobbingProcessSimulationViewModel
"""
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _682, _668
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessSimulationViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessSimulationViewModel',)


class HobbingProcessSimulationViewModel(_682.ProcessSimulationViewModel['_668.HobbingProcessSimulationNew']):
    """HobbingProcessSimulationViewModel

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_SIMULATION_VIEW_MODEL

    class _Cast_HobbingProcessSimulationViewModel:
        """Special nested class for casting HobbingProcessSimulationViewModel to subclasses."""

        def __init__(self, parent: 'HobbingProcessSimulationViewModel'):
            self._parent = parent

        @property
        def process_simulation_view_model(self):
            return self._parent._cast(_682.ProcessSimulationViewModel)

        @property
        def gear_manufacturing_configuration_view_model(self):
            from mastapy.gears.manufacturing.cylindrical import _623
            
            return self._parent._cast(_623.GearManufacturingConfigurationViewModel)

        @property
        def hobbing_process_simulation_view_model(self) -> 'HobbingProcessSimulationViewModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessSimulationViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HobbingProcessSimulationViewModel._Cast_HobbingProcessSimulationViewModel':
        return self._Cast_HobbingProcessSimulationViewModel(self)
