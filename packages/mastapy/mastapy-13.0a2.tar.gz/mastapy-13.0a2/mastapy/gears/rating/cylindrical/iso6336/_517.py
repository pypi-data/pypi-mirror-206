"""_517.py

ISO6336MetalRateableMesh
"""
from mastapy.gears.rating.cylindrical.iso6336 import _518
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_METAL_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO6336MetalRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336MetalRateableMesh',)


class ISO6336MetalRateableMesh(_518.ISO6336RateableMesh):
    """ISO6336MetalRateableMesh

    This is a mastapy class.
    """

    TYPE = _ISO6336_METAL_RATEABLE_MESH

    class _Cast_ISO6336MetalRateableMesh:
        """Special nested class for casting ISO6336MetalRateableMesh to subclasses."""

        def __init__(self, parent: 'ISO6336MetalRateableMesh'):
            self._parent = parent

        @property
        def iso6336_rateable_mesh(self):
            return self._parent._cast(_518.ISO6336RateableMesh)

        @property
        def cylindrical_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical import _467
            
            return self._parent._cast(_467.CylindricalRateableMesh)

        @property
        def rateable_mesh(self):
            from mastapy.gears.rating import _363
            
            return self._parent._cast(_363.RateableMesh)

        @property
        def iso6336_metal_rateable_mesh(self) -> 'ISO6336MetalRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336MetalRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh':
        return self._Cast_ISO6336MetalRateableMesh(self)
