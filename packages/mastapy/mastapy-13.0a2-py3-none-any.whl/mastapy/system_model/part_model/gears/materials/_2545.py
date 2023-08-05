"""_2545.py

GearMaterialExpertSystemMaterialDetails
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_EXPERT_SYSTEM_MATERIAL_DETAILS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.Materials', 'GearMaterialExpertSystemMaterialDetails')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMaterialExpertSystemMaterialDetails',)


class GearMaterialExpertSystemMaterialDetails(_0.APIBase):
    """GearMaterialExpertSystemMaterialDetails

    This is a mastapy class.
    """

    TYPE = _GEAR_MATERIAL_EXPERT_SYSTEM_MATERIAL_DETAILS

    class _Cast_GearMaterialExpertSystemMaterialDetails:
        """Special nested class for casting GearMaterialExpertSystemMaterialDetails to subclasses."""

        def __init__(self, parent: 'GearMaterialExpertSystemMaterialDetails'):
            self._parent = parent

        @property
        def gear_material_expert_system_material_details(self) -> 'GearMaterialExpertSystemMaterialDetails':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMaterialExpertSystemMaterialDetails.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bar_length(self) -> 'float':
        """float: 'BarLength' is the original name of this property."""

        temp = self.wrapped.BarLength

        if temp is None:
            return 0.0

        return temp

    @bar_length.setter
    def bar_length(self, value: 'float'):
        self.wrapped.BarLength = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'GearMaterialExpertSystemMaterialDetails._Cast_GearMaterialExpertSystemMaterialDetails':
        return self._Cast_GearMaterialExpertSystemMaterialDetails(self)
