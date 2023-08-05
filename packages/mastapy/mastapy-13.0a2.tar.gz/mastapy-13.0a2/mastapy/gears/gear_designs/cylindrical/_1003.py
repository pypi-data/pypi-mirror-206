"""_1003.py

CylindricalGearBasicRack
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.cylindrical import (
    _995, _1075, _1018, _1001
)
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BASIC_RACK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearBasicRack')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearBasicRack',)


class CylindricalGearBasicRack(_1001.CylindricalGearAbstractRack):
    """CylindricalGearBasicRack

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BASIC_RACK

    class _Cast_CylindricalGearBasicRack:
        """Special nested class for casting CylindricalGearBasicRack to subclasses."""

        def __init__(self, parent: 'CylindricalGearBasicRack'):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_rack(self):
            return self._parent._cast(_1001.CylindricalGearAbstractRack)

        @property
        def standard_rack(self):
            from mastapy.gears.gear_designs.cylindrical import _1070
            
            return self._parent._cast(_1070.StandardRack)

        @property
        def cylindrical_gear_basic_rack(self) -> 'CylindricalGearBasicRack':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearBasicRack.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_rack_clearance_factor(self) -> 'float':
        """float: 'BasicRackClearanceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRackClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_profile(self) -> '_995.BasicRackProfiles':
        """BasicRackProfiles: 'BasicRackProfile' is the original name of this property."""

        temp = self.wrapped.BasicRackProfile

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _995.BasicRackProfiles)
        return constructor.new_from_mastapy_type(_995.BasicRackProfiles)(value) if value is not None else None

    @basic_rack_profile.setter
    def basic_rack_profile(self, value: '_995.BasicRackProfiles'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _995.BasicRackProfiles.type_())
        self.wrapped.BasicRackProfile = value

    @property
    def proportional_method_for_tip_clearance(self) -> '_1075.TipAlterationCoefficientMethod':
        """TipAlterationCoefficientMethod: 'ProportionalMethodForTipClearance' is the original name of this property."""

        temp = self.wrapped.ProportionalMethodForTipClearance

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1075.TipAlterationCoefficientMethod)
        return constructor.new_from_mastapy_type(_1075.TipAlterationCoefficientMethod)(value) if value is not None else None

    @proportional_method_for_tip_clearance.setter
    def proportional_method_for_tip_clearance(self, value: '_1075.TipAlterationCoefficientMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1075.TipAlterationCoefficientMethod.type_())
        self.wrapped.ProportionalMethodForTipClearance = value

    @property
    def tip_alteration_proportional_method_mesh(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'TipAlterationProportionalMethodMesh' is the original name of this property."""

        temp = self.wrapped.TipAlterationProportionalMethodMesh

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @tip_alteration_proportional_method_mesh.setter
    def tip_alteration_proportional_method_mesh(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.TipAlterationProportionalMethodMesh = value

    @property
    def pinion_type_cutter_for_rating(self) -> '_1018.CylindricalGearPinionTypeCutter':
        """CylindricalGearPinionTypeCutter: 'PinionTypeCutterForRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionTypeCutterForRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearBasicRack._Cast_CylindricalGearBasicRack':
        return self._Cast_CylindricalGearBasicRack(self)
