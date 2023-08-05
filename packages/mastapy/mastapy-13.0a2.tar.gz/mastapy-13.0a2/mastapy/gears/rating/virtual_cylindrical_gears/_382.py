"""_382.py

KlingelnbergVirtualCylindricalGear
"""
from mastapy._internal import constructor
from mastapy.gears.rating.virtual_cylindrical_gears import _384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'KlingelnbergVirtualCylindricalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergVirtualCylindricalGear',)


class KlingelnbergVirtualCylindricalGear(_384.VirtualCylindricalGear):
    """KlingelnbergVirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR

    class _Cast_KlingelnbergVirtualCylindricalGear:
        """Special nested class for casting KlingelnbergVirtualCylindricalGear to subclasses."""

        def __init__(self, parent: 'KlingelnbergVirtualCylindricalGear'):
            self._parent = parent

        @property
        def virtual_cylindrical_gear(self):
            return self._parent._cast(_384.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_basic(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _385
            
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
        def klingelnberg_virtual_cylindrical_gear(self) -> 'KlingelnbergVirtualCylindricalGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergVirtualCylindricalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_face_width(self) -> 'float':
        """float: 'EffectiveFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def face_contact_ratio_transverse_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'FaceContactRatioTransverseForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceContactRatioTransverseForVirtualCylindricalGears

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
    def outside_diameter_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'OutsideDiameterOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OutsideDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_number_of_teeth_normal(self) -> 'float':
        """float: 'VirtualNumberOfTeethNormal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualNumberOfTeethNormal

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_number_of_teeth_transverse(self) -> 'float':
        """float: 'VirtualNumberOfTeethTransverse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualNumberOfTeethTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'KlingelnbergVirtualCylindricalGear._Cast_KlingelnbergVirtualCylindricalGear':
        return self._Cast_KlingelnbergVirtualCylindricalGear(self)
