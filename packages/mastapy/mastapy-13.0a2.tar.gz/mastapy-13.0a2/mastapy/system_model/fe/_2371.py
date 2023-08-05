﻿"""_2371.py

FESubstructureWithSelectionComponents
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.math_utility import _1488
from mastapy.system_model.fe import (
    _2357, _2348, _2349, _2379,
    _2370
)
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
    _206, _207, _208, _205,
    _209, _210, _211, _212
)
from mastapy.system_model.fe.links import _2400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION_COMPONENTS = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FESubstructureWithSelectionComponents')


__docformat__ = 'restructuredtext en'
__all__ = ('FESubstructureWithSelectionComponents',)


class FESubstructureWithSelectionComponents(_2370.FESubstructureWithSelection):
    """FESubstructureWithSelectionComponents

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION_COMPONENTS

    class _Cast_FESubstructureWithSelectionComponents:
        """Special nested class for casting FESubstructureWithSelectionComponents to subclasses."""

        def __init__(self, parent: 'FESubstructureWithSelectionComponents'):
            self._parent = parent

        @property
        def fe_substructure_with_selection(self):
            return self._parent._cast(_2370.FESubstructureWithSelection)

        @property
        def base_fe_with_selection(self):
            from mastapy.system_model.fe import _2341
            
            return self._parent._cast(_2341.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_components(self) -> 'FESubstructureWithSelectionComponents':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FESubstructureWithSelectionComponents.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def radius_of_circle_through_selected_nodes(self) -> 'float':
        """float: 'RadiusOfCircleThroughSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusOfCircleThroughSelectedNodes

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_of_circle_through_selected_nodes(self) -> 'Vector3D':
        """Vector3D: 'CentreOfCircleThroughSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentreOfCircleThroughSelectedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def distance_between_selected_nodes(self) -> 'Vector3D':
        """Vector3D: 'DistanceBetweenSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceBetweenSelectedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def manual_alignment(self) -> '_1488.CoordinateSystemEditor':
        """CoordinateSystemEditor: 'ManualAlignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManualAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def midpoint_of_selected_nodes(self) -> 'Vector3D':
        """Vector3D: 'MidpointOfSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MidpointOfSelectedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def beam_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_206.ElementPropertiesBeam]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesBeam]]: 'BeamElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeamElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_links(self) -> 'List[_2400.FELinkWithSelection]':
        """List[FELinkWithSelection]: 'ComponentLinks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLinks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def contact_pairs(self) -> 'List[_2348.ContactPairWithSelection]':
        """List[ContactPairWithSelection]: 'ContactPairs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactPairs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def coordinate_systems(self) -> 'List[_2349.CoordinateSystemWithSelection]':
        """List[CoordinateSystemWithSelection]: 'CoordinateSystems' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoordinateSystems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def interface_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_207.ElementPropertiesInterface]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesInterface]]: 'InterfaceElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InterfaceElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def links_for_electric_machine(self) -> 'List[_2400.FELinkWithSelection]':
        """List[FELinkWithSelection]: 'LinksForElectricMachine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinksForElectricMachine

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def links_for_selected_component(self) -> 'List[_2400.FELinkWithSelection]':
        """List[FELinkWithSelection]: 'LinksForSelectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinksForSelectedComponent

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_208.ElementPropertiesMass]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesMass]]: 'MassElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def materials(self) -> 'List[_2379.MaterialPropertiesWithSelection]':
        """List[MaterialPropertiesWithSelection]: 'Materials' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Materials

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def other_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_205.ElementPropertiesBase]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesBase]]: 'OtherElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OtherElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rigid_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_209.ElementPropertiesRigid]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesRigid]]: 'RigidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RigidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shell_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_210.ElementPropertiesShell]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesShell]]: 'ShellElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShellElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def solid_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_211.ElementPropertiesSolid]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesSolid]]: 'SolidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SolidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dashpot_element_properties(self) -> 'List[_2357.ElementPropertiesWithSelection[_212.ElementPropertiesSpringDashpot]]':
        """List[ElementPropertiesWithSelection[ElementPropertiesSpringDashpot]]: 'SpringDashpotElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDashpotElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def auto_select_node_ring(self):
        """ 'AutoSelectNodeRing' is the original name of this method."""

        self.wrapped.AutoSelectNodeRing()

    def replace_selected_shaft(self):
        """ 'ReplaceSelectedShaft' is the original name of this method."""

        self.wrapped.ReplaceSelectedShaft()

    def use_selected_component_for_alignment(self):
        """ 'UseSelectedComponentForAlignment' is the original name of this method."""

        self.wrapped.UseSelectedComponentForAlignment()

    @property
    def cast_to(self) -> 'FESubstructureWithSelectionComponents._Cast_FESubstructureWithSelectionComponents':
        return self._Cast_FESubstructureWithSelectionComponents(self)
