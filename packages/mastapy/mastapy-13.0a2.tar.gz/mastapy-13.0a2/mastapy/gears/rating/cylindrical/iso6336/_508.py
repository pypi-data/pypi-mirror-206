"""_508.py

ISO63362006GearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _503, _514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63362006_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO63362006GearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO63362006GearSingleFlankRating',)


class ISO63362006GearSingleFlankRating(_514.ISO6336AbstractMetalGearSingleFlankRating):
    """ISO63362006GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63362006_GEAR_SINGLE_FLANK_RATING

    class _Cast_ISO63362006GearSingleFlankRating:
        """Special nested class for casting ISO63362006GearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO63362006GearSingleFlankRating'):
            self._parent = parent

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(self):
            return self._parent._cast(_514.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _512
            
            return self._parent._cast(_512.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _461
            
            return self._parent._cast(_461.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _360
            
            return self._parent._cast(_360.GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _510
            
            return self._parent._cast(_510.ISO63362019GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(self) -> 'ISO63362006GearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO63362006GearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def nominal_tooth_root_stress(self) -> 'float':
        """float: 'NominalToothRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_factor(self) -> 'float':
        """float: 'RimThicknessFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_over_whole_depth(self) -> 'float':
        """float: 'RimThicknessOverWholeDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessOverWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def work_hardening_factor_for_reference_contact_stress(self) -> 'float':
        """float: 'WorkHardeningFactorForReferenceContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkHardeningFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def work_hardening_factor_for_static_contact_stress(self) -> 'float':
        """float: 'WorkHardeningFactorForStaticContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkHardeningFactorForStaticContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_fatigue_fracture_results(self) -> '_503.CylindricalGearToothFatigueFractureResults':
        """CylindricalGearToothFatigueFractureResults: 'ToothFatigueFractureResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothFatigueFractureResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating':
        return self._Cast_ISO63362006GearSingleFlankRating(self)
