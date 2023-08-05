"""_894.py

CylindricalGearTIFFAnalysisDutyCycle
"""
from mastapy.gears.gear_two_d_fe_analysis import _895
from mastapy._internal import constructor
from mastapy.gears.analysis import _1212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TIFF_ANALYSIS_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'CylindricalGearTIFFAnalysisDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearTIFFAnalysisDutyCycle',)


class CylindricalGearTIFFAnalysisDutyCycle(_1212.GearDesignAnalysis):
    """CylindricalGearTIFFAnalysisDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TIFF_ANALYSIS_DUTY_CYCLE

    class _Cast_CylindricalGearTIFFAnalysisDutyCycle:
        """Special nested class for casting CylindricalGearTIFFAnalysisDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalGearTIFFAnalysisDutyCycle'):
            self._parent = parent

        @property
        def gear_design_analysis(self):
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(self) -> 'CylindricalGearTIFFAnalysisDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearTIFFAnalysisDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis(self) -> '_895.CylindricalGearTwoDimensionalFEAnalysis':
        """CylindricalGearTwoDimensionalFEAnalysis: 'Analysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Analysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearTIFFAnalysisDutyCycle._Cast_CylindricalGearTIFFAnalysisDutyCycle':
        return self._Cast_CylindricalGearTIFFAnalysisDutyCycle(self)
