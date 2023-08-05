"""_1793.py

OrderWithRadius
"""
from mastapy._internal import constructor
from mastapy.utility.modal_analysis.gears import _1791
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ORDER_WITH_RADIUS = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'OrderWithRadius')


__docformat__ = 'restructuredtext en'
__all__ = ('OrderWithRadius',)


class OrderWithRadius(_1791.OrderForTE):
    """OrderWithRadius

    This is a mastapy class.
    """

    TYPE = _ORDER_WITH_RADIUS

    class _Cast_OrderWithRadius:
        """Special nested class for casting OrderWithRadius to subclasses."""

        def __init__(self, parent: 'OrderWithRadius'):
            self._parent = parent

        @property
        def order_for_te(self):
            return self._parent._cast(_1791.OrderForTE)

        @property
        def gear_order_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1787
            
            return self._parent._cast(_1787.GearOrderForTE)

        @property
        def user_defined_order_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1796
            
            return self._parent._cast(_1796.UserDefinedOrderForTE)

        @property
        def order_with_radius(self) -> 'OrderWithRadius':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OrderWithRadius.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'OrderWithRadius._Cast_OrderWithRadius':
        return self._Cast_OrderWithRadius(self)
