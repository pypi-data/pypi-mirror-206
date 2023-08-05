﻿"""_882.py

ConicalMeshLoadCase
"""
from mastapy.gears.gear_designs.conical import _1144, _1154
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.load_case import _870
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Conical', 'ConicalMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshLoadCase',)


class ConicalMeshLoadCase(_870.MeshLoadCase):
    """ConicalMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_LOAD_CASE

    class _Cast_ConicalMeshLoadCase:
        """Special nested class for casting ConicalMeshLoadCase to subclasses."""

        def __init__(self, parent: 'ConicalMeshLoadCase'):
            self._parent = parent

        @property
        def mesh_load_case(self):
            return self._parent._cast(_870.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def bevel_mesh_load_case(self):
            from mastapy.gears.load_case.bevel import _887
            
            return self._parent._cast(_887.BevelMeshLoadCase)

        @property
        def conical_mesh_load_case(self) -> 'ConicalMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self) -> '_1144.ActiveConicalFlank':
        """ActiveConicalFlank: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1144.ActiveConicalFlank)
        return constructor.new_from_mastapy_type(_1144.ActiveConicalFlank)(value) if value is not None else None

    @property
    def include_mesh_node_misalignments_in_default_report(self) -> 'bool':
        """bool: 'IncludeMeshNodeMisalignmentsInDefaultReport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport

        if temp is None:
            return False

        return temp

    @property
    def use_user_specified_misalignments_in_tca(self) -> 'bool':
        """bool: 'UseUserSpecifiedMisalignmentsInTCA' is the original name of this property."""

        temp = self.wrapped.UseUserSpecifiedMisalignmentsInTCA

        if temp is None:
            return False

        return temp

    @use_user_specified_misalignments_in_tca.setter
    def use_user_specified_misalignments_in_tca(self, value: 'bool'):
        self.wrapped.UseUserSpecifiedMisalignmentsInTCA = bool(value) if value else False

    @property
    def mesh_node_misalignments_pinion(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MeshNodeMisalignmentsPinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshNodeMisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_node_misalignments_total(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MeshNodeMisalignmentsTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshNodeMisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_node_misalignments_wheel(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MeshNodeMisalignmentsWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshNodeMisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_pinion(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsPinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_total(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_wheel(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_pinion(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodePinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodePinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_total(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_wheel(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def user_specified_misalignments(self) -> '_1154.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'UserSpecifiedMisalignments' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserSpecifiedMisalignments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalMeshLoadCase._Cast_ConicalMeshLoadCase':
        return self._Cast_ConicalMeshLoadCase(self)
