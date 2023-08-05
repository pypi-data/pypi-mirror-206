"""_686.py

WormGrinderManufactureError
"""
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _684
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDER_MANUFACTURE_ERROR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrinderManufactureError')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrinderManufactureError',)


class WormGrinderManufactureError(_684.RackManufactureError):
    """WormGrinderManufactureError

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDER_MANUFACTURE_ERROR

    class _Cast_WormGrinderManufactureError:
        """Special nested class for casting WormGrinderManufactureError to subclasses."""

        def __init__(self, parent: 'WormGrinderManufactureError'):
            self._parent = parent

        @property
        def rack_manufacture_error(self):
            return self._parent._cast(_684.RackManufactureError)

        @property
        def worm_grinder_manufacture_error(self) -> 'WormGrinderManufactureError':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrinderManufactureError.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WormGrinderManufactureError._Cast_WormGrinderManufactureError':
        return self._Cast_WormGrinderManufactureError(self)
