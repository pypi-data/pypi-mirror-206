"""_2014.py

LoadedRollerBearingResults
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2018
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollerBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollerBearingResults',)


class LoadedRollerBearingResults(_2018.LoadedRollingBearingResults):
    """LoadedRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_RESULTS

    class _Cast_LoadedRollerBearingResults:
        """Special nested class for casting LoadedRollerBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedRollerBearingResults'):
            self._parent = parent

        @property
        def loaded_rolling_bearing_results(self):
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
        def loaded_asymmetric_spherical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1974
            
            return self._parent._cast(_1974.LoadedAsymmetricSphericalRollerBearingResults)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1979
            
            return self._parent._cast(_1979.LoadedAxialThrustCylindricalRollerBearingResults)

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1982
            
            return self._parent._cast(_1982.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1990
            
            return self._parent._cast(_1990.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1994
            
            return self._parent._cast(_1994.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2006
            
            return self._parent._cast(_2006.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2009
            
            return self._parent._cast(_2009.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2025
            
            return self._parent._cast(_2025.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2028
            
            return self._parent._cast(_2028.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2033
            
            return self._parent._cast(_2033.LoadedTaperRollerBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2042
            
            return self._parent._cast(_2042.LoadedToroidalRollerBearingResults)

        @property
        def loaded_roller_bearing_results(self) -> 'LoadedRollerBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollerBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_angular_velocity(self) -> 'float':
        """float: 'ElementAngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def element_centrifugal_force(self) -> 'float':
        """float: 'ElementCentrifugalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementCentrifugalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def element_surface_velocity(self) -> 'float':
        """float: 'ElementSurfaceVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementSurfaceVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_inner(self) -> 'float':
        """float: 'HertzianContactWidthInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_outer(self) -> 'float':
        """float: 'HertzianContactWidthOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self) -> 'float':
        """float: 'MaximumShearStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self) -> 'float':
        """float: 'MaximumShearStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedRollerBearingResults._Cast_LoadedRollerBearingResults':
        return self._Cast_LoadedRollerBearingResults(self)
