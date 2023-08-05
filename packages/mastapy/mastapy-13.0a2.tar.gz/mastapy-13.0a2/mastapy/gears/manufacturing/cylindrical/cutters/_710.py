"""_710.py

CylindricalGearShaver
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.cutters import _713
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAVER = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearShaver')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearShaver',)


class CylindricalGearShaver(_713.InvoluteCutterDesign):
    """CylindricalGearShaver

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAVER

    class _Cast_CylindricalGearShaver:
        """Special nested class for casting CylindricalGearShaver to subclasses."""

        def __init__(self, parent: 'CylindricalGearShaver'):
            self._parent = parent

        @property
        def involute_cutter_design(self):
            return self._parent._cast(_713.InvoluteCutterDesign)

        @property
        def cylindrical_gear_real_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _708
            
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
        def cylindrical_gear_shaver(self) -> 'CylindricalGearShaver':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearShaver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def has_tolerances(self) -> 'bool':
        """bool: 'HasTolerances' is the original name of this property."""

        temp = self.wrapped.HasTolerances

        if temp is None:
            return False

        return temp

    @has_tolerances.setter
    def has_tolerances(self, value: 'bool'):
        self.wrapped.HasTolerances = bool(value) if value else False

    @property
    def normal_tip_thickness(self) -> 'float':
        """float: 'NormalTipThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def root_form_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootFormDiameter' is the original name of this property."""

        temp = self.wrapped.RootFormDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @root_form_diameter.setter
    def root_form_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RootFormDiameter = value

    @property
    def tip_diameter(self) -> 'float':
        """float: 'TipDiameter' is the original name of this property."""

        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @tip_diameter.setter
    def tip_diameter(self, value: 'float'):
        self.wrapped.TipDiameter = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CylindricalGearShaver._Cast_CylindricalGearShaver':
        return self._Cast_CylindricalGearShaver(self)
