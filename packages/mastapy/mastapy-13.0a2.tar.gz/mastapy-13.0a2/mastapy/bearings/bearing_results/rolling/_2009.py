"""_2009.py

LoadedNonBarrelRollerBearingResults
"""
from mastapy.bearings.bearing_results.rolling import _2057, _2014
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNonBarrelRollerBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonBarrelRollerBearingResults',)


class LoadedNonBarrelRollerBearingResults(_2014.LoadedRollerBearingResults):
    """LoadedNonBarrelRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_RESULTS

    class _Cast_LoadedNonBarrelRollerBearingResults:
        """Special nested class for casting LoadedNonBarrelRollerBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedNonBarrelRollerBearingResults'):
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
        def loaded_axial_thrust_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1979
            
            return self._parent._cast(_1979.LoadedAxialThrustCylindricalRollerBearingResults)

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1982
            
            return self._parent._cast(_1982.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1994
            
            return self._parent._cast(_1994.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2006
            
            return self._parent._cast(_2006.LoadedNeedleRollerBearingResults)

        @property
        def loaded_taper_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2033
            
            return self._parent._cast(_2033.LoadedTaperRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(self) -> 'LoadedNonBarrelRollerBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNonBarrelRollerBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def smt_rib_stress(self) -> '_2057.SMTRibStressResults':
        """SMTRibStressResults: 'SMTRibStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SMTRibStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults':
        return self._Cast_LoadedNonBarrelRollerBearingResults(self)
