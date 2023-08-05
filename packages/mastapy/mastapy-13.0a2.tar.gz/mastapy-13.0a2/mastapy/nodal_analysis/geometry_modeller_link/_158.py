"""_158.py

GeometryModellerLengthDimension
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.geometry_modeller_link import _151
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_LENGTH_DIMENSION = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'GeometryModellerLengthDimension')


__docformat__ = 'restructuredtext en'
__all__ = ('GeometryModellerLengthDimension',)


class GeometryModellerLengthDimension(_151.BaseGeometryModellerDimension):
    """GeometryModellerLengthDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_LENGTH_DIMENSION

    class _Cast_GeometryModellerLengthDimension:
        """Special nested class for casting GeometryModellerLengthDimension to subclasses."""

        def __init__(self, parent: 'GeometryModellerLengthDimension'):
            self._parent = parent

        @property
        def base_geometry_modeller_dimension(self):
            return self._parent._cast(_151.BaseGeometryModellerDimension)

        @property
        def geometry_modeller_length_dimension(self) -> 'GeometryModellerLengthDimension':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GeometryModellerLengthDimension.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'GeometryModellerLengthDimension._Cast_GeometryModellerLengthDimension':
        return self._Cast_GeometryModellerLengthDimension(self)
