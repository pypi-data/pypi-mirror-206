"""_1536.py

ParetoOptimisationInput
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.math_utility import _1477
from mastapy.math_utility.optimisation import _1546, _1543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_INPUT = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ParetoOptimisationInput')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimisationInput',)


class ParetoOptimisationInput(_1543.ParetoOptimistaionVariable):
    """ParetoOptimisationInput

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_INPUT

    class _Cast_ParetoOptimisationInput:
        """Special nested class for casting ParetoOptimisationInput to subclasses."""

        def __init__(self, parent: 'ParetoOptimisationInput'):
            self._parent = parent

        @property
        def pareto_optimistaion_variable(self):
            return self._parent._cast(_1543.ParetoOptimistaionVariable)

        @property
        def pareto_optimisation_variable_base(self):
            from mastapy.math_utility.optimisation import _1542
            
            return self._parent._cast(_1542.ParetoOptimisationVariableBase)

        @property
        def pareto_optimisation_input(self) -> 'ParetoOptimisationInput':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimisationInput.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_steps(self) -> 'int':
        """int: 'NumberOfSteps' is the original name of this property."""

        temp = self.wrapped.NumberOfSteps

        if temp is None:
            return 0

        return temp

    @number_of_steps.setter
    def number_of_steps(self, value: 'int'):
        self.wrapped.NumberOfSteps = int(value) if value else 0

    @property
    def range(self) -> '_1477.Range':
        """Range: 'Range' is the original name of this property."""

        temp = self.wrapped.Range

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @range.setter
    def range(self, value: '_1477.Range'):
        value = value.wrapped if value else None
        self.wrapped.Range = value

    @property
    def specify_input_range_as(self) -> '_1546.SpecifyOptimisationInputAs':
        """SpecifyOptimisationInputAs: 'SpecifyInputRangeAs' is the original name of this property."""

        temp = self.wrapped.SpecifyInputRangeAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1546.SpecifyOptimisationInputAs)
        return constructor.new_from_mastapy_type(_1546.SpecifyOptimisationInputAs)(value) if value is not None else None

    @specify_input_range_as.setter
    def specify_input_range_as(self, value: '_1546.SpecifyOptimisationInputAs'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1546.SpecifyOptimisationInputAs.type_())
        self.wrapped.SpecifyInputRangeAs = value

    @property
    def cast_to(self) -> 'ParetoOptimisationInput._Cast_ParetoOptimisationInput':
        return self._Cast_ParetoOptimisationInput(self)
