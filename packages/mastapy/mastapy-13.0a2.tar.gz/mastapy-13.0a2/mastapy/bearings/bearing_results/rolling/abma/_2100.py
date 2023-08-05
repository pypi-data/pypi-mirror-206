"""_2100.py

ANSIABMA112014Results
"""
from mastapy.bearings.bearing_results.rolling.abma import _2102
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANSIABMA112014_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.ABMA', 'ANSIABMA112014Results')


__docformat__ = 'restructuredtext en'
__all__ = ('ANSIABMA112014Results',)


class ANSIABMA112014Results(_2102.ANSIABMAResults):
    """ANSIABMA112014Results

    This is a mastapy class.
    """

    TYPE = _ANSIABMA112014_RESULTS

    class _Cast_ANSIABMA112014Results:
        """Special nested class for casting ANSIABMA112014Results to subclasses."""

        def __init__(self, parent: 'ANSIABMA112014Results'):
            self._parent = parent

        @property
        def ansiabma_results(self):
            return self._parent._cast(_2102.ANSIABMAResults)

        @property
        def iso_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2090
            
            return self._parent._cast(_2090.ISOResults)

        @property
        def ansiabma112014_results(self) -> 'ANSIABMA112014Results':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ANSIABMA112014Results.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ANSIABMA112014Results._Cast_ANSIABMA112014Results':
        return self._Cast_ANSIABMA112014Results(self)
