"""_130.py

BearingAxialMountingClearance
"""
from mastapy.nodal_analysis.nodal_entities import _124
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_AXIAL_MOUNTING_CLEARANCE = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'BearingAxialMountingClearance')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingAxialMountingClearance',)


class BearingAxialMountingClearance(_124.ArbitraryNodalComponent):
    """BearingAxialMountingClearance

    This is a mastapy class.
    """

    TYPE = _BEARING_AXIAL_MOUNTING_CLEARANCE

    class _Cast_BearingAxialMountingClearance:
        """Special nested class for casting BearingAxialMountingClearance to subclasses."""

        def __init__(self, parent: 'BearingAxialMountingClearance'):
            self._parent = parent

        @property
        def arbitrary_nodal_component(self):
            return self._parent._cast(_124.ArbitraryNodalComponent)

        @property
        def nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _141
            
            return self._parent._cast(_141.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def bearing_axial_mounting_clearance(self) -> 'BearingAxialMountingClearance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingAxialMountingClearance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingAxialMountingClearance._Cast_BearingAxialMountingClearance':
        return self._Cast_BearingAxialMountingClearance(self)
