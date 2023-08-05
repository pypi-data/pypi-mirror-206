"""_3045.py

PartToPartShearCouplingSteadyStateSynchronousResponse
"""
from mastapy.system_model.part_model.couplings import _2567
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6895
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3001
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'PartToPartShearCouplingSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingSteadyStateSynchronousResponse',)


class PartToPartShearCouplingSteadyStateSynchronousResponse(_3001.CouplingSteadyStateSynchronousResponse):
    """PartToPartShearCouplingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_PartToPartShearCouplingSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response(self):
            return self._parent._cast(_3001.CouplingSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3061
            
            return self._parent._cast(_3061.SpecialisedAssemblySteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2962
            
            return self._parent._cast(_2962.AbstractAssemblySteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
            
            return self._parent._cast(_3042.PartSteadyStateSynchronousResponse)

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
        def part_to_part_shear_coupling_steady_state_synchronous_response(self) -> 'PartToPartShearCouplingSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2567.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6895.PartToPartShearCouplingLoadCase':
        """PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse':
        return self._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse(self)
