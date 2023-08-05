"""_2093.py

RollerISOTS162812008Results
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2091
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_ISOTS162812008_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults', 'RollerISOTS162812008Results')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerISOTS162812008Results',)


class RollerISOTS162812008Results(_2091.ISOTS162812008Results):
    """RollerISOTS162812008Results

    This is a mastapy class.
    """

    TYPE = _ROLLER_ISOTS162812008_RESULTS

    class _Cast_RollerISOTS162812008Results:
        """Special nested class for casting RollerISOTS162812008Results to subclasses."""

        def __init__(self, parent: 'RollerISOTS162812008Results'):
            self._parent = parent

        @property
        def isots162812008_results(self):
            return self._parent._cast(_2091.ISOTS162812008Results)

        @property
        def iso_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2090
            
            return self._parent._cast(_2090.ISOResults)

        @property
        def roller_isots162812008_results(self) -> 'RollerISOTS162812008Results':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerISOTS162812008Results.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_dynamic_load_rating_of_a_bearing_lamina_of_the_inner_ring(self) -> 'float':
        """float: 'BasicDynamicLoadRatingOfABearingLaminaOfTheInnerRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicDynamicLoadRatingOfABearingLaminaOfTheInnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_dynamic_load_rating_of_a_bearing_lamina_of_the_outer_ring(self) -> 'float':
        """float: 'BasicDynamicLoadRatingOfABearingLaminaOfTheOuterRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicDynamicLoadRatingOfABearingLaminaOfTheOuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_load_assuming_line_contacts(self) -> 'float':
        """float: 'EquivalentLoadAssumingLineContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentLoadAssumingLineContacts

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'RollerISOTS162812008Results._Cast_RollerISOTS162812008Results':
        return self._Cast_RollerISOTS162812008Results(self)
