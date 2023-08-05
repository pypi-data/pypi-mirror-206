"""_707.py

CylindricalGearRackDesign
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _329, _347
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _725
from mastapy.gears.manufacturing.cylindrical.cutters import _708
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_RACK_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearRackDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearRackDesign',)


class CylindricalGearRackDesign(_708.CylindricalGearRealCutterDesign):
    """CylindricalGearRackDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_RACK_DESIGN

    class _Cast_CylindricalGearRackDesign:
        """Special nested class for casting CylindricalGearRackDesign to subclasses."""

        def __init__(self, parent: 'CylindricalGearRackDesign'):
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
        def cylindrical_gear_grinding_worm(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703
            
            return self._parent._cast(_703.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _704
            
            return self._parent._cast(_704.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_rack_design(self) -> 'CylindricalGearRackDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearRackDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self) -> 'float':
        """float: 'Addendum' is the original name of this property."""

        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @addendum.setter
    def addendum(self, value: 'float'):
        self.wrapped.Addendum = float(value) if value else 0.0

    @property
    def addendum_factor(self) -> 'float':
        """float: 'AddendumFactor' is the original name of this property."""

        temp = self.wrapped.AddendumFactor

        if temp is None:
            return 0.0

        return temp

    @addendum_factor.setter
    def addendum_factor(self, value: 'float'):
        self.wrapped.AddendumFactor = float(value) if value else 0.0

    @property
    def addendum_keeping_dedendum_constant(self) -> 'float':
        """float: 'AddendumKeepingDedendumConstant' is the original name of this property."""

        temp = self.wrapped.AddendumKeepingDedendumConstant

        if temp is None:
            return 0.0

        return temp

    @addendum_keeping_dedendum_constant.setter
    def addendum_keeping_dedendum_constant(self, value: 'float'):
        self.wrapped.AddendumKeepingDedendumConstant = float(value) if value else 0.0

    @property
    def dedendum(self) -> 'float':
        """float: 'Dedendum' is the original name of this property."""

        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @dedendum.setter
    def dedendum(self, value: 'float'):
        self.wrapped.Dedendum = float(value) if value else 0.0

    @property
    def dedendum_factor(self) -> 'float':
        """float: 'DedendumFactor' is the original name of this property."""

        temp = self.wrapped.DedendumFactor

        if temp is None:
            return 0.0

        return temp

    @dedendum_factor.setter
    def dedendum_factor(self, value: 'float'):
        self.wrapped.DedendumFactor = float(value) if value else 0.0

    @property
    def edge_height(self) -> 'float':
        """float: 'EdgeHeight' is the original name of this property."""

        temp = self.wrapped.EdgeHeight

        if temp is None:
            return 0.0

        return temp

    @edge_height.setter
    def edge_height(self, value: 'float'):
        self.wrapped.EdgeHeight = float(value) if value else 0.0

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
    def effective_length(self) -> 'float':
        """float: 'EffectiveLength' is the original name of this property."""

        temp = self.wrapped.EffectiveLength

        if temp is None:
            return 0.0

        return temp

    @effective_length.setter
    def effective_length(self, value: 'float'):
        self.wrapped.EffectiveLength = float(value) if value else 0.0

    @property
    def flat_root_width(self) -> 'float':
        """float: 'FlatRootWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlatRootWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def flat_tip_width(self) -> 'float':
        """float: 'FlatTipWidth' is the original name of this property."""

        temp = self.wrapped.FlatTipWidth

        if temp is None:
            return 0.0

        return temp

    @flat_tip_width.setter
    def flat_tip_width(self, value: 'float'):
        self.wrapped.FlatTipWidth = float(value) if value else 0.0

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
    def normal_thickness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NormalThickness' is the original name of this property."""

        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @normal_thickness.setter
    def normal_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NormalThickness = value

    @property
    def number_of_threads(self) -> 'int':
        """int: 'NumberOfThreads' is the original name of this property."""

        temp = self.wrapped.NumberOfThreads

        if temp is None:
            return 0

        return temp

    @number_of_threads.setter
    def number_of_threads(self, value: 'int'):
        self.wrapped.NumberOfThreads = int(value) if value else 0

    @property
    def reference_diameter(self) -> 'float':
        """float: 'ReferenceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

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
    def use_maximum_edge_radius(self) -> 'bool':
        """bool: 'UseMaximumEdgeRadius' is the original name of this property."""

        temp = self.wrapped.UseMaximumEdgeRadius

        if temp is None:
            return False

        return temp

    @use_maximum_edge_radius.setter
    def use_maximum_edge_radius(self, value: 'bool'):
        self.wrapped.UseMaximumEdgeRadius = bool(value) if value else False

    @property
    def whole_depth(self) -> 'float':
        """float: 'WholeDepth' is the original name of this property."""

        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @whole_depth.setter
    def whole_depth(self, value: 'float'):
        self.wrapped.WholeDepth = float(value) if value else 0.0

    @property
    def worm_type(self) -> '_347.WormType':
        """WormType: 'WormType' is the original name of this property."""

        temp = self.wrapped.WormType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _347.WormType)
        return constructor.new_from_mastapy_type(_347.WormType)(value) if value is not None else None

    @worm_type.setter
    def worm_type(self, value: '_347.WormType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _347.WormType.type_())
        self.wrapped.WormType = value

    @property
    def nominal_rack_shape(self) -> '_725.RackShape':
        """RackShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def convert_to_standard_thickness(self):
        """ 'ConvertToStandardThickness' is the original name of this method."""

        self.wrapped.ConvertToStandardThickness()

    @property
    def cast_to(self) -> 'CylindricalGearRackDesign._Cast_CylindricalGearRackDesign':
        return self._Cast_CylindricalGearRackDesign(self)
