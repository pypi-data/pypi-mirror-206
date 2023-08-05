"""_1543.py

ParetoOptimistaionVariable
"""
from mastapy.math_utility.optimisation import _1544, _1542
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISTAION_VARIABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ParetoOptimistaionVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimistaionVariable',)


class ParetoOptimistaionVariable(_1542.ParetoOptimisationVariableBase):
    """ParetoOptimistaionVariable

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISTAION_VARIABLE

    class _Cast_ParetoOptimistaionVariable:
        """Special nested class for casting ParetoOptimistaionVariable to subclasses."""

        def __init__(self, parent: 'ParetoOptimistaionVariable'):
            self._parent = parent

        @property
        def pareto_optimisation_variable_base(self):
            return self._parent._cast(_1542.ParetoOptimisationVariableBase)

        @property
        def pareto_optimisation_input(self):
            from mastapy.math_utility.optimisation import _1536
            
            return self._parent._cast(_1536.ParetoOptimisationInput)

        @property
        def pareto_optimisation_output(self):
            from mastapy.math_utility.optimisation import _1537
            
            return self._parent._cast(_1537.ParetoOptimisationOutput)

        @property
        def pareto_optimistaion_variable(self) -> 'ParetoOptimistaionVariable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimistaionVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def property_target_for_dominant_candidate_search(self) -> '_1544.PropertyTargetForDominantCandidateSearch':
        """PropertyTargetForDominantCandidateSearch: 'PropertyTargetForDominantCandidateSearch' is the original name of this property."""

        temp = self.wrapped.PropertyTargetForDominantCandidateSearch

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1544.PropertyTargetForDominantCandidateSearch)
        return constructor.new_from_mastapy_type(_1544.PropertyTargetForDominantCandidateSearch)(value) if value is not None else None

    @property_target_for_dominant_candidate_search.setter
    def property_target_for_dominant_candidate_search(self, value: '_1544.PropertyTargetForDominantCandidateSearch'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1544.PropertyTargetForDominantCandidateSearch.type_())
        self.wrapped.PropertyTargetForDominantCandidateSearch = value

    @property
    def cast_to(self) -> 'ParetoOptimistaionVariable._Cast_ParetoOptimistaionVariable':
        return self._Cast_ParetoOptimistaionVariable(self)
