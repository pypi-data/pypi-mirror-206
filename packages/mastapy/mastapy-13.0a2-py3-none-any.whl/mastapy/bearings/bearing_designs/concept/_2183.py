"""_2183.py

ConceptClearanceBearing
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs import _2119
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_CLEARANCE_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Concept', 'ConceptClearanceBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptClearanceBearing',)


class ConceptClearanceBearing(_2119.NonLinearBearing):
    """ConceptClearanceBearing

    This is a mastapy class.
    """

    TYPE = _CONCEPT_CLEARANCE_BEARING

    class _Cast_ConceptClearanceBearing:
        """Special nested class for casting ConceptClearanceBearing to subclasses."""

        def __init__(self, parent: 'ConceptClearanceBearing'):
            self._parent = parent

        @property
        def non_linear_bearing(self):
            return self._parent._cast(_2119.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2115
            
            return self._parent._cast(_2115.BearingDesign)

        @property
        def concept_axial_clearance_bearing(self):
            from mastapy.bearings.bearing_designs.concept import _2182
            
            return self._parent._cast(_2182.ConceptAxialClearanceBearing)

        @property
        def concept_radial_clearance_bearing(self):
            from mastapy.bearings.bearing_designs.concept import _2184
            
            return self._parent._cast(_2184.ConceptRadialClearanceBearing)

        @property
        def concept_clearance_bearing(self) -> 'ConceptClearanceBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptClearanceBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_diameter(self) -> 'float':
        """float: 'ContactDiameter' is the original name of this property."""

        temp = self.wrapped.ContactDiameter

        if temp is None:
            return 0.0

        return temp

    @contact_diameter.setter
    def contact_diameter(self, value: 'float'):
        self.wrapped.ContactDiameter = float(value) if value else 0.0

    @property
    def contact_stiffness(self) -> 'float':
        """float: 'ContactStiffness' is the original name of this property."""

        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return temp

    @contact_stiffness.setter
    def contact_stiffness(self, value: 'float'):
        self.wrapped.ContactStiffness = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ConceptClearanceBearing._Cast_ConceptClearanceBearing':
        return self._Cast_ConceptClearanceBearing(self)
