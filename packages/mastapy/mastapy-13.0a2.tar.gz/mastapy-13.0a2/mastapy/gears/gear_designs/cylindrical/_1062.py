"""_1062.py

RelativeValuesSpecification
"""
from typing import TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELATIVE_VALUES_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'RelativeValuesSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('RelativeValuesSpecification',)


T = TypeVar('T', bound='RelativeValuesSpecification')


class RelativeValuesSpecification(_0.APIBase, Generic[T]):
    """RelativeValuesSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _RELATIVE_VALUES_SPECIFICATION

    class _Cast_RelativeValuesSpecification:
        """Special nested class for casting RelativeValuesSpecification to subclasses."""

        def __init__(self, parent: 'RelativeValuesSpecification'):
            self._parent = parent

        @property
        def backlash_specification(self):
            from mastapy.gears.gear_designs.cylindrical import _994
            
            return self._parent._cast(_994.BacklashSpecification)

        @property
        def finish_stock_specification(self):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1083
            
            return self._parent._cast(_1083.FinishStockSpecification)

        @property
        def relative_values_specification(self) -> 'RelativeValuesSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RelativeValuesSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RelativeValuesSpecification._Cast_RelativeValuesSpecification':
        return self._Cast_RelativeValuesSpecification(self)
