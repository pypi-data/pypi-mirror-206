"""_768.py

BevelMachineSettingOptimizationResult
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _769
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_MACHINE_SETTING_OPTIMIZATION_RESULT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'BevelMachineSettingOptimizationResult')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelMachineSettingOptimizationResult',)


class BevelMachineSettingOptimizationResult(_0.APIBase):
    """BevelMachineSettingOptimizationResult

    This is a mastapy class.
    """

    TYPE = _BEVEL_MACHINE_SETTING_OPTIMIZATION_RESULT

    class _Cast_BevelMachineSettingOptimizationResult:
        """Special nested class for casting BevelMachineSettingOptimizationResult to subclasses."""

        def __init__(self, parent: 'BevelMachineSettingOptimizationResult'):
            self._parent = parent

        @property
        def bevel_machine_setting_optimization_result(self) -> 'BevelMachineSettingOptimizationResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelMachineSettingOptimizationResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_absolute_residual(self) -> 'float':
        """float: 'MaximumAbsoluteResidual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAbsoluteResidual

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_squared_residuals(self) -> 'float':
        """float: 'SumOfSquaredResiduals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SumOfSquaredResiduals

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_deviations_concave(self) -> '_769.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'CalculatedDeviationsConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedDeviationsConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def calculated_deviations_convex(self) -> '_769.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'CalculatedDeviationsConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedDeviationsConvex

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def imported_deviations_concave(self) -> '_769.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'ImportedDeviationsConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImportedDeviationsConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def imported_deviations_convex(self) -> '_769.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'ImportedDeviationsConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImportedDeviationsConvex

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelMachineSettingOptimizationResult._Cast_BevelMachineSettingOptimizationResult':
        return self._Cast_BevelMachineSettingOptimizationResult(self)
