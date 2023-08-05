"""_5587.py

PulleyCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2569
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5446
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'PulleyCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyCompoundMultibodyDynamicsAnalysis',)


class PulleyCompoundMultibodyDynamicsAnalysis(_5538.CouplingHalfCompoundMultibodyDynamicsAnalysis):
    """PulleyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_PulleyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PulleyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'PulleyCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coupling_half_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5538.CouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
            
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
        def cvt_pulley_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5541
            
            return self._parent._cast(_5541.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(self) -> 'PulleyCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2569.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5446.PulleyMultibodyDynamicsAnalysis]':
        """List[PulleyMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5446.PulleyMultibodyDynamicsAnalysis]':
        """List[PulleyMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PulleyCompoundMultibodyDynamicsAnalysis._Cast_PulleyCompoundMultibodyDynamicsAnalysis':
        return self._Cast_PulleyCompoundMultibodyDynamicsAnalysis(self)
