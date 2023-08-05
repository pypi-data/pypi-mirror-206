"""_2473.py

ClutchFromCAD
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'ClutchFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchFromCAD',)


class ClutchFromCAD(_2483.MountableComponentFromCAD):
    """ClutchFromCAD

    This is a mastapy class.
    """

    TYPE = _CLUTCH_FROM_CAD

    class _Cast_ClutchFromCAD:
        """Special nested class for casting ClutchFromCAD to subclasses."""

        def __init__(self, parent: 'ClutchFromCAD'):
            self._parent = parent

        @property
        def mountable_component_from_cad(self):
            return self._parent._cast(_2483.MountableComponentFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2474
            
            return self._parent._cast(_2474.ComponentFromCAD)

        @property
        def clutch_from_cad(self) -> 'ClutchFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_name(self) -> 'str':
        """str: 'ClutchName' is the original name of this property."""

        temp = self.wrapped.ClutchName

        if temp is None:
            return ''

        return temp

    @clutch_name.setter
    def clutch_name(self, value: 'str'):
        self.wrapped.ClutchName = str(value) if value else ''

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
    def cast_to(self) -> 'ClutchFromCAD._Cast_ClutchFromCAD':
        return self._Cast_ClutchFromCAD(self)
