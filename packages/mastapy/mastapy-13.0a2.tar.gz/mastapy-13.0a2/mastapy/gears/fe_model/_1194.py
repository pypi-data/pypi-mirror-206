"""_1194.py

GearSetFEModel
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.nodal_analysis import _58
from mastapy.gears.fe_model import _1191, _1192
from mastapy import _7521
from mastapy._internal.python_net import python_net_import
from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_GEAR_SET_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel', 'GearSetFEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetFEModel',)


class GearSetFEModel(_1225.GearSetImplementationDetail):
    """GearSetFEModel

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_FE_MODEL

    class _Cast_GearSetFEModel:
        """Special nested class for casting GearSetFEModel to subclasses."""

        def __init__(self, parent: 'GearSetFEModel'):
            self._parent = parent

        @property
        def gear_set_implementation_detail(self):
            return self._parent._cast(_1225.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1197
            
            return self._parent._cast(_1197.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(self):
            from mastapy.gears.fe_model.conical import _1200
            
            return self._parent._cast(_1200.ConicalSetFEModel)

        @property
        def gear_set_fe_model(self) -> 'GearSetFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self) -> 'str':
        """str: 'Comment' is the original name of this property."""

        temp = self.wrapped.Comment

        if temp is None:
            return ''

        return temp

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else ''

    @property
    def element_order(self) -> '_58.ElementOrder':
        """ElementOrder: 'ElementOrder' is the original name of this property."""

        temp = self.wrapped.ElementOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _58.ElementOrder)
        return constructor.new_from_mastapy_type(_58.ElementOrder)(value) if value is not None else None

    @element_order.setter
    def element_order(self, value: '_58.ElementOrder'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _58.ElementOrder.type_())
        self.wrapped.ElementOrder = value

    @property
    def number_of_coupled_teeth_either_side(self) -> 'int':
        """int: 'NumberOfCoupledTeethEitherSide' is the original name of this property."""

        temp = self.wrapped.NumberOfCoupledTeethEitherSide

        if temp is None:
            return 0

        return temp

    @number_of_coupled_teeth_either_side.setter
    def number_of_coupled_teeth_either_side(self, value: 'int'):
        self.wrapped.NumberOfCoupledTeethEitherSide = int(value) if value else 0

    @property
    def gear_fe_models(self) -> 'List[_1191.GearFEModel]':
        """List[GearFEModel]: 'GearFEModels' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearFEModels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mesh_fe_models(self) -> 'List[_1192.GearMeshFEModel]':
        """List[GearMeshFEModel]: 'MeshFEModels' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshFEModels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def is_ready_for_altca(self) -> 'bool':
        """bool: 'IsReadyForALTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsReadyForALTCA

        if temp is None:
            return False

        return temp

    def generate_stiffness_from_fe(self):
        """ 'GenerateStiffnessFromFE' is the original name of this method."""

        self.wrapped.GenerateStiffnessFromFE()

    def generate_stress_influence_coefficients_from_fe(self):
        """ 'GenerateStressInfluenceCoefficientsFromFE' is the original name of this method."""

        self.wrapped.GenerateStressInfluenceCoefficientsFromFE()

    def calculate_stiffness_from_fe(self):
        """ 'CalculateStiffnessFromFE' is the original name of this method."""

        self.wrapped.CalculateStiffnessFromFE()

    def calculate_stiffness_from_fe_with_progress(self, progress: '_7521.TaskProgress'):
        """ 'CalculateStiffnessFromFE' is the original name of this method.

        Args:
            progress (mastapy.TaskProgress)
        """

        self.wrapped.CalculateStiffnessFromFE.Overloads[_TASK_PROGRESS](progress.wrapped if progress else None)

    @property
    def cast_to(self) -> 'GearSetFEModel._Cast_GearSetFEModel':
        return self._Cast_GearSetFEModel(self)
