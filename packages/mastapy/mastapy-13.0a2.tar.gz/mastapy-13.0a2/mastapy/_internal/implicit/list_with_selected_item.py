"""list_with_selected_item.py

Implementations of 'ListWithSelectedItem' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from typing import List, Generic, TypeVar

from mastapy._internal import mixins, constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.ltca.cylindrical import _851, _852
from mastapy.gears.manufacturing.cylindrical import _620
from mastapy.gears.manufacturing.bevel import _786
from mastapy.electric_machines import _1259, _1285, _1254
from mastapy.electric_machines.results import _1315
from mastapy.utility import _1589
from mastapy.utility.units_and_measurements import _1599, _1594
from mastapy.utility.file_access_helpers import _1804
from mastapy.system_model.part_model import (
    _2452, _2424, _2428, _2435,
    _2433, _2451
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649, _5737
from mastapy._internal.tuple_with_name import TupleWithName
from mastapy.system_model.analyses_and_results.system_deflections import _2738, _2724
from mastapy.system_model.part_model.gears import _2511, _2504, _2505
from mastapy.system_model.fe import _2365, _2363, _2354
from mastapy.system_model.fe.links import _2398
from mastapy.system_model.part_model.part_groups import _2467
from mastapy.gears.gear_designs import _945
from mastapy.system_model.part_model.couplings import _2577
from mastapy.system_model.analyses_and_results.load_case_groups import _5633, _5634
from mastapy.nodal_analysis.component_mode_synthesis import _221
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5818
from mastapy.system_model.analyses_and_results.static_loads import _6769

_ARRAY = python_net_import('System', 'Array')
_LIST_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.Utility.Property', 'ListWithSelectedItem')


__docformat__ = 'restructuredtext en'
__all__ = (
    'ListWithSelectedItem_str', 'ListWithSelectedItem_int',
    'ListWithSelectedItem_T', 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis',
    'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis', 'ListWithSelectedItem_CylindricalSetManufacturingConfig',
    'ListWithSelectedItem_ConicalSetManufacturingConfig', 'ListWithSelectedItem_ElectricMachineSetup',
    'ListWithSelectedItem_float', 'ListWithSelectedItem_ElectricMachineResults',
    'ListWithSelectedItem_RotorSkewSlice', 'ListWithSelectedItem_SystemDirectory',
    'ListWithSelectedItem_Unit', 'ListWithSelectedItem_MeasurementBase',
    'ListWithSelectedItem_ColumnTitle', 'ListWithSelectedItem_PowerLoad',
    'ListWithSelectedItem_AbstractPeriodicExcitationDetail', 'ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase',
    'ListWithSelectedItem_TupleWithName', 'ListWithSelectedItem_GearMeshSystemDeflection',
    'ListWithSelectedItem_GearSet', 'ListWithSelectedItem_FESubstructureNode',
    'ListWithSelectedItem_Component', 'ListWithSelectedItem_Datum',
    'ListWithSelectedItem_FELink', 'ListWithSelectedItem_FESubstructure',
    'ListWithSelectedItem_CylindricalGear', 'ListWithSelectedItem_ElectricMachineDetail',
    'ListWithSelectedItem_GuideDxfModel', 'ListWithSelectedItem_ConcentricPartGroup',
    'ListWithSelectedItem_CylindricalGearSet', 'ListWithSelectedItem_GearSetDesign',
    'ListWithSelectedItem_ShaftHubConnection', 'ListWithSelectedItem_TSelectableItem',
    'ListWithSelectedItem_CylindricalGearSystemDeflection', 'ListWithSelectedItem_DesignState',
    'ListWithSelectedItem_FEPart', 'ListWithSelectedItem_TPartAnalysis',
    'ListWithSelectedItem_CMSElementFaceGroup', 'ListWithSelectedItem_ResultLocationSelectionGroup',
    'ListWithSelectedItem_StaticLoadCase', 'ListWithSelectedItem_DutyCycle',
    'ListWithSelectedItem_ElectricMachineDataSet', 'ListWithSelectedItem_PointLoad'
)


T = TypeVar('T')
TSelectableItem = TypeVar('TSelectableItem')
TPartAnalysis = TypeVar('TPartAnalysis')


class ListWithSelectedItem_str(str, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_str

    A specific implementation of 'ListWithSelectedItem' for 'str' types.
    """
    __qualname__ = 'str'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        return str.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else '')

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'str':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return str

    @property
    def selected_value(self) -> 'str':
        """str: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return ''

        return temp

    @property
    def available_values(self) -> 'List[str]':
        """List[str]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value


