"""_442.py

FaceGearMeshDutyCycleRating
"""
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearMeshDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshDutyCycleRating',)


class FaceGearMeshDutyCycleRating(_361.MeshDutyCycleRating):
    """FaceGearMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_DUTY_CYCLE_RATING

    class _Cast_FaceGearMeshDutyCycleRating:
        """Special nested class for casting FaceGearMeshDutyCycleRating to subclasses."""

        def __init__(self, parent: 'FaceGearMeshDutyCycleRating'):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(self):
            return self._parent._cast(_361.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _349
            
            return self._parent._cast(_349.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def face_gear_mesh_duty_cycle_rating(self) -> 'FaceGearMeshDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearMeshDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FaceGearMeshDutyCycleRating._Cast_FaceGearMeshDutyCycleRating':
        return self._Cast_FaceGearMeshDutyCycleRating(self)
