"""_1078.py

ToothFlankFractureAnalysisSettings
"""
from mastapy.math_utility import _1523
from mastapy._internal import constructor
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ToothFlankFractureAnalysisSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothFlankFractureAnalysisSettings',)


class ToothFlankFractureAnalysisSettings(_1575.IndependentReportablePropertiesBase['ToothFlankFractureAnalysisSettings']):
    """ToothFlankFractureAnalysisSettings

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS

    class _Cast_ToothFlankFractureAnalysisSettings:
        """Special nested class for casting ToothFlankFractureAnalysisSettings to subclasses."""

        def __init__(self, parent: 'ToothFlankFractureAnalysisSettings'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.gears.gear_designs.cylindrical import _1078
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def tooth_flank_fracture_analysis_settings(self) -> 'ToothFlankFractureAnalysisSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ToothFlankFractureAnalysisSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measured_residual_stress_profile_property(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'MeasuredResidualStressProfileProperty' is the original name of this property."""

        temp = self.wrapped.MeasuredResidualStressProfileProperty

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measured_residual_stress_profile_property.setter
    def measured_residual_stress_profile_property(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.MeasuredResidualStressProfileProperty = value

    @property
    def cast_to(self) -> 'ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings':
        return self._Cast_ToothFlankFractureAnalysisSettings(self)
