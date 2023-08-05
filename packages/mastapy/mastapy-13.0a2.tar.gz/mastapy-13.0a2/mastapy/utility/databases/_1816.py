"""_1816.py

NamedDatabaseItem
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility import _1571
from mastapy.utility.databases import _1817
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DATABASE_ITEM = python_net_import('SMT.MastaAPI.Utility.Databases', 'NamedDatabaseItem')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedDatabaseItem',)


class NamedDatabaseItem(_0.APIBase):
    """NamedDatabaseItem

    This is a mastapy class.
    """

    TYPE = _NAMED_DATABASE_ITEM

    class _Cast_NamedDatabaseItem:
        """Special nested class for casting NamedDatabaseItem to subclasses."""

        def __init__(self, parent: 'NamedDatabaseItem'):
            self._parent = parent

        @property
        def shaft_material(self):
            from mastapy.shafts import _24
            
            return self._parent._cast(_24.ShaftMaterial)

        @property
        def shaft_settings_item(self):
            from mastapy.shafts import _40
            
            return self._parent._cast(_40.ShaftSettingsItem)

        @property
        def simple_shaft_definition(self):
            from mastapy.shafts import _43
            
            return self._parent._cast(_43.SimpleShaftDefinition)

        @property
        def analysis_settings_item(self):
            from mastapy.nodal_analysis import _50
            
            return self._parent._cast(_50.AnalysisSettingsItem)

        @property
        def bearing_material(self):
            from mastapy.materials import _241
            
            return self._parent._cast(_241.BearingMaterial)

        @property
        def lubrication_detail(self):
            from mastapy.materials import _263
            
            return self._parent._cast(_263.LubricationDetail)

        @property
        def material(self):
            from mastapy.materials import _265
            
            return self._parent._cast(_265.Material)

        @property
        def materials_settings_item(self):
            from mastapy.materials import _269
            
            return self._parent._cast(_269.MaterialsSettingsItem)

        @property
        def pocketing_power_loss_coefficients(self):
            from mastapy.gears import _338
            
            return self._parent._cast(_338.PocketingPowerLossCoefficients)

        @property
        def cylindrical_gear_design_and_rating_settings_item(self):
            from mastapy.gears.rating.cylindrical import _450
            
            return self._parent._cast(_450.CylindricalGearDesignAndRatingSettingsItem)

        @property
        def cylindrical_plastic_gear_rating_settings_item(self):
            from mastapy.gears.rating.cylindrical import _466
            
            return self._parent._cast(_466.CylindricalPlasticGearRatingSettingsItem)

        @property
        def agma_cylindrical_gear_material(self):
            from mastapy.gears.materials import _578
            
            return self._parent._cast(_578.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(self):
            from mastapy.gears.materials import _580
            
            return self._parent._cast(_580.BevelGearISOMaterial)

        @property
        def bevel_gear_material(self):
            from mastapy.gears.materials import _582
            
            return self._parent._cast(_582.BevelGearMaterial)

        @property
        def cylindrical_gear_material(self):
            from mastapy.gears.materials import _586
            
            return self._parent._cast(_586.CylindricalGearMaterial)

        @property
        def gear_material(self):
            from mastapy.gears.materials import _589
            
            return self._parent._cast(_589.GearMaterial)

        @property
        def iso_cylindrical_gear_material(self):
            from mastapy.gears.materials import _592
            
            return self._parent._cast(_592.ISOCylindricalGearMaterial)

        @property
        def isotr1417912001_coefficient_of_friction_constants(self):
            from mastapy.gears.materials import _593
            
            return self._parent._cast(_593.ISOTR1417912001CoefficientOfFrictionConstants)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(self):
            from mastapy.gears.materials import _596
            
            return self._parent._cast(_596.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(self):
            from mastapy.gears.materials import _598
            
            return self._parent._cast(_598.PlasticCylindricalGearMaterial)

        @property
        def raw_material(self):
            from mastapy.gears.materials import _601
            
            return self._parent._cast(_601.RawMaterial)

        @property
        def cylindrical_gear_abstract_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _701
            
            return self._parent._cast(_701.CylindricalGearAbstractCutterDesign)

        @property
        def cylindrical_gear_form_grinding_wheel(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _702
            
            return self._parent._cast(_702.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703
            
            return self._parent._cast(_703.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _704
            
            return self._parent._cast(_704.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705
            
            return self._parent._cast(_705.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _707
            
            return self._parent._cast(_707.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _708
            
            return self._parent._cast(_708.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_shaper(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _709
            
            return self._parent._cast(_709.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _710
            
            return self._parent._cast(_710.CylindricalGearShaver)

        @property
        def involute_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713
            
            return self._parent._cast(_713.InvoluteCutterDesign)

        @property
        def manufacturing_machine(self):
            from mastapy.gears.manufacturing.bevel import _794
            
            return self._parent._cast(_794.ManufacturingMachine)

        @property
        def bevel_hypoid_gear_design_settings_item(self):
            from mastapy.gears.gear_designs import _936
            
            return self._parent._cast(_936.BevelHypoidGearDesignSettingsItem)

        @property
        def bevel_hypoid_gear_rating_settings_item(self):
            from mastapy.gears.gear_designs import _938
            
            return self._parent._cast(_938.BevelHypoidGearRatingSettingsItem)

        @property
        def design_constraints_collection(self):
            from mastapy.gears.gear_designs import _941
            
            return self._parent._cast(_941.DesignConstraintsCollection)

        @property
        def cylindrical_gear_design_constraints(self):
            from mastapy.gears.gear_designs.cylindrical import _1009
            
            return self._parent._cast(_1009.CylindricalGearDesignConstraints)

        @property
        def cylindrical_gear_micro_geometry_settings_item(self):
            from mastapy.gears.gear_designs.cylindrical import _1017
            
            return self._parent._cast(_1017.CylindricalGearMicroGeometrySettingsItem)

        @property
        def magnet_material(self):
            from mastapy.electric_machines import _1273
            
            return self._parent._cast(_1273.MagnetMaterial)

        @property
        def stator_rotor_material(self):
            from mastapy.electric_machines import _1291
            
            return self._parent._cast(_1291.StatorRotorMaterial)

        @property
        def winding_material(self):
            from mastapy.electric_machines import _1303
            
            return self._parent._cast(_1303.WindingMaterial)

        @property
        def spline_material(self):
            from mastapy.detailed_rigid_connectors.splines import _1404
            
            return self._parent._cast(_1404.SplineMaterial)

        @property
        def cycloidal_disc_material(self):
            from mastapy.cycloidal import _1444
            
            return self._parent._cast(_1444.CycloidalDiscMaterial)

        @property
        def ring_pins_material(self):
            from mastapy.cycloidal import _1451
            
            return self._parent._cast(_1451.RingPinsMaterial)

        @property
        def bolted_joint_material(self):
            from mastapy.bolts import _1454
            
            return self._parent._cast(_1454.BoltedJointMaterial)

        @property
        def bolt_geometry(self):
            from mastapy.bolts import _1456
            
            return self._parent._cast(_1456.BoltGeometry)

        @property
        def bolt_material(self):
            from mastapy.bolts import _1458
            
            return self._parent._cast(_1458.BoltMaterial)

        @property
        def pareto_optimisation_strategy(self):
            from mastapy.math_utility.optimisation import _1538
            
            return self._parent._cast(_1538.ParetoOptimisationStrategy)

        @property
        def bearing_settings_item(self):
            from mastapy.bearings import _1866
            
            return self._parent._cast(_1866.BearingSettingsItem)

        @property
        def iso14179_settings(self):
            from mastapy.bearings.bearing_results.rolling import _1959
            
            return self._parent._cast(_1959.ISO14179Settings)

        @property
        def conical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2211
            
            return self._parent._cast(_2211.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2214
            
            return self._parent._cast(_2214.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(self):
            from mastapy.system_model.optimization import _2220
            
            return self._parent._cast(_2220.OptimizationStrategy)

        @property
        def optimization_strategy_base(self):
            from mastapy.system_model.optimization import _2221
            
            return self._parent._cast(_2221.OptimizationStrategyBase)

        @property
        def supercharger_rotor_set(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2542
            
            return self._parent._cast(_2542.SuperchargerRotorSet)

        @property
        def named_database_item(self) -> 'NamedDatabaseItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedDatabaseItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self) -> 'str':
        """str: 'Comment' is the original name of this property."""

        temp = self.wrapped.Comment

        if temp is None:
            return ''

        return temp

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else ''

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def no_history(self) -> 'str':
        """str: 'NoHistory' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NoHistory

        if temp is None:
            return ''

        return temp

    @property
    def history(self) -> '_1571.FileHistory':
        """FileHistory: 'History' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def database_key(self) -> '_1817.NamedKey':
        """NamedKey: 'DatabaseKey' is the original name of this property."""

        temp = self.wrapped.DatabaseKey

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @database_key.setter
    def database_key(self, value: '_1817.NamedKey'):
        value = value.wrapped if value else None
        self.wrapped.DatabaseKey = value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'NamedDatabaseItem._Cast_NamedDatabaseItem':
        return self._Cast_NamedDatabaseItem(self)
