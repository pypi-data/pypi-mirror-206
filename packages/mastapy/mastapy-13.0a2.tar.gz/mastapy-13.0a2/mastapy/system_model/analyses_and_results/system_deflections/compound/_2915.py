"""_2915.py

PlanetaryGearSetCompoundSystemDeflection
"""
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2879
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'PlanetaryGearSetCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCompoundSystemDeflection',)


class PlanetaryGearSetCompoundSystemDeflection(_2879.CylindricalGearSetCompoundSystemDeflection):
    """PlanetaryGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_PlanetaryGearSetCompoundSystemDeflection:
        """Special nested class for casting PlanetaryGearSetCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetCompoundSystemDeflection'):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_system_deflection(self):
            return self._parent._cast(_2879.CylindricalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2891
            
            return self._parent._cast(_2891.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2930
            
            return self._parent._cast(_2930.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2830
            
            return self._parent._cast(_2830.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2910
            
            return self._parent._cast(_2910.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_system_deflection(self) -> 'PlanetaryGearSetCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection':
        return self._Cast_PlanetaryGearSetCompoundSystemDeflection(self)
