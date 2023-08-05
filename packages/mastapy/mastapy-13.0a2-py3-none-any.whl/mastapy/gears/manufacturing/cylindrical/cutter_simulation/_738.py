"""_738.py

RackSimulationCalculator
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACK_SIMULATION_CALCULATOR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'RackSimulationCalculator')


__docformat__ = 'restructuredtext en'
__all__ = ('RackSimulationCalculator',)


class RackSimulationCalculator(_726.CutterSimulationCalc):
    """RackSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _RACK_SIMULATION_CALCULATOR

    class _Cast_RackSimulationCalculator:
        """Special nested class for casting RackSimulationCalculator to subclasses."""

        def __init__(self, parent: 'RackSimulationCalculator'):
            self._parent = parent

        @property
        def cutter_simulation_calc(self):
            return self._parent._cast(_726.CutterSimulationCalc)

        @property
        def hob_simulation_calculator(self):
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _735
            
            return self._parent._cast(_735.HobSimulationCalculator)

        @property
        def worm_grinder_simulation_calculator(self):
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _743
            
            return self._parent._cast(_743.WormGrinderSimulationCalculator)

        @property
        def rack_simulation_calculator(self) -> 'RackSimulationCalculator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RackSimulationCalculator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hob_working_depth_delta(self) -> 'float':
        """float: 'HobWorkingDepthDelta' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobWorkingDepthDelta

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'RackSimulationCalculator._Cast_RackSimulationCalculator':
        return self._Cast_RackSimulationCalculator(self)
