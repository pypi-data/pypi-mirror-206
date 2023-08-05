"""_6899.py

PlanetCarrierLoadCase
"""
from typing import List

from mastapy.system_model.part_model import _2449
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898, _6888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetCarrierLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierLoadCase',)


class PlanetCarrierLoadCase(_6888.MountableComponentLoadCase):
    """PlanetCarrierLoadCase

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_LOAD_CASE

    class _Cast_PlanetCarrierLoadCase:
        """Special nested class for casting PlanetCarrierLoadCase to subclasses."""

        def __init__(self, parent: 'PlanetCarrierLoadCase'):
            self._parent = parent

        @property
        def mountable_component_load_case(self):
            return self._parent._cast(_6888.MountableComponentLoadCase)

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
        def planet_carrier_load_case(self) -> 'PlanetCarrierLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetCarrierLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2449.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planet_manufacture_errors(self) -> 'List[_6898.PlanetarySocketManufactureError]':
        """List[PlanetarySocketManufactureError]: 'PlanetManufactureErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetManufactureErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase':
        return self._Cast_PlanetCarrierLoadCase(self)
