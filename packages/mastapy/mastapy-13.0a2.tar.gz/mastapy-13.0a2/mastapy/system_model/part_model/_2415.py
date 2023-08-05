"""_2415.py

AbstractShaft
"""
from mastapy.system_model.part_model import _2416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaft',)


class AbstractShaft(_2416.AbstractShaftOrHousing):
    """AbstractShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT

    class _Cast_AbstractShaft:
        """Special nested class for casting AbstractShaft to subclasses."""

        def __init__(self, parent: 'AbstractShaft'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing(self):
            return self._parent._cast(_2416.AbstractShaftOrHousing)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
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
        def shaft(self):
            from mastapy.system_model.part_model.shaft_model import _2462
            
            return self._parent._cast(_2462.Shaft)

        @property
        def cycloidal_disc(self):
            from mastapy.system_model.part_model.cycloidal import _2548
            
            return self._parent._cast(_2548.CycloidalDisc)

        @property
        def abstract_shaft(self) -> 'AbstractShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AbstractShaft._Cast_AbstractShaft':
        return self._Cast_AbstractShaft(self)
