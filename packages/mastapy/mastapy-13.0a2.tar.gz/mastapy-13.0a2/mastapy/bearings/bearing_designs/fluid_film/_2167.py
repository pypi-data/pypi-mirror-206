"""_2167.py

AxialGrooveJournalBearing
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.fluid_film import _2166
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_GROOVE_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'AxialGrooveJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialGrooveJournalBearing',)


class AxialGrooveJournalBearing(_2166.AxialFeedJournalBearing):
    """AxialGrooveJournalBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_GROOVE_JOURNAL_BEARING

    class _Cast_AxialGrooveJournalBearing:
        """Special nested class for casting AxialGrooveJournalBearing to subclasses."""

        def __init__(self, parent: 'AxialGrooveJournalBearing'):
            self._parent = parent

        @property
        def axial_feed_journal_bearing(self):
            return self._parent._cast(_2166.AxialFeedJournalBearing)

        @property
        def axial_groove_journal_bearing(self) -> 'AxialGrooveJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AxialGrooveJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groove_length(self) -> 'float':
        """float: 'GrooveLength' is the original name of this property."""

        temp = self.wrapped.GrooveLength

        if temp is None:
            return 0.0

        return temp

    @groove_length.setter
    def groove_length(self, value: 'float'):
        self.wrapped.GrooveLength = float(value) if value else 0.0

    @property
    def groove_radial_dimension(self) -> 'float':
        """float: 'GrooveRadialDimension' is the original name of this property."""

        temp = self.wrapped.GrooveRadialDimension

        if temp is None:
            return 0.0

        return temp

    @groove_radial_dimension.setter
    def groove_radial_dimension(self, value: 'float'):
        self.wrapped.GrooveRadialDimension = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AxialGrooveJournalBearing._Cast_AxialGrooveJournalBearing':
        return self._Cast_AxialGrooveJournalBearing(self)
