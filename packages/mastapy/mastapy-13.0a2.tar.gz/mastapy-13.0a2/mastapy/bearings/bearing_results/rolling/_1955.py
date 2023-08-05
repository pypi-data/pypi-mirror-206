"""_1955.py

ForceAtLaminaGroupReportable
"""
from typing import List

from mastapy.bearings.bearing_results.rolling import _1956
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_AT_LAMINA_GROUP_REPORTABLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ForceAtLaminaGroupReportable')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceAtLaminaGroupReportable',)


class ForceAtLaminaGroupReportable(_0.APIBase):
    """ForceAtLaminaGroupReportable

    This is a mastapy class.
    """

    TYPE = _FORCE_AT_LAMINA_GROUP_REPORTABLE

    class _Cast_ForceAtLaminaGroupReportable:
        """Special nested class for casting ForceAtLaminaGroupReportable to subclasses."""

        def __init__(self, parent: 'ForceAtLaminaGroupReportable'):
            self._parent = parent

        @property
        def force_at_lamina_group_reportable(self) -> 'ForceAtLaminaGroupReportable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForceAtLaminaGroupReportable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def forces_at_laminae(self) -> 'List[_1956.ForceAtLaminaReportable]':
        """List[ForceAtLaminaReportable]: 'ForcesAtLaminae' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForcesAtLaminae

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ForceAtLaminaGroupReportable._Cast_ForceAtLaminaGroupReportable':
        return self._Cast_ForceAtLaminaGroupReportable(self)
