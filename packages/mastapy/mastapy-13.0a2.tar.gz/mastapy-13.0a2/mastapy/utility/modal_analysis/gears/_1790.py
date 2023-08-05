"""_1790.py

LabelOnlyOrder
"""
from mastapy.utility.modal_analysis.gears import _1791
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LABEL_ONLY_ORDER = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'LabelOnlyOrder')


__docformat__ = 'restructuredtext en'
__all__ = ('LabelOnlyOrder',)


class LabelOnlyOrder(_1791.OrderForTE):
    """LabelOnlyOrder

    This is a mastapy class.
    """

    TYPE = _LABEL_ONLY_ORDER

    class _Cast_LabelOnlyOrder:
        """Special nested class for casting LabelOnlyOrder to subclasses."""

        def __init__(self, parent: 'LabelOnlyOrder'):
            self._parent = parent

        @property
        def order_for_te(self):
            return self._parent._cast(_1791.OrderForTE)

        @property
        def label_only_order(self) -> 'LabelOnlyOrder':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LabelOnlyOrder.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LabelOnlyOrder._Cast_LabelOnlyOrder':
        return self._Cast_LabelOnlyOrder(self)
