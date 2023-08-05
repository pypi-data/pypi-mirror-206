"""_2028.py

LoadedSphericalRollerThrustBearingResults
"""
from mastapy.bearings.bearing_results.rolling import _2014
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_THRUST_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedSphericalRollerThrustBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedSphericalRollerThrustBearingResults',)


class LoadedSphericalRollerThrustBearingResults(_2014.LoadedRollerBearingResults):
    """LoadedSphericalRollerThrustBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_THRUST_BEARING_RESULTS

    class _Cast_LoadedSphericalRollerThrustBearingResults:
        """Special nested class for casting LoadedSphericalRollerThrustBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedSphericalRollerThrustBearingResults'):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(self):
            return self._parent._cast(_2014.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2018
            
            return self._parent._cast(_2018.LoadedRollingBearingResults)

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
        def loaded_spherical_roller_thrust_bearing_results(self) -> 'LoadedSphericalRollerThrustBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedSphericalRollerThrustBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedSphericalRollerThrustBearingResults._Cast_LoadedSphericalRollerThrustBearingResults':
        return self._Cast_LoadedSphericalRollerThrustBearingResults(self)
