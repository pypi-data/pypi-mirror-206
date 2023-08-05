"""_2027.py

LoadedSphericalRollerRadialBearingStripLoadResults
"""
from mastapy.bearings.bearing_results.rolling import _1966
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_STRIP_LOAD_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedSphericalRollerRadialBearingStripLoadResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedSphericalRollerRadialBearingStripLoadResults',)


class LoadedSphericalRollerRadialBearingStripLoadResults(_1966.LoadedAbstractSphericalRollerBearingStripLoadResults):
    """LoadedSphericalRollerRadialBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_STRIP_LOAD_RESULTS

    class _Cast_LoadedSphericalRollerRadialBearingStripLoadResults:
        """Special nested class for casting LoadedSphericalRollerRadialBearingStripLoadResults to subclasses."""

        def __init__(self, parent: 'LoadedSphericalRollerRadialBearingStripLoadResults'):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(self):
            return self._parent._cast(_1966.LoadedAbstractSphericalRollerBearingStripLoadResults)

        @property
        def loaded_roller_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _2016
            
            return self._parent._cast(_2016.LoadedRollerStripLoadResults)

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _2044
            
            return self._parent._cast(_2044.LoadedToroidalRollerBearingStripLoadResults)

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(self) -> 'LoadedSphericalRollerRadialBearingStripLoadResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedSphericalRollerRadialBearingStripLoadResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults':
        return self._Cast_LoadedSphericalRollerRadialBearingStripLoadResults(self)
