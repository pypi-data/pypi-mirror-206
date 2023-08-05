"""_2484.py

PlanetShaftFromCAD
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2472
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_SHAFT_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'PlanetShaftFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetShaftFromCAD',)


class PlanetShaftFromCAD(_2472.AbstractShaftFromCAD):
    """PlanetShaftFromCAD

    This is a mastapy class.
    """

    TYPE = _PLANET_SHAFT_FROM_CAD

    class _Cast_PlanetShaftFromCAD:
        """Special nested class for casting PlanetShaftFromCAD to subclasses."""

        def __init__(self, parent: 'PlanetShaftFromCAD'):
            self._parent = parent

        @property
        def abstract_shaft_from_cad(self):
            return self._parent._cast(_2472.AbstractShaftFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2474
            
            return self._parent._cast(_2474.ComponentFromCAD)

        @property
        def planet_shaft_from_cad(self) -> 'PlanetShaftFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetShaftFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_diameter(self) -> 'float':
        """float: 'PlanetDiameter' is the original name of this property."""

        temp = self.wrapped.PlanetDiameter

        if temp is None:
            return 0.0

        return temp

    @planet_diameter.setter
    def planet_diameter(self, value: 'float'):
        self.wrapped.PlanetDiameter = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'PlanetShaftFromCAD._Cast_PlanetShaftFromCAD':
        return self._Cast_PlanetShaftFromCAD(self)
