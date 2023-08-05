"""_2812.py

TransmissionErrorResult
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSMISSION_ERROR_RESULT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'TransmissionErrorResult')


__docformat__ = 'restructuredtext en'
__all__ = ('TransmissionErrorResult',)


class TransmissionErrorResult(_0.APIBase):
    """TransmissionErrorResult

    This is a mastapy class.
    """

    TYPE = _TRANSMISSION_ERROR_RESULT

    class _Cast_TransmissionErrorResult:
        """Special nested class for casting TransmissionErrorResult to subclasses."""

        def __init__(self, parent: 'TransmissionErrorResult'):
            self._parent = parent

        @property
        def transmission_error_result(self) -> 'TransmissionErrorResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TransmissionErrorResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def transmission_error(self) -> 'float':
        """float: 'TransmissionError' is the original name of this property."""

        temp = self.wrapped.TransmissionError

        if temp is None:
            return 0.0

        return temp

    @transmission_error.setter
    def transmission_error(self, value: 'float'):
        self.wrapped.TransmissionError = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'TransmissionErrorResult._Cast_TransmissionErrorResult':
        return self._Cast_TransmissionErrorResult(self)
