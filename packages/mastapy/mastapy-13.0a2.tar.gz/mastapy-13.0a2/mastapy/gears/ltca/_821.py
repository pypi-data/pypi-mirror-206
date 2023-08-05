"""_821.py

ConicalGearRootFilletStressResults
"""
from mastapy.gears.ltca import _840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_ROOT_FILLET_STRESS_RESULTS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'ConicalGearRootFilletStressResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearRootFilletStressResults',)


class ConicalGearRootFilletStressResults(_840.GearRootFilletStressResults):
    """ConicalGearRootFilletStressResults

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_ROOT_FILLET_STRESS_RESULTS

    class _Cast_ConicalGearRootFilletStressResults:
        """Special nested class for casting ConicalGearRootFilletStressResults to subclasses."""

        def __init__(self, parent: 'ConicalGearRootFilletStressResults'):
            self._parent = parent

        @property
        def gear_root_fillet_stress_results(self):
            return self._parent._cast(_840.GearRootFilletStressResults)

        @property
        def conical_gear_root_fillet_stress_results(self) -> 'ConicalGearRootFilletStressResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearRootFilletStressResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearRootFilletStressResults._Cast_ConicalGearRootFilletStressResults':
        return self._Cast_ConicalGearRootFilletStressResults(self)
