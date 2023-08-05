"""_1796.py

UserDefinedOrderForTE
"""
from mastapy.utility.modal_analysis.gears import _1793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_DEFINED_ORDER_FOR_TE = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'UserDefinedOrderForTE')


__docformat__ = 'restructuredtext en'
__all__ = ('UserDefinedOrderForTE',)


class UserDefinedOrderForTE(_1793.OrderWithRadius):
    """UserDefinedOrderForTE

    This is a mastapy class.
    """

    TYPE = _USER_DEFINED_ORDER_FOR_TE

    class _Cast_UserDefinedOrderForTE:
        """Special nested class for casting UserDefinedOrderForTE to subclasses."""

        def __init__(self, parent: 'UserDefinedOrderForTE'):
            self._parent = parent

        @property
        def order_with_radius(self):
            return self._parent._cast(_1793.OrderWithRadius)

        @property
        def order_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1791
            
            return self._parent._cast(_1791.OrderForTE)

        @property
        def user_defined_order_for_te(self) -> 'UserDefinedOrderForTE':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UserDefinedOrderForTE.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'UserDefinedOrderForTE._Cast_UserDefinedOrderForTE':
        return self._Cast_UserDefinedOrderForTE(self)
