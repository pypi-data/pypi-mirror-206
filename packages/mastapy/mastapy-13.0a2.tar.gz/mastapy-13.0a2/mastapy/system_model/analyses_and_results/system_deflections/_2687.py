"""_2687.py

BevelGearSystemDeflection
"""
from mastapy.system_model.part_model.gears import _2498
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4026
from mastapy.system_model.analyses_and_results.system_deflections import _2670
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BevelGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSystemDeflection',)


class BevelGearSystemDeflection(_2670.AGMAGleasonConicalGearSystemDeflection):
    """BevelGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SYSTEM_DEFLECTION

    class _Cast_BevelGearSystemDeflection:
        """Special nested class for casting BevelGearSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelGearSystemDeflection'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_system_deflection(self):
            return self._parent._cast(_2670.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2705
            
            return self._parent._cast(_2705.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2740
            
            return self._parent._cast(_2740.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2761
            
            return self._parent._cast(_2761.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2694
            
            return self._parent._cast(_2694.ComponentSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
            return self._parent._cast(_2764.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2682
            
            return self._parent._cast(_2682.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2683
            
            return self._parent._cast(_2683.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2684
            
            return self._parent._cast(_2684.BevelDifferentialSunGearSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2788
            
            return self._parent._cast(_2788.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2794
            
            return self._parent._cast(_2794.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2797
            
            return self._parent._cast(_2797.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2798
            
            return self._parent._cast(_2798.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2799
            
            return self._parent._cast(_2799.StraightBevelSunGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2820
            
            return self._parent._cast(_2820.ZerolBevelGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(self) -> 'BevelGearSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2498.BevelGear':
        """BevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4026.BevelGearPowerFlow':
        """BevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearSystemDeflection._Cast_BevelGearSystemDeflection':
        return self._Cast_BevelGearSystemDeflection(self)
