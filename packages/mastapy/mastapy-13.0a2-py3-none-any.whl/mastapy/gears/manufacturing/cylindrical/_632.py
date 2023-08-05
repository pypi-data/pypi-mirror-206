"""_632.py

ProfileModificationSegment
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical import _631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_MODIFICATION_SEGMENT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'ProfileModificationSegment')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfileModificationSegment',)


class ProfileModificationSegment(_631.ModificationSegment):
    """ProfileModificationSegment

    This is a mastapy class.
    """

    TYPE = _PROFILE_MODIFICATION_SEGMENT

    class _Cast_ProfileModificationSegment:
        """Special nested class for casting ProfileModificationSegment to subclasses."""

        def __init__(self, parent: 'ProfileModificationSegment'):
            self._parent = parent

        @property
        def modification_segment(self):
            return self._parent._cast(_631.ModificationSegment)

        @property
        def profile_modification_segment(self) -> 'ProfileModificationSegment':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ProfileModificationSegment.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self) -> 'float':
        """float: 'Diameter' is the original name of this property."""

        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    def diameter(self, value: 'float'):
        self.wrapped.Diameter = float(value) if value else 0.0

    @property
    def roll_angle(self) -> 'float':
        """float: 'RollAngle' is the original name of this property."""

        temp = self.wrapped.RollAngle

        if temp is None:
            return 0.0

        return temp

    @roll_angle.setter
    def roll_angle(self, value: 'float'):
        self.wrapped.RollAngle = float(value) if value else 0.0

    @property
    def roll_distance(self) -> 'float':
        """float: 'RollDistance' is the original name of this property."""

        temp = self.wrapped.RollDistance

        if temp is None:
            return 0.0

        return temp

    @roll_distance.setter
    def roll_distance(self, value: 'float'):
        self.wrapped.RollDistance = float(value) if value else 0.0

    @property
    def use_iso217712007_slope_sign_convention(self) -> 'bool':
        """bool: 'UseISO217712007SlopeSignConvention' is the original name of this property."""

        temp = self.wrapped.UseISO217712007SlopeSignConvention

        if temp is None:
            return False

        return temp

    @use_iso217712007_slope_sign_convention.setter
    def use_iso217712007_slope_sign_convention(self, value: 'bool'):
        self.wrapped.UseISO217712007SlopeSignConvention = bool(value) if value else False

    @property
    def cast_to(self) -> 'ProfileModificationSegment._Cast_ProfileModificationSegment':
        return self._Cast_ProfileModificationSegment(self)
