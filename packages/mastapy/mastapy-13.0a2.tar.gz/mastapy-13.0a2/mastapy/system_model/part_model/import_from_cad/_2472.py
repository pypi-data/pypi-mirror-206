"""_2472.py

AbstractShaftFromCAD
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2474
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'AbstractShaftFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftFromCAD',)


class AbstractShaftFromCAD(_2474.ComponentFromCAD):
    """AbstractShaftFromCAD

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_FROM_CAD

    class _Cast_AbstractShaftFromCAD:
        """Special nested class for casting AbstractShaftFromCAD to subclasses."""

        def __init__(self, parent: 'AbstractShaftFromCAD'):
            self._parent = parent

        @property
        def component_from_cad(self):
            return self._parent._cast(_2474.ComponentFromCAD)

        @property
        def planet_shaft_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2484
            
            return self._parent._cast(_2484.PlanetShaftFromCAD)

        @property
        def shaft_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2488
            
            return self._parent._cast(_2488.ShaftFromCAD)

        @property
        def abstract_shaft_from_cad(self) -> 'AbstractShaftFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_diameter(self) -> 'float':
        """float: 'InnerDiameter' is the original name of this property."""

        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @inner_diameter.setter
    def inner_diameter(self, value: 'float'):
        self.wrapped.InnerDiameter = float(value) if value else 0.0

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
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property."""

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    def offset(self, value: 'float'):
        self.wrapped.Offset = float(value) if value else 0.0

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AbstractShaftFromCAD._Cast_AbstractShaftFromCAD':
        return self._Cast_AbstractShaftFromCAD(self)
