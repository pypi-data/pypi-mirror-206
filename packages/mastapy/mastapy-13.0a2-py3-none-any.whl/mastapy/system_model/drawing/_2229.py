"""_2229.py

DynamicAnalysisViewable
"""
from mastapy.system_model.drawing import _2227, _2234
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'DynamicAnalysisViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicAnalysisViewable',)


class DynamicAnalysisViewable(_2234.PartAnalysisCaseWithContourViewable):
    """DynamicAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS_VIEWABLE

    class _Cast_DynamicAnalysisViewable:
        """Special nested class for casting DynamicAnalysisViewable to subclasses."""

        def __init__(self, parent: 'DynamicAnalysisViewable'):
            self._parent = parent

        @property
        def part_analysis_case_with_contour_viewable(self):
            return self._parent._cast(_2234.PartAnalysisCaseWithContourViewable)

        @property
        def harmonic_analysis_viewable(self):
            from mastapy.system_model.drawing import _2230
            
            return self._parent._cast(_2230.HarmonicAnalysisViewable)

        @property
        def modal_analysis_viewable(self):
            from mastapy.system_model.drawing import _2232
            
            return self._parent._cast(_2232.ModalAnalysisViewable)

        @property
        def dynamic_analysis_viewable(self) -> 'DynamicAnalysisViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicAnalysisViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour_draw_style(self) -> '_2227.ContourDrawStyle':
        """ContourDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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

    def fe_results(self):
        """ 'FEResults' is the original name of this method."""

        self.wrapped.FEResults()

    @property
    def cast_to(self) -> 'DynamicAnalysisViewable._Cast_DynamicAnalysisViewable':
        return self._Cast_DynamicAnalysisViewable(self)
