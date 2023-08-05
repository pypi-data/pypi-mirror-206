"""_377.py

HypoidVirtualCylindricalGearISO10300MethodB2
"""
from mastapy._internal import constructor
from mastapy.gears.rating.virtual_cylindrical_gears import _387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B2 = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'HypoidVirtualCylindricalGearISO10300MethodB2')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidVirtualCylindricalGearISO10300MethodB2',)


class HypoidVirtualCylindricalGearISO10300MethodB2(_387.VirtualCylindricalGearISO10300MethodB2):
    """HypoidVirtualCylindricalGearISO10300MethodB2

    This is a mastapy class.
    """

    TYPE = _HYPOID_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B2

    class _Cast_HypoidVirtualCylindricalGearISO10300MethodB2:
        """Special nested class for casting HypoidVirtualCylindricalGearISO10300MethodB2 to subclasses."""

        def __init__(self, parent: 'HypoidVirtualCylindricalGearISO10300MethodB2'):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_iso10300_method_b2(self):
            return self._parent._cast(_387.VirtualCylindricalGearISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_basic(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _385
            
            return self._parent._cast(_385.VirtualCylindricalGearBasic)

        @property
        def hypoid_virtual_cylindrical_gear_iso10300_method_b2(self) -> 'HypoidVirtualCylindricalGearISO10300MethodB2':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidVirtualCylindricalGearISO10300MethodB2.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'HypoidVirtualCylindricalGearISO10300MethodB2._Cast_HypoidVirtualCylindricalGearISO10300MethodB2':
        return self._Cast_HypoidVirtualCylindricalGearISO10300MethodB2(self)
