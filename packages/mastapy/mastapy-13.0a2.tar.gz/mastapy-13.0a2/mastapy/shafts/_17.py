"""_17.py

ShaftAxialBendingXBendingYTorsionalComponentValues
"""
from mastapy._internal import constructor
from mastapy.shafts import _18
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_AXIAL_BENDING_X_BENDING_Y_TORSIONAL_COMPONENT_VALUES = python_net_import('SMT.MastaAPI.Shafts', 'ShaftAxialBendingXBendingYTorsionalComponentValues')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftAxialBendingXBendingYTorsionalComponentValues',)


class ShaftAxialBendingXBendingYTorsionalComponentValues(_18.ShaftAxialTorsionalComponentValues):
    """ShaftAxialBendingXBendingYTorsionalComponentValues

    This is a mastapy class.
    """

    TYPE = _SHAFT_AXIAL_BENDING_X_BENDING_Y_TORSIONAL_COMPONENT_VALUES

    class _Cast_ShaftAxialBendingXBendingYTorsionalComponentValues:
        """Special nested class for casting ShaftAxialBendingXBendingYTorsionalComponentValues to subclasses."""

        def __init__(self, parent: 'ShaftAxialBendingXBendingYTorsionalComponentValues'):
            self._parent = parent

        @property
        def shaft_axial_torsional_component_values(self):
            return self._parent._cast(_18.ShaftAxialTorsionalComponentValues)

        @property
        def shaft_axial_bending_x_bending_y_torsional_component_values(self) -> 'ShaftAxialBendingXBendingYTorsionalComponentValues':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftAxialBendingXBendingYTorsionalComponentValues.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_x(self) -> 'float':
        """float: 'BendingX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingX

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_y(self) -> 'float':
        """float: 'BendingY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingY

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ShaftAxialBendingXBendingYTorsionalComponentValues._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues':
        return self._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues(self)
