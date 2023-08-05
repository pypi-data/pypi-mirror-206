"""_1077.py

TolerancedValueSpecification
"""
from typing import TypeVar

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1061
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOLERANCED_VALUE_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'TolerancedValueSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('TolerancedValueSpecification',)


T = TypeVar('T')


class TolerancedValueSpecification(_1061.RelativeMeasurementViewModel[T]):
    """TolerancedValueSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _TOLERANCED_VALUE_SPECIFICATION

    class _Cast_TolerancedValueSpecification:
        """Special nested class for casting TolerancedValueSpecification to subclasses."""

        def __init__(self, parent: 'TolerancedValueSpecification'):
            self._parent = parent

        @property
        def relative_measurement_view_model(self):
            return self._parent._cast(_1061.RelativeMeasurementViewModel)

        @property
        def cylindrical_mesh_angular_backlash(self):
            from mastapy.gears.gear_designs.cylindrical import _1031
            
            return self._parent._cast(_1031.CylindricalMeshAngularBacklash)

        @property
        def cylindrical_mesh_linear_backlash_specification(self):
            from mastapy.gears.gear_designs.cylindrical import _1034
            
            return self._parent._cast(_1034.CylindricalMeshLinearBacklashSpecification)

        @property
        def nominal_value_specification(self):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1085
            
            return self._parent._cast(_1085.NominalValueSpecification)

        @property
        def no_value_specification(self):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1086
            
            return self._parent._cast(_1086.NoValueSpecification)

        @property
        def toleranced_value_specification(self) -> 'TolerancedValueSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TolerancedValueSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_mean(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AverageMean' is the original name of this property."""

        temp = self.wrapped.AverageMean

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @average_mean.setter
    def average_mean(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AverageMean = value

    @property
    def maximum(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Maximum' is the original name of this property."""

        temp = self.wrapped.Maximum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum.setter
    def maximum(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Maximum = value

    @property
    def minimum(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Minimum' is the original name of this property."""

        temp = self.wrapped.Minimum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum.setter
    def minimum(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Minimum = value

    @property
    def spread(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Spread' is the original name of this property."""

        temp = self.wrapped.Spread

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @spread.setter
    def spread(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Spread = value

    @property
    def cast_to(self) -> 'TolerancedValueSpecification._Cast_TolerancedValueSpecification':
        return self._Cast_TolerancedValueSpecification(self)
