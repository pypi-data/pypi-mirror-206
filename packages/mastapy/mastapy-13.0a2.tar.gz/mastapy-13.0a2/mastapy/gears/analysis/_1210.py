"""_1210.py

AbstractGearMeshAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1209
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'AbstractGearMeshAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearMeshAnalysis',)


class AbstractGearMeshAnalysis(_0.APIBase):
    """AbstractGearMeshAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_ANALYSIS

    class _Cast_AbstractGearMeshAnalysis:
        """Special nested class for casting AbstractGearMeshAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractGearMeshAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _349
            
            return self._parent._cast(_349.AbstractGearMeshRating)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _356
            
            return self._parent._cast(_356.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(self):
            from mastapy.gears.rating import _361
            
            return self._parent._cast(_361.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.zerol_bevel import _365
            
            return self._parent._cast(_365.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(self):
            from mastapy.gears.rating.worm import _369
            
            return self._parent._cast(_369.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _373
            
            return self._parent._cast(_373.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel import _391
            
            return self._parent._cast(_391.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _394
            
            return self._parent._cast(_394.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.spiral_bevel import _398
            
            return self._parent._cast(_398.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _401
            
            return self._parent._cast(_401.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _404
            
            return self._parent._cast(_404.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _407
            
            return self._parent._cast(_407.KlingelnbergCycloPalloidConicalGearMeshRating)

        @property
        def hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.hypoid import _434
            
            return self._parent._cast(_434.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _442
            
            return self._parent._cast(_442.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(self):
            from mastapy.gears.rating.face import _443
            
            return self._parent._cast(_443.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(self):
            from mastapy.gears.rating.cylindrical import _454
            
            return self._parent._cast(_454.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _462
            
            return self._parent._cast(_462.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(self):
            from mastapy.gears.rating.conical import _534
            
            return self._parent._cast(_534.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _539
            
            return self._parent._cast(_539.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _544
            
            return self._parent._cast(_544.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(self):
            from mastapy.gears.rating.concept import _545
            
            return self._parent._cast(_545.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.bevel import _549
            
            return self._parent._cast(_549.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _560
            
            return self._parent._cast(_560.AGMAGleasonConicalGearMeshRating)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _613
            
            return self._parent._cast(_613.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _614
            
            return self._parent._cast(_614.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _617
            
            return self._parent._cast(_617.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _779
            
            return self._parent._cast(_779.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _780
            
            return self._parent._cast(_780.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _781
            
            return self._parent._cast(_781.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _782
            
            return self._parent._cast(_782.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca import _836
            
            return self._parent._cast(_836.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _852
            
            return self._parent._cast(_852.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _865
            
            return self._parent._cast(_865.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(self):
            from mastapy.gears.load_case import _870
            
            return self._parent._cast(_870.MeshLoadCase)

        @property
        def worm_mesh_load_case(self):
            from mastapy.gears.load_case.worm import _873
            
            return self._parent._cast(_873.WormMeshLoadCase)

        @property
        def face_mesh_load_case(self):
            from mastapy.gears.load_case.face import _876
            
            return self._parent._cast(_876.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(self):
            from mastapy.gears.load_case.cylindrical import _879
            
            return self._parent._cast(_879.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(self):
            from mastapy.gears.load_case.conical import _882
            
            return self._parent._cast(_882.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(self):
            from mastapy.gears.load_case.concept import _885
            
            return self._parent._cast(_885.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(self):
            from mastapy.gears.load_case.bevel import _887
            
            return self._parent._cast(_887.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _889
            
            return self._parent._cast(_889.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _890
            
            return self._parent._cast(_890.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _987
            
            return self._parent._cast(_987.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1092
            
            return self._parent._cast(_1092.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093
            
            return self._parent._cast(_1093.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(self):
            from mastapy.gears.fe_model import _1192
            
            return self._parent._cast(_1192.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1196
            
            return self._parent._cast(_1196.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(self):
            from mastapy.gears.fe_model.conical import _1199
            
            return self._parent._cast(_1199.ConicalMeshFEModel)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def gear_mesh_implementation_analysis(self):
            from mastapy.gears.analysis import _1217
            
            return self._parent._cast(_1217.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1218
            
            return self._parent._cast(_1218.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(self):
            from mastapy.gears.analysis import _1219
            
            return self._parent._cast(_1219.GearMeshImplementationDetail)

        @property
        def abstract_gear_mesh_analysis(self) -> 'AbstractGearMeshAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearMeshAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_name(self) -> 'str':
        """str: 'MeshName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshName

        if temp is None:
            return ''

        return temp

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
    def gear_a(self) -> '_1209.AbstractGearAnalysis':
        """AbstractGearAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_1209.AbstractGearAnalysis':
        """AbstractGearAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

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
    def cast_to(self) -> 'AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis':
        return self._Cast_AbstractGearMeshAnalysis(self)
