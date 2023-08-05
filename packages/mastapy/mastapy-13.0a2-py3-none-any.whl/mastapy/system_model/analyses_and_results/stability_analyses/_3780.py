"""_3780.py

CouplingHalfStabilityAnalysis
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'CouplingHalfStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfStabilityAnalysis',)


class CouplingHalfStabilityAnalysis(_3820.MountableComponentStabilityAnalysis):
    """CouplingHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STABILITY_ANALYSIS

    class _Cast_CouplingHalfStabilityAnalysis:
        """Special nested class for casting CouplingHalfStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingHalfStabilityAnalysis'):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(self):
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
        def clutch_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3764
            
            return self._parent._cast(_3764.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3769
            
            return self._parent._cast(_3769.ConceptCouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3784
            
            return self._parent._cast(_3784.CVTPulleyStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3824
            
            return self._parent._cast(_3824.PartToPartShearCouplingHalfStabilityAnalysis)

        @property
        def pulley_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3831
            
            return self._parent._cast(_3831.PulleyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3836
            
            return self._parent._cast(_3836.RollingRingStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3846
            
            return self._parent._cast(_3846.SpringDamperHalfStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3858
            
            return self._parent._cast(_3858.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3859
            
            return self._parent._cast(_3859.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3860
            
            return self._parent._cast(_3860.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3863
            
            return self._parent._cast(_3863.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3865
            
            return self._parent._cast(_3865.TorqueConverterTurbineStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(self) -> 'CouplingHalfStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis':
        return self._Cast_CouplingHalfStabilityAnalysis(self)
