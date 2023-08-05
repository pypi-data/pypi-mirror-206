"""_444.py

FaceGearRating
"""
from mastapy.gears.gear_designs.face import _984
from mastapy._internal import constructor
from mastapy.gears.rating import _357
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearRating',)


class FaceGearRating(_357.GearRating):
    """FaceGearRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_RATING

    class _Cast_FaceGearRating:
        """Special nested class for casting FaceGearRating to subclasses."""

        def __init__(self, parent: 'FaceGearRating'):
            self._parent = parent

        @property
        def gear_rating(self):
            return self._parent._cast(_357.GearRating)

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _350
            
            return self._parent._cast(_350.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def face_gear_rating(self) -> 'FaceGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear(self) -> '_984.FaceGearDesign':
        """FaceGearDesign: 'FaceGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FaceGearRating._Cast_FaceGearRating':
        return self._Cast_FaceGearRating(self)
