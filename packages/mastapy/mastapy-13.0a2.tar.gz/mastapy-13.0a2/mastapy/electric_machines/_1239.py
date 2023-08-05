"""_1239.py

CADConductor
"""
from mastapy.electric_machines import _1301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_CONDUCTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADConductor')


__docformat__ = 'restructuredtext en'
__all__ = ('CADConductor',)


class CADConductor(_1301.WindingConductor):
    """CADConductor

    This is a mastapy class.
    """

    TYPE = _CAD_CONDUCTOR

    class _Cast_CADConductor:
        """Special nested class for casting CADConductor to subclasses."""

        def __init__(self, parent: 'CADConductor'):
            self._parent = parent

        @property
        def winding_conductor(self):
            return self._parent._cast(_1301.WindingConductor)

        @property
        def cad_conductor(self) -> 'CADConductor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CADConductor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CADConductor._Cast_CADConductor':
        return self._Cast_CADConductor(self)
