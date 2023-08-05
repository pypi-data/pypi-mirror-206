"""_1839.py

ConstantLine
"""
from mastapy.utility_gui.charts import _1849
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONSTANT_LINE = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ConstantLine')


__docformat__ = 'restructuredtext en'
__all__ = ('ConstantLine',)


class ConstantLine(_0.APIBase):
    """ConstantLine

    This is a mastapy class.
    """

    TYPE = _CONSTANT_LINE

    class _Cast_ConstantLine:
        """Special nested class for casting ConstantLine to subclasses."""

        def __init__(self, parent: 'ConstantLine'):
            self._parent = parent

        @property
        def mode_constant_line(self):
            from mastapy.utility_gui.charts import _1843
            
            return self._parent._cast(_1843.ModeConstantLine)

        @property
        def constant_line(self) -> 'ConstantLine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConstantLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axis(self) -> '_1849.SMTAxis':
        """SMTAxis: 'Axis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Axis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1849.SMTAxis)
        return constructor.new_from_mastapy_type(_1849.SMTAxis)(value) if value is not None else None

    @property
    def end(self) -> 'float':
        """float: 'End' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.End

        if temp is None:
            return 0.0

        return temp

    @property
    def label(self) -> 'str':
        """str: 'Label' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Label

        if temp is None:
            return ''

        return temp

    @property
    def start(self) -> 'float':
        """float: 'Start' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Start

        if temp is None:
            return 0.0

        return temp

    @property
    def value(self) -> 'float':
        """float: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ConstantLine._Cast_ConstantLine':
        return self._Cast_ConstantLine(self)
