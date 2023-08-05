"""_24.py

ShaftMaterial
"""
from mastapy.shafts import _6
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.materials import _244, _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MATERIAL = python_net_import('SMT.MastaAPI.Shafts', 'ShaftMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftMaterial',)


class ShaftMaterial(_265.Material):
    """ShaftMaterial

    This is a mastapy class.
    """

    TYPE = _SHAFT_MATERIAL

    class _Cast_ShaftMaterial:
        """Special nested class for casting ShaftMaterial to subclasses."""

        def __init__(self, parent: 'ShaftMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def shaft_material(self) -> 'ShaftMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hardening_type_for_agma60016101e08(self) -> '_6.AGMAHardeningType':
        """AGMAHardeningType: 'HardeningTypeForAGMA60016101E08' is the original name of this property."""

        temp = self.wrapped.HardeningTypeForAGMA60016101E08

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _6.AGMAHardeningType)
        return constructor.new_from_mastapy_type(_6.AGMAHardeningType)(value) if value is not None else None

    @hardening_type_for_agma60016101e08.setter
    def hardening_type_for_agma60016101e08(self, value: '_6.AGMAHardeningType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _6.AGMAHardeningType.type_())
        self.wrapped.HardeningTypeForAGMA60016101E08 = value

    @property
    def specified_endurance_limit(self) -> 'float':
        """float: 'SpecifiedEnduranceLimit' is the original name of this property."""

        temp = self.wrapped.SpecifiedEnduranceLimit

        if temp is None:
            return 0.0

        return temp

    @specified_endurance_limit.setter
    def specified_endurance_limit(self, value: 'float'):
        self.wrapped.SpecifiedEnduranceLimit = float(value) if value else 0.0

    @property
    def use_custom_sn_curve(self) -> 'bool':
        """bool: 'UseCustomSNCurve' is the original name of this property."""

        temp = self.wrapped.UseCustomSNCurve

        if temp is None:
            return False

        return temp

    @use_custom_sn_curve.setter
    def use_custom_sn_curve(self, value: 'bool'):
        self.wrapped.UseCustomSNCurve = bool(value) if value else False

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
    def cast_to(self) -> 'ShaftMaterial._Cast_ShaftMaterial':
        return self._Cast_ShaftMaterial(self)
