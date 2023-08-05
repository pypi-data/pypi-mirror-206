"""_5148.py

GearModalAnalysisAtASpeed
"""
from mastapy.system_model.part_model.gears import _2509
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5166
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'GearModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('GearModalAnalysisAtASpeed',)


class GearModalAnalysisAtASpeed(_5166.MountableComponentModalAnalysisAtASpeed):
    """GearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_GearModalAnalysisAtASpeed:
        """Special nested class for casting GearModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'GearModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5166.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5114
            
            return self._parent._cast(_5114.ComponentModalAnalysisAtASpeed)

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
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5094
            
            return self._parent._cast(_5094.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5101
            
            return self._parent._cast(_5101.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5103
            
            return self._parent._cast(_5103.BevelDifferentialPlanetGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5104
            
            return self._parent._cast(_5104.BevelDifferentialSunGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5106
            
            return self._parent._cast(_5106.BevelGearModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5119
            
            return self._parent._cast(_5119.ConceptGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5122
            
            return self._parent._cast(_5122.ConicalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5137
            
            return self._parent._cast(_5137.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5139
            
            return self._parent._cast(_5139.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5143
            
            return self._parent._cast(_5143.FaceGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5152
            
            return self._parent._cast(_5152.HypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5156
            
            return self._parent._cast(_5156.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5159
            
            return self._parent._cast(_5159.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5162
            
            return self._parent._cast(_5162.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5189
            
            return self._parent._cast(_5189.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5195
            
            return self._parent._cast(_5195.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5198
            
            return self._parent._cast(_5198.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5200
            
            return self._parent._cast(_5200.StraightBevelPlanetGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5201
            
            return self._parent._cast(_5201.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5213
            
            return self._parent._cast(_5213.WormGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
            
            return self._parent._cast(_5216.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(self) -> 'GearModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2509.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearModalAnalysisAtASpeed._Cast_GearModalAnalysisAtASpeed':
        return self._Cast_GearModalAnalysisAtASpeed(self)
