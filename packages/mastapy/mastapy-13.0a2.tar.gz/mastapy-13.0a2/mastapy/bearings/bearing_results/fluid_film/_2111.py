"""_2111.py

LoadedTiltingJournalPad
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.fluid_film import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_JOURNAL_PAD = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedTiltingJournalPad')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTiltingJournalPad',)


class LoadedTiltingJournalPad(_2103.LoadedFluidFilmBearingPad):
    """LoadedTiltingJournalPad

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_JOURNAL_PAD

    class _Cast_LoadedTiltingJournalPad:
        """Special nested class for casting LoadedTiltingJournalPad to subclasses."""

        def __init__(self, parent: 'LoadedTiltingJournalPad'):
            self._parent = parent

        @property
        def loaded_fluid_film_bearing_pad(self):
            return self._parent._cast(_2103.LoadedFluidFilmBearingPad)

        @property
        def loaded_tilting_journal_pad(self) -> 'LoadedTiltingJournalPad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedTiltingJournalPad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def eccentricity_ratio(self) -> 'float':
        """float: 'EccentricityRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EccentricityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricant_film_thickness(self) -> 'float':
        """float: 'MinimumLubricantFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricantFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedTiltingJournalPad._Cast_LoadedTiltingJournalPad':
        return self._Cast_LoadedTiltingJournalPad(self)
