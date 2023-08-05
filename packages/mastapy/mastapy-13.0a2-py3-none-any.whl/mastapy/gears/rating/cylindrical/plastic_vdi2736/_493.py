"""_493.py

VDI2736MetalPlasticRateableMesh
"""
from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _488
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VDI2736_METAL_PLASTIC_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'VDI2736MetalPlasticRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('VDI2736MetalPlasticRateableMesh',)


class VDI2736MetalPlasticRateableMesh(_488.PlasticGearVDI2736AbstractRateableMesh):
    """VDI2736MetalPlasticRateableMesh

    This is a mastapy class.
    """

    TYPE = _VDI2736_METAL_PLASTIC_RATEABLE_MESH

    class _Cast_VDI2736MetalPlasticRateableMesh:
        """Special nested class for casting VDI2736MetalPlasticRateableMesh to subclasses."""

        def __init__(self, parent: 'VDI2736MetalPlasticRateableMesh'):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(self):
            return self._parent._cast(_488.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def iso6336_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _518
            
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
        def vdi2736_metal_plastic_rateable_mesh(self) -> 'VDI2736MetalPlasticRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VDI2736MetalPlasticRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh':
        return self._Cast_VDI2736MetalPlasticRateableMesh(self)
