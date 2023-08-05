"""_1125.py

TotalProfileReliefWithDeviation
"""
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1120
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOTAL_PROFILE_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'TotalProfileReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('TotalProfileReliefWithDeviation',)


class TotalProfileReliefWithDeviation(_1120.ProfileReliefWithDeviation):
    """TotalProfileReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _TOTAL_PROFILE_RELIEF_WITH_DEVIATION

    class _Cast_TotalProfileReliefWithDeviation:
        """Special nested class for casting TotalProfileReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'TotalProfileReliefWithDeviation'):
            self._parent = parent

        @property
        def profile_relief_with_deviation(self):
            return self._parent._cast(_1120.ProfileReliefWithDeviation)

        @property
        def relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1122
            
            return self._parent._cast(_1122.ReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(self) -> 'TotalProfileReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TotalProfileReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TotalProfileReliefWithDeviation._Cast_TotalProfileReliefWithDeviation':
        return self._Cast_TotalProfileReliefWithDeviation(self)
