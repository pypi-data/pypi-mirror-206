"""_1575.py

IndependentReportablePropertiesBase
"""
from typing import TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import('SMT.MastaAPI.Utility', 'IndependentReportablePropertiesBase')


__docformat__ = 'restructuredtext en'
__all__ = ('IndependentReportablePropertiesBase',)


T = TypeVar('T', bound='IndependentReportablePropertiesBase')


class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE

    class _Cast_IndependentReportablePropertiesBase:
        """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

        def __init__(self, parent: 'IndependentReportablePropertiesBase'):
            self._parent = parent

        @property
        def oil_pump_detail(self):
            from mastapy.materials.efficiency import _294
            
            return self._parent._cast(_294.OilPumpDetail)

        @property
        def packaging_limits(self):
            from mastapy.geometry import _305
            
            return self._parent._cast(_305.PackagingLimits)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(self):
            from mastapy.gears import _342
            
            return self._parent._cast(_342.SpecificationForTheEffectOfOilKinematicViscosity)

        @property
        def cylindrical_gear_micro_geometry_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1015
            
            return self._parent._cast(_1015.CylindricalGearMicroGeometrySettings)

        @property
        def hardened_material_properties(self):
            from mastapy.gears.gear_designs.cylindrical import _1045
            
            return self._parent._cast(_1045.HardenedMaterialProperties)

        @property
        def ltca_load_case_modifiable_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1053
            
            return self._parent._cast(_1053.LTCALoadCaseModifiableSettings)

        @property
        def ltca_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1054
            
            return self._parent._cast(_1054.LtcaSettings)

        @property
        def micropitting(self):
            from mastapy.gears.gear_designs.cylindrical import _1057
            
            return self._parent._cast(_1057.Micropitting)

        @property
        def scuffing(self):
            from mastapy.gears.gear_designs.cylindrical import _1064
            
            return self._parent._cast(_1064.Scuffing)

        @property
        def surface_roughness(self):
            from mastapy.gears.gear_designs.cylindrical import _1072
            
            return self._parent._cast(_1072.SurfaceRoughness)

        @property
        def tiff_analysis_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1074
            
            return self._parent._cast(_1074.TiffAnalysisSettings)

        @property
        def tooth_flank_fracture_analysis_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1078
            
            return self._parent._cast(_1078.ToothFlankFractureAnalysisSettings)

        @property
        def usage(self):
            from mastapy.gears.gear_designs.cylindrical import _1082
            
            return self._parent._cast(_1082.Usage)

        @property
        def eccentricity(self):
            from mastapy.electric_machines import _1253
            
            return self._parent._cast(_1253.Eccentricity)

        @property
        def temperatures(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1365
            
            return self._parent._cast(_1365.Temperatures)

        @property
        def lookup_table_base(self):
            from mastapy.math_utility.measured_data import _1555
            
            return self._parent._cast(_1555.LookupTableBase)

        @property
        def onedimensional_function_lookup_table(self):
            from mastapy.math_utility.measured_data import _1556
            
            return self._parent._cast(_1556.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(self):
            from mastapy.math_utility.measured_data import _1557
            
            return self._parent._cast(_1557.TwodimensionalFunctionLookupTable)

        @property
        def roundness_specification(self):
            from mastapy.bearings.tolerances import _1903
            
            return self._parent._cast(_1903.RoundnessSpecification)

        @property
        def equivalent_load_factors(self):
            from mastapy.bearings.bearing_results import _1930
            
            return self._parent._cast(_1930.EquivalentLoadFactors)

        @property
        def iso14179_settings_per_bearing_type(self):
            from mastapy.bearings.bearing_results.rolling import _1961
            
            return self._parent._cast(_1961.ISO14179SettingsPerBearingType)

        @property
        def rolling_bearing_friction_coefficients(self):
            from mastapy.bearings.bearing_results.rolling import _2055
            
            return self._parent._cast(_2055.RollingBearingFrictionCoefficients)

        @property
        def additional_acceleration_options(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6775
            
            return self._parent._cast(_6775.AdditionalAccelerationOptions)

        @property
        def independent_reportable_properties_base(self) -> 'IndependentReportablePropertiesBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'IndependentReportablePropertiesBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase':
        return self._Cast_IndependentReportablePropertiesBase(self)
