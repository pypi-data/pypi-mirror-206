"""_96.py

NonDimensionalInputComponent
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.varying_input_components import _92
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_DIMENSIONAL_INPUT_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.VaryingInputComponents', 'NonDimensionalInputComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('NonDimensionalInputComponent',)


class NonDimensionalInputComponent(_92.AbstractVaryingInputComponent):
    """NonDimensionalInputComponent

    This is a mastapy class.
    """

    TYPE = _NON_DIMENSIONAL_INPUT_COMPONENT

    class _Cast_NonDimensionalInputComponent:
        """Special nested class for casting NonDimensionalInputComponent to subclasses."""

        def __init__(self, parent: 'NonDimensionalInputComponent'):
            self._parent = parent

        @property
        def abstract_varying_input_component(self):
            return self._parent._cast(_92.AbstractVaryingInputComponent)

        @property
        def non_dimensional_input_component(self) -> 'NonDimensionalInputComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NonDimensionalInputComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def non_dimensional_quantity(self) -> 'float':
        """float: 'NonDimensionalQuantity' is the original name of this property."""

        temp = self.wrapped.NonDimensionalQuantity

        if temp is None:
            return 0.0

        return temp

    @non_dimensional_quantity.setter
    def non_dimensional_quantity(self, value: 'float'):
        self.wrapped.NonDimensionalQuantity = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'NonDimensionalInputComponent._Cast_NonDimensionalInputComponent':
        return self._Cast_NonDimensionalInputComponent(self)
