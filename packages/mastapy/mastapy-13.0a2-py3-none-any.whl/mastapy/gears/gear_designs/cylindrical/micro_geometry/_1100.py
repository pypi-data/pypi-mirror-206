"""_1100.py

CylindricalGearProfileModificationAtFaceWidthPosition
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PROFILE_MODIFICATION_AT_FACE_WIDTH_POSITION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearProfileModificationAtFaceWidthPosition')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearProfileModificationAtFaceWidthPosition',)


class CylindricalGearProfileModificationAtFaceWidthPosition(_1099.CylindricalGearProfileModification):
    """CylindricalGearProfileModificationAtFaceWidthPosition

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PROFILE_MODIFICATION_AT_FACE_WIDTH_POSITION

    class _Cast_CylindricalGearProfileModificationAtFaceWidthPosition:
        """Special nested class for casting CylindricalGearProfileModificationAtFaceWidthPosition to subclasses."""

        def __init__(self, parent: 'CylindricalGearProfileModificationAtFaceWidthPosition'):
            self._parent = parent

        @property
        def cylindrical_gear_profile_modification(self):
            return self._parent._cast(_1099.CylindricalGearProfileModification)

        @property
        def profile_modification(self):
            from mastapy.gears.micro_geometry import _577
            
            return self._parent._cast(_577.ProfileModification)

        @property
        def modification(self):
            from mastapy.gears.micro_geometry import _574
            
            return self._parent._cast(_574.Modification)

        @property
        def cylindrical_gear_profile_modification_at_face_width_position(self) -> 'CylindricalGearProfileModificationAtFaceWidthPosition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearProfileModificationAtFaceWidthPosition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width_position(self) -> 'float':
        """float: 'FaceWidthPosition' is the original name of this property."""

        temp = self.wrapped.FaceWidthPosition

        if temp is None:
            return 0.0

        return temp

    @face_width_position.setter
    def face_width_position(self, value: 'float'):
        self.wrapped.FaceWidthPosition = float(value) if value else 0.0

    @property
    def face_width_position_factor(self) -> 'float':
        """float: 'FaceWidthPositionFactor' is the original name of this property."""

        temp = self.wrapped.FaceWidthPositionFactor

        if temp is None:
            return 0.0

        return temp

    @face_width_position_factor.setter
    def face_width_position_factor(self, value: 'float'):
        self.wrapped.FaceWidthPositionFactor = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition':
        return self._Cast_CylindricalGearProfileModificationAtFaceWidthPosition(self)
