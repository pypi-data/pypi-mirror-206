"""_4630.py

ModalAnalysisOptions
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4608
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ModalAnalysisOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisOptions',)


class ModalAnalysisOptions(_0.APIBase):
    """ModalAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_OPTIONS

    class _Cast_ModalAnalysisOptions:
        """Special nested class for casting ModalAnalysisOptions to subclasses."""

        def __init__(self, parent: 'ModalAnalysisOptions'):
            self._parent = parent

        @property
        def modal_analysis_options(self) -> 'ModalAnalysisOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ModalAnalysisOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_mode_frequency(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumModeFrequency' is the original name of this property."""

        temp = self.wrapped.MaximumModeFrequency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum_mode_frequency.setter
    def maximum_mode_frequency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumModeFrequency = value

    @property
    def number_of_modes(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfModes' is the original name of this property."""

        temp = self.wrapped.NumberOfModes

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_modes.setter
    def number_of_modes(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfModes = value

    @property
    def frequency_response_options_for_reports(self) -> '_4608.FrequencyResponseAnalysisOptions':
        """FrequencyResponseAnalysisOptions: 'FrequencyResponseOptionsForReports' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyResponseOptionsForReports

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ModalAnalysisOptions._Cast_ModalAnalysisOptions':
        return self._Cast_ModalAnalysisOptions(self)
