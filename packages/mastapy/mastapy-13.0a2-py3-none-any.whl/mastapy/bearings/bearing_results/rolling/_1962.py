"""_1962.py

ISO153122018Results
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO153122018_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ISO153122018Results')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO153122018Results',)


class ISO153122018Results(_0.APIBase):
    """ISO153122018Results

    This is a mastapy class.
    """

    TYPE = _ISO153122018_RESULTS

    class _Cast_ISO153122018Results:
        """Special nested class for casting ISO153122018Results to subclasses."""

        def __init__(self, parent: 'ISO153122018Results'):
            self._parent = parent

        @property
        def iso153122018_results(self) -> 'ISO153122018Results':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO153122018Results.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_for_the_load_dependent_friction_moment_for_the_reference_conditions(self) -> 'float':
        """float: 'CoefficientForTheLoadDependentFrictionMomentForTheReferenceConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientForTheLoadDependentFrictionMomentForTheReferenceConditions

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_for_the_load_independent_friction_moment_for_the_reference_conditions(self) -> 'float':
        """float: 'CoefficientForTheLoadIndependentFrictionMomentForTheReferenceConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientForTheLoadIndependentFrictionMomentForTheReferenceConditions

        if temp is None:
            return 0.0

        return temp

    @property
    def heat_emitting_reference_surface_area(self) -> 'float':
        """float: 'HeatEmittingReferenceSurfaceArea' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeatEmittingReferenceSurfaceArea

        if temp is None:
            return 0.0

        return temp

    @property
    def load_dependent_frictional_moment_under_reference_conditions_at_the_thermal_speed_rating(self) -> 'float':
        """float: 'LoadDependentFrictionalMomentUnderReferenceConditionsAtTheThermalSpeedRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDependentFrictionalMomentUnderReferenceConditionsAtTheThermalSpeedRating

        if temp is None:
            return 0.0

        return temp

    @property
    def load_independent_frictional_moment_under_reference_conditions_at_the_thermal_speed_rating(self) -> 'float':
        """float: 'LoadIndependentFrictionalMomentUnderReferenceConditionsAtTheThermalSpeedRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadIndependentFrictionalMomentUnderReferenceConditionsAtTheThermalSpeedRating

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_under_reference_conditions_at_the_thermal_speed_rating(self) -> 'float':
        """float: 'PowerLossUnderReferenceConditionsAtTheThermalSpeedRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossUnderReferenceConditionsAtTheThermalSpeedRating

        if temp is None:
            return 0.0

        return temp

    @property
    def reason_for_invalidity(self) -> 'str':
        """str: 'ReasonForInvalidity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonForInvalidity

        if temp is None:
            return ''

        return temp

    @property
    def reference_heat_flow(self) -> 'float':
        """float: 'ReferenceHeatFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceHeatFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_heat_flow_density(self) -> 'float':
        """float: 'ReferenceHeatFlowDensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceHeatFlowDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_load(self) -> 'float':
        """float: 'ReferenceLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_speed_rating(self) -> 'float':
        """float: 'ThermalSpeedRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThermalSpeedRating

        if temp is None:
            return 0.0

        return temp

    @property
    def viscosity_of_reference_oil(self) -> 'float':
        """float: 'ViscosityOfReferenceOil' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ViscosityOfReferenceOil

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO153122018Results._Cast_ISO153122018Results':
        return self._Cast_ISO153122018Results(self)
