"""_1963.py

ISOTR1417912001Results
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1964
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISOTR1417912001_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ISOTR1417912001Results')


__docformat__ = 'restructuredtext en'
__all__ = ('ISOTR1417912001Results',)


class ISOTR1417912001Results(_1964.ISOTR141792001Results):
    """ISOTR1417912001Results

    This is a mastapy class.
    """

    TYPE = _ISOTR1417912001_RESULTS

    class _Cast_ISOTR1417912001Results:
        """Special nested class for casting ISOTR1417912001Results to subclasses."""

        def __init__(self, parent: 'ISOTR1417912001Results'):
            self._parent = parent

        @property
        def isotr141792001_results(self):
            return self._parent._cast(_1964.ISOTR141792001Results)

        @property
        def isotr1417912001_results(self) -> 'ISOTR1417912001Results':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISOTR1417912001Results.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_dip_factor(self) -> 'float':
        """float: 'BearingDipFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDipFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_dip_factor_max(self) -> 'float':
        """float: 'BearingDipFactorMax' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDipFactorMax

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_dip_factor_min(self) -> 'float':
        """float: 'BearingDipFactorMin' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDipFactorMin

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_moment_of_the_bearing_seal(self) -> 'float':
        """float: 'FrictionalMomentOfTheBearingSeal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalMomentOfTheBearingSeal

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISOTR1417912001Results._Cast_ISOTR1417912001Results':
        return self._Cast_ISOTR1417912001Results(self)
