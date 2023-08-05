"""_1520.py

StressPoint
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS_POINT = python_net_import('SMT.MastaAPI.MathUtility', 'StressPoint')


__docformat__ = 'restructuredtext en'
__all__ = ('StressPoint',)


class StressPoint(_0.APIBase):
    """StressPoint

    This is a mastapy class.
    """

    TYPE = _STRESS_POINT

    class _Cast_StressPoint:
        """Special nested class for casting StressPoint to subclasses."""

        def __init__(self, parent: 'StressPoint'):
            self._parent = parent

        @property
        def shaft_point_stress(self):
            from mastapy.shafts import _27
            
            return self._parent._cast(_27.ShaftPointStress)

        @property
        def stress_point(self) -> 'StressPoint':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StressPoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stress(self) -> 'float':
        """float: 'AxialStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialStress

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_stress(self) -> 'float':
        """float: 'TorsionalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorsionalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def x_bending_stress(self) -> 'float':
        """float: 'XBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def y_bending_stress(self) -> 'float':
        """float: 'YBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'StressPoint._Cast_StressPoint':
        return self._Cast_StressPoint(self)
