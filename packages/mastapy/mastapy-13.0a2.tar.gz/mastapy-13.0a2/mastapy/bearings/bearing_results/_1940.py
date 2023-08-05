"""_1940.py

LoadedLinearBearingResults
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_LINEAR_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedLinearBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedLinearBearingResults',)


class LoadedLinearBearingResults(_1934.LoadedBearingResults):
    """LoadedLinearBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_LINEAR_BEARING_RESULTS

    class _Cast_LoadedLinearBearingResults:
        """Special nested class for casting LoadedLinearBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedLinearBearingResults'):
            self._parent = parent

        @property
        def loaded_bearing_results(self):
            return self._parent._cast(_1934.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(self):
            from mastapy.bearings import _1860
            
            return self._parent._cast(_1860.BearingLoadCaseResultsLightweight)

        @property
        def loaded_linear_bearing_results(self) -> 'LoadedLinearBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedLinearBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self) -> 'float':
        """float: 'RelativeMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedLinearBearingResults._Cast_LoadedLinearBearingResults':
        return self._Cast_LoadedLinearBearingResults(self)
