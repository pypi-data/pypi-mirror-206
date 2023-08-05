"""_1060.py

ReadonlyToothThicknessSpecification
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1079
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_READONLY_TOOTH_THICKNESS_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ReadonlyToothThicknessSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('ReadonlyToothThicknessSpecification',)


class ReadonlyToothThicknessSpecification(_1079.ToothThicknessSpecification):
    """ReadonlyToothThicknessSpecification

    This is a mastapy class.
    """

    TYPE = _READONLY_TOOTH_THICKNESS_SPECIFICATION

    class _Cast_ReadonlyToothThicknessSpecification:
        """Special nested class for casting ReadonlyToothThicknessSpecification to subclasses."""

        def __init__(self, parent: 'ReadonlyToothThicknessSpecification'):
            self._parent = parent

        @property
        def tooth_thickness_specification(self):
            return self._parent._cast(_1079.ToothThicknessSpecification)

        @property
        def tooth_thickness_specification_base(self):
            from mastapy.gears.gear_designs.cylindrical import _1080
            
            return self._parent._cast(_1080.ToothThicknessSpecificationBase)

        @property
        def readonly_tooth_thickness_specification(self) -> 'ReadonlyToothThicknessSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ReadonlyToothThicknessSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ball_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BallDiameter' is the original name of this property."""

        temp = self.wrapped.BallDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @ball_diameter.setter
    def ball_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BallDiameter = value

    @property
    def diameter_at_thickness_measurement(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DiameterAtThicknessMeasurement' is the original name of this property."""

        temp = self.wrapped.DiameterAtThicknessMeasurement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @diameter_at_thickness_measurement.setter
    def diameter_at_thickness_measurement(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DiameterAtThicknessMeasurement = value

    @property
    def number_of_teeth_for_chordal_span_test(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfTeethForChordalSpanTest' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethForChordalSpanTest

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_teeth_for_chordal_span_test.setter
    def number_of_teeth_for_chordal_span_test(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfTeethForChordalSpanTest = value

    @property
    def cast_to(self) -> 'ReadonlyToothThicknessSpecification._Cast_ReadonlyToothThicknessSpecification':
        return self._Cast_ReadonlyToothThicknessSpecification(self)
