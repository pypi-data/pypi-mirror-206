"""_718.py

CutterShapeDefinition
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _708
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _724
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUTTER_SHAPE_DEFINITION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CutterShapeDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('CutterShapeDefinition',)


class CutterShapeDefinition(_0.APIBase):
    """CutterShapeDefinition

    This is a mastapy class.
    """

    TYPE = _CUTTER_SHAPE_DEFINITION

    class _Cast_CutterShapeDefinition:
        """Special nested class for casting CutterShapeDefinition to subclasses."""

        def __init__(self, parent: 'CutterShapeDefinition'):
            self._parent = parent

        @property
        def cylindrical_gear_formed_wheel_grinder_tangible(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _719
            
            return self._parent._cast(_719.CylindricalGearFormedWheelGrinderTangible)

        @property
        def cylindrical_gear_hob_shape(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _720
            
            return self._parent._cast(_720.CylindricalGearHobShape)

        @property
        def cylindrical_gear_shaper_tangible(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _721
            
            return self._parent._cast(_721.CylindricalGearShaperTangible)

        @property
        def cylindrical_gear_shaver_tangible(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _722
            
            return self._parent._cast(_722.CylindricalGearShaverTangible)

        @property
        def cylindrical_gear_worm_grinder_shape(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _723
            
            return self._parent._cast(_723.CylindricalGearWormGrinderShape)

        @property
        def rack_shape(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _725
            
            return self._parent._cast(_725.RackShape)

        @property
        def cutter_shape_definition(self) -> 'CutterShapeDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CutterShapeDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def normal_module(self) -> 'float':
        """float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pitch(self) -> 'float':
        """float: 'NormalPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def design(self) -> '_708.CylindricalGearRealCutterDesign':
        """CylindricalGearRealCutterDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fillet_points(self) -> 'List[_724.NamedPoint]':
        """List[NamedPoint]: 'FilletPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilletPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def main_blade_points(self) -> 'List[_724.NamedPoint]':
        """List[NamedPoint]: 'MainBladePoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MainBladePoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CutterShapeDefinition._Cast_CutterShapeDefinition':
        return self._Cast_CutterShapeDefinition(self)
