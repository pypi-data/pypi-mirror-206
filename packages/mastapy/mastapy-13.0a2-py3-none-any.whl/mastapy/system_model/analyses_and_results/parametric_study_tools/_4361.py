"""_4361.py

ParametricStudyHistogram
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_HISTOGRAM = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ParametricStudyHistogram')


__docformat__ = 'restructuredtext en'
__all__ = ('ParametricStudyHistogram',)


class ParametricStudyHistogram(_1749.CustomReportDefinitionItem):
    """ParametricStudyHistogram

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_HISTOGRAM

    class _Cast_ParametricStudyHistogram:
        """Special nested class for casting ParametricStudyHistogram to subclasses."""

        def __init__(self, parent: 'ParametricStudyHistogram'):
            self._parent = parent

        @property
        def custom_report_definition_item(self):
            return self._parent._cast(_1749.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def parametric_study_histogram(self) -> 'ParametricStudyHistogram':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParametricStudyHistogram.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height(self) -> 'int':
        """int: 'Height' is the original name of this property."""

        temp = self.wrapped.Height

        if temp is None:
            return 0

        return temp

    @height.setter
    def height(self, value: 'int'):
        self.wrapped.Height = int(value) if value else 0

    @property
    def number_of_bins(self) -> 'int':
        """int: 'NumberOfBins' is the original name of this property."""

        temp = self.wrapped.NumberOfBins

        if temp is None:
            return 0

        return temp

    @number_of_bins.setter
    def number_of_bins(self, value: 'int'):
        self.wrapped.NumberOfBins = int(value) if value else 0

    @property
    def use_bin_range_for_label(self) -> 'bool':
        """bool: 'UseBinRangeForLabel' is the original name of this property."""

        temp = self.wrapped.UseBinRangeForLabel

        if temp is None:
            return False

        return temp

    @use_bin_range_for_label.setter
    def use_bin_range_for_label(self, value: 'bool'):
        self.wrapped.UseBinRangeForLabel = bool(value) if value else False

    @property
    def width(self) -> 'int':
        """int: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0

        return temp

    @width.setter
    def width(self, value: 'int'):
        self.wrapped.Width = int(value) if value else 0

    @property
    def cast_to(self) -> 'ParametricStudyHistogram._Cast_ParametricStudyHistogram':
        return self._Cast_ParametricStudyHistogram(self)
