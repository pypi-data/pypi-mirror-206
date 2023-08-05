"""_480.py

ScuffingResultsRowGear
"""
from mastapy.gears.gear_designs.cylindrical import _1020
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCUFFING_RESULTS_ROW_GEAR = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'ScuffingResultsRowGear')


__docformat__ = 'restructuredtext en'
__all__ = ('ScuffingResultsRowGear',)


class ScuffingResultsRowGear(_0.APIBase):
    """ScuffingResultsRowGear

    This is a mastapy class.
    """

    TYPE = _SCUFFING_RESULTS_ROW_GEAR

    class _Cast_ScuffingResultsRowGear:
        """Special nested class for casting ScuffingResultsRowGear to subclasses."""

        def __init__(self, parent: 'ScuffingResultsRowGear'):
            self._parent = parent

        @property
        def scuffing_results_row_gear(self) -> 'ScuffingResultsRowGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ScuffingResultsRowGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def profile_measurement(self) -> '_1020.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ProfileMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ScuffingResultsRowGear._Cast_ScuffingResultsRowGear':
        return self._Cast_ScuffingResultsRowGear(self)
