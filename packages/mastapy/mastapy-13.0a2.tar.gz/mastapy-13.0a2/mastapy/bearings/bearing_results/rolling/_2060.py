"""_2060.py

TrackTruncationSafetyFactorResults
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRACK_TRUNCATION_SAFETY_FACTOR_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'TrackTruncationSafetyFactorResults')


__docformat__ = 'restructuredtext en'
__all__ = ('TrackTruncationSafetyFactorResults',)


class TrackTruncationSafetyFactorResults(_0.APIBase):
    """TrackTruncationSafetyFactorResults

    This is a mastapy class.
    """

    TYPE = _TRACK_TRUNCATION_SAFETY_FACTOR_RESULTS

    class _Cast_TrackTruncationSafetyFactorResults:
        """Special nested class for casting TrackTruncationSafetyFactorResults to subclasses."""

        def __init__(self, parent: 'TrackTruncationSafetyFactorResults'):
            self._parent = parent

        @property
        def track_truncation_safety_factor_results(self) -> 'TrackTruncationSafetyFactorResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TrackTruncationSafetyFactorResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_with_worst_track_truncation(self) -> 'str':
        """str: 'ElementWithWorstTrackTruncation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementWithWorstTrackTruncation

        if temp is None:
            return ''

        return temp

    @property
    def safety_factor(self) -> 'float':
        """float: 'SafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_arc_distance_of_raceway_edge_to_hertzian_contact(self) -> 'float':
        """float: 'SmallestArcDistanceOfRacewayEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestArcDistanceOfRacewayEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def track_truncation_occurring_beyond_permissible_limit(self) -> 'bool':
        """bool: 'TrackTruncationOccurringBeyondPermissibleLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationOccurringBeyondPermissibleLimit

        if temp is None:
            return False

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation(self) -> 'float':
        """float: 'WorstHertzianEllipseMajor2bTrackTruncation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncation

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation_inner(self) -> 'float':
        """float: 'WorstHertzianEllipseMajor2bTrackTruncationInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncationInner

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation_outer(self) -> 'float':
        """float: 'WorstHertzianEllipseMajor2bTrackTruncationOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncationOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'TrackTruncationSafetyFactorResults._Cast_TrackTruncationSafetyFactorResults':
        return self._Cast_TrackTruncationSafetyFactorResults(self)
