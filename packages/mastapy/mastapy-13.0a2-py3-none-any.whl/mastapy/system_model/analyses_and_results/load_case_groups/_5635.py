"""_5635.py

GenericClutchEngagementStatus
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy.system_model import _2188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERIC_CLUTCH_ENGAGEMENT_STATUS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'GenericClutchEngagementStatus')


__docformat__ = 'restructuredtext en'
__all__ = ('GenericClutchEngagementStatus',)


T = TypeVar('T', bound='_2188.DesignEntity')


class GenericClutchEngagementStatus(_0.APIBase, Generic[T]):
    """GenericClutchEngagementStatus

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GENERIC_CLUTCH_ENGAGEMENT_STATUS

    class _Cast_GenericClutchEngagementStatus:
        """Special nested class for casting GenericClutchEngagementStatus to subclasses."""

        def __init__(self, parent: 'GenericClutchEngagementStatus'):
            self._parent = parent

        @property
        def clutch_engagement_status(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5631
            
            return self._parent._cast(_5631.ClutchEngagementStatus)

        @property
        def concept_synchro_gear_engagement_status(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5632
            
            return self._parent._cast(_5632.ConceptSynchroGearEngagementStatus)

        @property
        def generic_clutch_engagement_status(self) -> 'GenericClutchEngagementStatus':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GenericClutchEngagementStatus.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_engaged(self) -> 'bool':
        """bool: 'IsEngaged' is the original name of this property."""

        temp = self.wrapped.IsEngaged

        if temp is None:
            return False

        return temp

    @is_engaged.setter
    def is_engaged(self, value: 'bool'):
        self.wrapped.IsEngaged = bool(value) if value else False

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
    def unique_name(self) -> 'str':
        """str: 'UniqueName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UniqueName

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'GenericClutchEngagementStatus._Cast_GenericClutchEngagementStatus':
        return self._Cast_GenericClutchEngagementStatus(self)
