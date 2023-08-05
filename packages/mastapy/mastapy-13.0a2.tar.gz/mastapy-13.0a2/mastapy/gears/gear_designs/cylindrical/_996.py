"""_996.py

CaseHardeningProperties
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.cylindrical import _1046, _1047
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CASE_HARDENING_PROPERTIES = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CaseHardeningProperties')


__docformat__ = 'restructuredtext en'
__all__ = ('CaseHardeningProperties',)


class CaseHardeningProperties(_0.APIBase):
    """CaseHardeningProperties

    This is a mastapy class.
    """

    TYPE = _CASE_HARDENING_PROPERTIES

    class _Cast_CaseHardeningProperties:
        """Special nested class for casting CaseHardeningProperties to subclasses."""

        def __init__(self, parent: 'CaseHardeningProperties'):
            self._parent = parent

        @property
        def case_hardening_properties(self) -> 'CaseHardeningProperties':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CaseHardeningProperties.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth_at_maximum_hardness(self) -> 'float':
        """float: 'DepthAtMaximumHardness' is the original name of this property."""

        temp = self.wrapped.DepthAtMaximumHardness

        if temp is None:
            return 0.0

        return temp

    @depth_at_maximum_hardness.setter
    def depth_at_maximum_hardness(self, value: 'float'):
        self.wrapped.DepthAtMaximumHardness = float(value) if value else 0.0

    @property
    def effective_case_depth(self) -> 'float':
        """float: 'EffectiveCaseDepth' is the original name of this property."""

        temp = self.wrapped.EffectiveCaseDepth

        if temp is None:
            return 0.0

        return temp

    @effective_case_depth.setter
    def effective_case_depth(self, value: 'float'):
        self.wrapped.EffectiveCaseDepth = float(value) if value else 0.0

    @property
    def hardness_profile_calculation_method(self) -> '_1046.HardnessProfileCalculationMethod':
        """HardnessProfileCalculationMethod: 'HardnessProfileCalculationMethod' is the original name of this property."""

        temp = self.wrapped.HardnessProfileCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1046.HardnessProfileCalculationMethod)
        return constructor.new_from_mastapy_type(_1046.HardnessProfileCalculationMethod)(value) if value is not None else None

    @hardness_profile_calculation_method.setter
    def hardness_profile_calculation_method(self, value: '_1046.HardnessProfileCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1046.HardnessProfileCalculationMethod.type_())
        self.wrapped.HardnessProfileCalculationMethod = value

    @property
    def heat_treatment_type(self) -> '_1047.HeatTreatmentType':
        """HeatTreatmentType: 'HeatTreatmentType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeatTreatmentType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1047.HeatTreatmentType)
        return constructor.new_from_mastapy_type(_1047.HeatTreatmentType)(value) if value is not None else None

    @property
    def total_case_depth(self) -> 'float':
        """float: 'TotalCaseDepth' is the original name of this property."""

        temp = self.wrapped.TotalCaseDepth

        if temp is None:
            return 0.0

        return temp

    @total_case_depth.setter
    def total_case_depth(self, value: 'float'):
        self.wrapped.TotalCaseDepth = float(value) if value else 0.0

    @property
    def vickers_hardness_hv_at_effective_case_depth(self) -> 'float':
        """float: 'VickersHardnessHVAtEffectiveCaseDepth' is the original name of this property."""

        temp = self.wrapped.VickersHardnessHVAtEffectiveCaseDepth

        if temp is None:
            return 0.0

        return temp

    @vickers_hardness_hv_at_effective_case_depth.setter
    def vickers_hardness_hv_at_effective_case_depth(self, value: 'float'):
        self.wrapped.VickersHardnessHVAtEffectiveCaseDepth = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CaseHardeningProperties._Cast_CaseHardeningProperties':
        return self._Cast_CaseHardeningProperties(self)
