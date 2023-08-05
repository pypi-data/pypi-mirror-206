"""_952.py

WormGearDesign
"""
from mastapy.gears import _329
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs import _942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Worm', 'WormGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearDesign',)


class WormGearDesign(_942.GearDesign):
    """WormGearDesign

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_DESIGN

    class _Cast_WormGearDesign:
        """Special nested class for casting WormGearDesign to subclasses."""

        def __init__(self, parent: 'WormGearDesign'):
            self._parent = parent

        @property
        def gear_design(self):
            return self._parent._cast(_942.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def worm_design(self):
            from mastapy.gears.gear_designs.worm import _951
            
            return self._parent._cast(_951.WormDesign)

        @property
        def worm_wheel_design(self):
            from mastapy.gears.gear_designs.worm import _955
            
            return self._parent._cast(_955.WormWheelDesign)

        @property
        def worm_gear_design(self) -> 'WormGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self) -> '_329.Hand':
        """Hand: 'Hand' is the original name of this property."""

        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _329.Hand)
        return constructor.new_from_mastapy_type(_329.Hand)(value) if value is not None else None

    @hand.setter
    def hand(self, value: '_329.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _329.Hand.type_())
        self.wrapped.Hand = value

    @property
    def root_diameter(self) -> 'float':
        """float: 'RootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def whole_depth(self) -> 'float':
        """float: 'WholeDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'WormGearDesign._Cast_WormGearDesign':
        return self._Cast_WormGearDesign(self)
