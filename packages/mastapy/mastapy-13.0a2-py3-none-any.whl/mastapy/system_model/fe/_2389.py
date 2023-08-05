"""_2389.py

ReplacedShaftSelectionHelper
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.shaft_model import _2462
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REPLACED_SHAFT_SELECTION_HELPER = python_net_import('SMT.MastaAPI.SystemModel.FE', 'ReplacedShaftSelectionHelper')


__docformat__ = 'restructuredtext en'
__all__ = ('ReplacedShaftSelectionHelper',)


class ReplacedShaftSelectionHelper(_0.APIBase):
    """ReplacedShaftSelectionHelper

    This is a mastapy class.
    """

    TYPE = _REPLACED_SHAFT_SELECTION_HELPER

    class _Cast_ReplacedShaftSelectionHelper:
        """Special nested class for casting ReplacedShaftSelectionHelper to subclasses."""

        def __init__(self, parent: 'ReplacedShaftSelectionHelper'):
            self._parent = parent

        @property
        def replaced_shaft_selection_helper(self) -> 'ReplacedShaftSelectionHelper':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ReplacedShaftSelectionHelper.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_replaced_by_fe(self) -> 'bool':
        """bool: 'IsReplacedByFE' is the original name of this property."""

        temp = self.wrapped.IsReplacedByFE

        if temp is None:
            return False

        return temp

    @is_replaced_by_fe.setter
    def is_replaced_by_fe(self, value: 'bool'):
        self.wrapped.IsReplacedByFE = bool(value) if value else False

    @property
    def shaft(self) -> '_2462.Shaft':
        """Shaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ReplacedShaftSelectionHelper._Cast_ReplacedShaftSelectionHelper':
        return self._Cast_ReplacedShaftSelectionHelper(self)
