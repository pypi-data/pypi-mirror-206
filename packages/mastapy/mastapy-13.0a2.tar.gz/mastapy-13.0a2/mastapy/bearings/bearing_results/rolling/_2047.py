"""_2047.py

MaximumStaticContactStressResultsAbstract
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAXIMUM_STATIC_CONTACT_STRESS_RESULTS_ABSTRACT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'MaximumStaticContactStressResultsAbstract')


__docformat__ = 'restructuredtext en'
__all__ = ('MaximumStaticContactStressResultsAbstract',)


class MaximumStaticContactStressResultsAbstract(_0.APIBase):
    """MaximumStaticContactStressResultsAbstract

    This is a mastapy class.
    """

    TYPE = _MAXIMUM_STATIC_CONTACT_STRESS_RESULTS_ABSTRACT

    class _Cast_MaximumStaticContactStressResultsAbstract:
        """Special nested class for casting MaximumStaticContactStressResultsAbstract to subclasses."""

        def __init__(self, parent: 'MaximumStaticContactStressResultsAbstract'):
            self._parent = parent

        @property
        def maximum_static_contact_stress(self):
            from mastapy.bearings.bearing_results.rolling import _2045
            
            return self._parent._cast(_2045.MaximumStaticContactStress)

        @property
        def maximum_static_contact_stress_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _2046
            
            return self._parent._cast(_2046.MaximumStaticContactStressDutyCycle)

        @property
        def maximum_static_contact_stress_results_abstract(self) -> 'MaximumStaticContactStressResultsAbstract':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaximumStaticContactStressResultsAbstract.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def safety_factor_inner(self) -> 'float':
        """float: 'SafetyFactorInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorInner

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_outer(self) -> 'float':
        """float: 'SafetyFactorOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_ratio_inner(self) -> 'float':
        """float: 'StressRatioInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressRatioInner

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_ratio_outer(self) -> 'float':
        """float: 'StressRatioOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressRatioOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'MaximumStaticContactStressResultsAbstract._Cast_MaximumStaticContactStressResultsAbstract':
        return self._Cast_MaximumStaticContactStressResultsAbstract(self)
