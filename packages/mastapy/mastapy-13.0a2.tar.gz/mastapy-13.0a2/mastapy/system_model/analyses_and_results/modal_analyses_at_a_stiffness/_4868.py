"""_4868.py

CouplingHalfModalAnalysisAtAStiffness
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CouplingHalfModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfModalAnalysisAtAStiffness',)


class CouplingHalfModalAnalysisAtAStiffness(_4908.MountableComponentModalAnalysisAtAStiffness):
    """CouplingHalfModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CouplingHalfModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingHalfModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CouplingHalfModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4908.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4855
            
            return self._parent._cast(_4855.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4910
            
            return self._parent._cast(_4910.PartModalAnalysisAtAStiffness)

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
        def clutch_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4852
            
            return self._parent._cast(_4852.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4857
            
            return self._parent._cast(_4857.ConceptCouplingHalfModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4872
            
            return self._parent._cast(_4872.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4912
            
            return self._parent._cast(_4912.PartToPartShearCouplingHalfModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4919
            
            return self._parent._cast(_4919.PulleyModalAnalysisAtAStiffness)

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4924
            
            return self._parent._cast(_4924.RollingRingModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4934
            
            return self._parent._cast(_4934.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4944
            
            return self._parent._cast(_4944.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4946
            
            return self._parent._cast(_4946.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4947
            
            return self._parent._cast(_4947.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4950
            
            return self._parent._cast(_4950.TorqueConverterPumpModalAnalysisAtAStiffness)

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4951
            
            return self._parent._cast(_4951.TorqueConverterTurbineModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(self) -> 'CouplingHalfModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfModalAnalysisAtAStiffness.TYPE'):
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
    def cast_to(self) -> 'CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness':
        return self._Cast_CouplingHalfModalAnalysisAtAStiffness(self)
