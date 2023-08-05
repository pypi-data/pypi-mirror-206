"""_1542.py

ParetoOptimisationVariableBase
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility import _1577
from mastapy.math_utility import _1477
from mastapy.math_utility.optimisation import _1547, _1546
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_VARIABLE_BASE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ParetoOptimisationVariableBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimisationVariableBase',)


class ParetoOptimisationVariableBase(_0.APIBase):
    """ParetoOptimisationVariableBase

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_VARIABLE_BASE

    class _Cast_ParetoOptimisationVariableBase:
        """Special nested class for casting ParetoOptimisationVariableBase to subclasses."""

        def __init__(self, parent: 'ParetoOptimisationVariableBase'):
            self._parent = parent

        @property
        def pareto_optimisation_input(self):
            from mastapy.math_utility.optimisation import _1536
            
            return self._parent._cast(_1536.ParetoOptimisationInput)

        @property
        def pareto_optimisation_output(self):
            from mastapy.math_utility.optimisation import _1537
            
            return self._parent._cast(_1537.ParetoOptimisationOutput)

        @property
        def pareto_optimistaion_variable(self):
            from mastapy.math_utility.optimisation import _1543
            
            return self._parent._cast(_1543.ParetoOptimistaionVariable)

        @property
        def parametric_study_doe_result_variable(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4359
            
            return self._parent._cast(_4359.ParametricStudyDOEResultVariable)

        @property
        def pareto_optimisation_variable_base(self) -> 'ParetoOptimisationVariableBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimisationVariableBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def percent(self) -> 'float':
        """float: 'Percent' is the original name of this property."""

        temp = self.wrapped.Percent

        if temp is None:
            return 0.0

        return temp

    @percent.setter
    def percent(self, value: 'float'):
        self.wrapped.Percent = float(value) if value else 0.0

    @property
    def integer_range(self) -> '_1577.IntegerRange':
        """IntegerRange: 'IntegerRange' is the original name of this property."""

        temp = self.wrapped.IntegerRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @integer_range.setter
    def integer_range(self, value: '_1577.IntegerRange'):
        value = value.wrapped if value else None
        self.wrapped.IntegerRange = value

    @property
    def property_(self) -> 'str':
        """str: 'Property' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Property

        if temp is None:
            return ''

        return temp

    @property
    def range(self) -> '_1477.Range':
        """Range: 'Range' is the original name of this property."""

        temp = self.wrapped.Range

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @range.setter
    def range(self, value: '_1477.Range'):
        value = value.wrapped if value else None
        self.wrapped.Range = value

    @property
    def specification_type(self) -> '_1547.TargetingPropertyTo':
        """TargetingPropertyTo: 'SpecificationType' is the original name of this property."""

        temp = self.wrapped.SpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1547.TargetingPropertyTo)
        return constructor.new_from_mastapy_type(_1547.TargetingPropertyTo)(value) if value is not None else None

    @specification_type.setter
    def specification_type(self, value: '_1547.TargetingPropertyTo'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1547.TargetingPropertyTo.type_())
        self.wrapped.SpecificationType = value

    @property
    def specify_input_range_as(self) -> '_1546.SpecifyOptimisationInputAs':
        """SpecifyOptimisationInputAs: 'SpecifyInputRangeAs' is the original name of this property."""

        temp = self.wrapped.SpecifyInputRangeAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1546.SpecifyOptimisationInputAs)
        return constructor.new_from_mastapy_type(_1546.SpecifyOptimisationInputAs)(value) if value is not None else None

    @specify_input_range_as.setter
    def specify_input_range_as(self, value: '_1546.SpecifyOptimisationInputAs'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1546.SpecifyOptimisationInputAs.type_())
        self.wrapped.SpecifyInputRangeAs = value

    @property
    def unit(self) -> 'str':
        """str: 'Unit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Unit

        if temp is None:
            return ''

        return temp

    @property
    def value(self) -> 'float':
        """float: 'Value' is the original name of this property."""

        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @value.setter
    def value(self, value: 'float'):
        self.wrapped.Value = float(value) if value else 0.0

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def delete(self):
        """ 'Delete' is the original name of this method."""

        self.wrapped.Delete()

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase':
        return self._Cast_ParetoOptimisationVariableBase(self)
