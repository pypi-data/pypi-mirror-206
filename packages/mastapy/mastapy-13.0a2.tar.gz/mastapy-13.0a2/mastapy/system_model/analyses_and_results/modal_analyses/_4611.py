"""_4611.py

GearSetModalAnalysis
"""
from mastapy.system_model.part_model.gears import _2511
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2739
from mastapy.system_model.analyses_and_results.modal_analyses import _4655
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'GearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetModalAnalysis',)


class GearSetModalAnalysis(_4655.SpecialisedAssemblyModalAnalysis):
    """GearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MODAL_ANALYSIS

    class _Cast_GearSetModalAnalysis:
        """Special nested class for casting GearSetModalAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetModalAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(self):
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
        def concept_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578
            
            return self._parent._cast(_4578.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581
            
            return self._parent._cast(_4581.ConicalGearSetModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597
            
            return self._parent._cast(_4597.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605
            
            return self._parent._cast(_4605.FaceGearSetModalAnalysis)

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
        def planetary_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640
            
            return self._parent._cast(_4640.PlanetaryGearSetModalAnalysis)

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
        def worm_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685
            
            return self._parent._cast(_4685.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688
            
            return self._parent._cast(_4688.ZerolBevelGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(self) -> 'GearSetModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2739.GearSetSystemDeflection':
        """GearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetModalAnalysis._Cast_GearSetModalAnalysis':
        return self._Cast_GearSetModalAnalysis(self)
