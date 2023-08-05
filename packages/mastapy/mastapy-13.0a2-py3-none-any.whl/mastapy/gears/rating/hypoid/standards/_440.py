"""_440.py

HypoidRateableMesh
"""
from mastapy.gears.rating.agma_gleason_conical import _563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Hypoid.Standards', 'HypoidRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidRateableMesh',)


class HypoidRateableMesh(_563.AGMAGleasonConicalRateableMesh):
    """HypoidRateableMesh

    This is a mastapy class.
    """

    TYPE = _HYPOID_RATEABLE_MESH

    class _Cast_HypoidRateableMesh:
        """Special nested class for casting HypoidRateableMesh to subclasses."""

        def __init__(self, parent: 'HypoidRateableMesh'):
            self._parent = parent

        @property
        def agma_gleason_conical_rateable_mesh(self):
            return self._parent._cast(_563.AGMAGleasonConicalRateableMesh)

        @property
        def conical_rateable_mesh(self):
            from mastapy.gears.rating.conical import _542
            
            return self._parent._cast(_542.ConicalRateableMesh)

        @property
        def rateable_mesh(self):
            from mastapy.gears.rating import _363
            
            return self._parent._cast(_363.RateableMesh)

        @property
        def hypoid_rateable_mesh(self) -> 'HypoidRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HypoidRateableMesh._Cast_HypoidRateableMesh':
        return self._Cast_HypoidRateableMesh(self)
