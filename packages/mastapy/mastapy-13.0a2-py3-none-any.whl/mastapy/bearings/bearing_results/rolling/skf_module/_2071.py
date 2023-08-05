"""_2071.py

Grease
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2081
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GREASE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'Grease')


__docformat__ = 'restructuredtext en'
__all__ = ('Grease',)


class Grease(_2081.SKFCalculationResult):
    """Grease

    This is a mastapy class.
    """

    TYPE = _GREASE

    class _Cast_Grease:
        """Special nested class for casting Grease to subclasses."""

        def __init__(self, parent: 'Grease'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def grease(self) -> 'Grease':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Grease.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def grease_life(self) -> 'float':
        """float: 'GreaseLife' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GreaseLife

        if temp is None:
            return 0.0

        return temp

    @property
    def relubrication_interval(self) -> 'float':
        """float: 'RelubricationInterval' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelubricationInterval

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'Grease._Cast_Grease':
        return self._Cast_Grease(self)
