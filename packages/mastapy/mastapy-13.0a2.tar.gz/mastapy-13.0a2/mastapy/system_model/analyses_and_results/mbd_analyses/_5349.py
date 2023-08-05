"""_5349.py

AbstractShaftOrHousingMultibodyDynamicsAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2416
from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'AbstractShaftOrHousingMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingMultibodyDynamicsAnalysis',)


class AbstractShaftOrHousingMultibodyDynamicsAnalysis(_5375.ComponentMultibodyDynamicsAnalysis):
    """AbstractShaftOrHousingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftOrHousingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(self):
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
        def abstract_shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5348
            
            return self._parent._cast(_5348.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395
            
            return self._parent._cast(_5395.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406
            
            return self._parent._cast(_5406.FEPartMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456
            
            return self._parent._cast(_5456.ShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(self) -> 'AbstractShaftOrHousingMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_rigid_body_degrees_of_freedom(self) -> 'int':
        """int: 'NumberOfRigidBodyDegreesOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfRigidBodyDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self) -> '_2416.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis':
        return self._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis(self)
