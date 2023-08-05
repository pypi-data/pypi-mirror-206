"""_1197.py

CylindricalGearSetFEModel
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1026
from mastapy.gears.fe_model import _1194
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel.Cylindrical', 'CylindricalGearSetFEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetFEModel',)


class CylindricalGearSetFEModel(_1194.GearSetFEModel):
    """CylindricalGearSetFEModel

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_FE_MODEL

    class _Cast_CylindricalGearSetFEModel:
        """Special nested class for casting CylindricalGearSetFEModel to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetFEModel'):
            self._parent = parent

        @property
        def gear_set_fe_model(self):
            return self._parent._cast(_1194.GearSetFEModel)

        @property
        def gear_set_implementation_detail(self):
            from mastapy.gears.analysis import _1225
            
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
        def cylindrical_gear_set_fe_model(self) -> 'CylindricalGearSetFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def remove_local_compressive_stress_due_to_applied_point_load_from_root_stress(self) -> 'bool':
        """bool: 'RemoveLocalCompressiveStressDueToAppliedPointLoadFromRootStress' is the original name of this property."""

        temp = self.wrapped.RemoveLocalCompressiveStressDueToAppliedPointLoadFromRootStress

        if temp is None:
            return False

        return temp

    @remove_local_compressive_stress_due_to_applied_point_load_from_root_stress.setter
    def remove_local_compressive_stress_due_to_applied_point_load_from_root_stress(self, value: 'bool'):
        self.wrapped.RemoveLocalCompressiveStressDueToAppliedPointLoadFromRootStress = bool(value) if value else False

    @property
    def use_manufactured_profile_shape(self) -> 'bool':
        """bool: 'UseManufacturedProfileShape' is the original name of this property."""

        temp = self.wrapped.UseManufacturedProfileShape

        if temp is None:
            return False

        return temp

    @use_manufactured_profile_shape.setter
    def use_manufactured_profile_shape(self, value: 'bool'):
        self.wrapped.UseManufacturedProfileShape = bool(value) if value else False

    @property
    def manufacturing_configuration_selection(self) -> '_1026.CylindricalGearSetManufacturingConfigurationSelection':
        """CylindricalGearSetManufacturingConfigurationSelection: 'ManufacturingConfigurationSelection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingConfigurationSelection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel':
        return self._Cast_CylindricalGearSetFEModel(self)
