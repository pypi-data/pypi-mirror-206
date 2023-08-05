"""_630.py

MicroGeometryInputsProfile
"""
from mastapy._internal import constructor
from mastapy.math_utility import _1477
from mastapy.gears.manufacturing.cylindrical import _628, _632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS_PROFILE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'MicroGeometryInputsProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryInputsProfile',)


class MicroGeometryInputsProfile(_628.MicroGeometryInputs['_632.ProfileModificationSegment']):
    """MicroGeometryInputsProfile

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_INPUTS_PROFILE

    class _Cast_MicroGeometryInputsProfile:
        """Special nested class for casting MicroGeometryInputsProfile to subclasses."""

        def __init__(self, parent: 'MicroGeometryInputsProfile'):
            self._parent = parent

        @property
        def micro_geometry_inputs(self):
            return self._parent._cast(_628.MicroGeometryInputs)

        @property
        def micro_geometry_inputs_profile(self) -> 'MicroGeometryInputsProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryInputsProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_profile_segments(self) -> 'int':
        """int: 'NumberOfProfileSegments' is the original name of this property."""

        temp = self.wrapped.NumberOfProfileSegments

        if temp is None:
            return 0

        return temp

    @number_of_profile_segments.setter
    def number_of_profile_segments(self, value: 'int'):
        self.wrapped.NumberOfProfileSegments = int(value) if value else 0

    @property
    def profile_micro_geometry_range(self) -> '_1477.Range':
        """Range: 'ProfileMicroGeometryRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileMicroGeometryRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def z_plane(self) -> 'float':
        """float: 'ZPlane' is the original name of this property."""

        temp = self.wrapped.ZPlane

        if temp is None:
            return 0.0

        return temp

    @z_plane.setter
    def z_plane(self, value: 'float'):
        self.wrapped.ZPlane = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'MicroGeometryInputsProfile._Cast_MicroGeometryInputsProfile':
        return self._Cast_MicroGeometryInputsProfile(self)
