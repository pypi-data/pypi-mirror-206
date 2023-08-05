"""_386.py

VirtualCylindricalGearISO10300MethodB1
"""
from mastapy._internal import constructor
from mastapy.gears.rating.virtual_cylindrical_gears import _384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B1 = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'VirtualCylindricalGearISO10300MethodB1')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualCylindricalGearISO10300MethodB1',)


class VirtualCylindricalGearISO10300MethodB1(_384.VirtualCylindricalGear):
    """VirtualCylindricalGearISO10300MethodB1

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B1

    class _Cast_VirtualCylindricalGearISO10300MethodB1:
        """Special nested class for casting VirtualCylindricalGearISO10300MethodB1 to subclasses."""

        def __init__(self, parent: 'VirtualCylindricalGearISO10300MethodB1'):
            self._parent = parent

        @property
        def virtual_cylindrical_gear(self):
            return self._parent._cast(_384.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_basic(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _385
            
            return self._parent._cast(_385.VirtualCylindricalGearBasic)

        @property
        def virtual_cylindrical_gear_iso10300_method_b1(self) -> 'VirtualCylindricalGearISO10300MethodB1':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualCylindricalGearISO10300MethodB1.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter_of_virtual_cylindrical_gear_in_normal_section(self) -> 'float':
        """float: 'BaseDiameterOfVirtualCylindricalGearInNormalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameterOfVirtualCylindricalGearInNormalSection

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
    def reference_diameter_in_normal_section(self) -> 'float':
        """float: 'ReferenceDiameterInNormalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameterInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def root_diameter_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'RootDiameterOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootDiameterOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter_of_virtual_cylindrical_gear_in_normal_section(self) -> 'float':
        """float: 'TipDiameterOfVirtualCylindricalGearInNormalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipDiameterOfVirtualCylindricalGearInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_module(self) -> 'float':
        """float: 'TransverseModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseModule

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
    def virtual_spur_gear_number_of_teeth(self) -> 'float':
        """float: 'VirtualSpurGearNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualSpurGearNumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'VirtualCylindricalGearISO10300MethodB1._Cast_VirtualCylindricalGearISO10300MethodB1':
        return self._Cast_VirtualCylindricalGearISO10300MethodB1(self)
