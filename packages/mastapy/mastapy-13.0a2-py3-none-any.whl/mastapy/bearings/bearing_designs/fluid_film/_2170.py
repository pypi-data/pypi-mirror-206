"""_2170.py

CylindricalHousingJournalBearing
"""
from mastapy.bearings.bearing_designs.fluid_film import _2177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_HOUSING_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'CylindricalHousingJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalHousingJournalBearing',)


class CylindricalHousingJournalBearing(_2177.PlainJournalHousing):
    """CylindricalHousingJournalBearing

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_HOUSING_JOURNAL_BEARING

    class _Cast_CylindricalHousingJournalBearing:
        """Special nested class for casting CylindricalHousingJournalBearing to subclasses."""

        def __init__(self, parent: 'CylindricalHousingJournalBearing'):
            self._parent = parent

        @property
        def plain_journal_housing(self):
            return self._parent._cast(_2177.PlainJournalHousing)

        @property
        def cylindrical_housing_journal_bearing(self) -> 'CylindricalHousingJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalHousingJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalHousingJournalBearing._Cast_CylindricalHousingJournalBearing':
        return self._Cast_CylindricalHousingJournalBearing(self)
