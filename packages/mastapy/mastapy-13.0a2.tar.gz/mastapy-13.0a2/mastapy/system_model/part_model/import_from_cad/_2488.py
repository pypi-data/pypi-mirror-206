"""_2488.py

ShaftFromCAD
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2472
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'ShaftFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftFromCAD',)


class ShaftFromCAD(_2472.AbstractShaftFromCAD):
    """ShaftFromCAD

    This is a mastapy class.
    """

    TYPE = _SHAFT_FROM_CAD

    class _Cast_ShaftFromCAD:
        """Special nested class for casting ShaftFromCAD to subclasses."""

        def __init__(self, parent: 'ShaftFromCAD'):
            self._parent = parent

        @property
        def abstract_shaft_from_cad(self):
            return self._parent._cast(_2472.AbstractShaftFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2474
            
            return self._parent._cast(_2474.ComponentFromCAD)

        @property
        def shaft_from_cad(self) -> 'ShaftFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_assembly(self) -> 'bool':
        """bool: 'CreateAssembly' is the original name of this property."""

        temp = self.wrapped.CreateAssembly

        if temp is None:
            return False

        return temp

    @create_assembly.setter
    def create_assembly(self, value: 'bool'):
        self.wrapped.CreateAssembly = bool(value) if value else False

    @property
    def cast_to(self) -> 'ShaftFromCAD._Cast_ShaftFromCAD':
        return self._Cast_ShaftFromCAD(self)
