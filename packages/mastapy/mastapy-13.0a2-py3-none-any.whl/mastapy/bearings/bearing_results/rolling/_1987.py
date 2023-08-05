"""_1987.py

LoadedBallBearingResults
"""
from mastapy.bearings.bearing_results.rolling import _1957, _2060, _2018
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedBallBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBallBearingResults',)


class LoadedBallBearingResults(_2018.LoadedRollingBearingResults):
    """LoadedBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_RESULTS

    class _Cast_LoadedBallBearingResults:
        """Special nested class for casting LoadedBallBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedBallBearingResults'):
            self._parent = parent

        @property
        def loaded_rolling_bearing_results(self):
            return self._parent._cast(_2018.LoadedRollingBearingResults)

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
        def loaded_angular_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1968
            
            return self._parent._cast(_1968.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1971
            
            return self._parent._cast(_1971.LoadedAngularContactThrustBallBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1997
            
            return self._parent._cast(_1997.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2002
            
            return self._parent._cast(_2002.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2021
            
            return self._parent._cast(_2021.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2036
            
            return self._parent._cast(_2036.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2039
            
            return self._parent._cast(_2039.LoadedThrustBallBearingResults)

        @property
        def loaded_ball_bearing_results(self) -> 'LoadedBallBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBallBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def friction_model_for_gyroscopic_moment(self) -> '_1957.FrictionModelForGyroscopicMoment':
        """FrictionModelForGyroscopicMoment: 'FrictionModelForGyroscopicMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionModelForGyroscopicMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1957.FrictionModelForGyroscopicMoment)
        return constructor.new_from_mastapy_type(_1957.FrictionModelForGyroscopicMoment)(value) if value is not None else None

    @property
    def smearing_safety_factor(self) -> 'float':
        """float: 'SmearingSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmearingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def use_element_contact_angles_for_angular_velocities(self) -> 'bool':
        """bool: 'UseElementContactAnglesForAngularVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UseElementContactAnglesForAngularVelocities

        if temp is None:
            return False

        return temp

    @property
    def track_truncation(self) -> '_2060.TrackTruncationSafetyFactorResults':
        """TrackTruncationSafetyFactorResults: 'TrackTruncation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedBallBearingResults._Cast_LoadedBallBearingResults':
        return self._Cast_LoadedBallBearingResults(self)
