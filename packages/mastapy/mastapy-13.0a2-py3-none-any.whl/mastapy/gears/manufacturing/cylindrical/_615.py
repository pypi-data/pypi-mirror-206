"""_615.py

CylindricalManufacturedGearSetDutyCycle
"""
from mastapy.gears.manufacturing.cylindrical import _620
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical import _459
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_SET_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearSetDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearSetDutyCycle',)


class CylindricalManufacturedGearSetDutyCycle(_1224.GearSetImplementationAnalysisDutyCycle):
    """CylindricalManufacturedGearSetDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_SET_DUTY_CYCLE

    class _Cast_CylindricalManufacturedGearSetDutyCycle:
        """Special nested class for casting CylindricalManufacturedGearSetDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalManufacturedGearSetDutyCycle'):
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
        def cylindrical_manufactured_gear_set_duty_cycle(self) -> 'CylindricalManufacturedGearSetDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearSetDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manufacturing_configuration(self) -> '_620.CylindricalSetManufacturingConfig':
        """CylindricalSetManufacturingConfig: 'ManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def cast_to(self) -> 'CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle':
        return self._Cast_CylindricalManufacturedGearSetDutyCycle(self)
