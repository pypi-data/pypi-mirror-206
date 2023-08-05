"""_2176.py

PlainJournalBearing
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs import _2116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'PlainJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('PlainJournalBearing',)


class PlainJournalBearing(_2116.DetailedBearing):
    """PlainJournalBearing

    This is a mastapy class.
    """

    TYPE = _PLAIN_JOURNAL_BEARING

    class _Cast_PlainJournalBearing:
        """Special nested class for casting PlainJournalBearing to subclasses."""

        def __init__(self, parent: 'PlainJournalBearing'):
            self._parent = parent

        @property
        def detailed_bearing(self):
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
        def plain_grease_filled_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2174
            
            return self._parent._cast(_2174.PlainGreaseFilledJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2178
            
            return self._parent._cast(_2178.PlainOilFedJournalBearing)

        @property
        def plain_journal_bearing(self) -> 'PlainJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlainJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diametrical_clearance(self) -> 'float':
        """float: 'DiametricalClearance' is the original name of this property."""

        temp = self.wrapped.DiametricalClearance

        if temp is None:
            return 0.0

        return temp

    @diametrical_clearance.setter
    def diametrical_clearance(self, value: 'float'):
        self.wrapped.DiametricalClearance = float(value) if value else 0.0

    @property
    def land_width(self) -> 'float':
        """float: 'LandWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LandWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def land_width_to_diameter_ratio(self) -> 'float':
        """float: 'LandWidthToDiameterRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LandWidthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'PlainJournalBearing._Cast_PlainJournalBearing':
        return self._Cast_PlainJournalBearing(self)
