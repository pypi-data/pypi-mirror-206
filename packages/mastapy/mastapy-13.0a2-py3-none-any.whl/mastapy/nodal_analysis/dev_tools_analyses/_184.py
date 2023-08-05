"""_184.py

FEModelInstanceDrawStyle
"""
from mastapy.nodal_analysis.dev_tools_analyses import _175
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_INSTANCE_DRAW_STYLE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelInstanceDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelInstanceDrawStyle',)


class FEModelInstanceDrawStyle(_0.APIBase):
    """FEModelInstanceDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_INSTANCE_DRAW_STYLE

    class _Cast_FEModelInstanceDrawStyle:
        """Special nested class for casting FEModelInstanceDrawStyle to subclasses."""

        def __init__(self, parent: 'FEModelInstanceDrawStyle'):
            self._parent = parent

        @property
        def fe_model_instance_draw_style(self) -> 'FEModelInstanceDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEModelInstanceDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def model_draw_style(self) -> '_175.DrawStyleForFE':
        """DrawStyleForFE: 'ModelDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FEModelInstanceDrawStyle._Cast_FEModelInstanceDrawStyle':
        return self._Cast_FEModelInstanceDrawStyle(self)
