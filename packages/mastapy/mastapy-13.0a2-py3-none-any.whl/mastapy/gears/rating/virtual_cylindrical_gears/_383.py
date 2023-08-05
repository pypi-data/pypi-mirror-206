"""_383.py

KlingelnbergVirtualCylindricalGearSet
"""
from mastapy._internal import constructor
from mastapy.gears.rating.virtual_cylindrical_gears import _388, _382
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR_SET = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'KlingelnbergVirtualCylindricalGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergVirtualCylindricalGearSet',)


class KlingelnbergVirtualCylindricalGearSet(_388.VirtualCylindricalGearSet['_382.KlingelnbergVirtualCylindricalGear']):
    """KlingelnbergVirtualCylindricalGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_VIRTUAL_CYLINDRICAL_GEAR_SET

    class _Cast_KlingelnbergVirtualCylindricalGearSet:
        """Special nested class for casting KlingelnbergVirtualCylindricalGearSet to subclasses."""

        def __init__(self, parent: 'KlingelnbergVirtualCylindricalGearSet'):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_set(self):
            return self._parent._cast(_388.VirtualCylindricalGearSet)

        @property
        def klingelnberg_virtual_cylindrical_gear_set(self) -> 'KlingelnbergVirtualCylindricalGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergVirtualCylindricalGearSet.TYPE'):
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
    def length_of_path_of_contact_of_virtual_cylindrical_gear_in_transverse_section(self) -> 'float':
        """float: 'LengthOfPathOfContactOfVirtualCylindricalGearInTransverseSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfPathOfContactOfVirtualCylindricalGearInTransverseSection

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_ratio_transverse_for_virtual_cylindrical_gears(self) -> 'float':
        """float: 'TotalContactRatioTransverseForVirtualCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalContactRatioTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_transmission_ratio(self) -> 'float':
        """float: 'VirtualTransmissionRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualTransmissionRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'KlingelnbergVirtualCylindricalGearSet._Cast_KlingelnbergVirtualCylindricalGearSet':
        return self._Cast_KlingelnbergVirtualCylindricalGearSet(self)
