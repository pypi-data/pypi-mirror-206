"""_5689.py

CouplingHarmonicAnalysis
"""
from mastapy.system_model.part_model.couplings import _2562
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2710
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'CouplingHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHarmonicAnalysis',)


class CouplingHarmonicAnalysis(_5777.SpecialisedAssemblyHarmonicAnalysis):
    """CouplingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HARMONIC_ANALYSIS

    class _Cast_CouplingHarmonicAnalysis:
        """Special nested class for casting CouplingHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingHarmonicAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(self):
            return self._parent._cast(_5777.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5648
            
            return self._parent._cast(_5648.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
            
            return self._parent._cast(_5755.PartHarmonicAnalysis)

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
        def clutch_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5672
            
            return self._parent._cast(_5672.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
            
            return self._parent._cast(_5678.ConceptCouplingHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
            
            return self._parent._cast(_5758.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5784
            
            return self._parent._cast(_5784.SpringDamperHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5799
            
            return self._parent._cast(_5799.TorqueConverterHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(self) -> 'CouplingHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2562.Coupling':
        """Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2710.CouplingSystemDeflection':
        """CouplingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis':
        return self._Cast_CouplingHarmonicAnalysis(self)
