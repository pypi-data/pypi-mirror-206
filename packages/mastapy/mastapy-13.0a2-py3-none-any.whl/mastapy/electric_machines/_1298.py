"""_1298.py

TwoDimensionalFEModelForAnalysis
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy.electric_machines import _1258
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TWO_DIMENSIONAL_FE_MODEL_FOR_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines', 'TwoDimensionalFEModelForAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TwoDimensionalFEModelForAnalysis',)


T = TypeVar('T', bound='_1258.ElectricMachineMeshingOptionsBase')


class TwoDimensionalFEModelForAnalysis(_0.APIBase, Generic[T]):
    """TwoDimensionalFEModelForAnalysis

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _TWO_DIMENSIONAL_FE_MODEL_FOR_ANALYSIS

    class _Cast_TwoDimensionalFEModelForAnalysis:
        """Special nested class for casting TwoDimensionalFEModelForAnalysis to subclasses."""

        def __init__(self, parent: 'TwoDimensionalFEModelForAnalysis'):
            self._parent = parent

        @property
        def two_dimensional_fe_model_for_analysis(self) -> 'TwoDimensionalFEModelForAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TwoDimensionalFEModelForAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_elements(self) -> 'int':
        """int: 'NumberOfElements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfElements

        if temp is None:
            return 0

        return temp

    @property
    def number_of_nodes(self) -> 'int':
        """int: 'NumberOfNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfNodes

        if temp is None:
            return 0

        return temp

    @property
    def meshing_options(self) -> 'T':
        """T: 'MeshingOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshingOptions

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TwoDimensionalFEModelForAnalysis._Cast_TwoDimensionalFEModelForAnalysis':
        return self._Cast_TwoDimensionalFEModelForAnalysis(self)
