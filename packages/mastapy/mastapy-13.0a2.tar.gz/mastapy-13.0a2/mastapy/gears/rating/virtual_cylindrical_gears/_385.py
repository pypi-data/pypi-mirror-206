"""_385.py

VirtualCylindricalGearBasic
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_BASIC = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'VirtualCylindricalGearBasic')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualCylindricalGearBasic',)


class VirtualCylindricalGearBasic(_0.APIBase):
    """VirtualCylindricalGearBasic

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_BASIC

    class _Cast_VirtualCylindricalGearBasic:
        """Special nested class for casting VirtualCylindricalGearBasic to subclasses."""

        def __init__(self, parent: 'VirtualCylindricalGearBasic'):
            self._parent = parent

        @property
        def bevel_virtual_cylindrical_gear_iso10300_method_b2(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _374
            
            return self._parent._cast(_374.BevelVirtualCylindricalGearISO10300MethodB2)

        @property
        def hypoid_virtual_cylindrical_gear_iso10300_method_b2(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _377
            
            return self._parent._cast(_377.HypoidVirtualCylindricalGearISO10300MethodB2)

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
        def virtual_cylindrical_gear(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _384
            
            return self._parent._cast(_384.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_iso10300_method_b1(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _386
            
            return self._parent._cast(_386.VirtualCylindricalGearISO10300MethodB1)

        @property
        def virtual_cylindrical_gear_iso10300_method_b2(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _387
            
            return self._parent._cast(_387.VirtualCylindricalGearISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_basic(self) -> 'VirtualCylindricalGearBasic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualCylindricalGearBasic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle_at_base_circle_of_virtual_cylindrical_gears(self) -> 'float':
        """float: 'HelixAngleAtBaseCircleOfVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleAtBaseCircleOfVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle_of_virtual_cylindrical_gears(self) -> 'float':
        """float: 'HelixAngleOfVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleOfVirtualCylindricalGears

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
    def normal_module(self) -> 'float':
        """float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'ReferenceDiameterOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'TipDiameterOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_radius_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'TipRadiusOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipRadiusOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'VirtualCylindricalGearBasic._Cast_VirtualCylindricalGearBasic':
        return self._Cast_VirtualCylindricalGearBasic(self)
