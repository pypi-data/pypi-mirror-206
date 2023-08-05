"""_4345.py

KlingelnbergCycloPalloidConicalGearParametricStudyTool
"""
from mastapy.system_model.part_model.gears import _2515
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'KlingelnbergCycloPalloidConicalGearParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearParametricStudyTool',)


class KlingelnbergCycloPalloidConicalGearParametricStudyTool(_4304.ConicalGearParametricStudyTool):
    """KlingelnbergCycloPalloidConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL

    class _Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearParametricStudyTool to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearParametricStudyTool'):
            self._parent = parent

        @property
        def conical_gear_parametric_study_tool(self):
            return self._parent._cast(_4304.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337
            
            return self._parent._cast(_4337.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4356
            
            return self._parent._cast(_4356.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
            
            return self._parent._cast(_4296.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4368
            
            return self._parent._cast(_4368.PartParametricStudyTool)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4348
            
            return self._parent._cast(_4348.KlingelnbergCycloPalloidHypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4351
            
            return self._parent._cast(_4351.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(self) -> 'KlingelnbergCycloPalloidConicalGearParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2515.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool':
        return self._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool(self)
