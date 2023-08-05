"""_5444.py

PointLoadMultibodyDynamicsAnalysis
"""
from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2451
from mastapy.system_model.analyses_and_results.static_loads import _6902
from mastapy.system_model.analyses_and_results.mbd_analyses import _5485
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'PointLoadMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadMultibodyDynamicsAnalysis',)


class PointLoadMultibodyDynamicsAnalysis(_5485.VirtualComponentMultibodyDynamicsAnalysis):
    """PointLoadMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_PointLoadMultibodyDynamicsAnalysis:
        """Special nested class for casting PointLoadMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'PointLoadMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def virtual_component_multibody_dynamics_analysis(self):
            return self._parent._cast(_5485.VirtualComponentMultibodyDynamicsAnalysis)

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
        def point_load_multibody_dynamics_analysis(self) -> 'PointLoadMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoadMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def applied_force(self) -> 'Vector3D':
        """Vector3D: 'AppliedForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AppliedForce

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def applied_moment(self) -> 'Vector3D':
        """Vector3D: 'AppliedMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AppliedMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def component_design(self) -> '_2451.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6902.PointLoadLoadCase':
        """PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PointLoadMultibodyDynamicsAnalysis._Cast_PointLoadMultibodyDynamicsAnalysis':
        return self._Cast_PointLoadMultibodyDynamicsAnalysis(self)
