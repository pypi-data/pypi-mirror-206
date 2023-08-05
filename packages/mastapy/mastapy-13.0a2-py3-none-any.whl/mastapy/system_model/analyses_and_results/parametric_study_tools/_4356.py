"""_4356.py

MountableComponentParametricStudyTool
"""
from mastapy.system_model.part_model import _2444
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'MountableComponentParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentParametricStudyTool',)


class MountableComponentParametricStudyTool(_4296.ComponentParametricStudyTool):
    """MountableComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL

    class _Cast_MountableComponentParametricStudyTool:
        """Special nested class for casting MountableComponentParametricStudyTool to subclasses."""

        def __init__(self, parent: 'MountableComponentParametricStudyTool'):
            self._parent = parent

        @property
        def component_parametric_study_tool(self):
            return self._parent._cast(_4296.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4368
            
            return self._parent._cast(_4368.PartParametricStudyTool)

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
        def agma_gleason_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4276
            
            return self._parent._cast(_4276.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bearing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4279
            
            return self._parent._cast(_4279.BearingParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4283
            
            return self._parent._cast(_4283.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4285
            
            return self._parent._cast(_4285.BevelDifferentialPlanetGearParametricStudyTool)

        @property
        def bevel_differential_sun_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4286
            
            return self._parent._cast(_4286.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4288
            
            return self._parent._cast(_4288.BevelGearParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4293
            
            return self._parent._cast(_4293.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298
            
            return self._parent._cast(_4298.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4301
            
            return self._parent._cast(_4301.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4304
            
            return self._parent._cast(_4304.ConicalGearParametricStudyTool)

        @property
        def connector_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4307
            
            return self._parent._cast(_4307.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309
            
            return self._parent._cast(_4309.CouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
            
            return self._parent._cast(_4313.CVTPulleyParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4319
            
            return self._parent._cast(_4319.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4321
            
            return self._parent._cast(_4321.CylindricalPlanetGearParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4332
            
            return self._parent._cast(_4332.FaceGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337
            
            return self._parent._cast(_4337.GearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
            
            return self._parent._cast(_4341.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4345
            
            return self._parent._cast(_4345.KlingelnbergCycloPalloidConicalGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4348
            
            return self._parent._cast(_4348.KlingelnbergCycloPalloidHypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4351
            
            return self._parent._cast(_4351.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool)

        @property
        def mass_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4353
            
            return self._parent._cast(_4353.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
            
            return self._parent._cast(_4354.MeasurementComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4357
            
            return self._parent._cast(_4357.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4370
            
            return self._parent._cast(_4370.PartToPartShearCouplingHalfParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4374
            
            return self._parent._cast(_4374.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4375
            
            return self._parent._cast(_4375.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4376
            
            return self._parent._cast(_4376.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4377
            
            return self._parent._cast(_4377.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4378
            
            return self._parent._cast(_4378.RingPinsParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
            
            return self._parent._cast(_4382.RollingRingParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4384
            
            return self._parent._cast(_4384.ShaftHubConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389
            
            return self._parent._cast(_4389.SpiralBevelGearParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4392
            
            return self._parent._cast(_4392.SpringDamperHalfParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4395
            
            return self._parent._cast(_4395.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4398
            
            return self._parent._cast(_4398.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4400
            
            return self._parent._cast(_4400.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4401
            
            return self._parent._cast(_4401.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
            
            return self._parent._cast(_4402.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4404
            
            return self._parent._cast(_4404.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4405
            
            return self._parent._cast(_4405.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4408
            
            return self._parent._cast(_4408.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409
            
            return self._parent._cast(_4409.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
            
            return self._parent._cast(_4410.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4411
            
            return self._parent._cast(_4411.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4413
            
            return self._parent._cast(_4413.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4416
            
            return self._parent._cast(_4416.ZerolBevelGearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(self) -> 'MountableComponentParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2444.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool':
        return self._Cast_MountableComponentParametricStudyTool(self)
