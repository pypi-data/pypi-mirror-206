"""_1843.py

ModeConstantLine
"""
from mastapy.utility_gui.charts import _1839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODE_CONSTANT_LINE = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ModeConstantLine')


__docformat__ = 'restructuredtext en'
__all__ = ('ModeConstantLine',)


class ModeConstantLine(_1839.ConstantLine):
    """ModeConstantLine

    This is a mastapy class.
    """

    TYPE = _MODE_CONSTANT_LINE

    class _Cast_ModeConstantLine:
        """Special nested class for casting ModeConstantLine to subclasses."""

        def __init__(self, parent: 'ModeConstantLine'):
            self._parent = parent

        @property
        def constant_line(self):
            return self._parent._cast(_1839.ConstantLine)

        @property
        def mode_constant_line(self) -> 'ModeConstantLine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ModeConstantLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ModeConstantLine._Cast_ModeConstantLine':
        return self._Cast_ModeConstantLine(self)
