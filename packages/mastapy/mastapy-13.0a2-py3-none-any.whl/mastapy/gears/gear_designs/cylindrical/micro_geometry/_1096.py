"""_1096.py

CylindricalGearMicroGeometryDutyCycle
"""
from mastapy.gears.gear_two_d_fe_analysis import _894
from mastapy._internal import constructor
from mastapy.gears.analysis import _1212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometryDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometryDutyCycle',)


class CylindricalGearMicroGeometryDutyCycle(_1212.GearDesignAnalysis):
    """CylindricalGearMicroGeometryDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_DUTY_CYCLE

    class _Cast_CylindricalGearMicroGeometryDutyCycle:
        """Special nested class for casting CylindricalGearMicroGeometryDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalGearMicroGeometryDutyCycle'):
            self._parent = parent

        @property
        def gear_design_analysis(self):
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(self) -> 'CylindricalGearMicroGeometryDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometryDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tiff_analysis(self) -> '_894.CylindricalGearTIFFAnalysisDutyCycle':
        """CylindricalGearTIFFAnalysisDutyCycle: 'TIFFAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearMicroGeometryDutyCycle._Cast_CylindricalGearMicroGeometryDutyCycle':
        return self._Cast_CylindricalGearMicroGeometryDutyCycle(self)
