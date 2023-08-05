"""_5541.py

CVTPulleyCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5587
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CVTPulleyCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyCompoundMultibodyDynamicsAnalysis',)


class CVTPulleyCompoundMultibodyDynamicsAnalysis(_5587.PulleyCompoundMultibodyDynamicsAnalysis):
    """CVTPulleyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTPulleyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CVTPulleyCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def pulley_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5587.PulleyCompoundMultibodyDynamicsAnalysis)

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
        def cvt_pulley_compound_multibody_dynamics_analysis(self) -> 'CVTPulleyCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_5392.CVTPulleyMultibodyDynamicsAnalysis]':
        """List[CVTPulleyMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5392.CVTPulleyMultibodyDynamicsAnalysis]':
        """List[CVTPulleyMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTPulleyCompoundMultibodyDynamicsAnalysis._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis':
        return self._Cast_CVTPulleyCompoundMultibodyDynamicsAnalysis(self)
