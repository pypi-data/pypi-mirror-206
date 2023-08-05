"""_2454.py

RootAssembly
"""
from typing import List

from mastapy.system_model import _2185
from mastapy._internal import constructor, conversion
from mastapy.geometry import _305
from mastapy.system_model.part_model.part_groups import _2470
from mastapy.system_model.part_model.projections import _2465
from mastapy.system_model.part_model import _2413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'RootAssembly')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssembly',)


class RootAssembly(_2413.Assembly):
    """RootAssembly

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY

    class _Cast_RootAssembly:
        """Special nested class for casting RootAssembly to subclasses."""

        def __init__(self, parent: 'RootAssembly'):
            self._parent = parent

        @property
        def assembly(self):
            return self._parent._cast(_2413.Assembly)

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
        def root_assembly(self) -> 'RootAssembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def model(self) -> '_2185.Design':
        """Design: 'Model' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Model

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def packaging_limits(self) -> '_305.PackagingLimits':
        """PackagingLimits: 'PackagingLimits' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PackagingLimits

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parallel_part_groups(self) -> 'List[_2470.ParallelPartGroup]':
        """List[ParallelPartGroup]: 'ParallelPartGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParallelPartGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def parallel_part_groups_drawing_order(self) -> 'List[_2465.SpecifiedParallelPartGroupDrawingOrder]':
        """List[SpecifiedParallelPartGroupDrawingOrder]: 'ParallelPartGroupsDrawingOrder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParallelPartGroupsDrawingOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def attempt_to_fix_all_cylindrical_gear_sets_by_changing_normal_module(self):
        """ 'AttemptToFixAllCylindricalGearSetsByChangingNormalModule' is the original name of this method."""

        self.wrapped.AttemptToFixAllCylindricalGearSetsByChangingNormalModule()

    def attempt_to_fix_all_gear_sets(self):
        """ 'AttemptToFixAllGearSets' is the original name of this method."""

        self.wrapped.AttemptToFixAllGearSets()

    def open_fe_substructure_version_comparer(self):
        """ 'OpenFESubstructureVersionComparer' is the original name of this method."""

        self.wrapped.OpenFESubstructureVersionComparer()

    def set_packaging_limits_to_current_bounding_box(self):
        """ 'SetPackagingLimitsToCurrentBoundingBox' is the original name of this method."""

        self.wrapped.SetPackagingLimitsToCurrentBoundingBox()

    def set_packaging_limits_to_current_bounding_box_of_all_gears(self):
        """ 'SetPackagingLimitsToCurrentBoundingBoxOfAllGears' is the original name of this method."""

        self.wrapped.SetPackagingLimitsToCurrentBoundingBoxOfAllGears()

    @property
    def cast_to(self) -> 'RootAssembly._Cast_RootAssembly':
        return self._Cast_RootAssembly(self)
