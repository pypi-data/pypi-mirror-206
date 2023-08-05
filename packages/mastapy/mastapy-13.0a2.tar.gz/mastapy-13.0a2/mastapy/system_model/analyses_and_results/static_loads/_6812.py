"""_6812.py

ConicalGearSetLoadCase
"""
from mastapy.system_model.part_model.gears import _2503
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6811, _6859
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetLoadCase',)


class ConicalGearSetLoadCase(_6859.GearSetLoadCase):
    """ConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_CASE

    class _Cast_ConicalGearSetLoadCase:
        """Special nested class for casting ConicalGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'ConicalGearSetLoadCase'):
            self._parent = parent

        @property
        def gear_set_load_case(self):
            return self._parent._cast(_6859.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
            return self._parent._cast(_6916.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.AbstractAssemblyLoadCase)

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
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6780
            
            return self._parent._cast(_6780.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6789
            
            return self._parent._cast(_6789.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6794
            
            return self._parent._cast(_6794.BevelGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6871
            
            return self._parent._cast(_6871.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6878
            
            return self._parent._cast(_6878.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6881
            
            return self._parent._cast(_6881.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6884
            
            return self._parent._cast(_6884.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6919
            
            return self._parent._cast(_6919.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6925
            
            return self._parent._cast(_6925.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6928
            
            return self._parent._cast(_6928.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6951
            
            return self._parent._cast(_6951.ZerolBevelGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self) -> 'ConicalGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2503.ConicalGearSet':
        """ConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def get_harmonic_load_data_for_import(self) -> '_6811.ConicalGearSetHarmonicLoadData':
        """ 'GetHarmonicLoadDataForImport' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetHarmonicLoadData
        """

        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase':
        return self._Cast_ConicalGearSetLoadCase(self)
