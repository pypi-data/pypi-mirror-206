"""_1082.py

Usage
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _341
from mastapy.gears.gear_designs.cylindrical import _1069
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USAGE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'Usage')


__docformat__ = 'restructuredtext en'
__all__ = ('Usage',)


class Usage(_1575.IndependentReportablePropertiesBase['Usage']):
    """Usage

    This is a mastapy class.
    """

    TYPE = _USAGE

    class _Cast_Usage:
        """Special nested class for casting Usage to subclasses."""

        def __init__(self, parent: 'Usage'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.gears.gear_designs.cylindrical import _1082
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def usage(self) -> 'Usage':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Usage.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gearing_is_runin(self) -> 'bool':
        """bool: 'GearingIsRunin' is the original name of this property."""

        temp = self.wrapped.GearingIsRunin

        if temp is None:
            return False

        return temp

    @gearing_is_runin.setter
    def gearing_is_runin(self, value: 'bool'):
        self.wrapped.GearingIsRunin = bool(value) if value else False

    @property
    def improved_gearing(self) -> 'bool':
        """bool: 'ImprovedGearing' is the original name of this property."""

        temp = self.wrapped.ImprovedGearing

        if temp is None:
            return False

        return temp

    @improved_gearing.setter
    def improved_gearing(self, value: 'bool'):
        self.wrapped.ImprovedGearing = bool(value) if value else False

    @property
    def leads_modified(self) -> 'bool':
        """bool: 'LeadsModified' is the original name of this property."""

        temp = self.wrapped.LeadsModified

        if temp is None:
            return False

        return temp

    @leads_modified.setter
    def leads_modified(self, value: 'bool'):
        self.wrapped.LeadsModified = bool(value) if value else False

    @property
    def safety_requirement(self) -> '_341.SafetyRequirementsAGMA':
        """SafetyRequirementsAGMA: 'SafetyRequirement' is the original name of this property."""

        temp = self.wrapped.SafetyRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _341.SafetyRequirementsAGMA)
        return constructor.new_from_mastapy_type(_341.SafetyRequirementsAGMA)(value) if value is not None else None

    @safety_requirement.setter
    def safety_requirement(self, value: '_341.SafetyRequirementsAGMA'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _341.SafetyRequirementsAGMA.type_())
        self.wrapped.SafetyRequirement = value

    @property
    def spur_gear_load_sharing_code(self) -> '_1069.SpurGearLoadSharingCodes':
        """SpurGearLoadSharingCodes: 'SpurGearLoadSharingCode' is the original name of this property."""

        temp = self.wrapped.SpurGearLoadSharingCode

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1069.SpurGearLoadSharingCodes)
        return constructor.new_from_mastapy_type(_1069.SpurGearLoadSharingCodes)(value) if value is not None else None

    @spur_gear_load_sharing_code.setter
    def spur_gear_load_sharing_code(self, value: '_1069.SpurGearLoadSharingCodes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1069.SpurGearLoadSharingCodes.type_())
        self.wrapped.SpurGearLoadSharingCode = value

    @property
    def cast_to(self) -> 'Usage._Cast_Usage':
        return self._Cast_Usage(self)
