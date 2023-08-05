"""_5687.py

CouplingConnectionHarmonicAnalysis
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2708
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'CouplingConnectionHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionHarmonicAnalysis',)


class CouplingConnectionHarmonicAnalysis(_5741.InterMountableComponentConnectionHarmonicAnalysis):
    """CouplingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_CouplingConnectionHarmonicAnalysis:
        """Special nested class for casting CouplingConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis(self):
            return self._parent._cast(_5741.InterMountableComponentConnectionHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685
            
            return self._parent._cast(_5685.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def clutch_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5670
            
            return self._parent._cast(_5670.ClutchConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5676
            
            return self._parent._cast(_5676.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5756
            
            return self._parent._cast(_5756.PartToPartShearCouplingConnectionHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
            
            return self._parent._cast(_5782.SpringDamperConnectionHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5798
            
            return self._parent._cast(_5798.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(self) -> 'CouplingConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2708.CouplingConnectionSystemDeflection':
        """CouplingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis':
        return self._Cast_CouplingConnectionHarmonicAnalysis(self)
