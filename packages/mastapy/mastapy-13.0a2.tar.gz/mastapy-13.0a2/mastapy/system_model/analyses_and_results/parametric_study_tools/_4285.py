"""_4285.py

BevelDifferentialPlanetGearParametricStudyTool
"""
from mastapy.system_model.part_model.gears import _2496
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BevelDifferentialPlanetGearParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearParametricStudyTool',)


class BevelDifferentialPlanetGearParametricStudyTool(_4283.BevelDifferentialGearParametricStudyTool):
    """BevelDifferentialPlanetGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL

    class _Cast_BevelDifferentialPlanetGearParametricStudyTool:
        """Special nested class for casting BevelDifferentialPlanetGearParametricStudyTool to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGearParametricStudyTool'):
            self._parent = parent

        @property
        def bevel_differential_gear_parametric_study_tool(self):
            return self._parent._cast(_4283.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4288
            
            return self._parent._cast(_4288.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4276
            
            return self._parent._cast(_4276.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4304
            
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
        def bevel_differential_planet_gear_parametric_study_tool(self) -> 'BevelDifferentialPlanetGearParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2496.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialPlanetGearParametricStudyTool._Cast_BevelDifferentialPlanetGearParametricStudyTool':
        return self._Cast_BevelDifferentialPlanetGearParametricStudyTool(self)
