"""_1172.py

ConceptGearSetDesign
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.concept import _1170, _1171
from mastapy.gears.gear_designs import _945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Concept', 'ConceptGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetDesign',)


class ConceptGearSetDesign(_945.GearSetDesign):
    """ConceptGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_DESIGN

    class _Cast_ConceptGearSetDesign:
        """Special nested class for casting ConceptGearSetDesign to subclasses."""

        def __init__(self, parent: 'ConceptGearSetDesign'):
            self._parent = parent

        @property
        def gear_set_design(self):
            return self._parent._cast(_945.GearSetDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def concept_gear_set_design(self) -> 'ConceptGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def working_normal_pressure_angle_gear_a_concave_flank(self) -> 'float':
        """float: 'WorkingNormalPressureAngleGearAConcaveFlank' is the original name of this property."""

        temp = self.wrapped.WorkingNormalPressureAngleGearAConcaveFlank

        if temp is None:
            return 0.0

        return temp

    @working_normal_pressure_angle_gear_a_concave_flank.setter
    def working_normal_pressure_angle_gear_a_concave_flank(self, value: 'float'):
        self.wrapped.WorkingNormalPressureAngleGearAConcaveFlank = float(value) if value else 0.0

    @property
    def working_normal_pressure_angle_gear_a_convex_flank(self) -> 'float':
        """float: 'WorkingNormalPressureAngleGearAConvexFlank' is the original name of this property."""

        temp = self.wrapped.WorkingNormalPressureAngleGearAConvexFlank

        if temp is None:
            return 0.0

        return temp

    @working_normal_pressure_angle_gear_a_convex_flank.setter
    def working_normal_pressure_angle_gear_a_convex_flank(self, value: 'float'):
        self.wrapped.WorkingNormalPressureAngleGearAConvexFlank = float(value) if value else 0.0

    @property
    def gears(self) -> 'List[_1170.ConceptGearDesign]':
        """List[ConceptGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears(self) -> 'List[_1170.ConceptGearDesign]':
        """List[ConceptGearDesign]: 'ConceptGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes(self) -> 'List[_1171.ConceptGearMeshDesign]':
        """List[ConceptGearMeshDesign]: 'ConceptMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetDesign._Cast_ConceptGearSetDesign':
        return self._Cast_ConceptGearSetDesign(self)
