"""_2474.py

ComponentFromCAD
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'ComponentFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentFromCAD',)


class ComponentFromCAD(_0.APIBase):
    """ComponentFromCAD

    This is a mastapy class.
    """

    TYPE = _COMPONENT_FROM_CAD

    class _Cast_ComponentFromCAD:
        """Special nested class for casting ComponentFromCAD to subclasses."""

        def __init__(self, parent: 'ComponentFromCAD'):
            self._parent = parent

        @property
        def abstract_shaft_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2472
            
            return self._parent._cast(_2472.AbstractShaftFromCAD)

        @property
        def clutch_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2473
            
            return self._parent._cast(_2473.ClutchFromCAD)

        @property
        def concept_bearing_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2475
            
            return self._parent._cast(_2475.ConceptBearingFromCAD)

        @property
        def connector_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2476
            
            return self._parent._cast(_2476.ConnectorFromCAD)

        @property
        def cylindrical_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2477
            
            return self._parent._cast(_2477.CylindricalGearFromCAD)

        @property
        def cylindrical_gear_in_planetary_set_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2478
            
            return self._parent._cast(_2478.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_planet_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2479
            
            return self._parent._cast(_2479.CylindricalPlanetGearFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2480
            
            return self._parent._cast(_2480.CylindricalRingGearFromCAD)

        @property
        def cylindrical_sun_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2481
            
            return self._parent._cast(_2481.CylindricalSunGearFromCAD)

        @property
        def mountable_component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2483
            
            return self._parent._cast(_2483.MountableComponentFromCAD)

        @property
        def planet_shaft_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2484
            
            return self._parent._cast(_2484.PlanetShaftFromCAD)

        @property
        def pulley_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2485
            
            return self._parent._cast(_2485.PulleyFromCAD)

        @property
        def rigid_connector_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2486
            
            return self._parent._cast(_2486.RigidConnectorFromCAD)

        @property
        def rolling_bearing_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2487
            
            return self._parent._cast(_2487.RollingBearingFromCAD)

        @property
        def shaft_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2488
            
            return self._parent._cast(_2488.ShaftFromCAD)

        @property
        def component_from_cad(self) -> 'ComponentFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def cast_to(self) -> 'ComponentFromCAD._Cast_ComponentFromCAD':
        return self._Cast_ComponentFromCAD(self)
