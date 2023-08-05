"""_5425.py

KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
"""
from mastapy.system_model.part_model.gears import _2517
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6879
from mastapy.system_model.analyses_and_results.mbd_analyses import _5422
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis',)


class KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis(_5422.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis):
    """KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(self):
            return self._parent._cast(_5422.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5383
            
            return self._parent._cast(_5383.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410
            
            return self._parent._cast(_5410.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(self) -> 'KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2517.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6879.KlingelnbergCycloPalloidHypoidGearLoadCase':
        """KlingelnbergCycloPalloidHypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis(self)
