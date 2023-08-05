"""_1168.py

ConicalGearLeadModification
"""
from mastapy.gears.micro_geometry import _567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LEAD_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry', 'ConicalGearLeadModification')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearLeadModification',)


class ConicalGearLeadModification(_567.LeadModification):
    """ConicalGearLeadModification

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LEAD_MODIFICATION

    class _Cast_ConicalGearLeadModification:
        """Special nested class for casting ConicalGearLeadModification to subclasses."""

        def __init__(self, parent: 'ConicalGearLeadModification'):
            self._parent = parent

        @property
        def lead_modification(self):
            return self._parent._cast(_567.LeadModification)

        @property
        def modification(self):
            from mastapy.gears.micro_geometry import _574
            
            return self._parent._cast(_574.Modification)

        @property
        def conical_gear_lead_modification(self) -> 'ConicalGearLeadModification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearLeadModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearLeadModification._Cast_ConicalGearLeadModification':
        return self._Cast_ConicalGearLeadModification(self)
