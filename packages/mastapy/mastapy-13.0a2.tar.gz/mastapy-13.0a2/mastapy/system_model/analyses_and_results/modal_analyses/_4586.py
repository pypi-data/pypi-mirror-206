"""_4586.py

CouplingHalfModalAnalysis
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2709
from mastapy.system_model.analyses_and_results.modal_analyses import _4631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'CouplingHalfModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfModalAnalysis',)


class CouplingHalfModalAnalysis(_4631.MountableComponentModalAnalysis):
    """CouplingHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MODAL_ANALYSIS

    class _Cast_CouplingHalfModalAnalysis:
        """Special nested class for casting CouplingHalfModalAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingHalfModalAnalysis'):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(self):
            return self._parent._cast(_4631.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572
            
            return self._parent._cast(_4572.ComponentModalAnalysis)

        @property
        def part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635
            
            return self._parent._cast(_4635.PartModalAnalysis)

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
        def clutch_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569
            
            return self._parent._cast(_4569.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574
            
            return self._parent._cast(_4574.ConceptCouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590
            
            return self._parent._cast(_4590.CVTPulleyModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637
            
            return self._parent._cast(_4637.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def pulley_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644
            
            return self._parent._cast(_4644.PulleyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649
            
            return self._parent._cast(_4649.RollingRingModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660
            
            return self._parent._cast(_4660.SpringDamperHalfModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670
            
            return self._parent._cast(_4670.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672
            
            return self._parent._cast(_4672.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673
            
            return self._parent._cast(_4673.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676
            
            return self._parent._cast(_4676.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677
            
            return self._parent._cast(_4677.TorqueConverterTurbineModalAnalysis)

        @property
        def coupling_half_modal_analysis(self) -> 'CouplingHalfModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfModalAnalysis.TYPE'):
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
    def cast_to(self) -> 'CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis':
        return self._Cast_CouplingHalfModalAnalysis(self)
