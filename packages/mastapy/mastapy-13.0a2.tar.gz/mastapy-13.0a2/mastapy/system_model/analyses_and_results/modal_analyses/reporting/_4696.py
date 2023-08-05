"""_4696.py

RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4691
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_FOR_SINGLE_MODE_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting', 'RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis',)


class RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis(_0.APIBase):
    """RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_FOR_SINGLE_MODE_MODAL_ANALYSIS

    class _Cast_RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis:
        """Special nested class for casting RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis to subclasses."""

        def __init__(self, parent: 'RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis'):
            self._parent = parent

        @property
        def rigidly_connected_design_entity_group_for_single_excitation_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4695
            
            return self._parent._cast(_4695.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis)

        @property
        def rigidly_connected_design_entity_group_for_single_mode_modal_analysis(self) -> 'RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mode_frequency(self) -> 'float':
        """float: 'ModeFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModeFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def mode_id(self) -> 'int':
        """int: 'ModeID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModeID

        if temp is None:
            return 0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def percentage_kinetic_energy(self) -> 'float':
        """float: 'PercentageKineticEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageKineticEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_strain_energy(self) -> 'float':
        """float: 'PercentageStrainEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageStrainEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_names(self) -> 'str':
        """str: 'ShaftNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftNames

        if temp is None:
            return ''

        return temp

    @property
    def component_results(self) -> 'List[_4691.ComponentPerModeResult]':
        """List[ComponentPerModeResult]: 'ComponentResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis':
        return self._Cast_RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis(self)
