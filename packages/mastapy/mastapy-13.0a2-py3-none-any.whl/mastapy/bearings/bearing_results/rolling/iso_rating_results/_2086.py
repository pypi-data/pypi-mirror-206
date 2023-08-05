"""_2086.py

BallISO2812007Results
"""
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2088
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_ISO2812007_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults', 'BallISO2812007Results')


__docformat__ = 'restructuredtext en'
__all__ = ('BallISO2812007Results',)


class BallISO2812007Results(_2088.ISO2812007Results):
    """BallISO2812007Results

    This is a mastapy class.
    """

    TYPE = _BALL_ISO2812007_RESULTS

    class _Cast_BallISO2812007Results:
        """Special nested class for casting BallISO2812007Results to subclasses."""

        def __init__(self, parent: 'BallISO2812007Results'):
            self._parent = parent

        @property
        def iso2812007_results(self):
            return self._parent._cast(_2088.ISO2812007Results)

        @property
        def iso_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2090
            
            return self._parent._cast(_2090.ISOResults)

        @property
        def ball_iso2812007_results(self) -> 'BallISO2812007Results':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BallISO2812007Results.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BallISO2812007Results._Cast_BallISO2812007Results':
        return self._Cast_BallISO2812007Results(self)
