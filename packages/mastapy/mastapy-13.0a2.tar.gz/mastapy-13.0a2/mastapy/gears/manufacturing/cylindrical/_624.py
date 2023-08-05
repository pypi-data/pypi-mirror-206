"""_624.py

GearManufacturingConfigurationViewModelPlaceholder
"""
from mastapy.gears.manufacturing.cylindrical import _623
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL_PLACEHOLDER = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'GearManufacturingConfigurationViewModelPlaceholder')


__docformat__ = 'restructuredtext en'
__all__ = ('GearManufacturingConfigurationViewModelPlaceholder',)


class GearManufacturingConfigurationViewModelPlaceholder(_623.GearManufacturingConfigurationViewModel):
    """GearManufacturingConfigurationViewModelPlaceholder

    This is a mastapy class.
    """

    TYPE = _GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL_PLACEHOLDER

    class _Cast_GearManufacturingConfigurationViewModelPlaceholder:
        """Special nested class for casting GearManufacturingConfigurationViewModelPlaceholder to subclasses."""

        def __init__(self, parent: 'GearManufacturingConfigurationViewModelPlaceholder'):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model(self):
            return self._parent._cast(_623.GearManufacturingConfigurationViewModel)

        @property
        def gear_manufacturing_configuration_view_model_placeholder(self) -> 'GearManufacturingConfigurationViewModelPlaceholder':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearManufacturingConfigurationViewModelPlaceholder.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearManufacturingConfigurationViewModelPlaceholder._Cast_GearManufacturingConfigurationViewModelPlaceholder':
        return self._Cast_GearManufacturingConfigurationViewModelPlaceholder(self)
