"""_362.py

MeshSingleFlankRating
"""
from typing import List

from mastapy.gears import _315
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.materials.efficiency import _290
from mastapy.gears.rating import _360
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshSingleFlankRating',)


class MeshSingleFlankRating(_0.APIBase):
    """MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _MESH_SINGLE_FLANK_RATING

    class _Cast_MeshSingleFlankRating:
        """Special nested class for casting MeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'MeshSingleFlankRating'):
            self._parent = parent

        @property
        def klingelnberg_conical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _410
            
            return self._parent._cast(_410.KlingelnbergConicalMeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_mesh_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _414
            
            return self._parent._cast(_414.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _415
            
            return self._parent._cast(_415.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating(self):
            from mastapy.gears.rating.iso_10300 import _418
            
            return self._parent._cast(_418.ISO10300MeshSingleFlankRating)

        @property
        def iso_10300_mesh_single_flank_rating_bevel_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _419
            
            return self._parent._cast(_419.Iso10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso_10300_mesh_single_flank_rating_hypoid_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _420
            
            return self._parent._cast(_420.Iso10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(self):
            from mastapy.gears.rating.iso_10300 import _421
            
            return self._parent._cast(_421.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _422
            
            return self._parent._cast(_422.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(self):
            from mastapy.gears.rating.hypoid.standards import _439
            
            return self._parent._cast(_439.GleasonHypoidMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _463
            
            return self._parent._cast(_463.CylindricalMeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _485
            
            return self._parent._cast(_485.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _487
            
            return self._parent._cast(_487.PlasticGearVDI2736AbstractMeshSingleFlankRating)

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _489
            
            return self._parent._cast(_489.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _507
            
            return self._parent._cast(_507.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _509
            
            return self._parent._cast(_509.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _511
            
            return self._parent._cast(_511.ISO63362019MeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _513
            
            return self._parent._cast(_513.ISO6336AbstractMeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _515
            
            return self._parent._cast(_515.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _528
            
            return self._parent._cast(_528.DIN3990MeshSingleFlankRating)

        @property
        def agma2101_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.agma import _530
            
            return self._parent._cast(_530.AGMA2101MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.conical import _541
            
            return self._parent._cast(_541.ConicalMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _553
            
            return self._parent._cast(_553.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _555
            
            return self._parent._cast(_555.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _557
            
            return self._parent._cast(_557.SpiralBevelMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(self) -> 'MeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_calculation_method(self) -> '_315.CoefficientOfFrictionCalculationMethod':
        """CoefficientOfFrictionCalculationMethod: 'CoefficientOfFrictionCalculationMethod' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFrictionCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _315.CoefficientOfFrictionCalculationMethod)
        return constructor.new_from_mastapy_type(_315.CoefficientOfFrictionCalculationMethod)(value) if value is not None else None

    @coefficient_of_friction_calculation_method.setter
    def coefficient_of_friction_calculation_method(self, value: '_315.CoefficientOfFrictionCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _315.CoefficientOfFrictionCalculationMethod.type_())
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def efficiency_rating_method(self) -> '_290.EfficiencyRatingMethod':
        """EfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _290.EfficiencyRatingMethod)
        return constructor.new_from_mastapy_type(_290.EfficiencyRatingMethod)(value) if value is not None else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: '_290.EfficiencyRatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _290.EfficiencyRatingMethod.type_())
        self.wrapped.EfficiencyRatingMethod = value

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
    def power(self) -> 'float':
        """float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ''

        return temp

    @property
    def gear_single_flank_ratings(self) -> 'List[_360.GearSingleFlankRating]':
        """List[GearSingleFlankRating]: 'GearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
    def cast_to(self) -> 'MeshSingleFlankRating._Cast_MeshSingleFlankRating':
        return self._Cast_MeshSingleFlankRating(self)
