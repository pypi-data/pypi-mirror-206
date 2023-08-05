"""_7296.py

GearMeshAdvancedSystemDeflection
"""
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy.math_utility import _1501
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'GearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshAdvancedSystemDeflection',)


class GearMeshAdvancedSystemDeflection(_7302.InterMountableComponentConnectionAdvancedSystemDeflection):
    """GearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_GearMeshAdvancedSystemDeflection:
        """Special nested class for casting GearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearMeshAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_system_deflection(self):
            return self._parent._cast(_7302.InterMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
            
            return self._parent._cast(_7270.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

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
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7240
            
            return self._parent._cast(_7240.AGMAGleasonConicalGearMeshAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7247
            
            return self._parent._cast(_7247.BevelDifferentialGearMeshAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7252
            
            return self._parent._cast(_7252.BevelGearMeshAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7265
            
            return self._parent._cast(_7265.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7268
            
            return self._parent._cast(_7268.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7284
            
            return self._parent._cast(_7284.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7291
            
            return self._parent._cast(_7291.FaceGearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7300
            
            return self._parent._cast(_7300.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7304
            
            return self._parent._cast(_7304.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7307
            
            return self._parent._cast(_7307.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310
            
            return self._parent._cast(_7310.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7338
            
            return self._parent._cast(_7338.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7344
            
            return self._parent._cast(_7344.StraightBevelDiffGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7347
            
            return self._parent._cast(_7347.StraightBevelGearMeshAdvancedSystemDeflection)

        @property
        def worm_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7363
            
            return self._parent._cast(_7363.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7366
            
            return self._parent._cast(_7366.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(self) -> 'GearMeshAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_misalignment(self) -> 'float':
        """float: 'MeanMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_moment_about_centre_from_ltca(self) -> 'float':
        """float: 'MeanMomentAboutCentreFromLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanMomentAboutCentreFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_left_flank(self) -> 'float':
        """float: 'MinimumSeparationLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_right_flank(self) -> 'float':
        """float: 'MinimumSeparationRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_teeth_passed(self) -> 'float':
        """float: 'NumberOfTeethPassed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTeethPassed

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_total_contact_ratio_for_first_tooth_passing_period(self) -> 'float':
        """float: 'OperatingTotalContactRatioForFirstToothPassingPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OperatingTotalContactRatioForFirstToothPassingPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_moment_about_centre_from_ltca(self) -> 'float':
        """float: 'PeakToPeakMomentAboutCentreFromLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakMomentAboutCentreFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_misalignment(self) -> 'float':
        """float: 'PeakToPeakMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_root_mean_square_misalignment(self) -> 'float':
        """float: 'SignedRootMeanSquareMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedRootMeanSquareMisalignment

        if temp is None:
            return 0.0

        return temp

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

    @property
    def misalignment_fourier_series_for_first_tooth_passing_period(self) -> '_1501.FourierSeries':
        """FourierSeries: 'MisalignmentFourierSeriesForFirstToothPassingPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentFourierSeriesForFirstToothPassingPeriod

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection':
        return self._Cast_GearMeshAdvancedSystemDeflection(self)
