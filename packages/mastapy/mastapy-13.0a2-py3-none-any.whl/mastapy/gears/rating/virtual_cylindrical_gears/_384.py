"""_384.py

VirtualCylindricalGear
"""
from mastapy._internal import constructor
from mastapy.gears.rating.virtual_cylindrical_gears import _385
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'VirtualCylindricalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualCylindricalGear',)


class VirtualCylindricalGear(_385.VirtualCylindricalGearBasic):
    """VirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR

    class _Cast_VirtualCylindricalGear:
        """Special nested class for casting VirtualCylindricalGear to subclasses."""

        def __init__(self, parent: 'VirtualCylindricalGear'):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_basic(self):
            return self._parent._cast(_385.VirtualCylindricalGearBasic)

        @property
        def klingelnberg_hypoid_virtual_cylindrical_gear(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _380
            
            return self._parent._cast(_380.KlingelnbergHypoidVirtualCylindricalGear)

        @property
        def klingelnberg_spiral_bevel_virtual_cylindrical_gear(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _381
            
            return self._parent._cast(_381.KlingelnbergSpiralBevelVirtualCylindricalGear)

        @property
        def klingelnberg_virtual_cylindrical_gear(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _382
            
            return self._parent._cast(_382.KlingelnbergVirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_iso10300_method_b1(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _386
            
            return self._parent._cast(_386.VirtualCylindricalGearISO10300MethodB1)

        @property
        def virtual_cylindrical_gear(self) -> 'VirtualCylindricalGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualCylindricalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'BaseDiameterOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_normal_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'BasePitchNormalForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasePitchNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def base_pitch_transverse_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'BasePitchTransverseForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasePitchTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_of_addendum_normal_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'ContactRatioOfAddendumNormalForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRatioOfAddendumNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_of_addendum_transverse_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'ContactRatioOfAddendumTransverseForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRatioOfAddendumTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_pressure_angle(self) -> 'float':
        """float: 'EffectivePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectivePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def path_of_addendum_contact_normal(self) -> 'float':
        """float: 'PathOfAddendumContactNormal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PathOfAddendumContactNormal

        if temp is None:
            return 0.0

        return temp

    @property
    def path_of_addendum_contact_transverse(self) -> 'float':
        """float: 'PathOfAddendumContactTransverse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PathOfAddendumContactTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self) -> 'float':
        """float: 'TransversePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'VirtualCylindricalGear._Cast_VirtualCylindricalGear':
        return self._Cast_VirtualCylindricalGear(self)
