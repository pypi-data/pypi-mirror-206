"""_276.py

SafetyFactorItem
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_ITEM = python_net_import('SMT.MastaAPI.Materials', 'SafetyFactorItem')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorItem',)


class SafetyFactorItem(_0.APIBase):
    """SafetyFactorItem

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_ITEM

    class _Cast_SafetyFactorItem:
        """Special nested class for casting SafetyFactorItem to subclasses."""

        def __init__(self, parent: 'SafetyFactorItem'):
            self._parent = parent

        @property
        def composite_fatigue_safety_factor_item(self):
            from mastapy.materials import _246
            
            return self._parent._cast(_246.CompositeFatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item(self):
            from mastapy.materials import _249
            
            return self._parent._cast(_249.FatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item_base(self):
            from mastapy.materials import _250
            
            return self._parent._cast(_250.FatigueSafetyFactorItemBase)

        @property
        def safety_factor_item(self) -> 'SafetyFactorItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactorItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage(self) -> 'float':
        """float: 'Damage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Damage

        if temp is None:
            return 0.0

        return temp

    @property
    def description(self) -> 'str':
        """str: 'Description' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Description

        if temp is None:
            return ''

        return temp

    @property
    def minimum_required_safety_factor(self) -> 'float':
        """float: 'MinimumRequiredSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRequiredSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability(self) -> 'float':
        """float: 'Reliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Reliability

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor(self) -> 'float':
        """float: 'SafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def time_until_failure(self) -> 'float':
        """float: 'TimeUntilFailure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeUntilFailure

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'SafetyFactorItem._Cast_SafetyFactorItem':
        return self._Cast_SafetyFactorItem(self)
