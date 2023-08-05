"""_2721.py

CylindricalGearSetSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2505
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6829
from mastapy.gears.rating.cylindrical import _460
from mastapy.gears.manufacturing.cylindrical import _616
from mastapy.system_model.analyses_and_results.power_flows import _4059
from mastapy.system_model.analyses_and_results.system_deflections import _2724, _2718, _2739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetSystemDeflection',)


class CylindricalGearSetSystemDeflection(_2739.GearSetSystemDeflection):
    """CylindricalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION

    class _Cast_CylindricalGearSetSystemDeflection:
        """Special nested class for casting CylindricalGearSetSystemDeflection to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetSystemDeflection'):
            self._parent = parent

        @property
        def gear_set_system_deflection(self):
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
        def cylindrical_gear_set_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2722
            
            return self._parent._cast(_2722.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2723
            
            return self._parent._cast(_2723.CylindricalGearSetSystemDeflectionWithLTCAResults)

        @property
        def cylindrical_gear_set_system_deflection(self) -> 'CylindricalGearSetSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2505.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6829.CylindricalGearSetLoadCase':
        """CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_460.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_460.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_analysis(self) -> '_616.CylindricalManufacturedGearSetLoadCase':
        """CylindricalManufacturedGearSetLoadCase: 'ManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4059.CylindricalGearSetPowerFlow':
        """CylindricalGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gears_system_deflection(self) -> 'List[_2724.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'CylindricalGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_system_deflection(self) -> 'List[_2718.CylindricalGearMeshSystemDeflection]':
        """List[CylindricalGearMeshSystemDeflection]: 'CylindricalMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetSystemDeflection._Cast_CylindricalGearSetSystemDeflection':
        return self._Cast_CylindricalGearSetSystemDeflection(self)
