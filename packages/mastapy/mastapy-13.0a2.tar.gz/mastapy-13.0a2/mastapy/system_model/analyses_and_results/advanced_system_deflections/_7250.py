"""_7250.py

BevelDifferentialSunGearAdvancedSystemDeflection
"""
from mastapy.system_model.part_model.gears import _2497
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7246
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BevelDifferentialSunGearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearAdvancedSystemDeflection',)


class BevelDifferentialSunGearAdvancedSystemDeflection(_7246.BevelDifferentialGearAdvancedSystemDeflection):
    """BevelDifferentialSunGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_BevelDifferentialSunGearAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialSunGearAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelDifferentialSunGearAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def bevel_differential_gear_advanced_system_deflection(self):
            return self._parent._cast(_7246.BevelDifferentialGearAdvancedSystemDeflection)

        @property
        def bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7251
            
            return self._parent._cast(_7251.BevelGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7239
            
            return self._parent._cast(_7239.AGMAGleasonConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7267
            
            return self._parent._cast(_7267.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7295
            
            return self._parent._cast(_7295.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
            
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
        def bevel_differential_sun_gear_advanced_system_deflection(self) -> 'BevelDifferentialSunGearAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2497.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialSunGearAdvancedSystemDeflection._Cast_BevelDifferentialSunGearAdvancedSystemDeflection':
        return self._Cast_BevelDifferentialSunGearAdvancedSystemDeflection(self)
