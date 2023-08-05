"""_2179.py

TiltingPadJournalBearing
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.fluid_film import _2172
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TILTING_PAD_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'TiltingPadJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('TiltingPadJournalBearing',)


class TiltingPadJournalBearing(_2172.PadFluidFilmBearing):
    """TiltingPadJournalBearing

    This is a mastapy class.
    """

    TYPE = _TILTING_PAD_JOURNAL_BEARING

    class _Cast_TiltingPadJournalBearing:
        """Special nested class for casting TiltingPadJournalBearing to subclasses."""

        def __init__(self, parent: 'TiltingPadJournalBearing'):
            self._parent = parent

        @property
        def pad_fluid_film_bearing(self):
            return self._parent._cast(_2172.PadFluidFilmBearing)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2116
            
            return self._parent._cast(_2116.DetailedBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2119
            
            return self._parent._cast(_2119.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2115
            
            return self._parent._cast(_2115.BearingDesign)

        @property
        def tilting_pad_journal_bearing(self) -> 'TiltingPadJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TiltingPadJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_aspect_ratio(self) -> 'float':
        """float: 'BearingAspectRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingAspectRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_between_pad_contact_surface_radius_and_bearing_inner_radius(self) -> 'float':
        """float: 'DifferenceBetweenPadContactSurfaceRadiusAndBearingInnerRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DifferenceBetweenPadContactSurfaceRadiusAndBearingInnerRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_contact_surface_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PadContactSurfaceRadius' is the original name of this property."""

        temp = self.wrapped.PadContactSurfaceRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @pad_contact_surface_radius.setter
    def pad_contact_surface_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PadContactSurfaceRadius = value

    @property
    def pivot_angular_offset(self) -> 'float':
        """float: 'PivotAngularOffset' is the original name of this property."""

        temp = self.wrapped.PivotAngularOffset

        if temp is None:
            return 0.0

        return temp

    @pivot_angular_offset.setter
    def pivot_angular_offset(self, value: 'float'):
        self.wrapped.PivotAngularOffset = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'TiltingPadJournalBearing._Cast_TiltingPadJournalBearing':
        return self._Cast_TiltingPadJournalBearing(self)
