"""_809.py

PinionRoughCutter
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.conical import _1147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_ROUGH_CUTTER = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.Cutters', 'PinionRoughCutter')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionRoughCutter',)


class PinionRoughCutter(_1147.ConicalGearCutter):
    """PinionRoughCutter

    This is a mastapy class.
    """

    TYPE = _PINION_ROUGH_CUTTER

    class _Cast_PinionRoughCutter:
        """Special nested class for casting PinionRoughCutter to subclasses."""

        def __init__(self, parent: 'PinionRoughCutter'):
            self._parent = parent

        @property
        def conical_gear_cutter(self):
            return self._parent._cast(_1147.ConicalGearCutter)

        @property
        def pinion_rough_cutter(self) -> 'PinionRoughCutter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionRoughCutter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def point_width(self) -> 'float':
        """float: 'PointWidth' is the original name of this property."""

        temp = self.wrapped.PointWidth

        if temp is None:
            return 0.0

        return temp

    @point_width.setter
    def point_width(self, value: 'float'):
        self.wrapped.PointWidth = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'PinionRoughCutter._Cast_PinionRoughCutter':
        return self._Cast_PinionRoughCutter(self)
