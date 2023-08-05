"""_5538.py

CouplingHalfCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CouplingHalfCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundMultibodyDynamicsAnalysis',)


class CouplingHalfCompoundMultibodyDynamicsAnalysis(_5576.MountableComponentCompoundMultibodyDynamicsAnalysis):
    """CouplingHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingHalfCompoundMultibodyDynamicsAnalysis'):
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
        def clutch_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5522
            
            return self._parent._cast(_5522.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
            
            return self._parent._cast(_5527.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5541
            
            return self._parent._cast(_5541.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5581
            
            return self._parent._cast(_5581.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5587
            
            return self._parent._cast(_5587.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5591
            
            return self._parent._cast(_5591.RollingRingCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5603
            
            return self._parent._cast(_5603.SpringDamperHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5613
            
            return self._parent._cast(_5613.SynchroniserHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5614
            
            return self._parent._cast(_5614.SynchroniserPartCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5615
            
            return self._parent._cast(_5615.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5618
            
            return self._parent._cast(_5618.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5619
            
            return self._parent._cast(_5619.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(self) -> 'CouplingHalfCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5388.CouplingHalfMultibodyDynamicsAnalysis]':
        """List[CouplingHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5388.CouplingHalfMultibodyDynamicsAnalysis]':
        """List[CouplingHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis':
        return self._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis(self)
