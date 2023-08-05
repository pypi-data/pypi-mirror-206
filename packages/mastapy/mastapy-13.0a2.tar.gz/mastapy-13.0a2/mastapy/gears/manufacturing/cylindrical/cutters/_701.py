"""_701.py

CylindricalGearAbstractCutterDesign
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ABSTRACT_CUTTER_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearAbstractCutterDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearAbstractCutterDesign',)


class CylindricalGearAbstractCutterDesign(_1816.NamedDatabaseItem):
    """CylindricalGearAbstractCutterDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ABSTRACT_CUTTER_DESIGN

    class _Cast_CylindricalGearAbstractCutterDesign:
        """Special nested class for casting CylindricalGearAbstractCutterDesign to subclasses."""

        def __init__(self, parent: 'CylindricalGearAbstractCutterDesign'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def cylindrical_gear_form_grinding_wheel(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _702
            
            return self._parent._cast(_702.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703
            
            return self._parent._cast(_703.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _704
            
            return self._parent._cast(_704.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705
            
            return self._parent._cast(_705.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _707
            
            return self._parent._cast(_707.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _708
            
            return self._parent._cast(_708.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_shaper(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _709
            
            return self._parent._cast(_709.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _710
            
            return self._parent._cast(_710.CylindricalGearShaver)

        @property
        def involute_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713
            
            return self._parent._cast(_713.InvoluteCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(self) -> 'CylindricalGearAbstractCutterDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearAbstractCutterDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutter_type(self) -> 'str':
        """str: 'CutterType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterType

        if temp is None:
            return ''

        return temp

    @property
    def edge_radius(self) -> 'float':
        """float: 'EdgeRadius' is the original name of this property."""

        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    def edge_radius(self, value: 'float'):
        self.wrapped.EdgeRadius = float(value) if value else 0.0

    @property
    def nominal_normal_pressure_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NominalNormalPressureAngle' is the original name of this property."""

        temp = self.wrapped.NominalNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @nominal_normal_pressure_angle.setter
    def nominal_normal_pressure_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NominalNormalPressureAngle = value

    @property
    def normal_module(self) -> 'float':
        """float: 'NormalModule' is the original name of this property."""

        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_module.setter
    def normal_module(self, value: 'float'):
        self.wrapped.NormalModule = float(value) if value else 0.0

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property."""

        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    def normal_pressure_angle(self, value: 'float'):
        self.wrapped.NormalPressureAngle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign':
        return self._Cast_CylindricalGearAbstractCutterDesign(self)
