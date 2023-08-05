"""_5869.py

ClutchHalfCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2558
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5671
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5885
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ClutchHalfCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfCompoundHarmonicAnalysis',)


class ClutchHalfCompoundHarmonicAnalysis(_5885.CouplingHalfCompoundHarmonicAnalysis):
    """ClutchHalfCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_ClutchHalfCompoundHarmonicAnalysis:
        """Special nested class for casting ClutchHalfCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ClutchHalfCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(self):
            return self._parent._cast(_5885.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5923
            
            return self._parent._cast(_5923.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5871
            
            return self._parent._cast(_5871.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.PartCompoundHarmonicAnalysis)

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
        def clutch_half_compound_harmonic_analysis(self) -> 'ClutchHalfCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchHalfCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2558.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5671.ClutchHalfHarmonicAnalysis]':
        """List[ClutchHalfHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5671.ClutchHalfHarmonicAnalysis]':
        """List[ClutchHalfHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis':
        return self._Cast_ClutchHalfCompoundHarmonicAnalysis(self)
