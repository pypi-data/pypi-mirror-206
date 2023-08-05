"""_1939.py

LoadedDetailedBearingResults
"""
from mastapy._internal import constructor
from mastapy.materials import _263
from mastapy.bearings.bearing_results import _1942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_DETAILED_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedDetailedBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedDetailedBearingResults',)


class LoadedDetailedBearingResults(_1942.LoadedNonLinearBearingResults):
    """LoadedDetailedBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_DETAILED_BEARING_RESULTS

    class _Cast_LoadedDetailedBearingResults:
        """Special nested class for casting LoadedDetailedBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedDetailedBearingResults'):
            self._parent = parent

        @property
        def loaded_non_linear_bearing_results(self):
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
        def loaded_angular_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1968
            
            return self._parent._cast(_1968.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1971
            
            return self._parent._cast(_1971.LoadedAngularContactThrustBallBearingResults)

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1974
            
            return self._parent._cast(_1974.LoadedAsymmetricSphericalRollerBearingResults)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1979
            
            return self._parent._cast(_1979.LoadedAxialThrustCylindricalRollerBearingResults)

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1982
            
            return self._parent._cast(_1982.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1987
            
            return self._parent._cast(_1987.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1990
            
            return self._parent._cast(_1990.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1994
            
            return self._parent._cast(_1994.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1997
            
            return self._parent._cast(_1997.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2002
            
            return self._parent._cast(_2002.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2006
            
            return self._parent._cast(_2006.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2009
            
            return self._parent._cast(_2009.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2014
            
            return self._parent._cast(_2014.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2018
            
            return self._parent._cast(_2018.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2021
            
            return self._parent._cast(_2021.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2025
            
            return self._parent._cast(_2025.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2028
            
            return self._parent._cast(_2028.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2033
            
            return self._parent._cast(_2033.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2036
            
            return self._parent._cast(_2036.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2039
            
            return self._parent._cast(_2039.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2042
            
            return self._parent._cast(_2042.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2104
            
            return self._parent._cast(_2104.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2105
            
            return self._parent._cast(_2105.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2106
            
            return self._parent._cast(_2106.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2107
            
            return self._parent._cast(_2107.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(self):
            from mastapy.bearings.bearing_results.fluid_film import _2109
            
            return self._parent._cast(_2109.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2112
            
            return self._parent._cast(_2112.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2113
            
            return self._parent._cast(_2113.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_detailed_bearing_results(self) -> 'LoadedDetailedBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedDetailedBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def oil_sump_temperature(self) -> 'float':
        """float: 'OilSumpTemperature' is the original name of this property."""

        temp = self.wrapped.OilSumpTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_sump_temperature.setter
    def oil_sump_temperature(self, value: 'float'):
        self.wrapped.OilSumpTemperature = float(value) if value else 0.0

    @property
    def operating_air_temperature(self) -> 'float':
        """float: 'OperatingAirTemperature' is the original name of this property."""

        temp = self.wrapped.OperatingAirTemperature

        if temp is None:
            return 0.0

        return temp

    @operating_air_temperature.setter
    def operating_air_temperature(self, value: 'float'):
        self.wrapped.OperatingAirTemperature = float(value) if value else 0.0

    @property
    def temperature_when_assembled(self) -> 'float':
        """float: 'TemperatureWhenAssembled' is the original name of this property."""

        temp = self.wrapped.TemperatureWhenAssembled

        if temp is None:
            return 0.0

        return temp

    @temperature_when_assembled.setter
    def temperature_when_assembled(self, value: 'float'):
        self.wrapped.TemperatureWhenAssembled = float(value) if value else 0.0

    @property
    def lubrication(self) -> '_263.LubricationDetail':
        """LubricationDetail: 'Lubrication' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Lubrication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults':
        return self._Cast_LoadedDetailedBearingResults(self)
