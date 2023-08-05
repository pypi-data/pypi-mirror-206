"""_1054.py

LtcaSettings
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1053
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LTCA_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'LtcaSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('LtcaSettings',)


class LtcaSettings(_1575.IndependentReportablePropertiesBase['LtcaSettings']):
    """LtcaSettings

    This is a mastapy class.
    """

    TYPE = _LTCA_SETTINGS

    class _Cast_LtcaSettings:
        """Special nested class for casting LtcaSettings to subclasses."""

        def __init__(self, parent: 'LtcaSettings'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.gears.gear_designs.cylindrical import _1054
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def ltca_settings(self) -> 'LtcaSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LtcaSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_utilization_load_cutoff_parameter(self) -> 'float':
        """float: 'FaceUtilizationLoadCutoffParameter' is the original name of this property."""

        temp = self.wrapped.FaceUtilizationLoadCutoffParameter

        if temp is None:
            return 0.0

        return temp

    @face_utilization_load_cutoff_parameter.setter
    def face_utilization_load_cutoff_parameter(self, value: 'float'):
        self.wrapped.FaceUtilizationLoadCutoffParameter = float(value) if value else 0.0

    @property
    def include_extended_tip_contact(self) -> 'bool':
        """bool: 'IncludeExtendedTipContact' is the original name of this property."""

        temp = self.wrapped.IncludeExtendedTipContact

        if temp is None:
            return False

        return temp

    @include_extended_tip_contact.setter
    def include_extended_tip_contact(self, value: 'bool'):
        self.wrapped.IncludeExtendedTipContact = bool(value) if value else False

    @property
    def load_case_modifiable_settings(self) -> '_1053.LTCALoadCaseModifiableSettings':
        """LTCALoadCaseModifiableSettings: 'LoadCaseModifiableSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseModifiableSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LtcaSettings._Cast_LtcaSettings':
        return self._Cast_LtcaSettings(self)