class ListWithSelectedItem_int(int, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_int

    A specific implementation of 'ListWithSelectedItem' for 'int' types.
    """
    __qualname__ = 'int'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        return int.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'int':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return int

    @property
    def selected_value(self) -> 'int':
        """int: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return 0

        return temp

    @property
    def available_values(self) -> 'List[int]':
        """List[int]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)
        return value


class ListWithSelectedItem_T(Generic[T], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_T

    A specific implementation of 'ListWithSelectedItem' for 'T' types.
    """
    __qualname__ = 'T'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_T.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'T':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return T

    @property
    def selected_value(self) -> 'T':
        """T: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[T]':
        """List[T]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis(_851.CylindricalGearLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearLoadDistributionAnalysis' types.
    """
    __qualname__ = 'CylindricalGearLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_851.CylindricalGearLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _851.CylindricalGearLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_851.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_851.CylindricalGearLoadDistributionAnalysis]':
        """List[CylindricalGearLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis(_852.CylindricalGearMeshLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearMeshLoadDistributionAnalysis' types.
    """
    __qualname__ = 'CylindricalGearMeshLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_852.CylindricalGearMeshLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _852.CylindricalGearMeshLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_852.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_852.CylindricalGearMeshLoadDistributionAnalysis]':
        """List[CylindricalGearMeshLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalSetManufacturingConfig(_620.CylindricalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalSetManufacturingConfig' types.
    """
    __qualname__ = 'CylindricalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_620.CylindricalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _620.CylindricalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_620.CylindricalSetManufacturingConfig':
        """CylindricalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_620.CylindricalSetManufacturingConfig]':
        """List[CylindricalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConicalSetManufacturingConfig(_786.ConicalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConicalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'ConicalSetManufacturingConfig' types.
    """
    __qualname__ = 'ConicalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConicalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_786.ConicalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _786.ConicalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_786.ConicalSetManufacturingConfig':
        """ConicalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_786.ConicalSetManufacturingConfig]':
        """List[ConicalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineSetup(_1259.ElectricMachineSetup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineSetup

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineSetup' types.
    """
    __qualname__ = 'ElectricMachineSetup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineSetup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1259.ElectricMachineSetup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1259.ElectricMachineSetup.TYPE

    @property
    def selected_value(self) -> '_1259.ElectricMachineSetup':
        """ElectricMachineSetup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1259.ElectricMachineSetup]':
        """List[ElectricMachineSetup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_float(float, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_float

    A specific implementation of 'ListWithSelectedItem' for 'float' types.
    """
    __qualname__ = 'float'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        return float.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0.0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'float':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return float

    @property
    def selected_value(self) -> 'float':
        """float: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return 0.0

        return temp

    @property
    def available_values(self) -> 'List[float]':
        """List[float]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value


class ListWithSelectedItem_ElectricMachineResults(_1315.ElectricMachineResults, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineResults

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineResults' types.
    """
    __qualname__ = 'ElectricMachineResults'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineResults.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1315.ElectricMachineResults.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1315.ElectricMachineResults.TYPE

    @property
    def selected_value(self) -> '_1315.ElectricMachineResults':
        """ElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1315.ElectricMachineResults]':
        """List[ElectricMachineResults]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_RotorSkewSlice(_1285.RotorSkewSlice, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_RotorSkewSlice

    A specific implementation of 'ListWithSelectedItem' for 'RotorSkewSlice' types.
    """
    __qualname__ = 'RotorSkewSlice'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_RotorSkewSlice.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1285.RotorSkewSlice.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1285.RotorSkewSlice.TYPE

    @property
    def selected_value(self) -> '_1285.RotorSkewSlice':
        """RotorSkewSlice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1285.RotorSkewSlice]':
        """List[RotorSkewSlice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_SystemDirectory(_1589.SystemDirectory, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_SystemDirectory

    A specific implementation of 'ListWithSelectedItem' for 'SystemDirectory' types.
    """
    __qualname__ = 'SystemDirectory'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_SystemDirectory.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1589.SystemDirectory.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1589.SystemDirectory.TYPE

    @property
    def selected_value(self) -> '_1589.SystemDirectory':
        """SystemDirectory: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1589.SystemDirectory]':
        """List[SystemDirectory]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Unit(_1599.Unit, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Unit

    A specific implementation of 'ListWithSelectedItem' for 'Unit' types.
    """
    __qualname__ = 'Unit'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Unit.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1599.Unit.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1599.Unit.TYPE

    @property
    def selected_value(self) -> '_1599.Unit':
        """Unit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1599.Unit]':
        """List[Unit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_MeasurementBase(_1594.MeasurementBase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_MeasurementBase

    A specific implementation of 'ListWithSelectedItem' for 'MeasurementBase' types.
    """
    __qualname__ = 'MeasurementBase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_MeasurementBase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1594.MeasurementBase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1594.MeasurementBase.TYPE

    @property
    def selected_value(self) -> '_1594.MeasurementBase':
        """MeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1594.MeasurementBase]':
        """List[MeasurementBase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ColumnTitle(_1804.ColumnTitle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ColumnTitle

    A specific implementation of 'ListWithSelectedItem' for 'ColumnTitle' types.
    """
    __qualname__ = 'ColumnTitle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ColumnTitle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1804.ColumnTitle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1804.ColumnTitle.TYPE

    @property
    def selected_value(self) -> '_1804.ColumnTitle':
        """ColumnTitle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1804.ColumnTitle]':
        """List[ColumnTitle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PowerLoad(_2452.PowerLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PowerLoad

    A specific implementation of 'ListWithSelectedItem' for 'PowerLoad' types.
    """
    __qualname__ = 'PowerLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PowerLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2452.PowerLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2452.PowerLoad.TYPE

    @property
    def selected_value(self) -> '_2452.PowerLoad':
        """PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2452.PowerLoad]':
        """List[PowerLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_AbstractPeriodicExcitationDetail(_5649.AbstractPeriodicExcitationDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_AbstractPeriodicExcitationDetail

    A specific implementation of 'ListWithSelectedItem' for 'AbstractPeriodicExcitationDetail' types.
    """
    __qualname__ = 'AbstractPeriodicExcitationDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_AbstractPeriodicExcitationDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5649.AbstractPeriodicExcitationDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5649.AbstractPeriodicExcitationDetail.TYPE

    @property
    def selected_value(self) -> '_5649.AbstractPeriodicExcitationDetail':
        """AbstractPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5649.AbstractPeriodicExcitationDetail]':
        """List[AbstractPeriodicExcitationDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase(_5737.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase

    A specific implementation of 'ListWithSelectedItem' for 'HarmonicAnalysisWithVaryingStiffnessStaticLoadCase' types.
    """
    __qualname__ = 'HarmonicAnalysisWithVaryingStiffnessStaticLoadCase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5737.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5737.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.TYPE

    @property
    def selected_value(self) -> '_5737.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase':
        """HarmonicAnalysisWithVaryingStiffnessStaticLoadCase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5737.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase]':
        """List[HarmonicAnalysisWithVaryingStiffnessStaticLoadCase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TupleWithName(TupleWithName, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TupleWithName

    A specific implementation of 'ListWithSelectedItem' for 'TupleWithName' types.
    """
    __qualname__ = 'TupleWithName'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TupleWithName.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TupleWithName.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TupleWithName.TYPE

    @property
    def selected_value(self) -> 'TupleWithName':
        """TupleWithName: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        value = conversion.pn_to_mp_tuple_with_name(temp, (None))
        return constructor.new_from_mastapy_type(TupleWithName)(value) if value is not None else None

    @property
    def available_values(self) -> 'TupleWithName':
        """TupleWithName: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return constructor.new_from_mastapy_type(TupleWithName)(value) if value is not None else None


class ListWithSelectedItem_GearMeshSystemDeflection(_2738.GearMeshSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearMeshSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'GearMeshSystemDeflection' types.
    """
    __qualname__ = 'GearMeshSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearMeshSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2738.GearMeshSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2738.GearMeshSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2738.GearMeshSystemDeflection':
        """GearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2738.GearMeshSystemDeflection]':
        """List[GearMeshSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSet(_2511.GearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSet

    A specific implementation of 'ListWithSelectedItem' for 'GearSet' types.
    """
    __qualname__ = 'GearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2511.GearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2511.GearSet.TYPE

    @property
    def selected_value(self) -> '_2511.GearSet':
        """GearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2511.GearSet]':
        """List[GearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructureNode(_2365.FESubstructureNode, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructureNode

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructureNode' types.
    """
    __qualname__ = 'FESubstructureNode'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructureNode.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2365.FESubstructureNode.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2365.FESubstructureNode.TYPE

    @property
    def selected_value(self) -> '_2365.FESubstructureNode':
        """FESubstructureNode: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2365.FESubstructureNode]':
        """List[FESubstructureNode]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Component(_2424.Component, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Component

    A specific implementation of 'ListWithSelectedItem' for 'Component' types.
    """
    __qualname__ = 'Component'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Component.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2424.Component.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2424.Component.TYPE

    @property
    def selected_value(self) -> '_2424.Component':
        """Component: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2424.Component]':
        """List[Component]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Datum(_2428.Datum, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Datum

    A specific implementation of 'ListWithSelectedItem' for 'Datum' types.
    """
    __qualname__ = 'Datum'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Datum.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2428.Datum.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2428.Datum.TYPE

    @property
    def selected_value(self) -> '_2428.Datum':
        """Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2428.Datum]':
        """List[Datum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FELink(_2398.FELink, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FELink

    A specific implementation of 'ListWithSelectedItem' for 'FELink' types.
    """
    __qualname__ = 'FELink'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FELink.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2398.FELink.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2398.FELink.TYPE

    @property
    def selected_value(self) -> '_2398.FELink':
        """FELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2398.FELink]':
        """List[FELink]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructure(_2363.FESubstructure, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructure

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructure' types.
    """
    __qualname__ = 'FESubstructure'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructure.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2363.FESubstructure.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2363.FESubstructure.TYPE

    @property
    def selected_value(self) -> '_2363.FESubstructure':
        """FESubstructure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2363.FESubstructure]':
        """List[FESubstructure]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGear(_2504.CylindricalGear, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGear

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGear' types.
    """
    __qualname__ = 'CylindricalGear'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGear.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2504.CylindricalGear.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2504.CylindricalGear.TYPE

    @property
    def selected_value(self) -> '_2504.CylindricalGear':
        """CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2504.CylindricalGear]':
        """List[CylindricalGear]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDetail(_1254.ElectricMachineDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDetail

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDetail' types.
    """
    __qualname__ = 'ElectricMachineDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1254.ElectricMachineDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1254.ElectricMachineDetail.TYPE

    @property
    def selected_value(self) -> '_1254.ElectricMachineDetail':
        """ElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1254.ElectricMachineDetail]':
        """List[ElectricMachineDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GuideDxfModel(_2435.GuideDxfModel, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GuideDxfModel

    A specific implementation of 'ListWithSelectedItem' for 'GuideDxfModel' types.
    """
    __qualname__ = 'GuideDxfModel'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GuideDxfModel.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2435.GuideDxfModel.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2435.GuideDxfModel.TYPE

    @property
    def selected_value(self) -> '_2435.GuideDxfModel':
        """GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2435.GuideDxfModel]':
        """List[GuideDxfModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConcentricPartGroup(_2467.ConcentricPartGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConcentricPartGroup

    A specific implementation of 'ListWithSelectedItem' for 'ConcentricPartGroup' types.
    """
    __qualname__ = 'ConcentricPartGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConcentricPartGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2467.ConcentricPartGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2467.ConcentricPartGroup.TYPE

    @property
    def selected_value(self) -> '_2467.ConcentricPartGroup':
        """ConcentricPartGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2467.ConcentricPartGroup]':
        """List[ConcentricPartGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSet(_2505.CylindricalGearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSet

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSet' types.
    """
    __qualname__ = 'CylindricalGearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2505.CylindricalGearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2505.CylindricalGearSet.TYPE

    @property
    def selected_value(self) -> '_2505.CylindricalGearSet':
        """CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2505.CylindricalGearSet]':
        """List[CylindricalGearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSetDesign(_945.GearSetDesign, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSetDesign

    A specific implementation of 'ListWithSelectedItem' for 'GearSetDesign' types.
    """
    __qualname__ = 'GearSetDesign'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSetDesign.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_945.GearSetDesign.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _945.GearSetDesign.TYPE

    @property
    def selected_value(self) -> '_945.GearSetDesign':
        """GearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_945.GearSetDesign]':
        """List[GearSetDesign]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ShaftHubConnection(_2577.ShaftHubConnection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ShaftHubConnection

    A specific implementation of 'ListWithSelectedItem' for 'ShaftHubConnection' types.
    """
    __qualname__ = 'ShaftHubConnection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ShaftHubConnection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2577.ShaftHubConnection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2577.ShaftHubConnection.TYPE

    @property
    def selected_value(self) -> '_2577.ShaftHubConnection':
        """ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2577.ShaftHubConnection]':
        """List[ShaftHubConnection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TSelectableItem(Generic[TSelectableItem], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TSelectableItem

    A specific implementation of 'ListWithSelectedItem' for 'TSelectableItem' types.
    """
    __qualname__ = 'TSelectableItem'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TSelectableItem.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TSelectableItem':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TSelectableItem

    @property
    def selected_value(self) -> 'TSelectableItem':
        """TSelectableItem: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(TSelectableItem)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TSelectableItem]':
        """List[TSelectableItem]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSystemDeflection(_2724.CylindricalGearSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSystemDeflection' types.
    """
    __qualname__ = 'CylindricalGearSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2724.CylindricalGearSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2724.CylindricalGearSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2724.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2724.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DesignState(_5633.DesignState, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DesignState

    A specific implementation of 'ListWithSelectedItem' for 'DesignState' types.
    """
    __qualname__ = 'DesignState'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DesignState.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5633.DesignState.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5633.DesignState.TYPE

    @property
    def selected_value(self) -> '_5633.DesignState':
        """DesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5633.DesignState]':
        """List[DesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FEPart(_2433.FEPart, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FEPart

    A specific implementation of 'ListWithSelectedItem' for 'FEPart' types.
    """
    __qualname__ = 'FEPart'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FEPart.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2433.FEPart.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2433.FEPart.TYPE

    @property
    def selected_value(self) -> '_2433.FEPart':
        """FEPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2433.FEPart]':
        """List[FEPart]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TPartAnalysis(Generic[TPartAnalysis], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TPartAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'TPartAnalysis' types.
    """
    __qualname__ = 'TPartAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TPartAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TPartAnalysis':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TPartAnalysis

    @property
    def selected_value(self) -> 'TPartAnalysis':
        """TPartAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(TPartAnalysis)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TPartAnalysis]':
        """List[TPartAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CMSElementFaceGroup(_221.CMSElementFaceGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CMSElementFaceGroup

    A specific implementation of 'ListWithSelectedItem' for 'CMSElementFaceGroup' types.
    """
    __qualname__ = 'CMSElementFaceGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CMSElementFaceGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_221.CMSElementFaceGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _221.CMSElementFaceGroup.TYPE

    @property
    def selected_value(self) -> '_221.CMSElementFaceGroup':
        """CMSElementFaceGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_221.CMSElementFaceGroup]':
        """List[CMSElementFaceGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ResultLocationSelectionGroup(_5818.ResultLocationSelectionGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ResultLocationSelectionGroup

    A specific implementation of 'ListWithSelectedItem' for 'ResultLocationSelectionGroup' types.
    """
    __qualname__ = 'ResultLocationSelectionGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ResultLocationSelectionGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5818.ResultLocationSelectionGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5818.ResultLocationSelectionGroup.TYPE

    @property
    def selected_value(self) -> '_5818.ResultLocationSelectionGroup':
        """ResultLocationSelectionGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5818.ResultLocationSelectionGroup]':
        """List[ResultLocationSelectionGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_StaticLoadCase(_6769.StaticLoadCase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_StaticLoadCase

    A specific implementation of 'ListWithSelectedItem' for 'StaticLoadCase' types.
    """
    __qualname__ = 'StaticLoadCase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_StaticLoadCase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_6769.StaticLoadCase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6769.StaticLoadCase.TYPE

    @property
    def selected_value(self) -> '_6769.StaticLoadCase':
        """StaticLoadCase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_6769.StaticLoadCase]':
        """List[StaticLoadCase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DutyCycle(_5634.DutyCycle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DutyCycle

    A specific implementation of 'ListWithSelectedItem' for 'DutyCycle' types.
    """
    __qualname__ = 'DutyCycle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DutyCycle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5634.DutyCycle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5634.DutyCycle.TYPE

    @property
    def selected_value(self) -> '_5634.DutyCycle':
        """DutyCycle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5634.DutyCycle]':
        """List[DutyCycle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDataSet(_2354.ElectricMachineDataSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDataSet

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDataSet' types.
    """
    __qualname__ = 'ElectricMachineDataSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDataSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2354.ElectricMachineDataSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2354.ElectricMachineDataSet.TYPE

    @property
    def selected_value(self) -> '_2354.ElectricMachineDataSet':
        """ElectricMachineDataSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2354.ElectricMachineDataSet]':
        """List[ElectricMachineDataSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PointLoad(_2451.PointLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PointLoad

    A specific implementation of 'ListWithSelectedItem' for 'PointLoad' types.
    """
    __qualname__ = 'PointLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PointLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2451.PointLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2451.PointLoad.TYPE

    @property
    def selected_value(self) -> '_2451.PointLoad':
        """PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2451.PointLoad]':
        """List[PointLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
