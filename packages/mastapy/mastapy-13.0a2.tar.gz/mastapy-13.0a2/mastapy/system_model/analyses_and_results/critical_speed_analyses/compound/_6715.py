"""_6715.py

MeasurementComponentCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2443
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6761
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'MeasurementComponentCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentCompoundCriticalSpeedAnalysis',)


class MeasurementComponentCompoundCriticalSpeedAnalysis(_6761.VirtualComponentCompoundCriticalSpeedAnalysis):
    """MeasurementComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_MeasurementComponentCompoundCriticalSpeedAnalysis:
        """Special nested class for casting MeasurementComponentCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'MeasurementComponentCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def virtual_component_compound_critical_speed_analysis(self):
            return self._parent._cast(_6761.VirtualComponentCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6716
            
            return self._parent._cast(_6716.MountableComponentCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
            
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
        def measurement_component_compound_critical_speed_analysis(self) -> 'MeasurementComponentCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementComponentCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2443.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6586.MeasurementComponentCriticalSpeedAnalysis]':
        """List[MeasurementComponentCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6586.MeasurementComponentCriticalSpeedAnalysis]':
        """List[MeasurementComponentCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MeasurementComponentCompoundCriticalSpeedAnalysis._Cast_MeasurementComponentCompoundCriticalSpeedAnalysis':
        return self._Cast_MeasurementComponentCompoundCriticalSpeedAnalysis(self)
