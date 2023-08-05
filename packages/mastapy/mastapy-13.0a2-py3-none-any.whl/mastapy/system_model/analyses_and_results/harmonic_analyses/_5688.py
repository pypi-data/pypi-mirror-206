"""_5688.py

CouplingHalfHarmonicAnalysis
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2709
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'CouplingHalfHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfHarmonicAnalysis',)


class CouplingHalfHarmonicAnalysis(_5753.MountableComponentHarmonicAnalysis):
    """CouplingHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS

    class _Cast_CouplingHalfHarmonicAnalysis:
        """Special nested class for casting CouplingHalfHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingHalfHarmonicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(self):
            return self._parent._cast(_5753.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5675
            
            return self._parent._cast(_5675.ComponentHarmonicAnalysis)

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
        def clutch_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5671
            
            return self._parent._cast(_5671.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5677
            
            return self._parent._cast(_5677.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5692
            
            return self._parent._cast(_5692.CVTPulleyHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5757
            
            return self._parent._cast(_5757.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5765
            
            return self._parent._cast(_5765.PulleyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5771
            
            return self._parent._cast(_5771.RollingRingHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
            
            return self._parent._cast(_5783.SpringDamperHalfHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
            
            return self._parent._cast(_5794.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
            
            return self._parent._cast(_5796.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5797
            
            return self._parent._cast(_5797.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800
            
            return self._parent._cast(_5800.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5801
            
            return self._parent._cast(_5801.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(self) -> 'CouplingHalfHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2563.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2709.CouplingHalfSystemDeflection':
        """CouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis':
        return self._Cast_CouplingHalfHarmonicAnalysis(self)
