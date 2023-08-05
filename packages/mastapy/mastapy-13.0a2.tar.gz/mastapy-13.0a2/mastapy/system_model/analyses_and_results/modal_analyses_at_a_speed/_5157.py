"""_5157.py

KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
"""
from mastapy.system_model.part_model.gears import _2516
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed',)


class KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed(_5123.ConicalGearSetModalAnalysisAtASpeed):
    """KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5123.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5149
            
            return self._parent._cast(_5149.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5187
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5160
            
            return self._parent._cast(_5160.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5163
            
            return self._parent._cast(_5163.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(self) -> 'KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2516.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed':
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed(self)
