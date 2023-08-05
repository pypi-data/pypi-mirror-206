"""_2166.py

AxialFeedJournalBearing
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_FEED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'AxialFeedJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialFeedJournalBearing',)


class AxialFeedJournalBearing(_0.APIBase):
    """AxialFeedJournalBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_FEED_JOURNAL_BEARING

    class _Cast_AxialFeedJournalBearing:
        """Special nested class for casting AxialFeedJournalBearing to subclasses."""

        def __init__(self, parent: 'AxialFeedJournalBearing'):
            self._parent = parent

        @property
        def axial_groove_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2167
            
            return self._parent._cast(_2167.AxialGrooveJournalBearing)

        @property
        def axial_hole_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2168
            
            return self._parent._cast(_2168.AxialHoleJournalBearing)

        @property
        def axial_feed_journal_bearing(self) -> 'AxialFeedJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AxialFeedJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groove_angular_location(self) -> 'float':
        """float: 'GrooveAngularLocation' is the original name of this property."""

        temp = self.wrapped.GrooveAngularLocation

        if temp is None:
            return 0.0

        return temp

    @groove_angular_location.setter
    def groove_angular_location(self, value: 'float'):
        self.wrapped.GrooveAngularLocation = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AxialFeedJournalBearing._Cast_AxialFeedJournalBearing':
        return self._Cast_AxialFeedJournalBearing(self)
