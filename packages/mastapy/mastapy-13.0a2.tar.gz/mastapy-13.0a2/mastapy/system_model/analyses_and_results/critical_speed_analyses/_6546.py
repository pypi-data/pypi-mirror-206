"""_6546.py

CouplingCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model.couplings import _2562
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CouplingCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCriticalSpeedAnalysis',)


class CouplingCriticalSpeedAnalysis(_6608.SpecialisedAssemblyCriticalSpeedAnalysis):
    """CouplingCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CRITICAL_SPEED_ANALYSIS

    class _Cast_CouplingCriticalSpeedAnalysis:
        """Special nested class for casting CouplingCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(self):
            return self._parent._cast(_6608.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6508
            
            return self._parent._cast(_6508.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
            
            return self._parent._cast(_6589.PartCriticalSpeedAnalysis)

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
        def clutch_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6530
            
            return self._parent._cast(_6530.ClutchCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6535
            
            return self._parent._cast(_6535.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6591
            
            return self._parent._cast(_6591.PartToPartShearCouplingCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6613
            
            return self._parent._cast(_6613.SpringDamperCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6628
            
            return self._parent._cast(_6628.TorqueConverterCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(self) -> 'CouplingCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2562.Coupling':
        """Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis':
        return self._Cast_CouplingCriticalSpeedAnalysis(self)
