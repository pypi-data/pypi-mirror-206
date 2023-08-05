"""_360.py

GearSingleFlankRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSingleFlankRating',)


class GearSingleFlankRating(_0.APIBase):
    """GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SINGLE_FLANK_RATING

    class _Cast_GearSingleFlankRating:
        """Special nested class for casting GearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'GearSingleFlankRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _412
            
            return self._parent._cast(_412.KlingelnbergCycloPalloidConicalGearSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_single_flank_rating(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _413
            
            return self._parent._cast(_413.KlingelnbergCycloPalloidHypoidGearSingleFlankRating)

        @property
        def iso10300_single_flank_rating(self):
            from mastapy.gears.rating.iso_10300 import _425
            
            return self._parent._cast(_425.ISO10300SingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _426
            
            return self._parent._cast(_426.ISO10300SingleFlankRatingBevelMethodB2)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _427
            
            return self._parent._cast(_427.ISO10300SingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_single_flank_rating_method_b1(self):
            from mastapy.gears.rating.iso_10300 import _428
            
            return self._parent._cast(_428.ISO10300SingleFlankRatingMethodB1)

        @property
        def iso10300_single_flank_rating_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _429
            
            return self._parent._cast(_429.ISO10300SingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_gear_single_flank_rating(self):
            from mastapy.gears.rating.hypoid.standards import _438
            
            return self._parent._cast(_438.GleasonHypoidGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _461
            
            return self._parent._cast(_461.CylindricalGearSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _486
            
            return self._parent._cast(_486.PlasticGearVDI2736AbstractGearSingleFlankRating)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _491
            
            return self._parent._cast(_491.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _492
            
            return self._parent._cast(_492.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh)

        @property
        def iso63361996_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _506
            
            return self._parent._cast(_506.ISO63361996GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _508
            
            return self._parent._cast(_508.ISO63362006GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _510
            
            return self._parent._cast(_510.ISO63362019GearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _512
            
            return self._parent._cast(_512.ISO6336AbstractGearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _514
            
            return self._parent._cast(_514.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _527
            
            return self._parent._cast(_527.DIN3990GearSingleFlankRating)

        @property
        def agma2101_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.agma import _529
            
            return self._parent._cast(_529.AGMA2101GearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(self):
            from mastapy.gears.rating.conical import _538
            
            return self._parent._cast(_538.ConicalGearSingleFlankRating)

        @property
        def agma_spiral_bevel_gear_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _552
            
            return self._parent._cast(_552.AGMASpiralBevelGearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _554
            
            return self._parent._cast(_554.GleasonSpiralBevelGearSingleFlankRating)

        @property
        def spiral_bevel_gear_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _556
            
            return self._parent._cast(_556.SpiralBevelGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self) -> 'GearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

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
    def number_of_load_cycles(self) -> 'float':
        """float: 'NumberOfLoadCycles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfLoadCycles

        if temp is None:
            return 0.0

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
    def rotation_speed(self) -> 'float':
        """float: 'RotationSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotationSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self) -> 'GearSingleFlankRating._Cast_GearSingleFlankRating':
        return self._Cast_GearSingleFlankRating(self)
