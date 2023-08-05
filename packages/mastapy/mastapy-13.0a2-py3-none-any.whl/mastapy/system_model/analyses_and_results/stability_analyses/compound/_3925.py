"""_3925.py

DatumCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2428
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3794
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'DatumCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundStabilityAnalysis',)


class DatumCompoundStabilityAnalysis(_3899.ComponentCompoundStabilityAnalysis):
    """DatumCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_STABILITY_ANALYSIS

    class _Cast_DatumCompoundStabilityAnalysis:
        """Special nested class for casting DatumCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'DatumCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def component_compound_stability_analysis(self):
            return self._parent._cast(_3899.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.PartCompoundStabilityAnalysis)

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
        def datum_compound_stability_analysis(self) -> 'DatumCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DatumCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2428.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3794.DatumStabilityAnalysis]':
        """List[DatumStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3794.DatumStabilityAnalysis]':
        """List[DatumStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DatumCompoundStabilityAnalysis._Cast_DatumCompoundStabilityAnalysis':
        return self._Cast_DatumCompoundStabilityAnalysis(self)
