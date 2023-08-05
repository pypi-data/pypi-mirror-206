"""_1150.py

ConicalGearSetDesign
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.conical import _1149
from mastapy.gears.gear_designs import _945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'ConicalGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetDesign',)


class ConicalGearSetDesign(_945.GearSetDesign):
    """ConicalGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_DESIGN

    class _Cast_ConicalGearSetDesign:
        """Special nested class for casting ConicalGearSetDesign to subclasses."""

        def __init__(self, parent: 'ConicalGearSetDesign'):
            self._parent = parent

        @property
        def gear_set_design(self):
            return self._parent._cast(_945.GearSetDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _949
            
            return self._parent._cast(_949.ZerolBevelGearSetDesign)

        @property
        def straight_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _958
            
            return self._parent._cast(_958.StraightBevelGearSetDesign)

        @property
        def straight_bevel_diff_gear_set_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _962
            
            return self._parent._cast(_962.StraightBevelDiffGearSetDesign)

        @property
        def spiral_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _966
            
            return self._parent._cast(_966.SpiralBevelGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _970
            
            return self._parent._cast(_970.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _974
            
            return self._parent._cast(_974.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _978
            
            return self._parent._cast(_978.KlingelnbergConicalGearSetDesign)

        @property
        def hypoid_gear_set_design(self):
            from mastapy.gears.gear_designs.hypoid import _982
            
            return self._parent._cast(_982.HypoidGearSetDesign)

        @property
        def bevel_gear_set_design(self):
            from mastapy.gears.gear_designs.bevel import _1176
            
            return self._parent._cast(_1176.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1189
            
            return self._parent._cast(_1189.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(self) -> 'ConicalGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def circular_pitch(self) -> 'float':
        """float: 'CircularPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_radius(self) -> 'float':
        """float: 'CutterRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def dominant_pinion(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'DominantPinion' is the original name of this property."""

        temp = self.wrapped.DominantPinion

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @dominant_pinion.setter
    def dominant_pinion(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.DominantPinion = value

    @property
    def imported_xml_file_name(self) -> 'str':
        """str: 'ImportedXMLFileName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImportedXMLFileName

        if temp is None:
            return ''

        return temp

    @property
    def mean_normal_module(self) -> 'float':
        """float: 'MeanNormalModule' is the original name of this property."""

        temp = self.wrapped.MeanNormalModule

        if temp is None:
            return 0.0

        return temp

    @mean_normal_module.setter
    def mean_normal_module(self, value: 'float'):
        self.wrapped.MeanNormalModule = float(value) if value else 0.0

    @property
    def module(self) -> 'float':
        """float: 'Module' is the original name of this property."""

        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    def module(self, value: 'float'):
        self.wrapped.Module = float(value) if value else 0.0

    @property
    def wheel_finish_cutter_point_width(self) -> 'float':
        """float: 'WheelFinishCutterPointWidth' is the original name of this property."""

        temp = self.wrapped.WheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_finish_cutter_point_width.setter
    def wheel_finish_cutter_point_width(self, value: 'float'):
        self.wrapped.WheelFinishCutterPointWidth = float(value) if value else 0.0

    @property
    def wheel_mean_cone_distance(self) -> 'float':
        """float: 'WheelMeanConeDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelMeanConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_cone_distance(self) -> 'float':
        """float: 'WheelOuterConeDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelOuterConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_pitch_diameter(self) -> 'float':
        """float: 'WheelPitchDiameter' is the original name of this property."""

        temp = self.wrapped.WheelPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @wheel_pitch_diameter.setter
    def wheel_pitch_diameter(self, value: 'float'):
        self.wrapped.WheelPitchDiameter = float(value) if value else 0.0

    @property
    def conical_meshes(self) -> 'List[_1149.ConicalGearMeshDesign]':
        """List[ConicalGearMeshDesign]: 'ConicalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearSetDesign._Cast_ConicalGearSetDesign':
        return self._Cast_ConicalGearSetDesign(self)
