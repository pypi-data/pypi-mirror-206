"""_1035.py

CylindricalPlanetaryGearSetDesign
"""
from mastapy._internal import constructor
from mastapy.utility_gui.charts import _1852
from mastapy.math_utility import _1501
from mastapy.gears.gear_designs.cylindrical import _1023
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANETARY_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalPlanetaryGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetaryGearSetDesign',)


class CylindricalPlanetaryGearSetDesign(_1023.CylindricalGearSetDesign):
    """CylindricalPlanetaryGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANETARY_GEAR_SET_DESIGN

    class _Cast_CylindricalPlanetaryGearSetDesign:
        """Special nested class for casting CylindricalPlanetaryGearSetDesign to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetaryGearSetDesign'):
            self._parent = parent

        @property
        def cylindrical_gear_set_design(self):
            return self._parent._cast(_1023.CylindricalGearSetDesign)

        @property
        def gear_set_design(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearSetDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def cylindrical_planetary_gear_set_design(self) -> 'CylindricalPlanetaryGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetaryGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equally_spaced_planets_are_assemblable(self) -> 'bool':
        """bool: 'EquallySpacedPlanetsAreAssemblable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquallySpacedPlanetsAreAssemblable

        if temp is None:
            return False

        return temp

    @property
    def least_mesh_angle(self) -> 'float':
        """float: 'LeastMeshAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeastMeshAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def planet_gear_phasing_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'PlanetGearPhasingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetGearPhasingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def reference_fixed_gear_for_planetary_sideband_fourier_series_is_annulus(self) -> 'bool':
        """bool: 'ReferenceFixedGearForPlanetarySidebandFourierSeriesIsAnnulus' is the original name of this property."""

        temp = self.wrapped.ReferenceFixedGearForPlanetarySidebandFourierSeriesIsAnnulus

        if temp is None:
            return False

        return temp

    @reference_fixed_gear_for_planetary_sideband_fourier_series_is_annulus.setter
    def reference_fixed_gear_for_planetary_sideband_fourier_series_is_annulus(self, value: 'bool'):
        self.wrapped.ReferenceFixedGearForPlanetarySidebandFourierSeriesIsAnnulus = bool(value) if value else False

    @property
    def use_planet_passing_window_function_in_planetary_sideband_fourier_series(self) -> 'bool':
        """bool: 'UsePlanetPassingWindowFunctionInPlanetarySidebandFourierSeries' is the original name of this property."""

        temp = self.wrapped.UsePlanetPassingWindowFunctionInPlanetarySidebandFourierSeries

        if temp is None:
            return False

        return temp

    @use_planet_passing_window_function_in_planetary_sideband_fourier_series.setter
    def use_planet_passing_window_function_in_planetary_sideband_fourier_series(self, value: 'bool'):
        self.wrapped.UsePlanetPassingWindowFunctionInPlanetarySidebandFourierSeries = bool(value) if value else False

    @property
    def planetary_sideband_fourier_series_for_rotating_planet_carrier(self) -> '_1501.FourierSeries':
        """FourierSeries: 'PlanetarySidebandFourierSeriesForRotatingPlanetCarrier' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetarySidebandFourierSeriesForRotatingPlanetCarrier

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_new_micro_geometry_using_planetary_duplicates(self):
        """ 'AddNewMicroGeometryUsingPlanetaryDuplicates' is the original name of this method."""

        self.wrapped.AddNewMicroGeometryUsingPlanetaryDuplicates()

    @property
    def cast_to(self) -> 'CylindricalPlanetaryGearSetDesign._Cast_CylindricalPlanetaryGearSetDesign':
        return self._Cast_CylindricalPlanetaryGearSetDesign(self)
