"""_2112.py

LoadedTiltingPadJournalBearingResults
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.fluid_film import _2106
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_PAD_JOURNAL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedTiltingPadJournalBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTiltingPadJournalBearingResults',)


class LoadedTiltingPadJournalBearingResults(_2106.LoadedPadFluidFilmBearingResults):
    """LoadedTiltingPadJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_PAD_JOURNAL_BEARING_RESULTS

    class _Cast_LoadedTiltingPadJournalBearingResults:
        """Special nested class for casting LoadedTiltingPadJournalBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedTiltingPadJournalBearingResults'):
            self._parent = parent

        @property
        def loaded_pad_fluid_film_bearing_results(self):
            return self._parent._cast(_2106.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2104
            
            return self._parent._cast(_2104.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(self):
            from mastapy.bearings.bearing_results import _1939
            
            return self._parent._cast(_1939.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(self):
            from mastapy.bearings.bearing_results import _1942
            
            return self._parent._cast(_1942.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(self):
            from mastapy.bearings.bearing_results import _1934
            
            return self._parent._cast(_1934.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(self):
            from mastapy.bearings import _1860
            
            return self._parent._cast(_1860.BearingLoadCaseResultsLightweight)

        @property
        def loaded_tilting_pad_journal_bearing_results(self) -> 'LoadedTiltingPadJournalBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedTiltingPadJournalBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_position_of_the_minimum_film_thickness_from_the_x_axis(self) -> 'float':
        """float: 'AngularPositionOfTheMinimumFilmThicknessFromTheXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularPositionOfTheMinimumFilmThicknessFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def critical_reynolds_number(self) -> 'float':
        """float: 'CriticalReynoldsNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalReynoldsNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def eccentricity_ratio(self) -> 'float':
        """float: 'EccentricityRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EccentricityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_film_temperature(self) -> 'float':
        """float: 'EffectiveFilmTemperature' is the original name of this property."""

        temp = self.wrapped.EffectiveFilmTemperature

        if temp is None:
            return 0.0

        return temp

    @effective_film_temperature.setter
    def effective_film_temperature(self, value: 'float'):
        self.wrapped.EffectiveFilmTemperature = float(value) if value else 0.0

    @property
    def exit_flow(self) -> 'float':
        """float: 'ExitFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExitFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def feed_flow_rate(self) -> 'float':
        """float: 'FeedFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FeedFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def force_in_direction_of_eccentricity(self) -> 'float':
        """float: 'ForceInDirectionOfEccentricity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceInDirectionOfEccentricity

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_preload_factor(self) -> 'float':
        """float: 'HydrodynamicPreloadFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicPreloadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inlet_flow(self) -> 'float':
        """float: 'InletFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InletFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_density(self) -> 'float':
        """float: 'LubricantDensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_dynamic_viscosity(self) -> 'float':
        """float: 'LubricantDynamicViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantDynamicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pad_eccentricity_ratio(self) -> 'float':
        """float: 'MaximumPadEccentricityRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPadEccentricityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pressure(self) -> 'float':
        """float: 'MaximumPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pressure_velocity(self) -> 'float':
        """float: 'MaximumPressureVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPressureVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_film_thickness(self) -> 'float':
        """float: 'MinimumFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_friction(self) -> 'float':
        """float: 'NonDimensionalFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_maximum_pressure(self) -> 'float':
        """float: 'NonDimensionalMaximumPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalMaximumPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_minimum_film_thickness(self) -> 'float':
        """float: 'NonDimensionalMinimumFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalMinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_out_flow(self) -> 'float':
        """float: 'NonDimensionalOutFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalOutFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_side_flow(self) -> 'float':
        """float: 'NonDimensionalSideFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalSideFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_shape_factor(self) -> 'float':
        """float: 'PadShapeFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PadShapeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_clearance(self) -> 'float':
        """float: 'RelativeClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def reynolds_number(self) -> 'float':
        """float: 'ReynoldsNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReynoldsNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def side_flow(self) -> 'float':
        """float: 'SideFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SideFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def sommerfeld_number(self) -> 'float':
        """float: 'SommerfeldNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SommerfeldNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults':
        return self._Cast_LoadedTiltingPadJournalBearingResults(self)
