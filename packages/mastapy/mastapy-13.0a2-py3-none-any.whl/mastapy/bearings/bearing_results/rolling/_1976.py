"""_1976.py

LoadedAsymmetricSphericalRollerBearingStripLoadResults
"""
from mastapy.bearings.bearing_results.rolling import _1966
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_STRIP_LOAD_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAsymmetricSphericalRollerBearingStripLoadResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAsymmetricSphericalRollerBearingStripLoadResults',)


class LoadedAsymmetricSphericalRollerBearingStripLoadResults(_1966.LoadedAbstractSphericalRollerBearingStripLoadResults):
    """LoadedAsymmetricSphericalRollerBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_STRIP_LOAD_RESULTS

    class _Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults:
        """Special nested class for casting LoadedAsymmetricSphericalRollerBearingStripLoadResults to subclasses."""

        def __init__(self, parent: 'LoadedAsymmetricSphericalRollerBearingStripLoadResults'):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(self):
            return self._parent._cast(_1966.LoadedAbstractSphericalRollerBearingStripLoadResults)

        @property
        def loaded_roller_strip_load_results(self):
            from mastapy.bearings.bearing_results.rolling import _2016
            
            return self._parent._cast(_2016.LoadedRollerStripLoadResults)

        @property
        def loaded_asymmetric_spherical_roller_bearing_strip_load_results(self) -> 'LoadedAsymmetricSphericalRollerBearingStripLoadResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAsymmetricSphericalRollerBearingStripLoadResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedAsymmetricSphericalRollerBearingStripLoadResults._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults':
        return self._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults(self)
