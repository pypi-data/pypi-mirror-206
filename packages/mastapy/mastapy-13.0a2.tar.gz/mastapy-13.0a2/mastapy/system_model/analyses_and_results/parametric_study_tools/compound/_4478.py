"""_4478.py

GearSetCompoundParametricStudyTool
"""
from typing import List

from mastapy.gears.rating import _358
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4338
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4516
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'GearSetCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundParametricStudyTool',)


class GearSetCompoundParametricStudyTool(_4516.SpecialisedAssemblyCompoundParametricStudyTool):
    """GearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_GearSetCompoundParametricStudyTool:
        """Special nested class for casting GearSetCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'GearSetCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def specialised_assembly_compound_parametric_study_tool(self):
            return self._parent._cast(_4516.SpecialisedAssemblyCompoundParametricStudyTool)

        @property
        def abstract_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4418
            
            return self._parent._cast(_4418.AbstractAssemblyCompoundParametricStudyTool)

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
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4424
            
            return self._parent._cast(_4424.AGMAGleasonConicalGearSetCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4431
            
            return self._parent._cast(_4431.BevelDifferentialGearSetCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4436
            
            return self._parent._cast(_4436.BevelGearSetCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4449
            
            return self._parent._cast(_4449.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4452
            
            return self._parent._cast(_4452.ConicalGearSetCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4467
            
            return self._parent._cast(_4467.CylindricalGearSetCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4473
            
            return self._parent._cast(_4473.FaceGearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4482
            
            return self._parent._cast(_4482.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4486
            
            return self._parent._cast(_4486.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4489
            
            return self._parent._cast(_4489.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4492
            
            return self._parent._cast(_4492.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool)

        @property
        def planetary_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4502
            
            return self._parent._cast(_4502.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4519
            
            return self._parent._cast(_4519.SpiralBevelGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4525
            
            return self._parent._cast(_4525.StraightBevelDiffGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4528
            
            return self._parent._cast(_4528.StraightBevelGearSetCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4543
            
            return self._parent._cast(_4543.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4546
            
            return self._parent._cast(_4546.ZerolBevelGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(self) -> 'GearSetCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_results(self) -> '_358.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases(self) -> 'List[_4338.GearSetParametricStudyTool]':
        """List[GearSetParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4338.GearSetParametricStudyTool]':
        """List[GearSetParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetCompoundParametricStudyTool._Cast_GearSetCompoundParametricStudyTool':
        return self._Cast_GearSetCompoundParametricStudyTool(self)
