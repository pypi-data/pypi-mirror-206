"""_5406.py

FEPartMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2433
from mastapy.system_model.analyses_and_results.static_loads import _6851
from mastapy.system_model.analyses_and_results.mbd_analyses import _5349
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'FEPartMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartMultibodyDynamicsAnalysis',)


class FEPartMultibodyDynamicsAnalysis(_5349.AbstractShaftOrHousingMultibodyDynamicsAnalysis):
    """FEPartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_FEPartMultibodyDynamicsAnalysis:
        """Special nested class for casting FEPartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'FEPartMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(self):
            return self._parent._cast(_5349.AbstractShaftOrHousingMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
            
            return self._parent._cast(_5375.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartTimeSeriesLoadAnalysisCase)

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
        def fe_part_multibody_dynamics_analysis(self) -> 'FEPartMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def elastic_deflections_total_magnitude(self) -> 'List[float]':
        """List[float]: 'ElasticDeflectionsTotalMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticDeflectionsTotalMagnitude

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_x_accelerations(self) -> 'List[float]':
        """List[float]: 'ElasticLocalXAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalXAccelerations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_x_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalXDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalXDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_x_velocities(self) -> 'List[float]':
        """List[float]: 'ElasticLocalXVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalXVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_y_accelerations(self) -> 'List[float]':
        """List[float]: 'ElasticLocalYAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalYAccelerations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_y_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalYDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalYDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_y_velocities(self) -> 'List[float]':
        """List[float]: 'ElasticLocalYVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalYVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_z_accelerations(self) -> 'List[float]':
        """List[float]: 'ElasticLocalZAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalZAccelerations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_z_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalZDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalZDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_z_velocities(self) -> 'List[float]':
        """List[float]: 'ElasticLocalZVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalZVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_x_accelerations(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaXAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaXAccelerations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_x_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaXDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaXDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_x_velocities(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaXVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaXVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_y_accelerations(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaYAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaYAccelerations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_y_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaYDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaYDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_y_velocities(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaYVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaYVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_z_accelerations(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaZAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaZAccelerations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_z_deflections(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaZDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaZDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def elastic_local_theta_z_velocities(self) -> 'List[float]':
        """List[float]: 'ElasticLocalThetaZVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticLocalThetaZVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def nodal_force_x(self) -> 'List[float]':
        """List[float]: 'NodalForceX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodalForceX

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def nodal_force_y(self) -> 'List[float]':
        """List[float]: 'NodalForceY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodalForceY

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def nodal_force_z(self) -> 'List[float]':
        """List[float]: 'NodalForceZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodalForceZ

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def nodal_force_theta_x(self) -> 'List[float]':
        """List[float]: 'NodalForceThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodalForceThetaX

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def nodal_force_theta_y(self) -> 'List[float]':
        """List[float]: 'NodalForceThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodalForceThetaY

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def nodal_force_theta_z(self) -> 'List[float]':
        """List[float]: 'NodalForceThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodalForceThetaZ

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def component_design(self) -> '_2433.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6851.FEPartLoadCase':
        """FEPartLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[FEPartMultibodyDynamicsAnalysis]':
        """List[FEPartMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FEPartMultibodyDynamicsAnalysis._Cast_FEPartMultibodyDynamicsAnalysis':
        return self._Cast_FEPartMultibodyDynamicsAnalysis(self)
