"""_363.py

RateableMesh
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating', 'RateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('RateableMesh',)


class RateableMesh(_0.APIBase):
    """RateableMesh

    This is a mastapy class.
    """

    TYPE = _RATEABLE_MESH

    class _Cast_RateableMesh:
        """Special nested class for casting RateableMesh to subclasses."""

        def __init__(self, parent: 'RateableMesh'):
            self._parent = parent

        @property
        def klingelnberg_conical_rateable_mesh(self):
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _411
            
            return self._parent._cast(_411.KlingelnbergConicalRateableMesh)

        @property
        def iso10300_rateable_mesh(self):
            from mastapy.gears.rating.iso_10300 import _423
            
            return self._parent._cast(_423.ISO10300RateableMesh)

        @property
        def hypoid_rateable_mesh(self):
            from mastapy.gears.rating.hypoid.standards import _440
            
            return self._parent._cast(_440.HypoidRateableMesh)

        @property
        def cylindrical_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical import _467
            
            return self._parent._cast(_467.CylindricalRateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _488
            
            return self._parent._cast(_488.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493
            
            return self._parent._cast(_493.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494
            
            return self._parent._cast(_494.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _495
            
            return self._parent._cast(_495.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _517
            
            return self._parent._cast(_517.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _518
            
            return self._parent._cast(_518.ISO6336RateableMesh)

        @property
        def agma2101_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.agma import _531
            
            return self._parent._cast(_531.AGMA2101RateableMesh)

        @property
        def conical_rateable_mesh(self):
            from mastapy.gears.rating.conical import _542
            
            return self._parent._cast(_542.ConicalRateableMesh)

        @property
        def spiral_bevel_rateable_mesh(self):
            from mastapy.gears.rating.bevel.standards import _559
            
            return self._parent._cast(_559.SpiralBevelRateableMesh)

        @property
        def agma_gleason_conical_rateable_mesh(self):
            from mastapy.gears.rating.agma_gleason_conical import _563
            
            return self._parent._cast(_563.AGMAGleasonConicalRateableMesh)

        @property
        def rateable_mesh(self) -> 'RateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RateableMesh._Cast_RateableMesh':
        return self._Cast_RateableMesh(self)
