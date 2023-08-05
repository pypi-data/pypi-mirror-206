"""_456.py

CylindricalGearRating
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1007
from mastapy.gears.rating import _355, _357
from mastapy.gears.rating.cylindrical import _483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearRating',)


class CylindricalGearRating(_357.GearRating):
    """CylindricalGearRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_RATING

    class _Cast_CylindricalGearRating:
        """Special nested class for casting CylindricalGearRating to subclasses."""

        def __init__(self, parent: 'CylindricalGearRating'):
            self._parent = parent

        @property
        def gear_rating(self):
            return self._parent._cast(_357.GearRating)

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _350
            
            return self._parent._cast(_350.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_rating(self) -> 'CylindricalGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage_bending(self) -> 'float':
        """float: 'DamageBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self) -> 'float':
        """float: 'DamageContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_crack_initiation_safety_factor_with_influence_of_rim(self) -> 'float':
        """float: 'WorstCrackInitiationSafetyFactorWithInfluenceOfRim' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstCrackInitiationSafetyFactorWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_fatigue_fracture_safety_factor_with_influence_of_rim(self) -> 'float':
        """float: 'WorstFatigueFractureSafetyFactorWithInfluenceOfRim' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstFatigueFractureSafetyFactorWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_permanent_deformation_safety_factor_with_influence_of_rim(self) -> 'float':
        """float: 'WorstPermanentDeformationSafetyFactorWithInfluenceOfRim' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstPermanentDeformationSafetyFactorWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def cylindrical_gear(self) -> '_1007.CylindricalGearDesign':
        """CylindricalGearDesign: 'CylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_rating(self) -> '_355.GearFlankRating':
        """GearFlankRating: 'LeftFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_rating(self) -> '_355.GearFlankRating':
        """GearFlankRating: 'RightFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def vdi2737_safety_factor(self) -> '_483.VDI2737SafetyFactorReportingObject':
        """VDI2737SafetyFactorReportingObject: 'VDI2737SafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VDI2737SafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearRating._Cast_CylindricalGearRating':
        return self._Cast_CylindricalGearRating(self)
