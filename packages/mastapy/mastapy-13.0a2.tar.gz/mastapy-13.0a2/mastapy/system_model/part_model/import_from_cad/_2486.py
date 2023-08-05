"""_2486.py

RigidConnectorFromCAD
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2476
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGID_CONNECTOR_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'RigidConnectorFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('RigidConnectorFromCAD',)


class RigidConnectorFromCAD(_2476.ConnectorFromCAD):
    """RigidConnectorFromCAD

    This is a mastapy class.
    """

    TYPE = _RIGID_CONNECTOR_FROM_CAD

    class _Cast_RigidConnectorFromCAD:
        """Special nested class for casting RigidConnectorFromCAD to subclasses."""

        def __init__(self, parent: 'RigidConnectorFromCAD'):
            self._parent = parent

        @property
        def connector_from_cad(self):
            return self._parent._cast(_2476.ConnectorFromCAD)

        @property
        def mountable_component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2483
            
            return self._parent._cast(_2483.MountableComponentFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2474
            
            return self._parent._cast(_2474.ComponentFromCAD)

        @property
        def rigid_connector_from_cad(self) -> 'RigidConnectorFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RigidConnectorFromCAD.TYPE'):
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
    def cast_to(self) -> 'RigidConnectorFromCAD._Cast_RigidConnectorFromCAD':
        return self._Cast_RigidConnectorFromCAD(self)
