"""_2927.py

ShaftDutyCycleSystemDeflection
"""
from typing import List

from mastapy.shafts import _19
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2462
from mastapy.system_model.analyses_and_results.system_deflections import _2783
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_DUTY_CYCLE_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ShaftDutyCycleSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftDutyCycleSystemDeflection',)


class ShaftDutyCycleSystemDeflection(_0.APIBase):
    """ShaftDutyCycleSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_DUTY_CYCLE_SYSTEM_DEFLECTION

    class _Cast_ShaftDutyCycleSystemDeflection:
        """Special nested class for casting ShaftDutyCycleSystemDeflection to subclasses."""

        def __init__(self, parent: 'ShaftDutyCycleSystemDeflection'):
            self._parent = parent

        @property
        def shaft_duty_cycle_system_deflection(self) -> 'ShaftDutyCycleSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftDutyCycleSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def shaft_damage_results(self) -> '_19.ShaftDamageResults':
        """ShaftDamageResults: 'ShaftDamageResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftDamageResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_design(self) -> '_2462.Shaft':
        """Shaft: 'ShaftDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_static_analyses(self) -> 'List[_2783.ShaftSystemDeflection]':
        """List[ShaftSystemDeflection]: 'ShaftStaticAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftStaticAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftDutyCycleSystemDeflection._Cast_ShaftDutyCycleSystemDeflection':
        return self._Cast_ShaftDutyCycleSystemDeflection(self)
