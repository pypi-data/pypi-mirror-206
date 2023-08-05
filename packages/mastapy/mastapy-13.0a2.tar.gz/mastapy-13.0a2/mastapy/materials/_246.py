"""_246.py

CompositeFatigueSafetyFactorItem
"""
from mastapy.materials import _249
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOSITE_FATIGUE_SAFETY_FACTOR_ITEM = python_net_import('SMT.MastaAPI.Materials', 'CompositeFatigueSafetyFactorItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CompositeFatigueSafetyFactorItem',)


class CompositeFatigueSafetyFactorItem(_249.FatigueSafetyFactorItem):
    """CompositeFatigueSafetyFactorItem

    This is a mastapy class.
    """

    TYPE = _COMPOSITE_FATIGUE_SAFETY_FACTOR_ITEM

    class _Cast_CompositeFatigueSafetyFactorItem:
        """Special nested class for casting CompositeFatigueSafetyFactorItem to subclasses."""

        def __init__(self, parent: 'CompositeFatigueSafetyFactorItem'):
            self._parent = parent

        @property
        def fatigue_safety_factor_item(self):
            return self._parent._cast(_249.FatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item_base(self):
            from mastapy.materials import _250
            
            return self._parent._cast(_250.FatigueSafetyFactorItemBase)

        @property
        def safety_factor_item(self):
            from mastapy.materials import _276
            
            return self._parent._cast(_276.SafetyFactorItem)

        @property
        def composite_fatigue_safety_factor_item(self) -> 'CompositeFatigueSafetyFactorItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompositeFatigueSafetyFactorItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompositeFatigueSafetyFactorItem._Cast_CompositeFatigueSafetyFactorItem':
        return self._Cast_CompositeFatigueSafetyFactorItem(self)
