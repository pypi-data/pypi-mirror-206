"""_773.py

ConicalGearMicroGeometryConfigBase
"""
from mastapy.gears.manufacturing.bevel import _791
from mastapy._internal import constructor
from mastapy.gears.analysis import _1215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalGearMicroGeometryConfigBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMicroGeometryConfigBase',)


class ConicalGearMicroGeometryConfigBase(_1215.GearImplementationDetail):
    """ConicalGearMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE

    class _Cast_ConicalGearMicroGeometryConfigBase:
        """Special nested class for casting ConicalGearMicroGeometryConfigBase to subclasses."""

        def __init__(self, parent: 'ConicalGearMicroGeometryConfigBase'):
            self._parent = parent

        @property
        def gear_implementation_detail(self):
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def conical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _771
            
            return self._parent._cast(_771.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _772
            
            return self._parent._cast(_772.ConicalGearMicroGeometryConfig)

        @property
        def conical_pinion_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _783
            
            return self._parent._cast(_783.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _784
            
            return self._parent._cast(_784.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _789
            
            return self._parent._cast(_789.ConicalWheelManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(self) -> 'ConicalGearMicroGeometryConfigBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMicroGeometryConfigBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_measurement_border(self) -> '_791.FlankMeasurementBorder':
        """FlankMeasurementBorder: 'FlankMeasurementBorder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase':
        return self._Cast_ConicalGearMicroGeometryConfigBase(self)
