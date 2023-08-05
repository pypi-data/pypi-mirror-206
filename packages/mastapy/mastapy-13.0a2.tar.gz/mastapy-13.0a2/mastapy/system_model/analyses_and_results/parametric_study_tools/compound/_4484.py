"""_4484.py

KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4345
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4450
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool',)


class KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool(_4450.ConicalGearCompoundParametricStudyTool):
    """KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def conical_gear_compound_parametric_study_tool(self):
            return self._parent._cast(_4450.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4476
            
            return self._parent._cast(_4476.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4495
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4487
            
            return self._parent._cast(_4487.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4490
            
            return self._parent._cast(_4490.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4345.KlingelnbergCycloPalloidConicalGearParametricStudyTool]':
        """List[KlingelnbergCycloPalloidConicalGearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4345.KlingelnbergCycloPalloidConicalGearParametricStudyTool]':
        """List[KlingelnbergCycloPalloidConicalGearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool':
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool(self)
