"""_1794.py

RollingBearingOrder
"""
from mastapy.utility.modal_analysis.gears import _1791
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_ORDER = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'RollingBearingOrder')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingBearingOrder',)


class RollingBearingOrder(_1791.OrderForTE):
    """RollingBearingOrder

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_ORDER

    class _Cast_RollingBearingOrder:
        """Special nested class for casting RollingBearingOrder to subclasses."""

        def __init__(self, parent: 'RollingBearingOrder'):
            self._parent = parent

        @property
        def order_for_te(self):
            return self._parent._cast(_1791.OrderForTE)

        @property
        def rolling_bearing_order(self) -> 'RollingBearingOrder':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingBearingOrder.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RollingBearingOrder._Cast_RollingBearingOrder':
        return self._Cast_RollingBearingOrder(self)
