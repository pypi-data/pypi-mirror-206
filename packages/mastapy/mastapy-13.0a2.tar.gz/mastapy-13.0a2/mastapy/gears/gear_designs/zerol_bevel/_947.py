"""_947.py

ZerolBevelGearDesign
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.bevel import _1174
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.ZerolBevel', 'ZerolBevelGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearDesign',)


class ZerolBevelGearDesign(_1174.BevelGearDesign):
    """ZerolBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_DESIGN

    class _Cast_ZerolBevelGearDesign:
        """Special nested class for casting ZerolBevelGearDesign to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearDesign'):
            self._parent = parent

        @property
        def bevel_gear_design(self):
            return self._parent._cast(_1174.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1187
            
            return self._parent._cast(_1187.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1148
            
            return self._parent._cast(_1148.ConicalGearDesign)

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _942
            
            return self._parent._cast(_942.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(self) -> 'ZerolBevelGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_spiral_angle(self) -> 'float':
        """float: 'MeanSpiralAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ZerolBevelGearDesign._Cast_ZerolBevelGearDesign':
        return self._Cast_ZerolBevelGearDesign(self)
