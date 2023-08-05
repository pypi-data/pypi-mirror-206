"""_2703.py

ConicalGearMeshSystemDeflection
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.conical import _1144, _1149, _1154
from mastapy.system_model.connections_and_sockets.gears import _2288
from mastapy.system_model.analyses_and_results.system_deflections import _2705, _2738
from mastapy.gears.ltca.conical import _865
from mastapy.gears.rating.conical import _534
from mastapy.system_model.analyses_and_results.power_flows import _4041
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConicalGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshSystemDeflection',)


class ConicalGearMeshSystemDeflection(_2738.GearMeshSystemDeflection):
    """ConicalGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_SYSTEM_DEFLECTION

    class _Cast_ConicalGearMeshSystemDeflection:
        """Special nested class for casting ConicalGearMeshSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshSystemDeflection'):
            self._parent = parent

        @property
        def gear_mesh_system_deflection(self):
            return self._parent._cast(_2738.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2746
            
            return self._parent._cast(_2746.InterMountableComponentConnectionSystemDeflection)

        @property
        def connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2706
            
            return self._parent._cast(_2706.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7502
            
            return self._parent._cast(_7502.ConnectionFEAnalysis)

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
        def agma_gleason_conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2668
            
            return self._parent._cast(_2668.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2680
            
            return self._parent._cast(_2680.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2685
            
            return self._parent._cast(_2685.BevelGearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2742
            
            return self._parent._cast(_2742.HypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2747
            
            return self._parent._cast(_2747.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2750
            
            return self._parent._cast(_2750.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2753
            
            return self._parent._cast(_2753.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2786
            
            return self._parent._cast(_2786.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2792
            
            return self._parent._cast(_2792.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2795
            
            return self._parent._cast(_2795.StraightBevelGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2818
            
            return self._parent._cast(_2818.ZerolBevelGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(self) -> 'ConicalGearMeshSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'AngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_e(self) -> 'float':
        """float: 'DeltaE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DeltaE

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_sigma(self) -> 'float':
        """float: 'DeltaSigma' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DeltaSigma

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_xp(self) -> 'float':
        """float: 'DeltaXP' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DeltaXP

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_xw(self) -> 'float':
        """float: 'DeltaXW' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DeltaXW

        if temp is None:
            return 0.0

        return temp

    @property
    def include_mesh_node_misalignments_in_default_report(self) -> 'bool':
        """bool: 'IncludeMeshNodeMisalignmentsInDefaultReport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport

        if temp is None:
            return False

        return temp

    @property
    def linear_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'LinearMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def load_in_line_of_action_from_ltca(self) -> 'float':
        """float: 'LoadInLineOfActionFromLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadInLineOfActionFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_flank(self) -> '_1144.ActiveConicalFlank':
        """ActiveConicalFlank: 'LoadedFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1144.ActiveConicalFlank)
        return constructor.new_from_mastapy_type(_1144.ActiveConicalFlank)(value) if value is not None else None

    @property
    def pinion_angular_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'PinionAngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionAngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_torque_for_ltca(self) -> 'float':
        """float: 'PinionTorqueForLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionTorqueForLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_a_due_to_force_in_line_of_action_at_mesh_node(self) -> 'float':
        """float: 'TorqueOnGearADueToForceInLineOfActionAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueOnGearADueToForceInLineOfActionAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_a_due_to_moment_at_mesh_node(self) -> 'float':
        """float: 'TorqueOnGearADueToMomentAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueOnGearADueToMomentAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_b_due_to_force_in_line_of_action_at_mesh_node(self) -> 'float':
        """float: 'TorqueOnGearBDueToForceInLineOfActionAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueOnGearBDueToForceInLineOfActionAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_b_due_to_moment_at_mesh_node(self) -> 'float':
        """float: 'TorqueOnGearBDueToMomentAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueOnGearBDueToMomentAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angular_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'WheelAngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelAngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2288.ConicalGearMesh':
        """ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a(self) -> '_2705.ConicalGearSystemDeflection':
        """ConicalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_2705.ConicalGearSystemDeflection':
        """ConicalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ltca_results(self) -> '_865.ConicalMeshLoadDistributionAnalysis':
        """ConicalMeshLoadDistributionAnalysis: 'LTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_design(self) -> '_1149.ConicalGearMeshDesign':
        """ConicalGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_node_misalignments_pinion(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MeshNodeMisalignmentsPinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshNodeMisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_node_misalignments_total(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MeshNodeMisalignmentsTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshNodeMisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_node_misalignments_wheel(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MeshNodeMisalignmentsWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshNodeMisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_pinion(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsPinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_total(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_wheel(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_pinion(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodePinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodePinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_total(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_wheel(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_534.ConicalGearMeshRating':
        """ConicalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearMeshSystemDeflection]':
        """List[ConicalGearMeshSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4041.ConicalGearMeshPowerFlow':
        """ConicalGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection':
        return self._Cast_ConicalGearMeshSystemDeflection(self)
