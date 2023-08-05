"""_1291.py

StatorRotorMaterial
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1269, _1250
from mastapy.utility_gui.charts import _1852
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials import _244, _265
from mastapy.utility import _1579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_ROTOR_MATERIAL = python_net_import('SMT.MastaAPI.ElectricMachines', 'StatorRotorMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('StatorRotorMaterial',)


class StatorRotorMaterial(_265.Material):
    """StatorRotorMaterial

    This is a mastapy class.
    """

    TYPE = _STATOR_ROTOR_MATERIAL

    class _Cast_StatorRotorMaterial:
        """Special nested class for casting StatorRotorMaterial to subclasses."""

        def __init__(self, parent: 'StatorRotorMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def stator_rotor_material(self) -> 'StatorRotorMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StatorRotorMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def annealing(self) -> 'str':
        """str: 'Annealing' is the original name of this property."""

        temp = self.wrapped.Annealing

        if temp is None:
            return ''

        return temp

    @annealing.setter
    def annealing(self, value: 'str'):
        self.wrapped.Annealing = str(value) if value else ''

    @property
    def coefficient_specification_method(self) -> '_1269.IronLossCoefficientSpecificationMethod':
        """IronLossCoefficientSpecificationMethod: 'CoefficientSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.CoefficientSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1269.IronLossCoefficientSpecificationMethod)
        return constructor.new_from_mastapy_type(_1269.IronLossCoefficientSpecificationMethod)(value) if value is not None else None

    @coefficient_specification_method.setter
    def coefficient_specification_method(self, value: '_1269.IronLossCoefficientSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1269.IronLossCoefficientSpecificationMethod.type_())
        self.wrapped.CoefficientSpecificationMethod = value

    @property
    def country(self) -> 'str':
        """str: 'Country' is the original name of this property."""

        temp = self.wrapped.Country

        if temp is None:
            return ''

        return temp

    @country.setter
    def country(self, value: 'str'):
        self.wrapped.Country = str(value) if value else ''

    @property
    def electrical_resistivity(self) -> 'float':
        """float: 'ElectricalResistivity' is the original name of this property."""

        temp = self.wrapped.ElectricalResistivity

        if temp is None:
            return 0.0

        return temp

    @electrical_resistivity.setter
    def electrical_resistivity(self, value: 'float'):
        self.wrapped.ElectricalResistivity = float(value) if value else 0.0

    @property
    def grade_name(self) -> 'str':
        """str: 'GradeName' is the original name of this property."""

        temp = self.wrapped.GradeName

        if temp is None:
            return ''

        return temp

    @grade_name.setter
    def grade_name(self, value: 'str'):
        self.wrapped.GradeName = str(value) if value else ''

    @property
    def lamination_thickness(self) -> 'float':
        """float: 'LaminationThickness' is the original name of this property."""

        temp = self.wrapped.LaminationThickness

        if temp is None:
            return 0.0

        return temp

    @lamination_thickness.setter
    def lamination_thickness(self, value: 'float'):
        self.wrapped.LaminationThickness = float(value) if value else 0.0

    @property
    def loss_curves(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'LossCurves' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LossCurves

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturer(self) -> 'str':
        """str: 'Manufacturer' is the original name of this property."""

        temp = self.wrapped.Manufacturer

        if temp is None:
            return ''

        return temp

    @manufacturer.setter
    def manufacturer(self, value: 'str'):
        self.wrapped.Manufacturer = str(value) if value else ''

    @property
    def material_category(self) -> 'str':
        """str: 'MaterialCategory' is the original name of this property."""

        temp = self.wrapped.MaterialCategory

        if temp is None:
            return ''

        return temp

    @material_category.setter
    def material_category(self, value: 'str'):
        self.wrapped.MaterialCategory = str(value) if value else ''

    @property
    def stacking_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'StackingFactor' is the original name of this property."""

        temp = self.wrapped.StackingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @stacking_factor.setter
    def stacking_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.StackingFactor = value

    @property
    def bh_curve_specification(self) -> '_244.BHCurveSpecification':
        """BHCurveSpecification: 'BHCurveSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BHCurveSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def core_loss_coefficients(self) -> '_1250.CoreLossCoefficients':
        """CoreLossCoefficients: 'CoreLossCoefficients' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoreLossCoefficients

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def loss_curve_flux_densities(self) -> 'List[float]':
        """List[float]: 'LossCurveFluxDensities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LossCurveFluxDensities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def loss_curve_frequencies(self) -> 'List[float]':
        """List[float]: 'LossCurveFrequencies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LossCurveFrequencies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def loss_curve_losses(self) -> 'List[float]':
        """List[float]: 'LossCurveLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LossCurveLosses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    def set_loss_curve_data(self, frequencies: 'List[float]', flux_densities: 'List[float]', loss: 'List[float]'):
        """ 'SetLossCurveData' is the original name of this method.

        Args:
            frequencies (List[float])
            flux_densities (List[float])
            loss (List[float])
        """

        frequencies = conversion.mp_to_pn_list_float(frequencies)
        flux_densities = conversion.mp_to_pn_list_float(flux_densities)
        loss = conversion.mp_to_pn_list_float(loss)
        self.wrapped.SetLossCurveData(frequencies, flux_densities, loss)

    def try_update_coefficients_from_loss_curve_data(self) -> '_1579.MethodOutcome':
        """ 'TryUpdateCoefficientsFromLossCurveData' is the original name of this method.

        Returns:
            mastapy.utility.MethodOutcome
        """

        method_result = self.wrapped.TryUpdateCoefficientsFromLossCurveData()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'StatorRotorMaterial._Cast_StatorRotorMaterial':
        return self._Cast_StatorRotorMaterial(self)
