"""_2169.py

CircumferentialFeedJournalBearing
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CIRCUMFERENTIAL_FEED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'CircumferentialFeedJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('CircumferentialFeedJournalBearing',)


class CircumferentialFeedJournalBearing(_0.APIBase):
    """CircumferentialFeedJournalBearing

    This is a mastapy class.
    """

    TYPE = _CIRCUMFERENTIAL_FEED_JOURNAL_BEARING

    class _Cast_CircumferentialFeedJournalBearing:
        """Special nested class for casting CircumferentialFeedJournalBearing to subclasses."""

        def __init__(self, parent: 'CircumferentialFeedJournalBearing'):
            self._parent = parent

        @property
        def circumferential_feed_journal_bearing(self) -> 'CircumferentialFeedJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CircumferentialFeedJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groove_width(self) -> 'float':
        """float: 'GrooveWidth' is the original name of this property."""

        temp = self.wrapped.GrooveWidth

        if temp is None:
            return 0.0

        return temp

    @groove_width.setter
    def groove_width(self, value: 'float'):
        self.wrapped.GrooveWidth = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CircumferentialFeedJournalBearing._Cast_CircumferentialFeedJournalBearing':
        return self._Cast_CircumferentialFeedJournalBearing(self)
