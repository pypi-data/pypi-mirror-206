"""_2694.py

ComponentSystemDeflection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2424
from mastapy.math_utility import _1506
from mastapy.materials.efficiency import _298, _299
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2827
from mastapy.math_utility.measured_vectors import _1550, _1551
from mastapy.system_model.analyses_and_results.power_flows import _4034
from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ComponentSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentSystemDeflection',)


class ComponentSystemDeflection(_2764.PartSystemDeflection):
    """ComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_SYSTEM_DEFLECTION

    class _Cast_ComponentSystemDeflection:
        """Special nested class for casting ComponentSystemDeflection to subclasses."""

        def __init__(self, parent: 'ComponentSystemDeflection'):
            self._parent = parent

        @property
        def part_system_deflection(self):
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
        def abstract_shaft_or_housing_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2665
            
            return self._parent._cast(_2665.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2666
            
            return self._parent._cast(_2666.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2670
            
            return self._parent._cast(_2670.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bearing_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2677
            
            return self._parent._cast(_2677.BearingSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2682
            
            return self._parent._cast(_2682.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2683
            
            return self._parent._cast(_2683.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2684
            
            return self._parent._cast(_2684.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2687
            
            return self._parent._cast(_2687.BevelGearSystemDeflection)

        @property
        def bolt_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2689
            
            return self._parent._cast(_2689.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2691
            
            return self._parent._cast(_2691.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2701
            
            return self._parent._cast(_2701.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2705
            
            return self._parent._cast(_2705.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2707
            
            return self._parent._cast(_2707.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2709
            
            return self._parent._cast(_2709.CouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2712
            
            return self._parent._cast(_2712.CVTPulleySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2717
            
            return self._parent._cast(_2717.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2724
            
            return self._parent._cast(_2724.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2725
            
            return self._parent._cast(_2725.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2726
            
            return self._parent._cast(_2726.CylindricalGearSystemDeflectionWithLTCAResults)

        @property
        def cylindrical_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2729
            
            return self._parent._cast(_2729.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2730
            
            return self._parent._cast(_2730.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2731
            
            return self._parent._cast(_2731.ExternalCADModelSystemDeflection)

        @property
        def face_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2735
            
            return self._parent._cast(_2735.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2736
            
            return self._parent._cast(_2736.FEPartSystemDeflection)

        @property
        def gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2740
            
            return self._parent._cast(_2740.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2741
            
            return self._parent._cast(_2741.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2744
            
            return self._parent._cast(_2744.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2749
            
            return self._parent._cast(_2749.KlingelnbergCycloPalloidConicalGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2752
            
            return self._parent._cast(_2752.KlingelnbergCycloPalloidHypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2755
            
            return self._parent._cast(_2755.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)

        @property
        def mass_disc_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2758
            
            return self._parent._cast(_2758.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2759
            
            return self._parent._cast(_2759.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2761
            
            return self._parent._cast(_2761.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2763
            
            return self._parent._cast(_2763.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2766
            
            return self._parent._cast(_2766.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def planet_carrier_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2769
            
            return self._parent._cast(_2769.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2770
            
            return self._parent._cast(_2770.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2771
            
            return self._parent._cast(_2771.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2772
            
            return self._parent._cast(_2772.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2773
            
            return self._parent._cast(_2773.RingPinsSystemDeflection)

        @property
        def rolling_ring_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2778
            
            return self._parent._cast(_2778.RollingRingSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2780
            
            return self._parent._cast(_2780.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2783
            
            return self._parent._cast(_2783.ShaftSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2788
            
            return self._parent._cast(_2788.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2790
            
            return self._parent._cast(_2790.SpringDamperHalfSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2794
            
            return self._parent._cast(_2794.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2797
            
            return self._parent._cast(_2797.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2798
            
            return self._parent._cast(_2798.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2799
            
            return self._parent._cast(_2799.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2800
            
            return self._parent._cast(_2800.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2801
            
            return self._parent._cast(_2801.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2802
            
            return self._parent._cast(_2802.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2808
            
            return self._parent._cast(_2808.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2810
            
            return self._parent._cast(_2810.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2813
            
            return self._parent._cast(_2813.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2814
            
            return self._parent._cast(_2814.VirtualComponentSystemDeflection)

        @property
        def worm_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2817
            
            return self._parent._cast(_2817.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2820
            
            return self._parent._cast(_2820.ZerolBevelGearSystemDeflection)

        @property
        def component_system_deflection(self) -> 'ComponentSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def energy_loss_during_load_case(self) -> 'float':
        """float: 'EnergyLossDuringLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyLossDuringLoadCase

        if temp is None:
            return 0.0

        return temp

    @property
    def has_converged(self) -> 'bool':
        """bool: 'HasConverged' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasConverged

        if temp is None:
            return False

        return temp

    @property
    def percentage_of_iterations_converged(self) -> 'float':
        """float: 'PercentageOfIterationsConverged' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageOfIterationsConverged

        if temp is None:
            return 0.0

        return temp

    @property
    def reason_for_non_convergence(self) -> 'str':
        """str: 'ReasonForNonConvergence' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonForNonConvergence

        if temp is None:
            return ''

        return temp

    @property
    def reason_mass_properties_are_unknown(self) -> 'str':
        """str: 'ReasonMassPropertiesAreUnknown' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ''

        return temp

    @property
    def reason_mass_properties_are_zero(self) -> 'str':
        """str: 'ReasonMassPropertiesAreZero' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ''

        return temp

    @property
    def relaxation(self) -> 'float':
        """float: 'Relaxation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Relaxation

        if temp is None:
            return 0.0

        return temp

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self) -> '_2424.Component':
        """Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass_properties_in_local_coordinate_system_from_node_model(self) -> '_1506.MassProperties':
        """MassProperties: 'MassPropertiesInLocalCoordinateSystemFromNodeModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesInLocalCoordinateSystemFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_loss(self) -> '_298.PowerLoss':
        """PowerLoss: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def resistive_torque(self) -> '_299.ResistiveTorque':
        """ResistiveTorque: 'ResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rigidly_connected_components(self) -> '_2827.RigidlyConnectedComponentGroupSystemDeflection':
        """RigidlyConnectedComponentGroupSystemDeflection: 'RigidlyConnectedComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RigidlyConnectedComponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connected_components_forces_in_lcs(self) -> 'List[_1550.ForceResults]':
        """List[ForceResults]: 'ConnectedComponentsForcesInLCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponentsForcesInLCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connected_components_forces_in_wcs(self) -> 'List[_1550.ForceResults]':
        """List[ForceResults]: 'ConnectedComponentsForcesInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponentsForcesInWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def node_results(self) -> 'List[_1551.NodeResults]':
        """List[NodeResults]: 'NodeResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4034.ComponentPowerFlow':
        """ComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ComponentSystemDeflection._Cast_ComponentSystemDeflection':
        return self._Cast_ComponentSystemDeflection(self)
