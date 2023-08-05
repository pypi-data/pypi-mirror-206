"""_740.py

ShaperSimulationCalculator
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _721
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAPER_SIMULATION_CALCULATOR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'ShaperSimulationCalculator')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaperSimulationCalculator',)


class ShaperSimulationCalculator(_726.CutterSimulationCalc):
    """ShaperSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _SHAPER_SIMULATION_CALCULATOR

    class _Cast_ShaperSimulationCalculator:
        """Special nested class for casting ShaperSimulationCalculator to subclasses."""

        def __init__(self, parent: 'ShaperSimulationCalculator'):
            self._parent = parent

        @property
        def cutter_simulation_calc(self):
            return self._parent._cast(_726.CutterSimulationCalc)

        @property
        def shaper_simulation_calculator(self) -> 'ShaperSimulationCalculator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaperSimulationCalculator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutting_centre_distance(self) -> 'float':
        """float: 'CuttingCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CuttingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def cutting_pressure_angle(self) -> 'float':
        """float: 'CuttingPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CuttingPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def shaper_sap_diameter(self) -> 'float':
        """float: 'ShaperSAPDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaperSAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaper(self) -> '_721.CylindricalGearShaperTangible':
        """CylindricalGearShaperTangible: 'Shaper' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaper

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaperSimulationCalculator._Cast_ShaperSimulationCalculator':
        return self._Cast_ShaperSimulationCalculator(self)
