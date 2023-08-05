"""_2485.py

PulleyFromCAD
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'PulleyFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyFromCAD',)


class PulleyFromCAD(_2483.MountableComponentFromCAD):
    """PulleyFromCAD

    This is a mastapy class.
    """

    TYPE = _PULLEY_FROM_CAD

    class _Cast_PulleyFromCAD:
        """Special nested class for casting PulleyFromCAD to subclasses."""

        def __init__(self, parent: 'PulleyFromCAD'):
            self._parent = parent

        @property
        def mountable_component_from_cad(self):
            return self._parent._cast(_2483.MountableComponentFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2474
            
            return self._parent._cast(_2474.ComponentFromCAD)

        @property
        def pulley_from_cad(self) -> 'PulleyFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleyFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self) -> 'float':
        """float: 'CentreDistance' is the original name of this property."""

        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @centre_distance.setter
    def centre_distance(self, value: 'float'):
        self.wrapped.CentreDistance = float(value) if value else 0.0

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
    def cast_to(self) -> 'PulleyFromCAD._Cast_PulleyFromCAD':
        return self._Cast_PulleyFromCAD(self)
