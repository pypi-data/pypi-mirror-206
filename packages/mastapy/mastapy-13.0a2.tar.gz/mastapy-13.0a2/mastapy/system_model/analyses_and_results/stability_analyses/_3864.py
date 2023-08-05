"""_3864.py

TorqueConverterStabilityAnalysis
"""
from mastapy.system_model.part_model.couplings import _2586
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6937
from mastapy.system_model.analyses_and_results.stability_analyses import _3781
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'TorqueConverterStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterStabilityAnalysis',)


class TorqueConverterStabilityAnalysis(_3781.CouplingStabilityAnalysis):
    """TorqueConverterStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_STABILITY_ANALYSIS

    class _Cast_TorqueConverterStabilityAnalysis:
        """Special nested class for casting TorqueConverterStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterStabilityAnalysis'):
            self._parent = parent

        @property
        def coupling_stability_analysis(self):
            return self._parent._cast(_3781.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3841
            
            return self._parent._cast(_3841.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3742
            
            return self._parent._cast(_3742.AbstractAssemblyStabilityAnalysis)

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
        def torque_converter_stability_analysis(self) -> 'TorqueConverterStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2586.TorqueConverter':
        """TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6937.TorqueConverterLoadCase':
        """TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis':
        return self._Cast_TorqueConverterStabilityAnalysis(self)
