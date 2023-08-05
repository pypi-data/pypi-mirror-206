"""_1139.py

OverridableTolerance
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OVERRIDABLE_TOLERANCE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'OverridableTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('OverridableTolerance',)


class OverridableTolerance(_0.APIBase):
    """OverridableTolerance

    This is a mastapy class.
    """

    TYPE = _OVERRIDABLE_TOLERANCE

    class _Cast_OverridableTolerance:
        """Special nested class for casting OverridableTolerance to subclasses."""

        def __init__(self, parent: 'OverridableTolerance'):
            self._parent = parent

        @property
        def overridable_tolerance(self) -> 'OverridableTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OverridableTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def standard_value(self) -> 'float':
        """float: 'StandardValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StandardValue

        if temp is None:
            return 0.0

        return temp

    @property
    def value(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Value' is the original name of this property."""

        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @value.setter
    def value(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Value = value

    @property
    def cast_to(self) -> 'OverridableTolerance._Cast_OverridableTolerance':
        return self._Cast_OverridableTolerance(self)
