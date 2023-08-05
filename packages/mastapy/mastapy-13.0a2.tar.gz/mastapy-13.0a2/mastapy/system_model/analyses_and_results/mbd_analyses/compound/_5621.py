"""_5621.py

VirtualComponentCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5485
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'VirtualComponentCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundMultibodyDynamicsAnalysis',)


class VirtualComponentCompoundMultibodyDynamicsAnalysis(_5576.MountableComponentCompoundMultibodyDynamicsAnalysis):
    """VirtualComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting VirtualComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5576.MountableComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5524
            
            return self._parent._cast(_5524.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5578
            
            return self._parent._cast(_5578.PartCompoundMultibodyDynamicsAnalysis)

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
        def mass_disc_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5574
            
            return self._parent._cast(_5574.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5575
            
            return self._parent._cast(_5575.MeasurementComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def point_load_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5585
            
            return self._parent._cast(_5585.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5586
            
            return self._parent._cast(_5586.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5620
            
            return self._parent._cast(_5620.UnbalancedMassCompoundMultibodyDynamicsAnalysis)

        @property
        def virtual_component_compound_multibody_dynamics_analysis(self) -> 'VirtualComponentCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5485.VirtualComponentMultibodyDynamicsAnalysis]':
        """List[VirtualComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5485.VirtualComponentMultibodyDynamicsAnalysis]':
        """List[VirtualComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundMultibodyDynamicsAnalysis._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis':
        return self._Cast_VirtualComponentCompoundMultibodyDynamicsAnalysis(self)
