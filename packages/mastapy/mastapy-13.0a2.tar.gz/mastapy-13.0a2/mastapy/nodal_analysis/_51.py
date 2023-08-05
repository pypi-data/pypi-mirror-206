"""_51.py

BarGeometry
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_GEOMETRY = python_net_import('SMT.MastaAPI.NodalAnalysis', 'BarGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('BarGeometry',)


class BarGeometry(_0.APIBase):
    """BarGeometry

    This is a mastapy class.
    """

    TYPE = _BAR_GEOMETRY

    class _Cast_BarGeometry:
        """Special nested class for casting BarGeometry to subclasses."""

        def __init__(self, parent: 'BarGeometry'):
            self._parent = parent

        @property
        def bar_geometry(self) -> 'BarGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BarGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cross_sectional_area_ratio(self) -> 'float':
        """float: 'CrossSectionalAreaRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrossSectionalAreaRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_area_moment_of_inertia_ratio(self) -> 'float':
        """float: 'PolarAreaMomentOfInertiaRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PolarAreaMomentOfInertiaRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'BarGeometry._Cast_BarGeometry':
        return self._Cast_BarGeometry(self)
