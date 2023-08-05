"""_1272.py

MagnetForLayer
"""
from mastapy._internal import constructor
from mastapy.electric_machines import _1271
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNET_FOR_LAYER = python_net_import('SMT.MastaAPI.ElectricMachines', 'MagnetForLayer')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetForLayer',)


class MagnetForLayer(_1271.MagnetDesign):
    """MagnetForLayer

    This is a mastapy class.
    """

    TYPE = _MAGNET_FOR_LAYER

    class _Cast_MagnetForLayer:
        """Special nested class for casting MagnetForLayer to subclasses."""

        def __init__(self, parent: 'MagnetForLayer'):
            self._parent = parent

        @property
        def magnet_design(self):
            return self._parent._cast(_1271.MagnetDesign)

        @property
        def magnet_for_layer(self) -> 'MagnetForLayer':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MagnetForLayer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_segments_along_width(self) -> 'int':
        """int: 'NumberOfSegmentsAlongWidth' is the original name of this property."""

        temp = self.wrapped.NumberOfSegmentsAlongWidth

        if temp is None:
            return 0

        return temp

    @number_of_segments_along_width.setter
    def number_of_segments_along_width(self, value: 'int'):
        self.wrapped.NumberOfSegmentsAlongWidth = int(value) if value else 0

    @property
    def thickness(self) -> 'float':
        """float: 'Thickness' is the original name of this property."""

        temp = self.wrapped.Thickness

        if temp is None:
            return 0.0

        return temp

    @thickness.setter
    def thickness(self, value: 'float'):
        self.wrapped.Thickness = float(value) if value else 0.0

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

    @property
    def width_of_each_segment(self) -> 'float':
        """float: 'WidthOfEachSegment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WidthOfEachSegment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'MagnetForLayer._Cast_MagnetForLayer':
        return self._Cast_MagnetForLayer(self)
