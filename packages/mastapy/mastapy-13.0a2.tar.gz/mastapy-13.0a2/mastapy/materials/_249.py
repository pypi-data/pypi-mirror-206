"""_249.py

FatigueSafetyFactorItem
"""
from mastapy.materials import _250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FATIGUE_SAFETY_FACTOR_ITEM = python_net_import('SMT.MastaAPI.Materials', 'FatigueSafetyFactorItem')


__docformat__ = 'restructuredtext en'
__all__ = ('FatigueSafetyFactorItem',)


class FatigueSafetyFactorItem(_250.FatigueSafetyFactorItemBase):
    """FatigueSafetyFactorItem

    This is a mastapy class.
    """

    TYPE = _FATIGUE_SAFETY_FACTOR_ITEM

    class _Cast_FatigueSafetyFactorItem:
        """Special nested class for casting FatigueSafetyFactorItem to subclasses."""

        def __init__(self, parent: 'FatigueSafetyFactorItem'):
            self._parent = parent

        @property
        def fatigue_safety_factor_item_base(self):
            return self._parent._cast(_250.FatigueSafetyFactorItemBase)

        @property
        def safety_factor_item(self):
            from mastapy.materials import _276
            
            return self._parent._cast(_276.SafetyFactorItem)

        @property
        def composite_fatigue_safety_factor_item(self):
            from mastapy.materials import _246
            
            return self._parent._cast(_246.CompositeFatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item(self) -> 'FatigueSafetyFactorItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FatigueSafetyFactorItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem':
        return self._Cast_FatigueSafetyFactorItem(self)
