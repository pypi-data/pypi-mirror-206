"""_2677.py

BearingSystemDeflection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy._math.vector_3d import Vector3D
from mastapy.utility_gui.charts import _1852
from mastapy.system_model.part_model import _2419, _2421
from mastapy.bearings.bearing_results import _1934, _1926
from mastapy.system_model.analyses_and_results.static_loads import _6784
from mastapy.system_model.analyses_and_results.power_flows import _4017
from mastapy.math_utility.measured_vectors import _1550
from mastapy.system_model.analyses_and_results.system_deflections import _2707
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSystemDeflection',)


class BearingSystemDeflection(_2707.ConnectorSystemDeflection):
    """BearingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEARING_SYSTEM_DEFLECTION

    class _Cast_BearingSystemDeflection:
        """Special nested class for casting BearingSystemDeflection to subclasses."""

        def __init__(self, parent: 'BearingSystemDeflection'):
            self._parent = parent

        @property
        def connector_system_deflection(self):
            return self._parent._cast(_2707.ConnectorSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2761
            
            return self._parent._cast(_2761.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2694
            
            return self._parent._cast(_2694.ComponentSystemDeflection)

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
        def bearing_system_deflection(self) -> 'BearingSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self) -> 'float':
        """float: 'AxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def component_angular_displacements(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'ComponentAngularDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAngularDisplacements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_axial_displacements(self) -> 'List[float]':
        """List[float]: 'ComponentAxialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAxialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def component_radial_displacements(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'ComponentRadialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentRadialDisplacements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def element_axial_displacements(self) -> 'List[float]':
        """List[float]: 'ElementAxialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementAxialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def element_radial_displacements(self) -> 'List[float]':
        """List[float]: 'ElementRadialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRadialDisplacements

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def element_tilts(self) -> 'List[float]':
        """List[float]: 'ElementTilts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementTilts

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elements_in_contact(self) -> 'int':
        """int: 'ElementsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementsInContact

        if temp is None:
            return 0

        return temp

    @property
    def inner_left_mounting_axial_stiffness(self) -> 'float':
        """float: 'InnerLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_left_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'InnerLeftMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def inner_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_left_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerLeftMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_radial_mounting_linear_displacement(self) -> 'Vector2D':
        """Vector2D: 'InnerRadialMountingLinearDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_radial_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerRadialMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_right_mounting_axial_stiffness(self) -> 'float':
        """float: 'InnerRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_right_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'InnerRightMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def inner_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_right_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerRightMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def internal_force(self) -> 'Vector3D':
        """Vector3D: 'InternalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalForce

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def internal_moment(self) -> 'Vector3D':
        """Vector3D: 'InternalMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def is_loaded(self) -> 'bool':
        """bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def maximum_radial_stiffness(self) -> 'float':
        """float: 'MaximumRadialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRadialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tilt_stiffness(self) -> 'float':
        """float: 'MaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_axial_stiffness(self) -> 'float':
        """float: 'OuterLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'OuterLeftMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def outer_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_left_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterLeftMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_radial_mounting_linear_displacement(self) -> 'Vector2D':
        """Vector2D: 'OuterRadialMountingLinearDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_radial_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterRadialMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_right_mounting_axial_stiffness(self) -> 'float':
        """float: 'OuterRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingAxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_right_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'OuterRightMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def outer_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingMaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_right_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterRightMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def percentage_preload_spring_compression(self) -> 'float':
        """float: 'PercentagePreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentagePreloadSpringCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def preload_spring_compression(self) -> 'float':
        """float: 'PreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreloadSpringCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def spring_preload_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'SpringPreloadChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringPreloadChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2419.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1934.LoadedBearingResults':
        """LoadedBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6784.BearingLoadCase':
        """BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_left_mounting_stiffness(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_radial_mounting_stiffness(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_right_mounting_stiffness(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_left_mounting_stiffness(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_radial_mounting_stiffness(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_right_mounting_stiffness(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4017.BearingPowerFlow':
        """BearingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def preload_spring_stiffness(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'PreloadSpringStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreloadSpringStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_between_rings(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessBetweenRings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessBetweenRings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_matrix(self) -> '_1926.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessMatrix' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrix

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def forces_at_zero_displacement_for_inner_and_outer_nodes(self) -> 'List[_1550.ForceResults]':
        """List[ForceResults]: 'ForcesAtZeroDisplacementForInnerAndOuterNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForcesAtZeroDisplacementForInnerAndOuterNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def race_mounting_options_for_analysis(self) -> 'List[_2421.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'RaceMountingOptionsForAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceMountingOptionsForAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def stiffness_between_each_ring(self) -> 'List[_1926.BearingStiffnessMatrixReporter]':
        """List[BearingStiffnessMatrixReporter]: 'StiffnessBetweenEachRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessBetweenEachRing

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def continue_dynamic_analysis(self):
        """ 'ContinueDynamicAnalysis' is the original name of this method."""

        self.wrapped.ContinueDynamicAnalysis()

    def dynamic_analysis(self):
        """ 'DynamicAnalysis' is the original name of this method."""

        self.wrapped.DynamicAnalysis()

    @property
    def cast_to(self) -> 'BearingSystemDeflection._Cast_BearingSystemDeflection':
        return self._Cast_BearingSystemDeflection(self)
