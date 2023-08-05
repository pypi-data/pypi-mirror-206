"""_949.py

ZerolBevelGearSetDesign
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _348
from mastapy.gears.gear_designs.zerol_bevel import _947, _948
from mastapy.gears.gear_designs.bevel import _1176
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.ZerolBevel', 'ZerolBevelGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetDesign',)


class ZerolBevelGearSetDesign(_1176.BevelGearSetDesign):
    """ZerolBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_DESIGN

    class _Cast_ZerolBevelGearSetDesign:
        """Special nested class for casting ZerolBevelGearSetDesign to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSetDesign'):
            self._parent = parent

        @property
        def bevel_gear_set_design(self):
            return self._parent._cast(_1176.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1189
            
            return self._parent._cast(_1189.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(self):
            from mastapy.gears.gear_designs.conical import _1150
            
            return self._parent._cast(_1150.ConicalGearSetDesign)

        @property
        def gear_set_design(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearSetDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(self) -> 'ZerolBevelGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(self) -> 'int':
        """int: 'MinimumNumberOfTeethForRecommendedToothProportions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions

        if temp is None:
            return 0

        return temp

    @property
    def tooth_taper_zerol(self) -> '_348.ZerolBevelGleasonToothTaperOption':
        """ZerolBevelGleasonToothTaperOption: 'ToothTaperZerol' is the original name of this property."""

        temp = self.wrapped.ToothTaperZerol

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _348.ZerolBevelGleasonToothTaperOption)
        return constructor.new_from_mastapy_type(_348.ZerolBevelGleasonToothTaperOption)(value) if value is not None else None

    @tooth_taper_zerol.setter
    def tooth_taper_zerol(self, value: '_348.ZerolBevelGleasonToothTaperOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _348.ZerolBevelGleasonToothTaperOption.type_())
        self.wrapped.ToothTaperZerol = value

    @property
    def gears(self) -> 'List[_947.ZerolBevelGearDesign]':
        """List[ZerolBevelGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gears(self) -> 'List[_947.ZerolBevelGearDesign]':
        """List[ZerolBevelGearDesign]: 'ZerolBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes(self) -> 'List[_948.ZerolBevelGearMeshDesign]':
        """List[ZerolBevelGearMeshDesign]: 'ZerolBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign':
        return self._Cast_ZerolBevelGearSetDesign(self)
