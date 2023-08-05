"""_6830.py

CylindricalPlanetGearLoadCase
"""
from mastapy.system_model.part_model.gears import _2506
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6825
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalPlanetGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearLoadCase',)


class CylindricalPlanetGearLoadCase(_6825.CylindricalGearLoadCase):
    """CylindricalPlanetGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_LOAD_CASE

    class _Cast_CylindricalPlanetGearLoadCase:
        """Special nested class for casting CylindricalPlanetGearLoadCase to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGearLoadCase'):
            self._parent = parent

        @property
        def cylindrical_gear_load_case(self):
            return self._parent._cast(_6825.CylindricalGearLoadCase)

        @property
        def gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6854
            
            return self._parent._cast(_6854.GearLoadCase)

        @property
        def mountable_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6888
            
            return self._parent._cast(_6888.MountableComponentLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

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
        def cylindrical_planet_gear_load_case(self) -> 'CylindricalPlanetGearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2506.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase':
        return self._Cast_CylindricalPlanetGearLoadCase(self)
