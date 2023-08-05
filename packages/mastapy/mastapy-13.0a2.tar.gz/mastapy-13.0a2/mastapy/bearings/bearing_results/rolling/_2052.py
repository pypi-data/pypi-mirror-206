"""_2052.py

ResultsAtRollerOffset
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_AT_ROLLER_OFFSET = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ResultsAtRollerOffset')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsAtRollerOffset',)


class ResultsAtRollerOffset(_0.APIBase):
    """ResultsAtRollerOffset

    This is a mastapy class.
    """

    TYPE = _RESULTS_AT_ROLLER_OFFSET

    class _Cast_ResultsAtRollerOffset:
        """Special nested class for casting ResultsAtRollerOffset to subclasses."""

        def __init__(self, parent: 'ResultsAtRollerOffset'):
            self._parent = parent

        @property
        def results_at_roller_offset(self) -> 'ResultsAtRollerOffset':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsAtRollerOffset.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_normal_stress(self) -> 'float':
        """float: 'MaximumNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress(self) -> 'float':
        """float: 'MaximumShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stress_inner(self) -> 'float':
        """float: 'NormalStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stress_outer(self) -> 'float':
        """float: 'NormalStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_stress_inner(self) -> 'float':
        """float: 'ShearStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_stress_outer(self) -> 'float':
        """float: 'ShearStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ResultsAtRollerOffset._Cast_ResultsAtRollerOffset':
        return self._Cast_ResultsAtRollerOffset(self)
