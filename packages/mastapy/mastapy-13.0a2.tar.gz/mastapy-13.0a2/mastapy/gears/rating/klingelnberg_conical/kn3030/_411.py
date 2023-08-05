"""_411.py

KlingelnbergConicalRateableMesh
"""
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030', 'KlingelnbergConicalRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergConicalRateableMesh',)


class KlingelnbergConicalRateableMesh(_363.RateableMesh):
    """KlingelnbergConicalRateableMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_RATEABLE_MESH

    class _Cast_KlingelnbergConicalRateableMesh:
        """Special nested class for casting KlingelnbergConicalRateableMesh to subclasses."""

        def __init__(self, parent: 'KlingelnbergConicalRateableMesh'):
            self._parent = parent

        @property
        def rateable_mesh(self):
            return self._parent._cast(_363.RateableMesh)

        @property
        def klingelnberg_conical_rateable_mesh(self) -> 'KlingelnbergConicalRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergConicalRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergConicalRateableMesh._Cast_KlingelnbergConicalRateableMesh':
        return self._Cast_KlingelnbergConicalRateableMesh(self)
