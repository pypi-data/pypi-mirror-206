"""_6691.py

ExternalCADModelCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2432
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6562
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'ExternalCADModelCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelCompoundCriticalSpeedAnalysis',)


class ExternalCADModelCompoundCriticalSpeedAnalysis(_6664.ComponentCompoundCriticalSpeedAnalysis):
    """ExternalCADModelCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_ExternalCADModelCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ExternalCADModelCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ExternalCADModelCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def component_compound_critical_speed_analysis(self):
            return self._parent._cast(_6664.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6718
            
            return self._parent._cast(_6718.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(self) -> 'ExternalCADModelCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExternalCADModelCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2432.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6562.ExternalCADModelCriticalSpeedAnalysis]':
        """List[ExternalCADModelCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6562.ExternalCADModelCriticalSpeedAnalysis]':
        """List[ExternalCADModelCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ExternalCADModelCompoundCriticalSpeedAnalysis._Cast_ExternalCADModelCompoundCriticalSpeedAnalysis':
        return self._Cast_ExternalCADModelCompoundCriticalSpeedAnalysis(self)
