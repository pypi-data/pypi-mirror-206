"""_2511.py

GearSet
"""
from typing import List

from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.gears.gear_designs import _945
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2456
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSet',)


class GearSet(_2456.SpecialisedAssembly):
    """GearSet

    This is a mastapy class.
    """

    TYPE = _GEAR_SET

    class _Cast_GearSet:
        """Special nested class for casting GearSet to subclasses."""

        def __init__(self, parent: 'GearSet'):
            self._parent = parent

        @property
        def specialised_assembly(self):
            return self._parent._cast(_2456.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2414
            
            return self._parent._cast(_2414.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def agma_gleason_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2493
            
            return self._parent._cast(_2493.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(self):
            from mastapy.system_model.part_model.gears import _2495
            
            return self._parent._cast(_2495.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2499
            
            return self._parent._cast(_2499.BevelGearSet)

        @property
        def concept_gear_set(self):
            from mastapy.system_model.part_model.gears import _2501
            
            return self._parent._cast(_2501.ConceptGearSet)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2503
            
            return self._parent._cast(_2503.ConicalGearSet)

        @property
        def cylindrical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2505
            
            return self._parent._cast(_2505.CylindricalGearSet)

        @property
        def face_gear_set(self):
            from mastapy.system_model.part_model.gears import _2508
            
            return self._parent._cast(_2508.FaceGearSet)

        @property
        def hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2514
            
            return self._parent._cast(_2514.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2516
            
            return self._parent._cast(_2516.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(self):
            from mastapy.system_model.part_model.gears import _2518
            
            return self._parent._cast(_2518.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2520
            
            return self._parent._cast(_2520.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self):
            from mastapy.system_model.part_model.gears import _2521
            
            return self._parent._cast(_2521.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2523
            
            return self._parent._cast(_2523.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(self):
            from mastapy.system_model.part_model.gears import _2525
            
            return self._parent._cast(_2525.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2527
            
            return self._parent._cast(_2527.StraightBevelGearSet)

        @property
        def worm_gear_set(self):
            from mastapy.system_model.part_model.gears import _2531
            
            return self._parent._cast(_2531.WormGearSet)

        @property
        def zerol_bevel_gear_set(self):
            from mastapy.system_model.part_model.gears import _2533
            
            return self._parent._cast(_2533.ZerolBevelGearSet)

        @property
        def gear_set(self) -> 'GearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_design(self) -> 'list_with_selected_item.ListWithSelectedItem_GearSetDesign':
        """list_with_selected_item.ListWithSelectedItem_GearSetDesign: 'ActiveDesign' is the original name of this property."""

        temp = self.wrapped.ActiveDesign

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_GearSetDesign)(temp) if temp is not None else None

    @active_design.setter
    def active_design(self, value: 'list_with_selected_item.ListWithSelectedItem_GearSetDesign.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_GearSetDesign.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_GearSetDesign.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ActiveDesign = value

    @property
    def maximum_mesh_ratio(self) -> 'float':
        """float: 'MaximumMeshRatio' is the original name of this property."""

        temp = self.wrapped.MaximumMeshRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_mesh_ratio.setter
    def maximum_mesh_ratio(self, value: 'float'):
        self.wrapped.MaximumMeshRatio = float(value) if value else 0.0

    @property
    def maximum_number_of_teeth_in_mesh(self) -> 'int':
        """int: 'MaximumNumberOfTeethInMesh' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfTeethInMesh

        if temp is None:
            return 0

        return temp

    @maximum_number_of_teeth_in_mesh.setter
    def maximum_number_of_teeth_in_mesh(self, value: 'int'):
        self.wrapped.MaximumNumberOfTeethInMesh = int(value) if value else 0

    @property
    def minimum_number_of_teeth_in_mesh(self) -> 'int':
        """int: 'MinimumNumberOfTeethInMesh' is the original name of this property."""

        temp = self.wrapped.MinimumNumberOfTeethInMesh

        if temp is None:
            return 0

        return temp

    @minimum_number_of_teeth_in_mesh.setter
    def minimum_number_of_teeth_in_mesh(self, value: 'int'):
        self.wrapped.MinimumNumberOfTeethInMesh = int(value) if value else 0

    @property
    def required_safety_factor_for_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForBending' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @required_safety_factor_for_bending.setter
    def required_safety_factor_for_bending(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForBending = value

    @property
    def required_safety_factor_for_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForContact' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @required_safety_factor_for_contact.setter
    def required_safety_factor_for_contact(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForContact = value

    @property
    def required_safety_factor_for_static_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForStaticBending' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForStaticBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @required_safety_factor_for_static_bending.setter
    def required_safety_factor_for_static_bending(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForStaticBending = value

    @property
    def required_safety_factor_for_static_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForStaticContact' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForStaticContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @required_safety_factor_for_static_contact.setter
    def required_safety_factor_for_static_contact(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForStaticContact = value

    @property
    def active_gear_set_design(self) -> '_945.GearSetDesign':
        """GearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_designs(self) -> 'List[_945.GearSetDesign]':
        """List[GearSetDesign]: 'GearSetDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_gear_set_design(self, design: '_945.GearSetDesign'):
        """ 'AddGearSetDesign' is the original name of this method.

        Args:
            design (mastapy.gears.gear_designs.GearSetDesign)
        """

        self.wrapped.AddGearSetDesign(design.wrapped if design else None)

    def set_active_gear_set_design(self, gear_set_design: '_945.GearSetDesign'):
        """ 'SetActiveGearSetDesign' is the original name of this method.

        Args:
            gear_set_design (mastapy.gears.gear_designs.GearSetDesign)
        """

        self.wrapped.SetActiveGearSetDesign(gear_set_design.wrapped if gear_set_design else None)

    @property
    def cast_to(self) -> 'GearSet._Cast_GearSet':
        return self._Cast_GearSet(self)
