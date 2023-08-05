"""_495.py

VDI2736PlasticPlasticRateableMesh
"""
from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _488
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VDI2736_PLASTIC_PLASTIC_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'VDI2736PlasticPlasticRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('VDI2736PlasticPlasticRateableMesh',)


class VDI2736PlasticPlasticRateableMesh(_488.PlasticGearVDI2736AbstractRateableMesh):
    """VDI2736PlasticPlasticRateableMesh

    This is a mastapy class.
    """

    TYPE = _VDI2736_PLASTIC_PLASTIC_RATEABLE_MESH

    class _Cast_VDI2736PlasticPlasticRateableMesh:
        """Special nested class for casting VDI2736PlasticPlasticRateableMesh to subclasses."""

        def __init__(self, parent: 'VDI2736PlasticPlasticRateableMesh'):
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
        def vdi2736_plastic_plastic_rateable_mesh(self) -> 'VDI2736PlasticPlasticRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VDI2736PlasticPlasticRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh':
        return self._Cast_VDI2736PlasticPlasticRateableMesh(self)
