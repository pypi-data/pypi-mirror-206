"""_6227.py

VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6098
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation',)


class VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(_6182.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation):
    """VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6182.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6130
            
            return self._parent._cast(_6130.ComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6184
            
            return self._parent._cast(_6184.PartCompoundHarmonicAnalysisOfSingleExcitation)

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
        def mass_disc_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6180
            
            return self._parent._cast(_6180.MassDiscCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6181
            
            return self._parent._cast(_6181.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6191
            
            return self._parent._cast(_6191.PointLoadCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6192
            
            return self._parent._cast(_6192.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6226
            
            return self._parent._cast(_6226.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(self) -> 'VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6098.VirtualComponentHarmonicAnalysisOfSingleExcitation]':
        """List[VirtualComponentHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6098.VirtualComponentHarmonicAnalysisOfSingleExcitation]':
        """List[VirtualComponentHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(self)
