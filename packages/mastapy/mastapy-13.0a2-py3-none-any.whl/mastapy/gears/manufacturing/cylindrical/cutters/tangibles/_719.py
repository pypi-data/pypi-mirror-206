"""_719.py

CylindricalGearFormedWheelGrinderTangible
"""
from mastapy.gears.manufacturing.cylindrical.cutters import _702
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _718
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FORMED_WHEEL_GRINDER_TANGIBLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CylindricalGearFormedWheelGrinderTangible')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFormedWheelGrinderTangible',)


class CylindricalGearFormedWheelGrinderTangible(_718.CutterShapeDefinition):
    """CylindricalGearFormedWheelGrinderTangible

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FORMED_WHEEL_GRINDER_TANGIBLE

    class _Cast_CylindricalGearFormedWheelGrinderTangible:
        """Special nested class for casting CylindricalGearFormedWheelGrinderTangible to subclasses."""

        def __init__(self, parent: 'CylindricalGearFormedWheelGrinderTangible'):
            self._parent = parent

        @property
        def cutter_shape_definition(self):
            return self._parent._cast(_718.CutterShapeDefinition)

        @property
        def cylindrical_gear_formed_wheel_grinder_tangible(self) -> 'CylindricalGearFormedWheelGrinderTangible':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFormedWheelGrinderTangible.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self) -> '_702.CylindricalGearFormGrindingWheel':
        """CylindricalGearFormGrindingWheel: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearFormedWheelGrinderTangible._Cast_CylindricalGearFormedWheelGrinderTangible':
        return self._Cast_CylindricalGearFormedWheelGrinderTangible(self)
