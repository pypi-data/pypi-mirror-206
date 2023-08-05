"""_2683.py

BevelDifferentialPlanetGearSystemDeflection
"""
from mastapy.system_model.part_model.gears import _2496
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4023
from mastapy.system_model.analyses_and_results.system_deflections import _2682
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BevelDifferentialPlanetGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearSystemDeflection',)


class BevelDifferentialPlanetGearSystemDeflection(_2682.BevelDifferentialGearSystemDeflection):
    """BevelDifferentialPlanetGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_SYSTEM_DEFLECTION

    class _Cast_BevelDifferentialPlanetGearSystemDeflection:
        """Special nested class for casting BevelDifferentialPlanetGearSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGearSystemDeflection'):
            self._parent = parent

        @property
        def bevel_differential_gear_system_deflection(self):
            return self._parent._cast(_2682.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2687
            
            return self._parent._cast(_2687.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2670
            
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
        def bevel_differential_planet_gear_system_deflection(self) -> 'BevelDifferentialPlanetGearSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2496.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4023.BevelDifferentialPlanetGearPowerFlow':
        """BevelDifferentialPlanetGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialPlanetGearSystemDeflection._Cast_BevelDifferentialPlanetGearSystemDeflection':
        return self._Cast_BevelDifferentialPlanetGearSystemDeflection(self)
