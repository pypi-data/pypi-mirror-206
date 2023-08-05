"""_2174.py

PlainGreaseFilledJournalBearing
"""
from mastapy.bearings.bearing_designs.fluid_film import _2175, _2177, _2176
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_GREASE_FILLED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'PlainGreaseFilledJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('PlainGreaseFilledJournalBearing',)


class PlainGreaseFilledJournalBearing(_2176.PlainJournalBearing):
    """PlainGreaseFilledJournalBearing

    This is a mastapy class.
    """

    TYPE = _PLAIN_GREASE_FILLED_JOURNAL_BEARING

    class _Cast_PlainGreaseFilledJournalBearing:
        """Special nested class for casting PlainGreaseFilledJournalBearing to subclasses."""

        def __init__(self, parent: 'PlainGreaseFilledJournalBearing'):
            self._parent = parent

        @property
        def plain_journal_bearing(self):
            return self._parent._cast(_2176.PlainJournalBearing)

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
        def plain_grease_filled_journal_bearing(self) -> 'PlainGreaseFilledJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlainGreaseFilledJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def housing_type(self) -> '_2175.PlainGreaseFilledJournalBearingHousingType':
        """PlainGreaseFilledJournalBearingHousingType: 'HousingType' is the original name of this property."""

        temp = self.wrapped.HousingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _2175.PlainGreaseFilledJournalBearingHousingType)
        return constructor.new_from_mastapy_type(_2175.PlainGreaseFilledJournalBearingHousingType)(value) if value is not None else None

    @housing_type.setter
    def housing_type(self, value: '_2175.PlainGreaseFilledJournalBearingHousingType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _2175.PlainGreaseFilledJournalBearingHousingType.type_())
        self.wrapped.HousingType = value

    @property
    def housing_detail(self) -> '_2177.PlainJournalHousing':
        """PlainJournalHousing: 'HousingDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HousingDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing':
        return self._Cast_PlainGreaseFilledJournalBearing(self)
