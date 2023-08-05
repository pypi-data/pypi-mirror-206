"""_866.py

ConicalMeshLoadDistributionAtRotation
"""
from mastapy.gears.ltca import _837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalMeshLoadDistributionAtRotation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshLoadDistributionAtRotation',)


class ConicalMeshLoadDistributionAtRotation(_837.GearMeshLoadDistributionAtRotation):
    """ConicalMeshLoadDistributionAtRotation

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION

    class _Cast_ConicalMeshLoadDistributionAtRotation:
        """Special nested class for casting ConicalMeshLoadDistributionAtRotation to subclasses."""

        def __init__(self, parent: 'ConicalMeshLoadDistributionAtRotation'):
            self._parent = parent

        @property
        def gear_mesh_load_distribution_at_rotation(self):
            return self._parent._cast(_837.GearMeshLoadDistributionAtRotation)

        @property
        def conical_mesh_load_distribution_at_rotation(self) -> 'ConicalMeshLoadDistributionAtRotation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshLoadDistributionAtRotation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalMeshLoadDistributionAtRotation._Cast_ConicalMeshLoadDistributionAtRotation':
        return self._Cast_ConicalMeshLoadDistributionAtRotation(self)
