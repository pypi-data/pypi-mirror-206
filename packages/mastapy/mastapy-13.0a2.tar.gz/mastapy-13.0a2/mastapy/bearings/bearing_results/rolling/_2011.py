"""_2011.py

LoadedNonBarrelRollerBearingStripLoadResults
"""
from mastapy.bearings.bearing_results.rolling import _2016
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_STRIP_LOAD_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNonBarrelRollerBearingStripLoadResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonBarrelRollerBearingStripLoadResults',)


class LoadedNonBarrelRollerBearingStripLoadResults(_2016.LoadedRollerStripLoadResults):
    """LoadedNonBarrelRollerBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_STRIP_LOAD_RESULTS

    class _Cast_LoadedNonBarrelRollerBearingStripLoadResults:
        """Special nested class for casting LoadedNonBarrelRollerBearingStripLoadResults to subclasses."""

        def __init__(self, parent: 'LoadedNonBarrelRollerBearingStripLoadResults'):
            self._parent = parent

        @property
        def loaded_roller_strip_load_results(self):
            return self._parent._cast(_2016.LoadedRollerStripLoadResults)

        @property
        def loaded_non_barrel_roller_bearing_strip_load_results(self) -> 'LoadedNonBarrelRollerBearingStripLoadResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNonBarrelRollerBearingStripLoadResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedNonBarrelRollerBearingStripLoadResults._Cast_LoadedNonBarrelRollerBearingStripLoadResults':
        return self._Cast_LoadedNonBarrelRollerBearingStripLoadResults(self)
