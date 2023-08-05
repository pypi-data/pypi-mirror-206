"""_1209.py

AbstractGearAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'AbstractGearAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearAnalysis',)


class AbstractGearAnalysis(_0.APIBase):
    """AbstractGearAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_ANALYSIS

    class _Cast_AbstractGearAnalysis:
        """Special nested class for casting AbstractGearAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractGearAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _350
            
            return self._parent._cast(_350.AbstractGearRating)

        @property
        def gear_duty_cycle_rating(self):
            from mastapy.gears.rating import _354
            
            return self._parent._cast(_354.GearDutyCycleRating)

        @property
        def gear_rating(self):
            from mastapy.gears.rating import _357
            
            return self._parent._cast(_357.GearRating)

        @property
        def zerol_bevel_gear_rating(self):
            from mastapy.gears.rating.zerol_bevel import _366
            
            return self._parent._cast(_366.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _368
            
            return self._parent._cast(_368.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(self):
            from mastapy.gears.rating.worm import _370
            
            return self._parent._cast(_370.WormGearRating)

        @property
        def straight_bevel_gear_rating(self):
            from mastapy.gears.rating.straight_bevel import _392
            
            return self._parent._cast(_392.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _395
            
            return self._parent._cast(_395.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.spiral_bevel import _399
            
            return self._parent._cast(_399.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _402
            
            return self._parent._cast(_402.KlingelnbergCycloPalloidSpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _405
            
            return self._parent._cast(_405.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _408
            
            return self._parent._cast(_408.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self):
            from mastapy.gears.rating.hypoid import _435
            
            return self._parent._cast(_435.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _441
            
            return self._parent._cast(_441.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(self):
            from mastapy.gears.rating.face import _444
            
            return self._parent._cast(_444.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _451
            
            return self._parent._cast(_451.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(self):
            from mastapy.gears.rating.cylindrical import _456
            
            return self._parent._cast(_456.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _533
            
            return self._parent._cast(_533.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(self):
            from mastapy.gears.rating.conical import _535
            
            return self._parent._cast(_535.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _543
            
            return self._parent._cast(_543.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(self):
            from mastapy.gears.rating.concept import _546
            
            return self._parent._cast(_546.ConceptGearRating)

        @property
        def bevel_gear_rating(self):
            from mastapy.gears.rating.bevel import _550
            
            return self._parent._cast(_550.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _561
            
            return self._parent._cast(_561.AGMAGleasonConicalGearRating)

        @property
        def cylindrical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _607
            
            return self._parent._cast(_607.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _611
            
            return self._parent._cast(_611.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _612
            
            return self._parent._cast(_612.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _770
            
            return self._parent._cast(_770.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _771
            
            return self._parent._cast(_771.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _772
            
            return self._parent._cast(_772.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _773
            
            return self._parent._cast(_773.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _783
            
            return self._parent._cast(_783.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _784
            
            return self._parent._cast(_784.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _789
            
            return self._parent._cast(_789.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(self):
            from mastapy.gears.ltca import _835
            
            return self._parent._cast(_835.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _851
            
            return self._parent._cast(_851.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _862
            
            return self._parent._cast(_862.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(self):
            from mastapy.gears.load_case import _868
            
            return self._parent._cast(_868.GearLoadCaseBase)

        @property
        def worm_gear_load_case(self):
            from mastapy.gears.load_case.worm import _871
            
            return self._parent._cast(_871.WormGearLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.gears.load_case.face import _874
            
            return self._parent._cast(_874.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.gears.load_case.cylindrical import _877
            
            return self._parent._cast(_877.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.gears.load_case.conical import _880
            
            return self._parent._cast(_880.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.gears.load_case.concept import _883
            
            return self._parent._cast(_883.ConceptGearLoadCase)

        @property
        def bevel_load_case(self):
            from mastapy.gears.load_case.bevel import _886
            
            return self._parent._cast(_886.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _893
            
            return self._parent._cast(_893.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _894
            
            return self._parent._cast(_894.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _988
            
            return self._parent._cast(_988.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1094
            
            return self._parent._cast(_1094.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1095
            
            return self._parent._cast(_1095.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1096
            
            return self._parent._cast(_1096.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098
            
            return self._parent._cast(_1098.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(self):
            from mastapy.gears.fe_model import _1191
            
            return self._parent._cast(_1191.GearFEModel)

        @property
        def cylindrical_gear_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1195
            
            return self._parent._cast(_1195.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(self):
            from mastapy.gears.fe_model.conical import _1198
            
            return self._parent._cast(_1198.ConicalGearFEModel)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def gear_implementation_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def abstract_gear_analysis(self) -> 'AbstractGearAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def name_with_gear_set_name(self) -> 'str':
        """str: 'NameWithGearSetName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NameWithGearSetName

        if temp is None:
            return ''

        return temp

    @property
    def planet_index(self) -> 'int':
        """int: 'PlanetIndex' is the original name of this property."""

        temp = self.wrapped.PlanetIndex

        if temp is None:
            return 0

        return temp

    @planet_index.setter
    def planet_index(self, value: 'int'):
        self.wrapped.PlanetIndex = int(value) if value else 0

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
    def cast_to(self) -> 'AbstractGearAnalysis._Cast_AbstractGearAnalysis':
        return self._Cast_AbstractGearAnalysis(self)
