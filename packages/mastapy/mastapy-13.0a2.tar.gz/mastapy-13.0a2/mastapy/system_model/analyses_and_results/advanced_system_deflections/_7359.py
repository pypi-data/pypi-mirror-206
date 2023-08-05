"""_7359.py

TransmissionErrorToOtherPowerLoad
"""
from mastapy._internal import constructor
from mastapy.math_utility import _1501
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSMISSION_ERROR_TO_OTHER_POWER_LOAD = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'TransmissionErrorToOtherPowerLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('TransmissionErrorToOtherPowerLoad',)


class TransmissionErrorToOtherPowerLoad(_0.APIBase):
    """TransmissionErrorToOtherPowerLoad

    This is a mastapy class.
    """

    TYPE = _TRANSMISSION_ERROR_TO_OTHER_POWER_LOAD

    class _Cast_TransmissionErrorToOtherPowerLoad:
        """Special nested class for casting TransmissionErrorToOtherPowerLoad to subclasses."""

        def __init__(self, parent: 'TransmissionErrorToOtherPowerLoad'):
            self._parent = parent

        @property
        def transmission_error_to_other_power_load(self) -> 'TransmissionErrorToOtherPowerLoad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TransmissionErrorToOtherPowerLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_te(self) -> 'float':
        """float: 'MeanTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanTE

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def peak_to_peak_te(self) -> 'float':
        """float: 'PeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakTE

        if temp is None:
            return 0.0

        return temp

    @property
    def fourier_series_of_te(self) -> '_1501.FourierSeries':
        """FourierSeries: 'FourierSeriesOfTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FourierSeriesOfTE

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TransmissionErrorToOtherPowerLoad._Cast_TransmissionErrorToOtherPowerLoad':
        return self._Cast_TransmissionErrorToOtherPowerLoad(self)
