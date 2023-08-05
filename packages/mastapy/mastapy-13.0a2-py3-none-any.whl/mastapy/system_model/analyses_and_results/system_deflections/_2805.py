"""_2805.py

SystemDeflectionDrawStyle
"""
from mastapy._internal import constructor
from mastapy.utility_gui import _1837
from mastapy.system_model.drawing import _2227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SystemDeflectionDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('SystemDeflectionDrawStyle',)


class SystemDeflectionDrawStyle(_2227.ContourDrawStyle):
    """SystemDeflectionDrawStyle

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_DRAW_STYLE

    class _Cast_SystemDeflectionDrawStyle:
        """Special nested class for casting SystemDeflectionDrawStyle to subclasses."""

        def __init__(self, parent: 'SystemDeflectionDrawStyle'):
            self._parent = parent

        @property
        def contour_draw_style(self):
            return self._parent._cast(_2227.ContourDrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _304
            
            return self._parent._cast(_304.DrawStyleBase)

        @property
        def system_deflection_draw_style(self) -> 'SystemDeflectionDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SystemDeflectionDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_arrows(self) -> 'bool':
        """bool: 'ShowArrows' is the original name of this property."""

        temp = self.wrapped.ShowArrows

        if temp is None:
            return False

        return temp

    @show_arrows.setter
    def show_arrows(self, value: 'bool'):
        self.wrapped.ShowArrows = bool(value) if value else False

    @property
    def force_arrow_scaling(self) -> '_1837.ScalingDrawStyle':
        """ScalingDrawStyle: 'ForceArrowScaling' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceArrowScaling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SystemDeflectionDrawStyle._Cast_SystemDeflectionDrawStyle':
        return self._Cast_SystemDeflectionDrawStyle(self)
