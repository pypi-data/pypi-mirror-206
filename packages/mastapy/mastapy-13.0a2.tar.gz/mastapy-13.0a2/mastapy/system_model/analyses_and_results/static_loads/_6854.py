"""_6854.py

GearLoadCase
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2509
from mastapy.system_model.analyses_and_results.static_loads import _6855, _6888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('GearLoadCase',)


class GearLoadCase(_6888.MountableComponentLoadCase):
    """GearLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_CASE

    class _Cast_GearLoadCase:
        """Special nested class for casting GearLoadCase to subclasses."""

        def __init__(self, parent: 'GearLoadCase'):
            self._parent = parent

        @property
        def mountable_component_load_case(self):
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
        def agma_gleason_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6778
            
            return self._parent._cast(_6778.AGMAGleasonConicalGearLoadCase)

        @property
        def bevel_differential_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6787
            
            return self._parent._cast(_6787.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6790
            
            return self._parent._cast(_6790.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6791
            
            return self._parent._cast(_6791.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6792
            
            return self._parent._cast(_6792.BevelGearLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6805
            
            return self._parent._cast(_6805.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6808
            
            return self._parent._cast(_6808.ConicalGearLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6825
            
            return self._parent._cast(_6825.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6830
            
            return self._parent._cast(_6830.CylindricalPlanetGearLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6848
            
            return self._parent._cast(_6848.FaceGearLoadCase)

        @property
        def hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6869
            
            return self._parent._cast(_6869.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6876
            
            return self._parent._cast(_6876.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6879
            
            return self._parent._cast(_6879.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6882
            
            return self._parent._cast(_6882.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6917
            
            return self._parent._cast(_6917.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6923
            
            return self._parent._cast(_6923.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6926
            
            return self._parent._cast(_6926.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6929
            
            return self._parent._cast(_6929.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6930
            
            return self._parent._cast(_6930.StraightBevelSunGearLoadCase)

        @property
        def worm_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6946
            
            return self._parent._cast(_6946.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6949
            
            return self._parent._cast(_6949.ZerolBevelGearLoadCase)

        @property
        def gear_load_case(self) -> 'GearLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'GearTemperature' is the original name of this property."""

        temp = self.wrapped.GearTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @gear_temperature.setter
    def gear_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.GearTemperature = value

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
    def gear_manufacture_errors(self) -> '_6855.GearManufactureError':
        """GearManufactureError: 'GearManufactureErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearManufactureErrors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearLoadCase._Cast_GearLoadCase':
        return self._Cast_GearLoadCase(self)
