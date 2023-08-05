"""_4476.py

GearCompoundParametricStudyTool
"""
from typing import List

from mastapy.gears.rating import _354
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4495
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'GearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundParametricStudyTool',)


class GearCompoundParametricStudyTool(_4495.MountableComponentCompoundParametricStudyTool):
    """GearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_GearCompoundParametricStudyTool:
        """Special nested class for casting GearCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'GearCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(self):
            return self._parent._cast(_4495.MountableComponentCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4443
            
            return self._parent._cast(_4443.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4497
            
            return self._parent._cast(_4497.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4422
            
            return self._parent._cast(_4422.AGMAGleasonConicalGearCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4429
            
            return self._parent._cast(_4429.BevelDifferentialGearCompoundParametricStudyTool)

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4432
            
            return self._parent._cast(_4432.BevelDifferentialPlanetGearCompoundParametricStudyTool)

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4433
            
            return self._parent._cast(_4433.BevelDifferentialSunGearCompoundParametricStudyTool)

        @property
        def bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4434
            
            return self._parent._cast(_4434.BevelGearCompoundParametricStudyTool)

        @property
        def concept_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4447
            
            return self._parent._cast(_4447.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4450
            
            return self._parent._cast(_4450.ConicalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4465
            
            return self._parent._cast(_4465.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4468
            
            return self._parent._cast(_4468.CylindricalPlanetGearCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4471
            
            return self._parent._cast(_4471.FaceGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4480
            
            return self._parent._cast(_4480.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4484
            
            return self._parent._cast(_4484.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4487
            
            return self._parent._cast(_4487.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4490
            
            return self._parent._cast(_4490.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4517
            
            return self._parent._cast(_4517.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4523
            
            return self._parent._cast(_4523.StraightBevelDiffGearCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4526
            
            return self._parent._cast(_4526.StraightBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4529
            
            return self._parent._cast(_4529.StraightBevelPlanetGearCompoundParametricStudyTool)

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4530
            
            return self._parent._cast(_4530.StraightBevelSunGearCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4541
            
            return self._parent._cast(_4541.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4544
            
            return self._parent._cast(_4544.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(self) -> 'GearCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_results(self) -> '_354.GearDutyCycleRating':
        """GearDutyCycleRating: 'GearDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_4337.GearParametricStudyTool]':
        """List[GearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4337.GearParametricStudyTool]':
        """List[GearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool':
        return self._Cast_GearCompoundParametricStudyTool(self)
