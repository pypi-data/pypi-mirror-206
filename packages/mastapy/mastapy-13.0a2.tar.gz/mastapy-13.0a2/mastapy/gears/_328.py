"""_328.py

GearSetOptimiser
"""
from typing import Optional

from mastapy._internal import constructor
from mastapy import _7521, _0
from mastapy.gears import _327
from mastapy._internal.python_net import python_net_import
from mastapy._internal.cast_exception import CastException

_INT_32 = python_net_import('System', 'Int32')
_BOOLEAN = python_net_import('System', 'Boolean')
_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_GEAR_SET_OPTIMISER = python_net_import('SMT.MastaAPI.Gears', 'GearSetOptimiser')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimiser',)


class GearSetOptimiser(_0.APIBase):
    """GearSetOptimiser

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISER

    class _Cast_GearSetOptimiser:
        """Special nested class for casting GearSetOptimiser to subclasses."""

        def __init__(self, parent: 'GearSetOptimiser'):
            self._parent = parent

        @property
        def cylindrical_gear_set_macro_geometry_optimiser(self):
            from mastapy.gears.gear_designs.cylindrical import _1025
            
            return self._parent._cast(_1025.CylindricalGearSetMacroGeometryOptimiser)

        @property
        def gear_set_optimiser(self) -> 'GearSetOptimiser':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetOptimiser.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'BendingSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'ContactSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def crack_initiation_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'CrackInitiationSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrackInitiationSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_fracture_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'FatigueFractureSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueFractureSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'MicropittingSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicropittingSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_deformation_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'PermanentDeformationSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentDeformationSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_flash_temperature_method_for_worst_gear(self) -> 'float':
        """float: 'ScuffingSafetyFactorFlashTemperatureMethodForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactorFlashTemperatureMethodForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_integral_method_for_worst_gear(self) -> 'float':
        """float: 'ScuffingSafetyFactorIntegralMethodForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactorIntegralMethodForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def static_bending_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'StaticBendingSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticBendingSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    @property
    def static_contact_safety_factor_for_worst_gear(self) -> 'float':
        """float: 'StaticContactSafetyFactorForWorstGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticContactSafetyFactorForWorstGear

        if temp is None:
            return 0.0

        return temp

    def dispose(self):
        """ 'Dispose' is the original name of this method."""

        self.wrapped.Dispose()

    def perform_strength_optimisation_with_progress(self, number_of_results: 'int', progress: '_7521.TaskProgress', use_current_design_as_starting_point: Optional['bool'] = False) -> '_327.GearSetOptimisationResults':
        """ 'PerformStrengthOptimisation' is the original name of this method.

        Args:
            number_of_results (int)
            progress (mastapy.TaskProgress)
            use_current_design_as_starting_point (bool, optional)

        Returns:
            mastapy.gears.GearSetOptimisationResults
        """

        number_of_results = int(number_of_results)
        use_current_design_as_starting_point = bool(use_current_design_as_starting_point)
        method_result = self.wrapped.PerformStrengthOptimisation.Overloads[_INT_32, _TASK_PROGRESS, _BOOLEAN](number_of_results if number_of_results else 0, progress.wrapped if progress else None, use_current_design_as_starting_point if use_current_design_as_starting_point else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform_strength_optimisation(self, number_of_results: 'int', use_current_design_as_starting_point: Optional['bool'] = False) -> '_327.GearSetOptimisationResults':
        """ 'PerformStrengthOptimisation' is the original name of this method.

        Args:
            number_of_results (int)
            use_current_design_as_starting_point (bool, optional)

        Returns:
            mastapy.gears.GearSetOptimisationResults
        """

        number_of_results = int(number_of_results)
        use_current_design_as_starting_point = bool(use_current_design_as_starting_point)
        method_result = self.wrapped.PerformStrengthOptimisation.Overloads[_INT_32, _BOOLEAN](number_of_results if number_of_results else 0, use_current_design_as_starting_point if use_current_design_as_starting_point else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.dispose()

    @property
    def cast_to(self) -> 'GearSetOptimiser._Cast_GearSetOptimiser':
        return self._Cast_GearSetOptimiser(self)
