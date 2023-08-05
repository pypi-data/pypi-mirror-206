"""_1795.py

ShaftOrderForTE
"""
from mastapy.utility.modal_analysis.gears import _1791
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_ORDER_FOR_TE = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'ShaftOrderForTE')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftOrderForTE',)


class ShaftOrderForTE(_1791.OrderForTE):
    """ShaftOrderForTE

    This is a mastapy class.
    """

    TYPE = _SHAFT_ORDER_FOR_TE

    class _Cast_ShaftOrderForTE:
        """Special nested class for casting ShaftOrderForTE to subclasses."""

        def __init__(self, parent: 'ShaftOrderForTE'):
            self._parent = parent

        @property
        def order_for_te(self):
            return self._parent._cast(_1791.OrderForTE)

        @property
        def shaft_order_for_te(self) -> 'ShaftOrderForTE':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftOrderForTE.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftOrderForTE._Cast_ShaftOrderForTE':
        return self._Cast_ShaftOrderForTE(self)
