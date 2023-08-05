"""_731.py

FinishCutterSimulation
"""
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_CUTTER_SIMULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'FinishCutterSimulation')


__docformat__ = 'restructuredtext en'
__all__ = ('FinishCutterSimulation',)


class FinishCutterSimulation(_734.GearCutterSimulation):
    """FinishCutterSimulation

    This is a mastapy class.
    """

    TYPE = _FINISH_CUTTER_SIMULATION

    class _Cast_FinishCutterSimulation:
        """Special nested class for casting FinishCutterSimulation to subclasses."""

        def __init__(self, parent: 'FinishCutterSimulation'):
            self._parent = parent

        @property
        def gear_cutter_simulation(self):
            return self._parent._cast(_734.GearCutterSimulation)

        @property
        def finish_cutter_simulation(self) -> 'FinishCutterSimulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FinishCutterSimulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FinishCutterSimulation._Cast_FinishCutterSimulation':
        return self._Cast_FinishCutterSimulation(self)
