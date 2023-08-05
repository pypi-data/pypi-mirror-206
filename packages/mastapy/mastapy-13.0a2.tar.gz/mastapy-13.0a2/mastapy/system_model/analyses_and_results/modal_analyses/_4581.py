"""_4581.py

ConicalGearSetModalAnalysis
"""
from mastapy.system_model.part_model.gears import _2503
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2704
from mastapy.system_model.analyses_and_results.modal_analyses import _4611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ConicalGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetModalAnalysis',)


class ConicalGearSetModalAnalysis(_4611.GearSetModalAnalysis):
    """ConicalGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_MODAL_ANALYSIS

    class _Cast_ConicalGearSetModalAnalysis:
        """Special nested class for casting ConicalGearSetModalAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearSetModalAnalysis'):
            self._parent = parent

        @property
        def gear_set_modal_analysis(self):
            return self._parent._cast(_4611.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655
            
            return self._parent._cast(_4655.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4547
            
            return self._parent._cast(_4547.AbstractAssemblyModalAnalysis)

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
        def agma_gleason_conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4553
            
            return self._parent._cast(_4553.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4560
            
            return self._parent._cast(_4560.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4565
            
            return self._parent._cast(_4565.BevelGearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615
            
            return self._parent._cast(_4615.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619
            
            return self._parent._cast(_4619.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622
            
            return self._parent._cast(_4622.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625
            
            return self._parent._cast(_4625.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658
            
            return self._parent._cast(_4658.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664
            
            return self._parent._cast(_4664.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667
            
            return self._parent._cast(_4667.StraightBevelGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688
            
            return self._parent._cast(_4688.ZerolBevelGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(self) -> 'ConicalGearSetModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2503.ConicalGearSet':
        """ConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2704.ConicalGearSetSystemDeflection':
        """ConicalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearSetModalAnalysis._Cast_ConicalGearSetModalAnalysis':
        return self._Cast_ConicalGearSetModalAnalysis(self)
