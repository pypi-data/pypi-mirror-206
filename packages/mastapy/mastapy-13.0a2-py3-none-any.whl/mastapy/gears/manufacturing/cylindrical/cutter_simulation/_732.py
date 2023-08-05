"""_732.py

FinishStockPoint
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_STOCK_POINT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'FinishStockPoint')


__docformat__ = 'restructuredtext en'
__all__ = ('FinishStockPoint',)


class FinishStockPoint(_0.APIBase):
    """FinishStockPoint

    This is a mastapy class.
    """

    TYPE = _FINISH_STOCK_POINT

    class _Cast_FinishStockPoint:
        """Special nested class for casting FinishStockPoint to subclasses."""

        def __init__(self, parent: 'FinishStockPoint'):
            self._parent = parent

        @property
        def finish_stock_point(self) -> 'FinishStockPoint':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FinishStockPoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_stock_arc_length(self) -> 'float':
        """float: 'FinishStockArcLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishStockArcLength

        if temp is None:
            return 0.0

        return temp

    @property
    def finish_stock_tangent_to_the_base_circle(self) -> 'float':
        """float: 'FinishStockTangentToTheBaseCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishStockTangentToTheBaseCircle

        if temp is None:
            return 0.0

        return temp

    @property
    def index(self) -> 'str':
        """str: 'Index' is the original name of this property."""

        temp = self.wrapped.Index

        if temp is None:
            return ''

        return temp

    @index.setter
    def index(self, value: 'str'):
        self.wrapped.Index = str(value) if value else ''

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FinishStockPoint._Cast_FinishStockPoint':
        return self._Cast_FinishStockPoint(self)
