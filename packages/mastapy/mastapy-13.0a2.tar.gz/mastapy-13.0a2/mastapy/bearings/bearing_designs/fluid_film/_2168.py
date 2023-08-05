"""_2168.py

AxialHoleJournalBearing
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.fluid_film import _2166
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_HOLE_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'AxialHoleJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialHoleJournalBearing',)


class AxialHoleJournalBearing(_2166.AxialFeedJournalBearing):
    """AxialHoleJournalBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_HOLE_JOURNAL_BEARING

    class _Cast_AxialHoleJournalBearing:
        """Special nested class for casting AxialHoleJournalBearing to subclasses."""

        def __init__(self, parent: 'AxialHoleJournalBearing'):
            self._parent = parent

        @property
        def axial_feed_journal_bearing(self):
            return self._parent._cast(_2166.AxialFeedJournalBearing)

        @property
        def axial_hole_journal_bearing(self) -> 'AxialHoleJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AxialHoleJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hole_diameter(self) -> 'float':
        """float: 'HoleDiameter' is the original name of this property."""

        temp = self.wrapped.HoleDiameter

        if temp is None:
            return 0.0

        return temp

    @hole_diameter.setter
    def hole_diameter(self, value: 'float'):
        self.wrapped.HoleDiameter = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AxialHoleJournalBearing._Cast_AxialHoleJournalBearing':
        return self._Cast_AxialHoleJournalBearing(self)
