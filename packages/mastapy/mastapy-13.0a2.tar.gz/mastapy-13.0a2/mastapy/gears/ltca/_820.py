"""_820.py

ConicalGearFilletStressResults
"""
from mastapy.gears.ltca import _832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FILLET_STRESS_RESULTS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'ConicalGearFilletStressResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearFilletStressResults',)


class ConicalGearFilletStressResults(_832.GearFilletNodeStressResults):
    """ConicalGearFilletStressResults

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_FILLET_STRESS_RESULTS

    class _Cast_ConicalGearFilletStressResults:
        """Special nested class for casting ConicalGearFilletStressResults to subclasses."""

        def __init__(self, parent: 'ConicalGearFilletStressResults'):
            self._parent = parent

        @property
        def gear_fillet_node_stress_results(self):
            return self._parent._cast(_832.GearFilletNodeStressResults)

        @property
        def conical_gear_fillet_stress_results(self) -> 'ConicalGearFilletStressResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearFilletStressResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearFilletStressResults._Cast_ConicalGearFilletStressResults':
        return self._Cast_ConicalGearFilletStressResults(self)
