"""_64.py

FEModalFrequencyComparison
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODAL_FREQUENCY_COMPARISON = python_net_import('SMT.MastaAPI.NodalAnalysis', 'FEModalFrequencyComparison')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModalFrequencyComparison',)


class FEModalFrequencyComparison(_0.APIBase):
    """FEModalFrequencyComparison

    This is a mastapy class.
    """

    TYPE = _FE_MODAL_FREQUENCY_COMPARISON

    class _Cast_FEModalFrequencyComparison:
        """Special nested class for casting FEModalFrequencyComparison to subclasses."""

        def __init__(self, parent: 'FEModalFrequencyComparison'):
            self._parent = parent

        @property
        def fe_modal_frequency_comparison(self) -> 'FEModalFrequencyComparison':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEModalFrequencyComparison.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def difference_in_frequencies(self) -> 'float':
        """float: 'DifferenceInFrequencies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DifferenceInFrequencies

        if temp is None:
            return 0.0

        return temp

    @property
    def full_model_frequency(self) -> 'float':
        """float: 'FullModelFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FullModelFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def mode(self) -> 'int':
        """int: 'Mode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mode

        if temp is None:
            return 0

        return temp

    @property
    def percentage_error(self) -> 'float':
        """float: 'PercentageError' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageError

        if temp is None:
            return 0.0

        return temp

    @property
    def reduced_model_frequency(self) -> 'float':
        """float: 'ReducedModelFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReducedModelFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FEModalFrequencyComparison._Cast_FEModalFrequencyComparison':
        return self._Cast_FEModalFrequencyComparison(self)
