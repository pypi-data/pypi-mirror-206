"""_1157.py

DummyConicalGearCutter
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.conical import _1147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUMMY_CONICAL_GEAR_CUTTER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'DummyConicalGearCutter')


__docformat__ = 'restructuredtext en'
__all__ = ('DummyConicalGearCutter',)


class DummyConicalGearCutter(_1147.ConicalGearCutter):
    """DummyConicalGearCutter

    This is a mastapy class.
    """

    TYPE = _DUMMY_CONICAL_GEAR_CUTTER

    class _Cast_DummyConicalGearCutter:
        """Special nested class for casting DummyConicalGearCutter to subclasses."""

        def __init__(self, parent: 'DummyConicalGearCutter'):
            self._parent = parent

        @property
        def conical_gear_cutter(self):
            return self._parent._cast(_1147.ConicalGearCutter)

        @property
        def dummy_conical_gear_cutter(self) -> 'DummyConicalGearCutter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DummyConicalGearCutter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_cutter_point_width(self) -> 'float':
        """float: 'FinishCutterPointWidth' is the original name of this property."""

        temp = self.wrapped.FinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @finish_cutter_point_width.setter
    def finish_cutter_point_width(self, value: 'float'):
        self.wrapped.FinishCutterPointWidth = float(value) if value else 0.0

    @property
    def inner_edge_radius_convex(self) -> 'float':
        """float: 'InnerEdgeRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerEdgeRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_edge_radius_convex.setter
    def inner_edge_radius_convex(self, value: 'float'):
        self.wrapped.InnerEdgeRadiusConvex = float(value) if value else 0.0

    @property
    def number_of_blade_groups(self) -> 'int':
        """int: 'NumberOfBladeGroups' is the original name of this property."""

        temp = self.wrapped.NumberOfBladeGroups

        if temp is None:
            return 0

        return temp

    @number_of_blade_groups.setter
    def number_of_blade_groups(self, value: 'int'):
        self.wrapped.NumberOfBladeGroups = int(value) if value else 0

    @property
    def outer_edge_radius_concave(self) -> 'float':
        """float: 'OuterEdgeRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterEdgeRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_edge_radius_concave.setter
    def outer_edge_radius_concave(self, value: 'float'):
        self.wrapped.OuterEdgeRadiusConcave = float(value) if value else 0.0

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
    def cast_to(self) -> 'DummyConicalGearCutter._Cast_DummyConicalGearCutter':
        return self._Cast_DummyConicalGearCutter(self)
