"""_5613.py

SynchroniserHalfCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2583
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5474
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5614
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'SynchroniserHalfCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfCompoundMultibodyDynamicsAnalysis',)


class SynchroniserHalfCompoundMultibodyDynamicsAnalysis(_5614.SynchroniserPartCompoundMultibodyDynamicsAnalysis):
    """SynchroniserHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'SynchroniserHalfCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5614.SynchroniserPartCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5538
            
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
        def synchroniser_half_compound_multibody_dynamics_analysis(self) -> 'SynchroniserHalfCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2583.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5474.SynchroniserHalfMultibodyDynamicsAnalysis]':
        """List[SynchroniserHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5474.SynchroniserHalfMultibodyDynamicsAnalysis]':
        """List[SynchroniserHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis':
        return self._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis(self)
