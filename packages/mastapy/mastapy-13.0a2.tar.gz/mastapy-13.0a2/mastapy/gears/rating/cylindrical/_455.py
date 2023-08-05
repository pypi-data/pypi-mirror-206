"""_455.py

CylindricalGearMicroPittingResults
"""
from typing import List

from mastapy.gears.rating.cylindrical import _473
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_PITTING_RESULTS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearMicroPittingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroPittingResults',)


class CylindricalGearMicroPittingResults(_0.APIBase):
    """CylindricalGearMicroPittingResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_PITTING_RESULTS

    class _Cast_CylindricalGearMicroPittingResults:
        """Special nested class for casting CylindricalGearMicroPittingResults to subclasses."""

        def __init__(self, parent: 'CylindricalGearMicroPittingResults'):
            self._parent = parent

        @property
        def cylindrical_gear_micro_pitting_results(self) -> 'CylindricalGearMicroPittingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroPittingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_pitting_results_row(self) -> 'List[_473.MicroPittingResultsRow]':
        """List[MicroPittingResultsRow]: 'MicroPittingResultsRow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroPittingResultsRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearMicroPittingResults._Cast_CylindricalGearMicroPittingResults':
        return self._Cast_CylindricalGearMicroPittingResults(self)
