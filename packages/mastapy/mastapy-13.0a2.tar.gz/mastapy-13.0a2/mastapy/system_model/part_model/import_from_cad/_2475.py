"""_2475.py

ConceptBearingFromCAD
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2476
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_BEARING_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'ConceptBearingFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptBearingFromCAD',)


class ConceptBearingFromCAD(_2476.ConnectorFromCAD):
    """ConceptBearingFromCAD

    This is a mastapy class.
    """

    TYPE = _CONCEPT_BEARING_FROM_CAD

    class _Cast_ConceptBearingFromCAD:
        """Special nested class for casting ConceptBearingFromCAD to subclasses."""

        def __init__(self, parent: 'ConceptBearingFromCAD'):
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
        def concept_bearing_from_cad(self) -> 'ConceptBearingFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptBearingFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'ConceptBearingFromCAD._Cast_ConceptBearingFromCAD':
        return self._Cast_ConceptBearingFromCAD(self)
