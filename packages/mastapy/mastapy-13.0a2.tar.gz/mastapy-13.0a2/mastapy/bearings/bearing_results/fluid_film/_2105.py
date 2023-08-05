"""_2105.py

LoadedGreaseFilledJournalBearingResults
"""
from mastapy.bearings.bearing_results.fluid_film import _2107
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_GREASE_FILLED_JOURNAL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedGreaseFilledJournalBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedGreaseFilledJournalBearingResults',)


class LoadedGreaseFilledJournalBearingResults(_2107.LoadedPlainJournalBearingResults):
    """LoadedGreaseFilledJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_GREASE_FILLED_JOURNAL_BEARING_RESULTS

    class _Cast_LoadedGreaseFilledJournalBearingResults:
        """Special nested class for casting LoadedGreaseFilledJournalBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedGreaseFilledJournalBearingResults'):
            self._parent = parent

        @property
        def loaded_plain_journal_bearing_results(self):
            return self._parent._cast(_2107.LoadedPlainJournalBearingResults)

        @property
        def loaded_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2104
            
            return self._parent._cast(_2104.LoadedFluidFilmBearingResults)

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
        def loaded_grease_filled_journal_bearing_results(self) -> 'LoadedGreaseFilledJournalBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedGreaseFilledJournalBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults':
        return self._Cast_LoadedGreaseFilledJournalBearingResults(self)
