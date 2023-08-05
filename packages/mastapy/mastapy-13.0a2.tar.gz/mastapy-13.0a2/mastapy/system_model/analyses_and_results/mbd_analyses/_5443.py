"""_5443.py

PlanetCarrierMultibodyDynamicsAnalysis
"""
from mastapy.system_model.part_model import _2449
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6899
from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'PlanetCarrierMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierMultibodyDynamicsAnalysis',)


class PlanetCarrierMultibodyDynamicsAnalysis(_5435.MountableComponentMultibodyDynamicsAnalysis):
    """PlanetCarrierMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_PlanetCarrierMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetCarrierMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetCarrierMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(self):
            return self._parent._cast(_5435.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
            
            return self._parent._cast(_5375.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartTimeSeriesLoadAnalysisCase)

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
        def planet_carrier_multibody_dynamics_analysis(self) -> 'PlanetCarrierMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetCarrierMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2449.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6899.PlanetCarrierLoadCase':
        """PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlanetCarrierMultibodyDynamicsAnalysis._Cast_PlanetCarrierMultibodyDynamicsAnalysis':
        return self._Cast_PlanetCarrierMultibodyDynamicsAnalysis(self)
