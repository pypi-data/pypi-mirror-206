"""_2428.py

Datum
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Datum')


__docformat__ = 'restructuredtext en'
__all__ = ('Datum',)


class Datum(_2424.Component):
    """Datum

    This is a mastapy class.
    """

    TYPE = _DATUM

    class _Cast_Datum:
        """Special nested class for casting Datum to subclasses."""

        def __init__(self, parent: 'Datum'):
            self._parent = parent

        @property
        def component(self):
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def datum(self) -> 'Datum':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Datum.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def drawing_diameter(self) -> 'float':
        """float: 'DrawingDiameter' is the original name of this property."""

        temp = self.wrapped.DrawingDiameter

        if temp is None:
            return 0.0

        return temp

    @drawing_diameter.setter
    def drawing_diameter(self, value: 'float'):
        self.wrapped.DrawingDiameter = float(value) if value else 0.0

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property."""

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    def offset(self, value: 'float'):
        self.wrapped.Offset = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'Datum._Cast_Datum':
        return self._Cast_Datum(self)
