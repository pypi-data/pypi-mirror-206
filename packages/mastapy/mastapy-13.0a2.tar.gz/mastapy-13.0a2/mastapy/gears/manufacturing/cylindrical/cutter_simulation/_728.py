"""_728.py

CylindricalGearSpecification
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1080
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'CylindricalGearSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSpecification',)


class CylindricalGearSpecification(_0.APIBase):
    """CylindricalGearSpecification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SPECIFICATION

    class _Cast_CylindricalGearSpecification:
        """Special nested class for casting CylindricalGearSpecification to subclasses."""

        def __init__(self, parent: 'CylindricalGearSpecification'):
            self._parent = parent

        @property
        def cylindrical_gear_specification(self) -> 'CylindricalGearSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

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
    def number_of_teeth_unsigned(self) -> 'float':
        """float: 'NumberOfTeethUnsigned' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTeethUnsigned

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_specification(self) -> '_1080.ToothThicknessSpecificationBase':
        """ToothThicknessSpecificationBase: 'ToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThicknessSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearSpecification._Cast_CylindricalGearSpecification':
        return self._Cast_CylindricalGearSpecification(self)
