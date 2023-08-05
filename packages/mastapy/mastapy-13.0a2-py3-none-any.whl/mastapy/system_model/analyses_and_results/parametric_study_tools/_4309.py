"""_4309.py

CouplingHalfParametricStudyTool
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4356
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CouplingHalfParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfParametricStudyTool',)


class CouplingHalfParametricStudyTool(_4356.MountableComponentParametricStudyTool):
    """CouplingHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_PARAMETRIC_STUDY_TOOL

    class _Cast_CouplingHalfParametricStudyTool:
        """Special nested class for casting CouplingHalfParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CouplingHalfParametricStudyTool'):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(self):
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
        def clutch_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4293
            
            return self._parent._cast(_4293.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298
            
            return self._parent._cast(_4298.ConceptCouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
            
            return self._parent._cast(_4313.CVTPulleyParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4370
            
            return self._parent._cast(_4370.PartToPartShearCouplingHalfParametricStudyTool)

        @property
        def pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4377
            
            return self._parent._cast(_4377.PulleyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
            
            return self._parent._cast(_4382.RollingRingParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4392
            
            return self._parent._cast(_4392.SpringDamperHalfParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
            
            return self._parent._cast(_4402.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4404
            
            return self._parent._cast(_4404.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4405
            
            return self._parent._cast(_4405.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4408
            
            return self._parent._cast(_4408.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409
            
            return self._parent._cast(_4409.TorqueConverterTurbineParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(self) -> 'CouplingHalfParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2563.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool':
        return self._Cast_CouplingHalfParametricStudyTool(self)
