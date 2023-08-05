"""_714.py

MutatableCommon
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.manufacturing.cylindrical import _604
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.cutters import _698
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MUTATABLE_COMMON = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'MutatableCommon')


__docformat__ = 'restructuredtext en'
__all__ = ('MutatableCommon',)


class MutatableCommon(_698.CurveInLinkedList):
    """MutatableCommon

    This is a mastapy class.
    """

    TYPE = _MUTATABLE_COMMON

    class _Cast_MutatableCommon:
        """Special nested class for casting MutatableCommon to subclasses."""

        def __init__(self, parent: 'MutatableCommon'):
            self._parent = parent

        @property
        def curve_in_linked_list(self):
            return self._parent._cast(_698.CurveInLinkedList)

        @property
        def mutatable_curve(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _715
            
            return self._parent._cast(_715.MutatableCurve)

        @property
        def mutatable_fillet(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _716
            
            return self._parent._cast(_716.MutatableFillet)

        @property
        def mutatable_common(self) -> 'MutatableCommon':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MutatableCommon.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def protuberance(self) -> 'float':
        """float: 'Protuberance' is the original name of this property."""

        temp = self.wrapped.Protuberance

        if temp is None:
            return 0.0

        return temp

    @protuberance.setter
    def protuberance(self, value: 'float'):
        self.wrapped.Protuberance = float(value) if value else 0.0

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value else 0.0

    @property
    def section(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections':
        """enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections: 'Section' is the original name of this property."""

        temp = self.wrapped.Section

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @section.setter
    def section(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Section = value

    def remove(self):
        """ 'Remove' is the original name of this method."""

        self.wrapped.Remove()

    def split(self):
        """ 'Split' is the original name of this method."""

        self.wrapped.Split()

    @property
    def cast_to(self) -> 'MutatableCommon._Cast_MutatableCommon':
        return self._Cast_MutatableCommon(self)
