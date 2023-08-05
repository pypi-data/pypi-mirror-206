"""_6856.py

GearMeshLoadCase
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy.system_model.analyses_and_results.static_loads import _6858, _6875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshLoadCase',)


class GearMeshLoadCase(_6875.InterMountableComponentConnectionLoadCase):
    """GearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOAD_CASE

    class _Cast_GearMeshLoadCase:
        """Special nested class for casting GearMeshLoadCase to subclasses."""

        def __init__(self, parent: 'GearMeshLoadCase'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(self):
            return self._parent._cast(_6875.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6813
            
            return self._parent._cast(_6813.ConnectionLoadCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6779
            
            return self._parent._cast(_6779.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6788
            
            return self._parent._cast(_6788.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6793
            
            return self._parent._cast(_6793.BevelGearMeshLoadCase)

        @property
        def concept_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6806
            
            return self._parent._cast(_6806.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6810
            
            return self._parent._cast(_6810.ConicalGearMeshLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6827
            
            return self._parent._cast(_6827.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6849
            
            return self._parent._cast(_6849.FaceGearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6870
            
            return self._parent._cast(_6870.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6877
            
            return self._parent._cast(_6877.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6880
            
            return self._parent._cast(_6880.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6883
            
            return self._parent._cast(_6883.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6918
            
            return self._parent._cast(_6918.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6924
            
            return self._parent._cast(_6924.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6927
            
            return self._parent._cast(_6927.StraightBevelGearMeshLoadCase)

        @property
        def worm_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6947
            
            return self._parent._cast(_6947.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6950
            
            return self._parent._cast(_6950.ZerolBevelGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self) -> 'GearMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_power_for_gear_mesh_to_be_loaded(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumPowerForGearMeshToBeLoaded' is the original name of this property."""

        temp = self.wrapped.MinimumPowerForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum_power_for_gear_mesh_to_be_loaded.setter
    def minimum_power_for_gear_mesh_to_be_loaded(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumPowerForGearMeshToBeLoaded = value

    @property
    def minimum_torque_for_gear_mesh_to_be_loaded(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumTorqueForGearMeshToBeLoaded' is the original name of this property."""

        temp = self.wrapped.MinimumTorqueForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum_torque_for_gear_mesh_to_be_loaded.setter
    def minimum_torque_for_gear_mesh_to_be_loaded(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumTorqueForGearMeshToBeLoaded = value

    @property
    def number_of_steps_for_one_tooth_pass(self) -> 'int':
        """int: 'NumberOfStepsForOneToothPass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfStepsForOneToothPass

        if temp is None:
            return 0

        return temp

    @property
    def number_of_teeth_passed(self) -> 'float':
        """float: 'NumberOfTeethPassed' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethPassed

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth_passed.setter
    def number_of_teeth_passed(self, value: 'float'):
        self.wrapped.NumberOfTeethPassed = float(value) if value else 0.0

    @property
    def rayleigh_damping_beta(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RayleighDampingBeta' is the original name of this property."""

        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @rayleigh_damping_beta.setter
    def rayleigh_damping_beta(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RayleighDampingBeta = value

    @property
    def connection_design(self) -> '_2294.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def get_harmonic_load_data_for_import(self) -> '_6858.GearSetHarmonicLoadData':
        """ 'GetHarmonicLoadDataForImport' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.GearSetHarmonicLoadData
        """

        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'GearMeshLoadCase._Cast_GearMeshLoadCase':
        return self._Cast_GearMeshLoadCase(self)
