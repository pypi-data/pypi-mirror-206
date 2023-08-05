"""_2097.py

OuterRingFittingThermalResults
"""
from mastapy.bearings.bearing_results.rolling.fitting import _2098
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_RING_FITTING_THERMAL_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.Fitting', 'OuterRingFittingThermalResults')


__docformat__ = 'restructuredtext en'
__all__ = ('OuterRingFittingThermalResults',)


class OuterRingFittingThermalResults(_2098.RingFittingThermalResults):
    """OuterRingFittingThermalResults

    This is a mastapy class.
    """

    TYPE = _OUTER_RING_FITTING_THERMAL_RESULTS

    class _Cast_OuterRingFittingThermalResults:
        """Special nested class for casting OuterRingFittingThermalResults to subclasses."""

        def __init__(self, parent: 'OuterRingFittingThermalResults'):
            self._parent = parent

        @property
        def ring_fitting_thermal_results(self):
            return self._parent._cast(_2098.RingFittingThermalResults)

        @property
        def outer_ring_fitting_thermal_results(self) -> 'OuterRingFittingThermalResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OuterRingFittingThermalResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OuterRingFittingThermalResults._Cast_OuterRingFittingThermalResults':
        return self._Cast_OuterRingFittingThermalResults(self)
