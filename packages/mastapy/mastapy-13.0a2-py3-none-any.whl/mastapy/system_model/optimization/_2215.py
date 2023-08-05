"""_2215.py

CylindricalGearOptimizationStep
"""
from mastapy._internal import constructor
from mastapy.system_model.optimization import _2219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_OPTIMIZATION_STEP = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'CylindricalGearOptimizationStep')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearOptimizationStep',)


class CylindricalGearOptimizationStep(_2219.OptimizationStep):
    """CylindricalGearOptimizationStep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_OPTIMIZATION_STEP

    class _Cast_CylindricalGearOptimizationStep:
        """Special nested class for casting CylindricalGearOptimizationStep to subclasses."""

        def __init__(self, parent: 'CylindricalGearOptimizationStep'):
            self._parent = parent

        @property
        def optimization_step(self):
            return self._parent._cast(_2219.OptimizationStep)

        @property
        def cylindrical_gear_optimization_step(self) -> 'CylindricalGearOptimizationStep':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearOptimizationStep.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_extended_tip_contact(self) -> 'bool':
        """bool: 'IncludeExtendedTipContact' is the original name of this property."""

        temp = self.wrapped.IncludeExtendedTipContact

        if temp is None:
            return False

        return temp

    @include_extended_tip_contact.setter
    def include_extended_tip_contact(self, value: 'bool'):
        self.wrapped.IncludeExtendedTipContact = bool(value) if value else False

    @property
    def include_tip_edge_stresses(self) -> 'bool':
        """bool: 'IncludeTipEdgeStresses' is the original name of this property."""

        temp = self.wrapped.IncludeTipEdgeStresses

        if temp is None:
            return False

        return temp

    @include_tip_edge_stresses.setter
    def include_tip_edge_stresses(self, value: 'bool'):
        self.wrapped.IncludeTipEdgeStresses = bool(value) if value else False

    @property
    def use_advanced_ltca(self) -> 'bool':
        """bool: 'UseAdvancedLTCA' is the original name of this property."""

        temp = self.wrapped.UseAdvancedLTCA

        if temp is None:
            return False

        return temp

    @use_advanced_ltca.setter
    def use_advanced_ltca(self, value: 'bool'):
        self.wrapped.UseAdvancedLTCA = bool(value) if value else False

    @property
    def cast_to(self) -> 'CylindricalGearOptimizationStep._Cast_CylindricalGearOptimizationStep':
        return self._Cast_CylindricalGearOptimizationStep(self)
