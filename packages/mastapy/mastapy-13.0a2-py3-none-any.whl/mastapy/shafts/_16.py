"""_16.py

ShaftAxialBendingTorsionalComponentValues
"""
from mastapy._internal import constructor
from mastapy.shafts import _18
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_AXIAL_BENDING_TORSIONAL_COMPONENT_VALUES = python_net_import('SMT.MastaAPI.Shafts', 'ShaftAxialBendingTorsionalComponentValues')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftAxialBendingTorsionalComponentValues',)


class ShaftAxialBendingTorsionalComponentValues(_18.ShaftAxialTorsionalComponentValues):
    """ShaftAxialBendingTorsionalComponentValues

    This is a mastapy class.
    """

    TYPE = _SHAFT_AXIAL_BENDING_TORSIONAL_COMPONENT_VALUES

    class _Cast_ShaftAxialBendingTorsionalComponentValues:
        """Special nested class for casting ShaftAxialBendingTorsionalComponentValues to subclasses."""

        def __init__(self, parent: 'ShaftAxialBendingTorsionalComponentValues'):
            self._parent = parent

        @property
        def shaft_axial_torsional_component_values(self):
            return self._parent._cast(_18.ShaftAxialTorsionalComponentValues)

        @property
        def shaft_axial_bending_torsional_component_values(self) -> 'ShaftAxialBendingTorsionalComponentValues':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftAxialBendingTorsionalComponentValues.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending(self) -> 'float':
        """float: 'Bending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ShaftAxialBendingTorsionalComponentValues._Cast_ShaftAxialBendingTorsionalComponentValues':
        return self._Cast_ShaftAxialBendingTorsionalComponentValues(self)
