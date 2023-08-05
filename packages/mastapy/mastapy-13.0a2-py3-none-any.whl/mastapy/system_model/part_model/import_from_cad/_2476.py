"""_2476.py

ConnectorFromCAD
"""
from mastapy.system_model.part_model.import_from_cad import _2482, _2483
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'ConnectorFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorFromCAD',)


class ConnectorFromCAD(_2483.MountableComponentFromCAD):
    """ConnectorFromCAD

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_FROM_CAD

    class _Cast_ConnectorFromCAD:
        """Special nested class for casting ConnectorFromCAD to subclasses."""

        def __init__(self, parent: 'ConnectorFromCAD'):
            self._parent = parent

        @property
        def mountable_component_from_cad(self):
            return self._parent._cast(_2483.MountableComponentFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2474
            
            return self._parent._cast(_2474.ComponentFromCAD)

        @property
        def concept_bearing_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2475
            
            return self._parent._cast(_2475.ConceptBearingFromCAD)

        @property
        def rigid_connector_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2486
            
            return self._parent._cast(_2486.RigidConnectorFromCAD)

        @property
        def rolling_bearing_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2487
            
            return self._parent._cast(_2487.RollingBearingFromCAD)

        @property
        def connector_from_cad(self) -> 'ConnectorFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mounting(self) -> '_2482.HousedOrMounted':
        """HousedOrMounted: 'Mounting' is the original name of this property."""

        temp = self.wrapped.Mounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _2482.HousedOrMounted)
        return constructor.new_from_mastapy_type(_2482.HousedOrMounted)(value) if value is not None else None

    @mounting.setter
    def mounting(self, value: '_2482.HousedOrMounted'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _2482.HousedOrMounted.type_())
        self.wrapped.Mounting = value

    @property
    def cast_to(self) -> 'ConnectorFromCAD._Cast_ConnectorFromCAD':
        return self._Cast_ConnectorFromCAD(self)
