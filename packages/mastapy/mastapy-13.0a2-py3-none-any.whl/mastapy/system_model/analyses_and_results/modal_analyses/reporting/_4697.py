"""_4697.py

RigidlyConnectedDesignEntityGroupModalAnalysis
"""
from typing import List

from mastapy.utility.modal_analysis import _1785
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results import _2631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting', 'RigidlyConnectedDesignEntityGroupModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RigidlyConnectedDesignEntityGroupModalAnalysis',)


class RigidlyConnectedDesignEntityGroupModalAnalysis(_2631.DesignEntityGroupAnalysis):
    """RigidlyConnectedDesignEntityGroupModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_MODAL_ANALYSIS

    class _Cast_RigidlyConnectedDesignEntityGroupModalAnalysis:
        """Special nested class for casting RigidlyConnectedDesignEntityGroupModalAnalysis to subclasses."""

        def __init__(self, parent: 'RigidlyConnectedDesignEntityGroupModalAnalysis'):
            self._parent = parent

        @property
        def design_entity_group_analysis(self):
            return self._parent._cast(_2631.DesignEntityGroupAnalysis)

        @property
        def rigidly_connected_design_entity_group_modal_analysis(self) -> 'RigidlyConnectedDesignEntityGroupModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RigidlyConnectedDesignEntityGroupModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_frequencies_at_reference_speed(self) -> 'List[_1785.DesignEntityExcitationDescription]':
        """List[DesignEntityExcitationDescription]: 'ExcitationFrequenciesAtReferenceSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitationFrequenciesAtReferenceSpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RigidlyConnectedDesignEntityGroupModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis':
        return self._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis(self)
