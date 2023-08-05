"""_808.py

PinionFinishCutter
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.conical import _1147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_FINISH_CUTTER = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.Cutters', 'PinionFinishCutter')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionFinishCutter',)


class PinionFinishCutter(_1147.ConicalGearCutter):
    """PinionFinishCutter

    This is a mastapy class.
    """

    TYPE = _PINION_FINISH_CUTTER

    class _Cast_PinionFinishCutter:
        """Special nested class for casting PinionFinishCutter to subclasses."""

        def __init__(self, parent: 'PinionFinishCutter'):
            self._parent = parent

        @property
        def conical_gear_cutter(self):
            return self._parent._cast(_1147.ConicalGearCutter)

        @property
        def pinion_finish_cutter(self) -> 'PinionFinishCutter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionFinishCutter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_blade_point_radius_convex(self) -> 'float':
        """float: 'InnerBladePointRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerBladePointRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_blade_point_radius_convex.setter
    def inner_blade_point_radius_convex(self, value: 'float'):
        self.wrapped.InnerBladePointRadiusConvex = float(value) if value else 0.0

    @property
    def outer_blade_point_radius_concave(self) -> 'float':
        """float: 'OuterBladePointRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterBladePointRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_blade_point_radius_concave.setter
    def outer_blade_point_radius_concave(self, value: 'float'):
        self.wrapped.OuterBladePointRadiusConcave = float(value) if value else 0.0

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
    def cast_to(self) -> 'PinionFinishCutter._Cast_PinionFinishCutter':
        return self._Cast_PinionFinishCutter(self)
