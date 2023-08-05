"""_840.py

GearRootFilletStressResults
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _833, _834
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_ROOT_FILLET_STRESS_RESULTS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearRootFilletStressResults')


__docformat__ = 'restructuredtext en'
__all__ = ('GearRootFilletStressResults',)


class GearRootFilletStressResults(_0.APIBase):
    """GearRootFilletStressResults

    This is a mastapy class.
    """

    TYPE = _GEAR_ROOT_FILLET_STRESS_RESULTS

    class _Cast_GearRootFilletStressResults:
        """Special nested class for casting GearRootFilletStressResults to subclasses."""

        def __init__(self, parent: 'GearRootFilletStressResults'):
            self._parent = parent

        @property
        def conical_gear_root_fillet_stress_results(self):
            from mastapy.gears.ltca import _821
            
            return self._parent._cast(_821.ConicalGearRootFilletStressResults)

        @property
        def cylindrical_gear_root_fillet_stress_results(self):
            from mastapy.gears.ltca import _826
            
            return self._parent._cast(_826.CylindricalGearRootFilletStressResults)

        @property
        def gear_root_fillet_stress_results(self) -> 'GearRootFilletStressResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearRootFilletStressResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_line_index(self) -> 'int':
        """int: 'ContactLineIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactLineIndex

        if temp is None:
            return 0

        return temp

    @property
    def columns(self) -> 'List[_833.GearFilletNodeStressResultsColumn]':
        """List[GearFilletNodeStressResultsColumn]: 'Columns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Columns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rows(self) -> 'List[_834.GearFilletNodeStressResultsRow]':
        """List[GearFilletNodeStressResultsRow]: 'Rows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearRootFilletStressResults._Cast_GearRootFilletStressResults':
        return self._Cast_GearRootFilletStressResults(self)
