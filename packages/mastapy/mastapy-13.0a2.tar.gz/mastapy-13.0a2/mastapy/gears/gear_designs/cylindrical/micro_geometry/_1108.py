"""_1108.py

LeadFormReliefWithDeviation
"""
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1109
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_FORM_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'LeadFormReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('LeadFormReliefWithDeviation',)


class LeadFormReliefWithDeviation(_1109.LeadReliefWithDeviation):
    """LeadFormReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _LEAD_FORM_RELIEF_WITH_DEVIATION

    class _Cast_LeadFormReliefWithDeviation:
        """Special nested class for casting LeadFormReliefWithDeviation to subclasses."""

        def __init__(self, parent: 'LeadFormReliefWithDeviation'):
            self._parent = parent

        @property
        def lead_relief_with_deviation(self):
            return self._parent._cast(_1109.LeadReliefWithDeviation)

        @property
        def relief_with_deviation(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1122
            
            return self._parent._cast(_1122.ReliefWithDeviation)

        @property
        def lead_form_relief_with_deviation(self) -> 'LeadFormReliefWithDeviation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LeadFormReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LeadFormReliefWithDeviation._Cast_LeadFormReliefWithDeviation':
        return self._Cast_LeadFormReliefWithDeviation(self)
