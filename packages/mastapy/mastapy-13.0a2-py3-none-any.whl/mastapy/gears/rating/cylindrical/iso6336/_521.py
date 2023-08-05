"""_521.py

ToothFlankFractureAnalysisContactPointMethodA
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _520
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_METHOD_A = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ToothFlankFractureAnalysisContactPointMethodA')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothFlankFractureAnalysisContactPointMethodA',)


class ToothFlankFractureAnalysisContactPointMethodA(_520.ToothFlankFractureAnalysisContactPointCommon):
    """ToothFlankFractureAnalysisContactPointMethodA

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_METHOD_A

    class _Cast_ToothFlankFractureAnalysisContactPointMethodA:
        """Special nested class for casting ToothFlankFractureAnalysisContactPointMethodA to subclasses."""

        def __init__(self, parent: 'ToothFlankFractureAnalysisContactPointMethodA'):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_contact_point_common(self):
            return self._parent._cast(_520.ToothFlankFractureAnalysisContactPointCommon)

        @property
        def tooth_flank_fracture_analysis_contact_point_method_a(self) -> 'ToothFlankFractureAnalysisContactPointMethodA':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ToothFlankFractureAnalysisContactPointMethodA.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def half_of_hertzian_contact_width(self) -> 'float':
        """float: 'HalfOfHertzianContactWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfOfHertzianContactWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_stress(self) -> 'float':
        """float: 'HertzianContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def local_normal_radius_of_relative_curvature(self) -> 'float':
        """float: 'LocalNormalRadiusOfRelativeCurvature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocalNormalRadiusOfRelativeCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ToothFlankFractureAnalysisContactPointMethodA._Cast_ToothFlankFractureAnalysisContactPointMethodA':
        return self._Cast_ToothFlankFractureAnalysisContactPointMethodA(self)
