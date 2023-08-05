"""_2819.py

ZerolBevelGearSetSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2533
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6951
from mastapy.gears.rating.zerol_bevel import _367
from mastapy.system_model.analyses_and_results.power_flows import _4141
from mastapy.system_model.analyses_and_results.system_deflections import _2820, _2818, _2686
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ZerolBevelGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetSystemDeflection',)


class ZerolBevelGearSetSystemDeflection(_2686.BevelGearSetSystemDeflection):
    """ZerolBevelGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_SYSTEM_DEFLECTION

    class _Cast_ZerolBevelGearSetSystemDeflection:
        """Special nested class for casting ZerolBevelGearSetSystemDeflection to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSetSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_set_system_deflection(self):
            return self._parent._cast(_2686.BevelGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2669
            
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
        def zerol_bevel_gear_set_system_deflection(self) -> 'ZerolBevelGearSetSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2533.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6951.ZerolBevelGearSetLoadCase':
        """ZerolBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_367.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_367.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4141.ZerolBevelGearSetPowerFlow':
        """ZerolBevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gears_system_deflection(self) -> 'List[_2820.ZerolBevelGearSystemDeflection]':
        """List[ZerolBevelGearSystemDeflection]: 'ZerolBevelGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_system_deflection(self) -> 'List[_2818.ZerolBevelGearMeshSystemDeflection]':
        """List[ZerolBevelGearMeshSystemDeflection]: 'ZerolBevelMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSetSystemDeflection._Cast_ZerolBevelGearSetSystemDeflection':
        return self._Cast_ZerolBevelGearSetSystemDeflection(self)
