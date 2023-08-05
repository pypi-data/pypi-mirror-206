"""_702.py

CylindricalGearFormGrindingWheel
"""
from mastapy._internal import constructor
from mastapy.math_utility import _1523
from mastapy.gears.manufacturing.cylindrical.cutters import _708
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FORM_GRINDING_WHEEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearFormGrindingWheel')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFormGrindingWheel',)


class CylindricalGearFormGrindingWheel(_708.CylindricalGearRealCutterDesign):
    """CylindricalGearFormGrindingWheel

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FORM_GRINDING_WHEEL

    class _Cast_CylindricalGearFormGrindingWheel:
        """Special nested class for casting CylindricalGearFormGrindingWheel to subclasses."""

        def __init__(self, parent: 'CylindricalGearFormGrindingWheel'):
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
        def cylindrical_gear_form_grinding_wheel(self) -> 'CylindricalGearFormGrindingWheel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFormGrindingWheel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def right_hand_cutting_edge_shape(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'RightHandCuttingEdgeShape' is the original name of this property."""

        temp = self.wrapped.RightHandCuttingEdgeShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @right_hand_cutting_edge_shape.setter
    def right_hand_cutting_edge_shape(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.RightHandCuttingEdgeShape = value

    @property
    def cast_to(self) -> 'CylindricalGearFormGrindingWheel._Cast_CylindricalGearFormGrindingWheel':
        return self._Cast_CylindricalGearFormGrindingWheel(self)
