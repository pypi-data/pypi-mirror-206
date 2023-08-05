"""_2232.py

ModalAnalysisViewable
"""
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
from mastapy._internal import constructor
from mastapy.system_model.drawing import _2229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'ModalAnalysisViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisViewable',)


class ModalAnalysisViewable(_2229.DynamicAnalysisViewable):
    """ModalAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_VIEWABLE

    class _Cast_ModalAnalysisViewable:
        """Special nested class for casting ModalAnalysisViewable to subclasses."""

        def __init__(self, parent: 'ModalAnalysisViewable'):
            self._parent = parent

        @property
        def dynamic_analysis_viewable(self):
            return self._parent._cast(_2229.DynamicAnalysisViewable)

        @property
        def part_analysis_case_with_contour_viewable(self):
            from mastapy.system_model.drawing import _2234
            
            return self._parent._cast(_2234.PartAnalysisCaseWithContourViewable)

        @property
        def modal_analysis_viewable(self) -> 'ModalAnalysisViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ModalAnalysisViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_analysis_draw_style(self) -> '_6295.DynamicAnalysisDrawStyle':
        """DynamicAnalysisDrawStyle: 'DynamicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ModalAnalysisViewable._Cast_ModalAnalysisViewable':
        return self._Cast_ModalAnalysisViewable(self)
