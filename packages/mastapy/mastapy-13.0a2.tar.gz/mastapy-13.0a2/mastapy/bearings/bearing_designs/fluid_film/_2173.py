"""_2173.py

PedestalJournalBearing
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.fluid_film import _2177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PEDESTAL_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'PedestalJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('PedestalJournalBearing',)


class PedestalJournalBearing(_2177.PlainJournalHousing):
    """PedestalJournalBearing

    This is a mastapy class.
    """

    TYPE = _PEDESTAL_JOURNAL_BEARING

    class _Cast_PedestalJournalBearing:
        """Special nested class for casting PedestalJournalBearing to subclasses."""

        def __init__(self, parent: 'PedestalJournalBearing'):
            self._parent = parent

        @property
        def plain_journal_housing(self):
            return self._parent._cast(_2177.PlainJournalHousing)

        @property
        def pedestal_journal_bearing(self) -> 'PedestalJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PedestalJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pedestal_base_depth(self) -> 'float':
        """float: 'PedestalBaseDepth' is the original name of this property."""

        temp = self.wrapped.PedestalBaseDepth

        if temp is None:
            return 0.0

        return temp

    @pedestal_base_depth.setter
    def pedestal_base_depth(self, value: 'float'):
        self.wrapped.PedestalBaseDepth = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'PedestalJournalBearing._Cast_PedestalJournalBearing':
        return self._Cast_PedestalJournalBearing(self)
