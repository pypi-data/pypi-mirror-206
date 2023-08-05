"""_6816.py

CouplingHalfLoadCase
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingHalfLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfLoadCase',)


class CouplingHalfLoadCase(_6888.MountableComponentLoadCase):
    """CouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_LOAD_CASE

    class _Cast_CouplingHalfLoadCase:
        """Special nested class for casting CouplingHalfLoadCase to subclasses."""

        def __init__(self, parent: 'CouplingHalfLoadCase'):
            self._parent = parent

        @property
        def mountable_component_load_case(self):
            return self._parent._cast(_6888.MountableComponentLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

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
        def clutch_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6798
            
            return self._parent._cast(_6798.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6803
            
            return self._parent._cast(_6803.ConceptCouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6820
            
            return self._parent._cast(_6820.CVTPulleyLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6894
            
            return self._parent._cast(_6894.PartToPartShearCouplingHalfLoadCase)

        @property
        def pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6904
            
            return self._parent._cast(_6904.PulleyLoadCase)

        @property
        def rolling_ring_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6911
            
            return self._parent._cast(_6911.RollingRingLoadCase)

        @property
        def spring_damper_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6921
            
            return self._parent._cast(_6921.SpringDamperHalfLoadCase)

        @property
        def synchroniser_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6931
            
            return self._parent._cast(_6931.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6933
            
            return self._parent._cast(_6933.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6934
            
            return self._parent._cast(_6934.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6938
            
            return self._parent._cast(_6938.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6939
            
            return self._parent._cast(_6939.TorqueConverterTurbineLoadCase)

        @property
        def coupling_half_load_case(self) -> 'CouplingHalfLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfLoadCase.TYPE'):
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
    def cast_to(self) -> 'CouplingHalfLoadCase._Cast_CouplingHalfLoadCase':
        return self._Cast_CouplingHalfLoadCase(self)
