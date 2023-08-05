"""_303.py

DrawStyle
"""
from mastapy._internal import constructor
from mastapy.geometry import _304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DRAW_STYLE = python_net_import('SMT.MastaAPI.Geometry', 'DrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('DrawStyle',)


class DrawStyle(_304.DrawStyleBase):
    """DrawStyle

    This is a mastapy class.
    """

    TYPE = _DRAW_STYLE

    class _Cast_DrawStyle:
        """Special nested class for casting DrawStyle to subclasses."""

        def __init__(self, parent: 'DrawStyle'):
            self._parent = parent

        @property
        def draw_style_base(self):
            return self._parent._cast(_304.DrawStyleBase)

        @property
        def model_view_options_draw_style(self):
            from mastapy.system_model.drawing import _2233
            
            return self._parent._cast(_2233.ModelViewOptionsDrawStyle)

        @property
        def cylindrical_gear_geometric_entity_draw_style(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4056
            
            return self._parent._cast(_4056.CylindricalGearGeometricEntityDrawStyle)

        @property
        def power_flow_draw_style(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4098
            
            return self._parent._cast(_4098.PowerFlowDrawStyle)

        @property
        def draw_style(self) -> 'DrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def outline_axis(self) -> 'bool':
        """bool: 'OutlineAxis' is the original name of this property."""

        temp = self.wrapped.OutlineAxis

        if temp is None:
            return False

        return temp

    @outline_axis.setter
    def outline_axis(self, value: 'bool'):
        self.wrapped.OutlineAxis = bool(value) if value else False

    @property
    def show_part_labels(self) -> 'bool':
        """bool: 'ShowPartLabels' is the original name of this property."""

        temp = self.wrapped.ShowPartLabels

        if temp is None:
            return False

        return temp

    @show_part_labels.setter
    def show_part_labels(self, value: 'bool'):
        self.wrapped.ShowPartLabels = bool(value) if value else False

    @property
    def cast_to(self) -> 'DrawStyle._Cast_DrawStyle':
        return self._Cast_DrawStyle(self)
