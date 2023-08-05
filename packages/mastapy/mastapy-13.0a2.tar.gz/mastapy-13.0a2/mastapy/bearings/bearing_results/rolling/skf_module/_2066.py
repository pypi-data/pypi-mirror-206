"""_2066.py

Frequencies
"""
from mastapy.bearings.bearing_results.rolling.skf_module import _2067, _2079, _2081
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FREQUENCIES = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'Frequencies')


__docformat__ = 'restructuredtext en'
__all__ = ('Frequencies',)


class Frequencies(_2081.SKFCalculationResult):
    """Frequencies

    This is a mastapy class.
    """

    TYPE = _FREQUENCIES

    class _Cast_Frequencies:
        """Special nested class for casting Frequencies to subclasses."""

        def __init__(self, parent: 'Frequencies'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def frequencies(self) -> 'Frequencies':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Frequencies.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency_of_over_rolling(self) -> '_2067.FrequencyOfOverRolling':
        """FrequencyOfOverRolling: 'FrequencyOfOverRolling' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyOfOverRolling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotational_frequency(self) -> '_2079.RotationalFrequency':
        """RotationalFrequency: 'RotationalFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotationalFrequency

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Frequencies._Cast_Frequencies':
        return self._Cast_Frequencies(self)
