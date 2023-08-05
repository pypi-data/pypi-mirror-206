"""_458.py

CylindricalGearScuffingResults
"""
from typing import List

from mastapy.gears.rating.cylindrical import _479
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SCUFFING_RESULTS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearScuffingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearScuffingResults',)


class CylindricalGearScuffingResults(_0.APIBase):
    """CylindricalGearScuffingResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SCUFFING_RESULTS

    class _Cast_CylindricalGearScuffingResults:
        """Special nested class for casting CylindricalGearScuffingResults to subclasses."""

        def __init__(self, parent: 'CylindricalGearScuffingResults'):
            self._parent = parent

        @property
        def cylindrical_gear_scuffing_results(self) -> 'CylindricalGearScuffingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearScuffingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def scuffing_results_row(self) -> 'List[_479.ScuffingResultsRow]':
        """List[ScuffingResultsRow]: 'ScuffingResultsRow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingResultsRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearScuffingResults._Cast_CylindricalGearScuffingResults':
        return self._Cast_CylindricalGearScuffingResults(self)
