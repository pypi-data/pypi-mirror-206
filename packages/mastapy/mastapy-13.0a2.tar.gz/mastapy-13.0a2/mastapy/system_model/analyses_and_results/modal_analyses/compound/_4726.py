"""_4726.py

ComponentCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4572
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ComponentCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentCompoundModalAnalysis',)


class ComponentCompoundModalAnalysis(_4780.PartCompoundModalAnalysis):
    """ComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS

    class _Cast_ComponentCompoundModalAnalysis:
        """Special nested class for casting ComponentCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'ComponentCompoundModalAnalysis'):
            self._parent = parent

        @property
        def part_compound_modal_analysis(self):
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

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
        def abstract_shaft_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4702
            
            return self._parent._cast(_4702.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4703
            
            return self._parent._cast(_4703.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4705
            
            return self._parent._cast(_4705.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4709
            
            return self._parent._cast(_4709.BearingCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4712
            
            return self._parent._cast(_4712.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4715
            
            return self._parent._cast(_4715.BevelDifferentialPlanetGearCompoundModalAnalysis)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4716
            
            return self._parent._cast(_4716.BevelDifferentialSunGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4717
            
            return self._parent._cast(_4717.BevelGearCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4720
            
            return self._parent._cast(_4720.BoltCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4724
            
            return self._parent._cast(_4724.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4729
            
            return self._parent._cast(_4729.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4730
            
            return self._parent._cast(_4730.ConceptGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4733
            
            return self._parent._cast(_4733.ConicalGearCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4737
            
            return self._parent._cast(_4737.ConnectorCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4740
            
            return self._parent._cast(_4740.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4743
            
            return self._parent._cast(_4743.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4746
            
            return self._parent._cast(_4746.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4748
            
            return self._parent._cast(_4748.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4751
            
            return self._parent._cast(_4751.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4752
            
            return self._parent._cast(_4752.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4753
            
            return self._parent._cast(_4753.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4754
            
            return self._parent._cast(_4754.FaceGearCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4757
            
            return self._parent._cast(_4757.FEPartCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
            
            return self._parent._cast(_4759.GearCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4762
            
            return self._parent._cast(_4762.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4763
            
            return self._parent._cast(_4763.HypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4767
            
            return self._parent._cast(_4767.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4770
            
            return self._parent._cast(_4770.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4773
            
            return self._parent._cast(_4773.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis)

        @property
        def mass_disc_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4776
            
            return self._parent._cast(_4776.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4777
            
            return self._parent._cast(_4777.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4778
            
            return self._parent._cast(_4778.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4779
            
            return self._parent._cast(_4779.OilSealCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
            
            return self._parent._cast(_4783.PartToPartShearCouplingHalfCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4786
            
            return self._parent._cast(_4786.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4787
            
            return self._parent._cast(_4787.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4788
            
            return self._parent._cast(_4788.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4789
            
            return self._parent._cast(_4789.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4790
            
            return self._parent._cast(_4790.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4793
            
            return self._parent._cast(_4793.RollingRingCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4796
            
            return self._parent._cast(_4796.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4797
            
            return self._parent._cast(_4797.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4800
            
            return self._parent._cast(_4800.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4805
            
            return self._parent._cast(_4805.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4806
            
            return self._parent._cast(_4806.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4809
            
            return self._parent._cast(_4809.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4812
            
            return self._parent._cast(_4812.StraightBevelPlanetGearCompoundModalAnalysis)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4813
            
            return self._parent._cast(_4813.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4815
            
            return self._parent._cast(_4815.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4816
            
            return self._parent._cast(_4816.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4817
            
            return self._parent._cast(_4817.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4820
            
            return self._parent._cast(_4820.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4821
            
            return self._parent._cast(_4821.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4822
            
            return self._parent._cast(_4822.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4823
            
            return self._parent._cast(_4823.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4824
            
            return self._parent._cast(_4824.WormGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4827
            
            return self._parent._cast(_4827.ZerolBevelGearCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self) -> 'ComponentCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4572.ComponentModalAnalysis]':
        """List[ComponentModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4572.ComponentModalAnalysis]':
        """List[ComponentModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis':
        return self._Cast_ComponentCompoundModalAnalysis(self)
