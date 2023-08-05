"""_2098.py

RingFittingThermalResults
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling.fitting import _2096
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_FITTING_THERMAL_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.Fitting', 'RingFittingThermalResults')


__docformat__ = 'restructuredtext en'
__all__ = ('RingFittingThermalResults',)


class RingFittingThermalResults(_0.APIBase):
    """RingFittingThermalResults

    This is a mastapy class.
    """

    TYPE = _RING_FITTING_THERMAL_RESULTS

    class _Cast_RingFittingThermalResults:
        """Special nested class for casting RingFittingThermalResults to subclasses."""

        def __init__(self, parent: 'RingFittingThermalResults'):
            self._parent = parent

        @property
        def inner_ring_fitting_thermal_results(self):
            from mastapy.bearings.bearing_results.rolling.fitting import _2095
            
            return self._parent._cast(_2095.InnerRingFittingThermalResults)

        @property
        def outer_ring_fitting_thermal_results(self):
            from mastapy.bearings.bearing_results.rolling.fitting import _2097
            
            return self._parent._cast(_2097.OuterRingFittingThermalResults)

        @property
        def ring_fitting_thermal_results(self) -> 'RingFittingThermalResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingFittingThermalResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def change_in_diameter_due_to_interference_and_centrifugal_effects(self) -> 'float':
        """float: 'ChangeInDiameterDueToInterferenceAndCentrifugalEffects' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChangeInDiameterDueToInterferenceAndCentrifugalEffects

        if temp is None:
            return 0.0

        return temp

    @property
    def interfacial_clearance_included_in_analysis(self) -> 'bool':
        """bool: 'InterfacialClearanceIncludedInAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InterfacialClearanceIncludedInAnalysis

        if temp is None:
            return False

        return temp

    @property
    def interfacial_normal_stress(self) -> 'float':
        """float: 'InterfacialNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InterfacialNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_hoop_stress(self) -> 'float':
        """float: 'MaximumHoopStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumHoopStress

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def interference_values(self) -> 'List[_2096.InterferenceComponents]':
        """List[InterferenceComponents]: 'InterferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InterferenceValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RingFittingThermalResults._Cast_RingFittingThermalResults':
        return self._Cast_RingFittingThermalResults(self)
