"""_2109.py

LoadedPlainOilFedJournalBearing
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.fluid_film import _2107
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PLAIN_OIL_FED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedPlainOilFedJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedPlainOilFedJournalBearing',)


class LoadedPlainOilFedJournalBearing(_2107.LoadedPlainJournalBearingResults):
    """LoadedPlainOilFedJournalBearing

    This is a mastapy class.
    """

    TYPE = _LOADED_PLAIN_OIL_FED_JOURNAL_BEARING

    class _Cast_LoadedPlainOilFedJournalBearing:
        """Special nested class for casting LoadedPlainOilFedJournalBearing to subclasses."""

        def __init__(self, parent: 'LoadedPlainOilFedJournalBearing'):
            self._parent = parent

        @property
        def loaded_plain_journal_bearing_results(self):
            return self._parent._cast(_2107.LoadedPlainJournalBearingResults)

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
        def loaded_plain_oil_fed_journal_bearing(self) -> 'LoadedPlainOilFedJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedPlainOilFedJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_oil_feed_inlet_and_minimum_film_thickness(self) -> 'float':
        """float: 'AngleBetweenOilFeedInletAndMinimumFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleBetweenOilFeedInletAndMinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_between_oil_feed_inlet_and_point_of_loading(self) -> 'float':
        """float: 'AngleBetweenOilFeedInletAndPointOfLoading' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleBetweenOilFeedInletAndPointOfLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_flow_rate(self) -> 'float':
        """float: 'CombinedFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def current_oil_inlet_angular_position_from_the_x_axis(self) -> 'float':
        """float: 'CurrentOilInletAngularPositionFromTheXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentOilInletAngularPositionFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def ideal_oil_inlet_angular_position_from_the_x_axis(self) -> 'float':
        """float: 'IdealOilInletAngularPositionFromTheXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IdealOilInletAngularPositionFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_exit_temperature(self) -> 'float':
        """float: 'OilExitTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilExitTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_flow_rate(self) -> 'float':
        """float: 'PressureFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def side_flow_rate(self) -> 'float':
        """float: 'SideFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SideFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedPlainOilFedJournalBearing._Cast_LoadedPlainOilFedJournalBearing':
        return self._Cast_LoadedPlainOilFedJournalBearing(self)
