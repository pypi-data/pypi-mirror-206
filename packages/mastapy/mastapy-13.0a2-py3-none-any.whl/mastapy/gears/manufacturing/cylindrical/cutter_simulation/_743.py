"""_743.py

WormGrinderSimulationCalculator
"""
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _723
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _738
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDER_SIMULATION_CALCULATOR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'WormGrinderSimulationCalculator')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrinderSimulationCalculator',)


class WormGrinderSimulationCalculator(_738.RackSimulationCalculator):
    """WormGrinderSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDER_SIMULATION_CALCULATOR

    class _Cast_WormGrinderSimulationCalculator:
        """Special nested class for casting WormGrinderSimulationCalculator to subclasses."""

        def __init__(self, parent: 'WormGrinderSimulationCalculator'):
            self._parent = parent

        @property
        def rack_simulation_calculator(self):
            return self._parent._cast(_738.RackSimulationCalculator)

        @property
        def cutter_simulation_calc(self):
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _726
            
            return self._parent._cast(_726.CutterSimulationCalc)

        @property
        def worm_grinder_simulation_calculator(self) -> 'WormGrinderSimulationCalculator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrinderSimulationCalculator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinder(self) -> '_723.CylindricalGearWormGrinderShape':
        """CylindricalGearWormGrinderShape: 'WormGrinder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrinder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrinderSimulationCalculator._Cast_WormGrinderSimulationCalculator':
        return self._Cast_WormGrinderSimulationCalculator(self)
