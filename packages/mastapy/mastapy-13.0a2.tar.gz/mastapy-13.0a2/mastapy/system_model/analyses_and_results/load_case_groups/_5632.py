"""_5632.py

ConceptSynchroGearEngagementStatus
"""
from mastapy.system_model.analyses_and_results.load_case_groups import _5635
from mastapy.system_model.part_model.gears import _2504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_SYNCHRO_GEAR_ENGAGEMENT_STATUS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'ConceptSynchroGearEngagementStatus')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptSynchroGearEngagementStatus',)


class ConceptSynchroGearEngagementStatus(_5635.GenericClutchEngagementStatus['_2504.CylindricalGear']):
    """ConceptSynchroGearEngagementStatus

    This is a mastapy class.
    """

    TYPE = _CONCEPT_SYNCHRO_GEAR_ENGAGEMENT_STATUS

    class _Cast_ConceptSynchroGearEngagementStatus:
        """Special nested class for casting ConceptSynchroGearEngagementStatus to subclasses."""

        def __init__(self, parent: 'ConceptSynchroGearEngagementStatus'):
            self._parent = parent

        @property
        def generic_clutch_engagement_status(self):
            return self._parent._cast(_5635.GenericClutchEngagementStatus)

        @property
        def concept_synchro_gear_engagement_status(self) -> 'ConceptSynchroGearEngagementStatus':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptSynchroGearEngagementStatus.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptSynchroGearEngagementStatus._Cast_ConceptSynchroGearEngagementStatus':
        return self._Cast_ConceptSynchroGearEngagementStatus(self)
