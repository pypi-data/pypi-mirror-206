"""_2087.py

BallISOTS162812008Results
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2091
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_ISOTS162812008_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults', 'BallISOTS162812008Results')


__docformat__ = 'restructuredtext en'
__all__ = ('BallISOTS162812008Results',)


class BallISOTS162812008Results(_2091.ISOTS162812008Results):
    """BallISOTS162812008Results

    This is a mastapy class.
    """

    TYPE = _BALL_ISOTS162812008_RESULTS

    class _Cast_BallISOTS162812008Results:
        """Special nested class for casting BallISOTS162812008Results to subclasses."""

        def __init__(self, parent: 'BallISOTS162812008Results'):
            self._parent = parent

        @property
        def isots162812008_results(self):
            return self._parent._cast(_2091.ISOTS162812008Results)

        @property
        def iso_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2090
            
            return self._parent._cast(_2090.ISOResults)

        @property
        def ball_isots162812008_results(self) -> 'BallISOTS162812008Results':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BallISOTS162812008Results.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stiffness_inner(self) -> 'float':
        """float: 'ContactStiffnessInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStiffnessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stiffness_outer(self) -> 'float':
        """float: 'ContactStiffnessOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStiffnessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'BallISOTS162812008Results._Cast_BallISOTS162812008Results':
        return self._Cast_BallISOTS162812008Results(self)
