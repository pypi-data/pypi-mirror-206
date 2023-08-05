"""_2016.py

LoadedRollerStripLoadResults
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_STRIP_LOAD_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollerStripLoadResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollerStripLoadResults',)


class LoadedRollerStripLoadResults(_0.APIBase):
    """LoadedRollerStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_STRIP_LOAD_RESULTS

    class _Cast_LoadedRollerStripLoadResults:
        """Special nested class for casting LoadedRollerStripLoadResults to subclasses."""

        def __init__(self, parent: 'LoadedRollerStripLoadResults'):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _1966
            
            return self._parent._cast(_1966.LoadedAbstractSphericalRollerBearingStripLoadResults)

        @property
        def loaded_asymmetric_spherical_roller_bearing_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _1976
            
            return self._parent._cast(_1976.LoadedAsymmetricSphericalRollerBearingStripLoadResults)

        @property
        def loaded_non_barrel_roller_bearing_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _2011
            
            return self._parent._cast(_2011.LoadedNonBarrelRollerBearingStripLoadResults)

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _2027
            
            return self._parent._cast(_2027.LoadedSphericalRollerRadialBearingStripLoadResults)

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _2044
            
            return self._parent._cast(_2044.LoadedToroidalRollerBearingStripLoadResults)

        @property
        def loaded_roller_strip_load_results(self) -> 'LoadedRollerStripLoadResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollerStripLoadResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults':
        return self._Cast_LoadedRollerStripLoadResults(self)
