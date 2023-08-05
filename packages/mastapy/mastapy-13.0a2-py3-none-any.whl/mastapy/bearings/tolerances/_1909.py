"""_1909.py

ToleranceCombination
"""
from mastapy.bearings.tolerances import _1890
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOLERANCE_COMBINATION = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'ToleranceCombination')


__docformat__ = 'restructuredtext en'
__all__ = ('ToleranceCombination',)


class ToleranceCombination(_0.APIBase):
    """ToleranceCombination

    This is a mastapy class.
    """

    TYPE = _TOLERANCE_COMBINATION

    class _Cast_ToleranceCombination:
        """Special nested class for casting ToleranceCombination to subclasses."""

        def __init__(self, parent: 'ToleranceCombination'):
            self._parent = parent

        @property
        def tolerance_combination(self) -> 'ToleranceCombination':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ToleranceCombination.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fit(self) -> '_1890.FitType':
        """FitType: 'Fit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Fit

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1890.FitType)
        return constructor.new_from_mastapy_type(_1890.FitType)(value) if value is not None else None

    @property
    def lower_value(self) -> 'float':
        """float: 'LowerValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowerValue

        if temp is None:
            return 0.0

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
    def upper_value(self) -> 'float':
        """float: 'UpperValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UpperValue

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ToleranceCombination._Cast_ToleranceCombination':
        return self._Cast_ToleranceCombination(self)
