"""_1211.py

AbstractGearSetAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility.model_validation import _1783, _1782
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'AbstractGearSetAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearSetAnalysis',)


class AbstractGearSetAnalysis(_0.APIBase):
    """AbstractGearSetAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_ANALYSIS

    class _Cast_AbstractGearSetAnalysis:
        """Special nested class for casting AbstractGearSetAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractGearSetAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearSetRating)

        @property
        def gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating import _358
            
            return self._parent._cast(_358.GearSetDutyCycleRating)

        @property
        def gear_set_rating(self):
            from mastapy.gears.rating import _359
            
            return self._parent._cast(_359.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(self):
            from mastapy.gears.rating.zerol_bevel import _367
            
            return self._parent._cast(_367.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _371
            
            return self._parent._cast(_371.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(self):
            from mastapy.gears.rating.worm import _372
            
            return self._parent._cast(_372.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel import _393
            
            return self._parent._cast(_393.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _396
            
            return self._parent._cast(_396.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.spiral_bevel import _400
            
            return self._parent._cast(_400.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _403
            
            return self._parent._cast(_403.KlingelnbergCycloPalloidSpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _406
            
            return self._parent._cast(_406.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _409
            
            return self._parent._cast(_409.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(self):
            from mastapy.gears.rating.hypoid import _436
            
            return self._parent._cast(_436.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _445
            
            return self._parent._cast(_445.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(self):
            from mastapy.gears.rating.face import _446
            
            return self._parent._cast(_446.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _459
            
            return self._parent._cast(_459.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(self):
            from mastapy.gears.rating.cylindrical import _460
            
            return self._parent._cast(_460.CylindricalGearSetRating)

        @property
        def conical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _536
            
            return self._parent._cast(_536.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(self):
            from mastapy.gears.rating.conical import _537
            
            return self._parent._cast(_537.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _547
            
            return self._parent._cast(_547.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(self):
            from mastapy.gears.rating.concept import _548
            
            return self._parent._cast(_548.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(self):
            from mastapy.gears.rating.bevel import _551
            
            return self._parent._cast(_551.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _562
            
            return self._parent._cast(_562.AGMAGleasonConicalGearSetRating)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _615
            
            return self._parent._cast(_615.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _616
            
            return self._parent._cast(_616.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _620
            
            return self._parent._cast(_620.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _785
            
            return self._parent._cast(_785.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _786
            
            return self._parent._cast(_786.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _787
            
            return self._parent._cast(_787.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _788
            
            return self._parent._cast(_788.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca import _841
            
            return self._parent._cast(_841.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _855
            
            return self._parent._cast(_855.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _857
            
            return self._parent._cast(_857.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _863
            
            return self._parent._cast(_863.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(self):
            from mastapy.gears.load_case import _869
            
            return self._parent._cast(_869.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(self):
            from mastapy.gears.load_case.worm import _872
            
            return self._parent._cast(_872.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.gears.load_case.face import _875
            
            return self._parent._cast(_875.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.gears.load_case.cylindrical import _878
            
            return self._parent._cast(_878.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.gears.load_case.conical import _881
            
            return self._parent._cast(_881.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.gears.load_case.concept import _884
            
            return self._parent._cast(_884.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(self):
            from mastapy.gears.load_case.bevel import _888
            
            return self._parent._cast(_888.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _891
            
            return self._parent._cast(_891.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _892
            
            return self._parent._cast(_892.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _991
            
            return self._parent._cast(_991.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101
            
            return self._parent._cast(_1101.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102
            
            return self._parent._cast(_1102.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(self):
            from mastapy.gears.fe_model import _1194
            
            return self._parent._cast(_1194.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1197
            
            return self._parent._cast(_1197.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(self):
            from mastapy.gears.fe_model.conical import _1200
            
            return self._parent._cast(_1200.ConicalSetFEModel)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def gear_set_implementation_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(self):
            from mastapy.gears.analysis import _1223
            
            return self._parent._cast(_1223.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1224
            
            return self._parent._cast(_1224.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(self):
            from mastapy.gears.analysis import _1225
            
            return self._parent._cast(_1225.GearSetImplementationDetail)

        @property
        def abstract_gear_set_analysis(self) -> 'AbstractGearSetAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearSetAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def all_status_errors(self) -> 'List[_1783.StatusItem]':
        """List[StatusItem]: 'AllStatusErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def status(self) -> '_1782.Status':
        """Status: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def cast_to(self) -> 'AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis':
        return self._Cast_AbstractGearSetAnalysis(self)
