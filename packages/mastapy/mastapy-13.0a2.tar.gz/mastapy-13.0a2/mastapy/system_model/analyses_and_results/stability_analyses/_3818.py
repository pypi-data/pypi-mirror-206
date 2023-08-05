"""_3818.py

MassDiscStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2442
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6885
from mastapy.system_model.analyses_and_results.stability_analyses import _3867
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'MassDiscStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscStabilityAnalysis',)


class MassDiscStabilityAnalysis(_3867.VirtualComponentStabilityAnalysis):
    """MassDiscStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_STABILITY_ANALYSIS

    class _Cast_MassDiscStabilityAnalysis:
        """Special nested class for casting MassDiscStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'MassDiscStabilityAnalysis'):
            self._parent = parent

        @property
        def virtual_component_stability_analysis(self):
            return self._parent._cast(_3867.VirtualComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3820
            
            return self._parent._cast(_3820.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3767
            
            return self._parent._cast(_3767.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3822
            
            return self._parent._cast(_3822.PartStabilityAnalysis)

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
        def mass_disc_stability_analysis(self) -> 'MassDiscStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MassDiscStabilityAnalysis.TYPE'):
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
    def planetaries(self) -> 'List[MassDiscStabilityAnalysis]':
        """List[MassDiscStabilityAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MassDiscStabilityAnalysis._Cast_MassDiscStabilityAnalysis':
        return self._Cast_MassDiscStabilityAnalysis(self)
