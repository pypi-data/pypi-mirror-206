"""_1045.py

HardenedMaterialProperties
"""
from mastapy._internal import constructor
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARDENED_MATERIAL_PROPERTIES = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'HardenedMaterialProperties')


__docformat__ = 'restructuredtext en'
__all__ = ('HardenedMaterialProperties',)


class HardenedMaterialProperties(_1575.IndependentReportablePropertiesBase['HardenedMaterialProperties']):
    """HardenedMaterialProperties

    This is a mastapy class.
    """

    TYPE = _HARDENED_MATERIAL_PROPERTIES

    class _Cast_HardenedMaterialProperties:
        """Special nested class for casting HardenedMaterialProperties to subclasses."""

        def __init__(self, parent: 'HardenedMaterialProperties'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.gears.gear_designs.cylindrical import _1045
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def hardened_material_properties(self) -> 'HardenedMaterialProperties':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HardenedMaterialProperties.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def critical_stress(self) -> 'float':
        """float: 'CriticalStress' is the original name of this property."""

        temp = self.wrapped.CriticalStress

        if temp is None:
            return 0.0

        return temp

    @critical_stress.setter
    def critical_stress(self, value: 'float'):
        self.wrapped.CriticalStress = float(value) if value else 0.0

    @property
    def fatigue_sensitivity_to_normal_stress(self) -> 'float':
        """float: 'FatigueSensitivityToNormalStress' is the original name of this property."""

        temp = self.wrapped.FatigueSensitivityToNormalStress

        if temp is None:
            return 0.0

        return temp

    @fatigue_sensitivity_to_normal_stress.setter
    def fatigue_sensitivity_to_normal_stress(self, value: 'float'):
        self.wrapped.FatigueSensitivityToNormalStress = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'HardenedMaterialProperties._Cast_HardenedMaterialProperties':
        return self._Cast_HardenedMaterialProperties(self)
