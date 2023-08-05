"""_1241.py

CADMagnetsForLayer
"""
from mastapy.electric_machines import _1271
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_MAGNETS_FOR_LAYER = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADMagnetsForLayer')


__docformat__ = 'restructuredtext en'
__all__ = ('CADMagnetsForLayer',)


class CADMagnetsForLayer(_1271.MagnetDesign):
    """CADMagnetsForLayer

    This is a mastapy class.
    """

    TYPE = _CAD_MAGNETS_FOR_LAYER

    class _Cast_CADMagnetsForLayer:
        """Special nested class for casting CADMagnetsForLayer to subclasses."""

        def __init__(self, parent: 'CADMagnetsForLayer'):
            self._parent = parent

        @property
        def magnet_design(self):
            return self._parent._cast(_1271.MagnetDesign)

        @property
        def cad_magnets_for_layer(self) -> 'CADMagnetsForLayer':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CADMagnetsForLayer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CADMagnetsForLayer._Cast_CADMagnetsForLayer':
        return self._Cast_CADMagnetsForLayer(self)
