"""_4368.py

PartParametricStudyTool
"""
from mastapy.utility_gui.charts import _1844, _1852, _1850
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2448
from mastapy.utility_gui import _1836
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4363
from mastapy.system_model.analyses_and_results.analysis_cases import _7507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'PartParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('PartParametricStudyTool',)


class PartParametricStudyTool(_7507.PartAnalysisCase):
    """PartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_PARAMETRIC_STUDY_TOOL

    class _Cast_PartParametricStudyTool:
        """Special nested class for casting PartParametricStudyTool to subclasses."""

        def __init__(self, parent: 'PartParametricStudyTool'):
            self._parent = parent

        @property
        def part_analysis_case(self):
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
        def abstract_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4271
            
            return self._parent._cast(_4271.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4272
            
            return self._parent._cast(_4272.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4273
            
            return self._parent._cast(_4273.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4276
            
            return self._parent._cast(_4276.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4277
            
            return self._parent._cast(_4277.AGMAGleasonConicalGearSetParametricStudyTool)

        @property
        def assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4278
            
            return self._parent._cast(_4278.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4279
            
            return self._parent._cast(_4279.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4281
            
            return self._parent._cast(_4281.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4283
            
            return self._parent._cast(_4283.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4284
            
            return self._parent._cast(_4284.BevelDifferentialGearSetParametricStudyTool)

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
        def bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4289
            
            return self._parent._cast(_4289.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4290
            
            return self._parent._cast(_4290.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4291
            
            return self._parent._cast(_4291.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4293
            
            return self._parent._cast(_4293.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4294
            
            return self._parent._cast(_4294.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
            
            return self._parent._cast(_4296.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298
            
            return self._parent._cast(_4298.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
            
            return self._parent._cast(_4299.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4301
            
            return self._parent._cast(_4301.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4302
            
            return self._parent._cast(_4302.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4304
            
            return self._parent._cast(_4304.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4305
            
            return self._parent._cast(_4305.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4307
            
            return self._parent._cast(_4307.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309
            
            return self._parent._cast(_4309.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4310
            
            return self._parent._cast(_4310.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4312
            
            return self._parent._cast(_4312.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
            
            return self._parent._cast(_4313.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4314
            
            return self._parent._cast(_4314.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
            
            return self._parent._cast(_4316.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4319
            
            return self._parent._cast(_4319.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4320
            
            return self._parent._cast(_4320.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4321
            
            return self._parent._cast(_4321.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4322
            
            return self._parent._cast(_4322.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4330
            
            return self._parent._cast(_4330.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4332
            
            return self._parent._cast(_4332.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4333
            
            return self._parent._cast(_4333.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4334
            
            return self._parent._cast(_4334.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4335
            
            return self._parent._cast(_4335.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337
            
            return self._parent._cast(_4337.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4338
            
            return self._parent._cast(_4338.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4339
            
            return self._parent._cast(_4339.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
            
            return self._parent._cast(_4341.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4342
            
            return self._parent._cast(_4342.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4345
            
            return self._parent._cast(_4345.KlingelnbergCycloPalloidConicalGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4346
            
            return self._parent._cast(_4346.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4348
            
            return self._parent._cast(_4348.KlingelnbergCycloPalloidHypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4349
            
            return self._parent._cast(_4349.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4351
            
            return self._parent._cast(_4351.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
            
            return self._parent._cast(_4352.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool)

        @property
        def mass_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4353
            
            return self._parent._cast(_4353.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
            
            return self._parent._cast(_4354.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4356
            
            return self._parent._cast(_4356.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4357
            
            return self._parent._cast(_4357.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4370
            
            return self._parent._cast(_4370.PartToPartShearCouplingHalfParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
            
            return self._parent._cast(_4371.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4373
            
            return self._parent._cast(_4373.PlanetaryGearSetParametricStudyTool)

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
        def rolling_ring_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4380
            
            return self._parent._cast(_4380.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
            
            return self._parent._cast(_4382.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4383
            
            return self._parent._cast(_4383.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4384
            
            return self._parent._cast(_4384.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4385
            
            return self._parent._cast(_4385.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4387
            
            return self._parent._cast(_4387.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389
            
            return self._parent._cast(_4389.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4390
            
            return self._parent._cast(_4390.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4392
            
            return self._parent._cast(_4392.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393
            
            return self._parent._cast(_4393.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4395
            
            return self._parent._cast(_4395.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4396
            
            return self._parent._cast(_4396.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4398
            
            return self._parent._cast(_4398.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4399
            
            return self._parent._cast(_4399.StraightBevelGearSetParametricStudyTool)

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
        def synchroniser_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4403
            
            return self._parent._cast(_4403.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4404
            
            return self._parent._cast(_4404.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4405
            
            return self._parent._cast(_4405.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4407
            
            return self._parent._cast(_4407.TorqueConverterParametricStudyTool)

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
        def worm_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4414
            
            return self._parent._cast(_4414.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4416
            
            return self._parent._cast(_4416.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4417
            
            return self._parent._cast(_4417.ZerolBevelGearSetParametricStudyTool)

        @property
        def part_parametric_study_tool(self) -> 'PartParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_of_experiments_chart(self) -> '_1844.NDChartDefinition':
        """NDChartDefinition: 'DesignOfExperimentsChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignOfExperimentsChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_sweep_chart_2d(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'LinearSweepChart2D' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearSweepChart2D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_sweep_chart_3d(self) -> '_1850.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'LinearSweepChart3D' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearSweepChart3D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2448.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def data_logger(self) -> '_1836.DataLoggerWithCharts':
        """DataLoggerWithCharts: 'DataLogger' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parametric_study_tool(self) -> '_4363.ParametricStudyTool':
        """ParametricStudyTool: 'ParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PartParametricStudyTool._Cast_PartParametricStudyTool':
        return self._Cast_PartParametricStudyTool(self)
