"""_1102.py

CylindricalGearSetMicroGeometryDutyCycle
"""
from typing import List

from mastapy.gears.rating.cylindrical import _459
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_two_d_fe_analysis import _892
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearSetMicroGeometryDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetMicroGeometryDutyCycle',)


class CylindricalGearSetMicroGeometryDutyCycle(_1224.GearSetImplementationAnalysisDutyCycle):
    """CylindricalGearSetMicroGeometryDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_DUTY_CYCLE

    class _Cast_CylindricalGearSetMicroGeometryDutyCycle:
        """Special nested class for casting CylindricalGearSetMicroGeometryDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetMicroGeometryDutyCycle'):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_duty_cycle(self):
            return self._parent._cast(_1224.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_analysis_abstract(self):
            from mastapy.gears.analysis import _1223
            
            return self._parent._cast(_1223.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(self) -> 'CylindricalGearSetMicroGeometryDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetMicroGeometryDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_459.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tiff_analysis(self) -> '_892.CylindricalGearSetTIFFAnalysisDutyCycle':
        """CylindricalGearSetTIFFAnalysisDutyCycle: 'TIFFAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshes(self) -> 'List[_1093.CylindricalGearMeshMicroGeometryDutyCycle]':
        """List[CylindricalGearMeshMicroGeometryDutyCycle]: 'Meshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetMicroGeometryDutyCycle._Cast_CylindricalGearSetMicroGeometryDutyCycle':
        return self._Cast_CylindricalGearSetMicroGeometryDutyCycle(self)
