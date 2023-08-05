"""_1950.py

StiffnessRow
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STIFFNESS_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'StiffnessRow')


__docformat__ = 'restructuredtext en'
__all__ = ('StiffnessRow',)


class StiffnessRow(_0.APIBase):
    """StiffnessRow

    This is a mastapy class.
    """

    TYPE = _STIFFNESS_ROW

    class _Cast_StiffnessRow:
        """Special nested class for casting StiffnessRow to subclasses."""

        def __init__(self, parent: 'StiffnessRow'):
            self._parent = parent

        @property
        def stiffness_row(self) -> 'StiffnessRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StiffnessRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comma_separated_values_mn_rad(self) -> 'str':
        """str: 'CommaSeparatedValuesMNRad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommaSeparatedValuesMNRad

        if temp is None:
            return ''

        return temp

    @property
    def row_index(self) -> 'int':
        """int: 'RowIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RowIndex

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self) -> 'StiffnessRow._Cast_StiffnessRow':
        return self._Cast_StiffnessRow(self)
