"""_7295.py

GearAdvancedSystemDeflection
"""
from mastapy.system_model.part_model.gears import _2509
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'GearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearAdvancedSystemDeflection',)


class GearAdvancedSystemDeflection(_7315.MountableComponentAdvancedSystemDeflection):
    """GearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_GearAdvancedSystemDeflection:
        """Special nested class for casting GearAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(self):
            return self._parent._cast(_7315.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7260
            
            return self._parent._cast(_7260.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.PartAdvancedSystemDeflection)

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
        def agma_gleason_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7239
            
            return self._parent._cast(_7239.AGMAGleasonConicalGearAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7246
            
            return self._parent._cast(_7246.BevelDifferentialGearAdvancedSystemDeflection)

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7249
            
            return self._parent._cast(_7249.BevelDifferentialPlanetGearAdvancedSystemDeflection)

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7250
            
            return self._parent._cast(_7250.BevelDifferentialSunGearAdvancedSystemDeflection)

        @property
        def bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7251
            
            return self._parent._cast(_7251.BevelGearAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7264
            
            return self._parent._cast(_7264.ConceptGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7267
            
            return self._parent._cast(_7267.ConicalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7283
            
            return self._parent._cast(_7283.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7287
            
            return self._parent._cast(_7287.CylindricalPlanetGearAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7290
            
            return self._parent._cast(_7290.FaceGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7299
            
            return self._parent._cast(_7299.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7303
            
            return self._parent._cast(_7303.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7306
            
            return self._parent._cast(_7306.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309
            
            return self._parent._cast(_7309.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7337
            
            return self._parent._cast(_7337.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7343
            
            return self._parent._cast(_7343.StraightBevelDiffGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7346
            
            return self._parent._cast(_7346.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7349
            
            return self._parent._cast(_7349.StraightBevelPlanetGearAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7350
            
            return self._parent._cast(_7350.StraightBevelSunGearAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7362
            
            return self._parent._cast(_7362.WormGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7365
            
            return self._parent._cast(_7365.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(self) -> 'GearAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2509.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearAdvancedSystemDeflection._Cast_GearAdvancedSystemDeflection':
        return self._Cast_GearAdvancedSystemDeflection(self)
