"""_2432.py

ExternalCADModel
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ExternalCADModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModel',)


class ExternalCADModel(_2424.Component):
    """ExternalCADModel

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL

    class _Cast_ExternalCADModel:
        """Special nested class for casting ExternalCADModel to subclasses."""

        def __init__(self, parent: 'ExternalCADModel'):
            self._parent = parent

        @property
        def component(self):
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def external_cad_model(self) -> 'ExternalCADModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExternalCADModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def draw_two_sided(self) -> 'bool':
        """bool: 'DrawTwoSided' is the original name of this property."""

        temp = self.wrapped.DrawTwoSided

        if temp is None:
            return False

        return temp

    @draw_two_sided.setter
    def draw_two_sided(self, value: 'bool'):
        self.wrapped.DrawTwoSided = bool(value) if value else False

    @property
    def opacity(self) -> 'float':
        """float: 'Opacity' is the original name of this property."""

        temp = self.wrapped.Opacity

        if temp is None:
            return 0.0

        return temp

    @opacity.setter
    def opacity(self, value: 'float'):
        self.wrapped.Opacity = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ExternalCADModel._Cast_ExternalCADModel':
        return self._Cast_ExternalCADModel(self)
