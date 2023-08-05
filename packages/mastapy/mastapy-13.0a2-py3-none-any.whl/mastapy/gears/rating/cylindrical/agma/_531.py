"""_531.py

AGMA2101RateableMesh
"""
from mastapy.gears.rating.cylindrical import _467
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA2101_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA', 'AGMA2101RateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMA2101RateableMesh',)


class AGMA2101RateableMesh(_467.CylindricalRateableMesh):
    """AGMA2101RateableMesh

    This is a mastapy class.
    """

    TYPE = _AGMA2101_RATEABLE_MESH

    class _Cast_AGMA2101RateableMesh:
        """Special nested class for casting AGMA2101RateableMesh to subclasses."""

        def __init__(self, parent: 'AGMA2101RateableMesh'):
            self._parent = parent

        @property
        def cylindrical_rateable_mesh(self):
            return self._parent._cast(_467.CylindricalRateableMesh)

        @property
        def rateable_mesh(self):
            from mastapy.gears.rating import _363
            
            return self._parent._cast(_363.RateableMesh)

        @property
        def agma2101_rateable_mesh(self) -> 'AGMA2101RateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMA2101RateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AGMA2101RateableMesh._Cast_AGMA2101RateableMesh':
        return self._Cast_AGMA2101RateableMesh(self)
