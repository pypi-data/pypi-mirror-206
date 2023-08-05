"""_5631.py

ClutchEngagementStatus
"""
from mastapy.system_model.analyses_and_results.load_case_groups import _5635
from mastapy.system_model.connections_and_sockets.couplings import _2323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_ENGAGEMENT_STATUS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'ClutchEngagementStatus')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchEngagementStatus',)


class ClutchEngagementStatus(_5635.GenericClutchEngagementStatus['_2323.ClutchConnection']):
    """ClutchEngagementStatus

    This is a mastapy class.
    """

    TYPE = _CLUTCH_ENGAGEMENT_STATUS

    class _Cast_ClutchEngagementStatus:
        """Special nested class for casting ClutchEngagementStatus to subclasses."""

        def __init__(self, parent: 'ClutchEngagementStatus'):
            self._parent = parent

        @property
        def generic_clutch_engagement_status(self):
            return self._parent._cast(_5635.GenericClutchEngagementStatus)

        @property
        def clutch_engagement_status(self) -> 'ClutchEngagementStatus':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchEngagementStatus.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ClutchEngagementStatus._Cast_ClutchEngagementStatus':
        return self._Cast_ClutchEngagementStatus(self)
