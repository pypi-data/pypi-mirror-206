"""_5348.py

AbstractShaftMultibodyDynamicsAnalysis
"""
from mastapy.system_model.part_model import _2415
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5349
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'AbstractShaftMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftMultibodyDynamicsAnalysis',)


class AbstractShaftMultibodyDynamicsAnalysis(_5349.AbstractShaftOrHousingMultibodyDynamicsAnalysis):
    """AbstractShaftMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AbstractShaftMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(self):
            return self._parent._cast(_5349.AbstractShaftOrHousingMultibodyDynamicsAnalysis)

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
        def cycloidal_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395
            
            return self._parent._cast(_5395.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456
            
            return self._parent._cast(_5456.ShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(self) -> 'AbstractShaftMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis':
        return self._Cast_AbstractShaftMultibodyDynamicsAnalysis(self)
