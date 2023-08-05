"""_2594.py

BearingDetailConfiguration
"""
from mastapy.system_model.part_model.configurations import _2596, _2595
from mastapy.system_model.part_model import _2419
from mastapy.bearings.bearing_designs import _2115
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_CONFIGURATION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailConfiguration',)


class BearingDetailConfiguration(_2596.PartDetailConfiguration['_2595.BearingDetailSelection', '_2419.Bearing', '_2115.BearingDesign']):
    """BearingDetailConfiguration

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_CONFIGURATION

    class _Cast_BearingDetailConfiguration:
        """Special nested class for casting BearingDetailConfiguration to subclasses."""

        def __init__(self, parent: 'BearingDetailConfiguration'):
            self._parent = parent

        @property
        def part_detail_configuration(self):
            return self._parent._cast(_2596.PartDetailConfiguration)

        @property
        def bearing_detail_configuration(self) -> 'BearingDetailConfiguration':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDetailConfiguration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingDetailConfiguration._Cast_BearingDetailConfiguration':
        return self._Cast_BearingDetailConfiguration(self)
