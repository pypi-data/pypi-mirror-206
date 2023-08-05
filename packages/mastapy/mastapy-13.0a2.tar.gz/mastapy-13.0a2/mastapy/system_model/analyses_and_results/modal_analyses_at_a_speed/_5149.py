"""_5149.py

GearSetModalAnalysisAtASpeed
"""
from mastapy.system_model.part_model.gears import _2511
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5187
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'GearSetModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetModalAnalysisAtASpeed',)


class GearSetModalAnalysisAtASpeed(_5187.SpecialisedAssemblyModalAnalysisAtASpeed):
    """GearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_GearSetModalAnalysisAtASpeed:
        """Special nested class for casting GearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'GearSetModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5187.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5089
            
            return self._parent._cast(_5089.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5168
            
            return self._parent._cast(_5168.PartModalAnalysisAtASpeed)

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
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5095
            
            return self._parent._cast(_5095.AGMAGleasonConicalGearSetModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5102
            
            return self._parent._cast(_5102.BevelDifferentialGearSetModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5107
            
            return self._parent._cast(_5107.BevelGearSetModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5120
            
            return self._parent._cast(_5120.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5123
            
            return self._parent._cast(_5123.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5138
            
            return self._parent._cast(_5138.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5144
            
            return self._parent._cast(_5144.FaceGearSetModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5153
            
            return self._parent._cast(_5153.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5157
            
            return self._parent._cast(_5157.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5160
            
            return self._parent._cast(_5160.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5163
            
            return self._parent._cast(_5163.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5173
            
            return self._parent._cast(_5173.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5190
            
            return self._parent._cast(_5190.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5196
            
            return self._parent._cast(_5196.StraightBevelDiffGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5199
            
            return self._parent._cast(_5199.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5214
            
            return self._parent._cast(_5214.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5217
            
            return self._parent._cast(_5217.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(self) -> 'GearSetModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2511.GearSet':
        """GearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetModalAnalysisAtASpeed._Cast_GearSetModalAnalysisAtASpeed':
        return self._Cast_GearSetModalAnalysisAtASpeed(self)
