"""_6319.py

MassDiscDynamicAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2442
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6885
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'MassDiscDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscDynamicAnalysis',)


class MassDiscDynamicAnalysis(_6366.VirtualComponentDynamicAnalysis):
    """MassDiscDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_DYNAMIC_ANALYSIS

    class _Cast_MassDiscDynamicAnalysis:
        """Special nested class for casting MassDiscDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'MassDiscDynamicAnalysis'):
            self._parent = parent

        @property
        def virtual_component_dynamic_analysis(self):
            return self._parent._cast(_6366.VirtualComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321
            
            return self._parent._cast(_6321.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6268
            
            return self._parent._cast(_6268.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
            
            return self._parent._cast(_6323.PartDynamicAnalysis)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

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
        def mass_disc_dynamic_analysis(self) -> 'MassDiscDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MassDiscDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2442.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6885.MassDiscLoadCase':
        """MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[MassDiscDynamicAnalysis]':
        """List[MassDiscDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MassDiscDynamicAnalysis._Cast_MassDiscDynamicAnalysis':
        return self._Cast_MassDiscDynamicAnalysis(self)
