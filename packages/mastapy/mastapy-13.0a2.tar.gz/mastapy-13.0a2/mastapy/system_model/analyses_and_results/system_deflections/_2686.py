"""_2686.py

BevelGearSetSystemDeflection
"""
from mastapy.system_model.part_model.gears import _2499
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4027
from mastapy.system_model.analyses_and_results.system_deflections import _2669
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BevelGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetSystemDeflection',)


class BevelGearSetSystemDeflection(_2669.AGMAGleasonConicalGearSetSystemDeflection):
    """BevelGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_SYSTEM_DEFLECTION

    class _Cast_BevelGearSetSystemDeflection:
        """Special nested class for casting BevelGearSetSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelGearSetSystemDeflection'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_system_deflection(self):
            return self._parent._cast(_2669.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2704
            
            return self._parent._cast(_2704.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2739
            
            return self._parent._cast(_2739.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2785
            
            return self._parent._cast(_2785.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2664
            
            return self._parent._cast(_2664.AbstractAssemblySystemDeflection)

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
        def bevel_differential_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2681
            
            return self._parent._cast(_2681.BevelDifferentialGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2787
            
            return self._parent._cast(_2787.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2793
            
            return self._parent._cast(_2793.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2796
            
            return self._parent._cast(_2796.StraightBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2819
            
            return self._parent._cast(_2819.ZerolBevelGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(self) -> 'BevelGearSetSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2499.BevelGearSet':
        """BevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4027.BevelGearSetPowerFlow':
        """BevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearSetSystemDeflection._Cast_BevelGearSetSystemDeflection':
        return self._Cast_BevelGearSetSystemDeflection(self)
