"""_2171.py

MachineryEncasedJournalBearing
"""
from mastapy.bearings.bearing_designs.fluid_film import _2177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MACHINERY_ENCASED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'MachineryEncasedJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('MachineryEncasedJournalBearing',)


class MachineryEncasedJournalBearing(_2177.PlainJournalHousing):
    """MachineryEncasedJournalBearing

    This is a mastapy class.
    """

    TYPE = _MACHINERY_ENCASED_JOURNAL_BEARING

    class _Cast_MachineryEncasedJournalBearing:
        """Special nested class for casting MachineryEncasedJournalBearing to subclasses."""

        def __init__(self, parent: 'MachineryEncasedJournalBearing'):
            self._parent = parent

        @property
        def plain_journal_housing(self):
            return self._parent._cast(_2177.PlainJournalHousing)

        @property
        def machinery_encased_journal_bearing(self) -> 'MachineryEncasedJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MachineryEncasedJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MachineryEncasedJournalBearing._Cast_MachineryEncasedJournalBearing':
        return self._Cast_MachineryEncasedJournalBearing(self)
