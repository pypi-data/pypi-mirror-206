"""_4359.py

ParametricStudyDOEResultVariable
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.math_utility.optimisation import _1544, _1542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_DOE_RESULT_VARIABLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ParametricStudyDOEResultVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('ParametricStudyDOEResultVariable',)


class ParametricStudyDOEResultVariable(_1542.ParetoOptimisationVariableBase):
    """ParametricStudyDOEResultVariable

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_DOE_RESULT_VARIABLE

    class _Cast_ParametricStudyDOEResultVariable:
        """Special nested class for casting ParametricStudyDOEResultVariable to subclasses."""

        def __init__(self, parent: 'ParametricStudyDOEResultVariable'):
            self._parent = parent

        @property
        def pareto_optimisation_variable_base(self):
            return self._parent._cast(_1542.ParetoOptimisationVariableBase)

        @property
        def parametric_study_doe_result_variable(self) -> 'ParametricStudyDOEResultVariable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParametricStudyDOEResultVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def entity_name(self) -> 'str':
        """str: 'EntityName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EntityName

        if temp is None:
            return ''

        return temp

    @property
    def parameter_name(self) -> 'str':
        """str: 'ParameterName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParameterName

        if temp is None:
            return ''

        return temp

    @property
    def target(self) -> '_1544.PropertyTargetForDominantCandidateSearch':
        """PropertyTargetForDominantCandidateSearch: 'Target' is the original name of this property."""

        temp = self.wrapped.Target

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1544.PropertyTargetForDominantCandidateSearch)
        return constructor.new_from_mastapy_type(_1544.PropertyTargetForDominantCandidateSearch)(value) if value is not None else None

    @target.setter
    def target(self, value: '_1544.PropertyTargetForDominantCandidateSearch'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1544.PropertyTargetForDominantCandidateSearch.type_())
        self.wrapped.Target = value

    @property
    def cast_to(self) -> 'ParametricStudyDOEResultVariable._Cast_ParametricStudyDOEResultVariable':
        return self._Cast_ParametricStudyDOEResultVariable(self)
