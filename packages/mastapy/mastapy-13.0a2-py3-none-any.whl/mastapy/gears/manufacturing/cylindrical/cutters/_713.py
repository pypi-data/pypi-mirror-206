"""_713.py

InvoluteCutterDesign
"""
from mastapy.gears import _329
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1080
from mastapy.gears.manufacturing.cylindrical.cutters import _708
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVOLUTE_CUTTER_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'InvoluteCutterDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('InvoluteCutterDesign',)


class InvoluteCutterDesign(_708.CylindricalGearRealCutterDesign):
    """InvoluteCutterDesign

    This is a mastapy class.
    """

    TYPE = _INVOLUTE_CUTTER_DESIGN

    class _Cast_InvoluteCutterDesign:
        """Special nested class for casting InvoluteCutterDesign to subclasses."""

        def __init__(self, parent: 'InvoluteCutterDesign'):
            self._parent = parent

        @property
        def cylindrical_gear_real_cutter_design(self):
            return self._parent._cast(_708.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _701
            
            return self._parent._cast(_701.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def cylindrical_gear_plunge_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705
            
            return self._parent._cast(_705.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_shaper(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _709
            
            return self._parent._cast(_709.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _710
            
            return self._parent._cast(_710.CylindricalGearShaver)

        @property
        def involute_cutter_design(self) -> 'InvoluteCutterDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InvoluteCutterDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self) -> '_329.Hand':
        """Hand: 'Hand' is the original name of this property."""

        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _329.Hand)
        return constructor.new_from_mastapy_type(_329.Hand)(value) if value is not None else None

    @hand.setter
    def hand(self, value: '_329.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _329.Hand.type_())
        self.wrapped.Hand = value

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property."""

        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    def helix_angle(self, value: 'float'):
        self.wrapped.HelixAngle = float(value) if value else 0.0

    @property
    def number_of_teeth(self) -> 'float':
        """float: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'float'):
        self.wrapped.NumberOfTeeth = float(value) if value else 0.0

    @property
    def tooth_thickness(self) -> '_1080.ToothThicknessSpecificationBase':
        """ToothThicknessSpecificationBase: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InvoluteCutterDesign._Cast_InvoluteCutterDesign':
        return self._Cast_InvoluteCutterDesign(self)
