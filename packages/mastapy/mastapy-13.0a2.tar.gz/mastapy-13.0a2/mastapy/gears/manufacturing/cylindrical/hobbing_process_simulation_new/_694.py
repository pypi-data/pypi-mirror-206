"""_694.py

WormGrindingProcessSimulationInput
"""
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _686, _680
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_INPUT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessSimulationInput')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessSimulationInput',)


class WormGrindingProcessSimulationInput(_680.ProcessSimulationInput):
    """WormGrindingProcessSimulationInput

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_INPUT

    class _Cast_WormGrindingProcessSimulationInput:
        """Special nested class for casting WormGrindingProcessSimulationInput to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessSimulationInput'):
            self._parent = parent

        @property
        def process_simulation_input(self):
            return self._parent._cast(_680.ProcessSimulationInput)

        @property
        def worm_grinding_process_simulation_input(self) -> 'WormGrindingProcessSimulationInput':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessSimulationInput.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinder_manufacture_error(self) -> '_686.WormGrinderManufactureError':
        """WormGrinderManufactureError: 'WormGrinderManufactureError' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrinderManufactureError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrindingProcessSimulationInput._Cast_WormGrindingProcessSimulationInput':
        return self._Cast_WormGrindingProcessSimulationInput(self)
