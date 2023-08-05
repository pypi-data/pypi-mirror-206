"""_4712.py

BevelDifferentialGearCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2494
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4559
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4717
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'BevelDifferentialGearCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearCompoundModalAnalysis',)


class BevelDifferentialGearCompoundModalAnalysis(_4717.BevelGearCompoundModalAnalysis):
    """BevelDifferentialGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS

    class _Cast_BevelDifferentialGearCompoundModalAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearCompoundModalAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis(self):
            return self._parent._cast(_4717.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4705
            
            return self._parent._cast(_4705.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4733
            
            return self._parent._cast(_4733.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
            
            return self._parent._cast(_4759.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4778
            
            return self._parent._cast(_4778.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4726
            
            return self._parent._cast(_4726.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
            
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

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
        def bevel_differential_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4715
            
            return self._parent._cast(_4715.BevelDifferentialPlanetGearCompoundModalAnalysis)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4716
            
            return self._parent._cast(_4716.BevelDifferentialSunGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(self) -> 'BevelDifferentialGearCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2494.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4559.BevelDifferentialGearModalAnalysis]':
        """List[BevelDifferentialGearModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4559.BevelDifferentialGearModalAnalysis]':
        """List[BevelDifferentialGearModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis':
        return self._Cast_BevelDifferentialGearCompoundModalAnalysis(self)
