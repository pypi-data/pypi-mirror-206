"""_4695.py

RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4696
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_FOR_SINGLE_EXCITATION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting', 'RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis',)


class RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis(_4696.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis):
    """RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_FOR_SINGLE_EXCITATION_MODAL_ANALYSIS

    class _Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis:
        """Special nested class for casting RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis to subclasses."""

        def __init__(self, parent: 'RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis'):
            self._parent = parent

        @property
        def rigidly_connected_design_entity_group_for_single_mode_modal_analysis(self):
            return self._parent._cast(_4696.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis)

        @property
        def rigidly_connected_design_entity_group_for_single_excitation_modal_analysis(self) -> 'RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reference_speed_of_crossing(self) -> 'float':
        """float: 'ReferenceSpeedOfCrossing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceSpeedOfCrossing

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis':
        return self._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis(self)
