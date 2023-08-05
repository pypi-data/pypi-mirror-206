"""_629.py

MicroGeometryInputsLead
"""
from mastapy.math_utility import _1477
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical import _628, _627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS_LEAD = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'MicroGeometryInputsLead')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryInputsLead',)


class MicroGeometryInputsLead(_628.MicroGeometryInputs['_627.LeadModificationSegment']):
    """MicroGeometryInputsLead

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_INPUTS_LEAD

    class _Cast_MicroGeometryInputsLead:
        """Special nested class for casting MicroGeometryInputsLead to subclasses."""

        def __init__(self, parent: 'MicroGeometryInputsLead'):
            self._parent = parent

        @property
        def micro_geometry_inputs(self):
            return self._parent._cast(_628.MicroGeometryInputs)

        @property
        def micro_geometry_inputs_lead(self) -> 'MicroGeometryInputsLead':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryInputsLead.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_micro_geometry_range(self) -> '_1477.Range':
        """Range: 'LeadMicroGeometryRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadMicroGeometryRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_lead_segments(self) -> 'int':
        """int: 'NumberOfLeadSegments' is the original name of this property."""

        temp = self.wrapped.NumberOfLeadSegments

        if temp is None:
            return 0

        return temp

    @number_of_lead_segments.setter
    def number_of_lead_segments(self, value: 'int'):
        self.wrapped.NumberOfLeadSegments = int(value) if value else 0

    @property
    def cast_to(self) -> 'MicroGeometryInputsLead._Cast_MicroGeometryInputsLead':
        return self._Cast_MicroGeometryInputsLead(self)
