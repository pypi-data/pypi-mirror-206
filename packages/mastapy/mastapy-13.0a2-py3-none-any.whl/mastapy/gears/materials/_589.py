"""_589.py

GearMaterial
"""
from mastapy._internal import constructor
from mastapy.materials import _277, _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL = python_net_import('SMT.MastaAPI.Gears.Materials', 'GearMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMaterial',)


class GearMaterial(_265.Material):
    """GearMaterial

    This is a mastapy class.
    """

    TYPE = _GEAR_MATERIAL

    class _Cast_GearMaterial:
        """Special nested class for casting GearMaterial to subclasses."""

        def __init__(self, parent: 'GearMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

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
        def iso_cylindrical_gear_material(self):
            from mastapy.gears.materials import _592
            
            return self._parent._cast(_592.ISOCylindricalGearMaterial)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(self):
            from mastapy.gears.materials import _596
            
            return self._parent._cast(_596.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(self):
            from mastapy.gears.materials import _598
            
            return self._parent._cast(_598.PlasticCylindricalGearMaterial)

        @property
        def gear_material(self) -> 'GearMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apply_derating_factors_to_bending_custom_sn_curve(self) -> 'bool':
        """bool: 'ApplyDeratingFactorsToBendingCustomSNCurve' is the original name of this property."""

        temp = self.wrapped.ApplyDeratingFactorsToBendingCustomSNCurve

        if temp is None:
            return False

        return temp

    @apply_derating_factors_to_bending_custom_sn_curve.setter
    def apply_derating_factors_to_bending_custom_sn_curve(self, value: 'bool'):
        self.wrapped.ApplyDeratingFactorsToBendingCustomSNCurve = bool(value) if value else False

    @property
    def apply_derating_factors_to_contact_custom_sn_curve(self) -> 'bool':
        """bool: 'ApplyDeratingFactorsToContactCustomSNCurve' is the original name of this property."""

        temp = self.wrapped.ApplyDeratingFactorsToContactCustomSNCurve

        if temp is None:
            return False

        return temp

    @apply_derating_factors_to_contact_custom_sn_curve.setter
    def apply_derating_factors_to_contact_custom_sn_curve(self, value: 'bool'):
        self.wrapped.ApplyDeratingFactorsToContactCustomSNCurve = bool(value) if value else False

    @property
    def core_hardness(self) -> 'float':
        """float: 'CoreHardness' is the original name of this property."""

        temp = self.wrapped.CoreHardness

        if temp is None:
            return 0.0

        return temp

    @core_hardness.setter
    def core_hardness(self, value: 'float'):
        self.wrapped.CoreHardness = float(value) if value else 0.0

    @property
    def n0_bending(self) -> 'float':
        """float: 'N0Bending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.N0Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def n0_contact(self) -> 'float':
        """float: 'N0Contact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.N0Contact

        if temp is None:
            return 0.0

        return temp

    @property
    def nc_bending(self) -> 'float':
        """float: 'NCBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NCBending

        if temp is None:
            return 0.0

        return temp

    @property
    def nc_contact(self) -> 'float':
        """float: 'NCContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NCContact

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_known_points_for_user_sn_curve_bending_stress(self) -> 'int':
        """int: 'NumberOfKnownPointsForUserSNCurveBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfKnownPointsForUserSNCurveBendingStress

        if temp is None:
            return 0

        return temp

    @property
    def number_of_known_points_for_user_sn_curve_for_contact_stress(self) -> 'int':
        """int: 'NumberOfKnownPointsForUserSNCurveForContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfKnownPointsForUserSNCurveForContactStress

        if temp is None:
            return 0

        return temp

    @property
    def sn_curve_bending(self) -> '_277.SNCurve':
        """SNCurve: 'SNCurveBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SNCurveBending

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def sn_curve_contact(self) -> '_277.SNCurve':
        """SNCurve: 'SNCurveContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SNCurveContact

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMaterial._Cast_GearMaterial':
        return self._Cast_GearMaterial(self)
