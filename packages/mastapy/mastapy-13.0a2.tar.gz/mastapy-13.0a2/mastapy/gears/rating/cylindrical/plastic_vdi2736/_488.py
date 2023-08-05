"""_488.py

PlasticGearVDI2736AbstractRateableMesh
"""
from mastapy.gears.rating.cylindrical.iso6336 import _518
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticGearVDI2736AbstractRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticGearVDI2736AbstractRateableMesh',)


class PlasticGearVDI2736AbstractRateableMesh(_518.ISO6336RateableMesh):
    """PlasticGearVDI2736AbstractRateableMesh

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_RATEABLE_MESH

    class _Cast_PlasticGearVDI2736AbstractRateableMesh:
        """Special nested class for casting PlasticGearVDI2736AbstractRateableMesh to subclasses."""

        def __init__(self, parent: 'PlasticGearVDI2736AbstractRateableMesh'):
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
        def plastic_gear_vdi2736_abstract_rateable_mesh(self) -> 'PlasticGearVDI2736AbstractRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlasticGearVDI2736AbstractRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh':
        return self._Cast_PlasticGearVDI2736AbstractRateableMesh(self)
