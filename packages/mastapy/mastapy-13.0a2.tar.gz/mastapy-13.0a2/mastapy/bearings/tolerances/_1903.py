"""_1903.py

RoundnessSpecification
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.tolerances import _1904, _1910, _1900
from mastapy.math_utility import _1523
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROUNDNESS_SPECIFICATION = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'RoundnessSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('RoundnessSpecification',)


class RoundnessSpecification(_1575.IndependentReportablePropertiesBase['RoundnessSpecification']):
    """RoundnessSpecification

    This is a mastapy class.
    """

    TYPE = _ROUNDNESS_SPECIFICATION

    class _Cast_RoundnessSpecification:
        """Special nested class for casting RoundnessSpecification to subclasses."""

        def __init__(self, parent: 'RoundnessSpecification'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.bearings.tolerances import _1903
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def roundness_specification(self) -> 'RoundnessSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RoundnessSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_first_max_deviation_from_round(self) -> 'float':
        """float: 'AngleOfFirstMaxDeviationFromRound' is the original name of this property."""

        temp = self.wrapped.AngleOfFirstMaxDeviationFromRound

        if temp is None:
            return 0.0

        return temp

    @angle_of_first_max_deviation_from_round.setter
    def angle_of_first_max_deviation_from_round(self, value: 'float'):
        self.wrapped.AngleOfFirstMaxDeviationFromRound = float(value) if value else 0.0

    @property
    def maximum_deviation_from_round(self) -> 'float':
        """float: 'MaximumDeviationFromRound' is the original name of this property."""

        temp = self.wrapped.MaximumDeviationFromRound

        if temp is None:
            return 0.0

        return temp

    @maximum_deviation_from_round.setter
    def maximum_deviation_from_round(self, value: 'float'):
        self.wrapped.MaximumDeviationFromRound = float(value) if value else 0.0

    @property
    def number_of_lobes(self) -> 'int':
        """int: 'NumberOfLobes' is the original name of this property."""

        temp = self.wrapped.NumberOfLobes

        if temp is None:
            return 0

        return temp

    @number_of_lobes.setter
    def number_of_lobes(self, value: 'int'):
        self.wrapped.NumberOfLobes = int(value) if value else 0

    @property
    def specification_type(self) -> '_1904.RoundnessSpecificationType':
        """RoundnessSpecificationType: 'SpecificationType' is the original name of this property."""

        temp = self.wrapped.SpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1904.RoundnessSpecificationType)
        return constructor.new_from_mastapy_type(_1904.RoundnessSpecificationType)(value) if value is not None else None

    @specification_type.setter
    def specification_type(self, value: '_1904.RoundnessSpecificationType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1904.RoundnessSpecificationType.type_())
        self.wrapped.SpecificationType = value

    @property
    def type_of_fit(self) -> '_1910.TypeOfFit':
        """TypeOfFit: 'TypeOfFit' is the original name of this property."""

        temp = self.wrapped.TypeOfFit

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1910.TypeOfFit)
        return constructor.new_from_mastapy_type(_1910.TypeOfFit)(value) if value is not None else None

    @type_of_fit.setter
    def type_of_fit(self, value: '_1910.TypeOfFit'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1910.TypeOfFit.type_())
        self.wrapped.TypeOfFit = value

    @property
    def user_specified_deviation(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'UserSpecifiedDeviation' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @user_specified_deviation.setter
    def user_specified_deviation(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.UserSpecifiedDeviation = value

    @property
    def roundness_distribution(self) -> 'List[_1900.RaceRoundnessAtAngle]':
        """List[RaceRoundnessAtAngle]: 'RoundnessDistribution' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoundnessDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RoundnessSpecification._Cast_RoundnessSpecification':
        return self._Cast_RoundnessSpecification(self)
