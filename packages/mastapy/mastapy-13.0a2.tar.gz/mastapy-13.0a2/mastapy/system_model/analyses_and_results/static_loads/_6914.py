"""_6914.py

ShaftLoadCase
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2462
from mastapy.system_model.analyses_and_results.static_loads import _6772
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftLoadCase',)


class ShaftLoadCase(_6772.AbstractShaftLoadCase):
    """ShaftLoadCase

    This is a mastapy class.
    """

    TYPE = _SHAFT_LOAD_CASE

    class _Cast_ShaftLoadCase:
        """Special nested class for casting ShaftLoadCase to subclasses."""

        def __init__(self, parent: 'ShaftLoadCase'):
            self._parent = parent

        @property
        def abstract_shaft_load_case(self):
            return self._parent._cast(_6772.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6773
            
            return self._parent._cast(_6773.AbstractShaftOrHousingLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def shaft_load_case(self) -> 'ShaftLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_scaling_factor(self) -> 'float':
        """float: 'DiameterScalingFactor' is the original name of this property."""

        temp = self.wrapped.DiameterScalingFactor

        if temp is None:
            return 0.0

        return temp

    @diameter_scaling_factor.setter
    def diameter_scaling_factor(self, value: 'float'):
        self.wrapped.DiameterScalingFactor = float(value) if value else 0.0

    @property
    def component_design(self) -> '_2462.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftLoadCase]':
        """List[ShaftLoadCase]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftLoadCase._Cast_ShaftLoadCase':
        return self._Cast_ShaftLoadCase(self)
