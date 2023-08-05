"""_1198.py

ConicalGearFEModel
"""
from mastapy.gears.fe_model import _1191
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel.Conical', 'ConicalGearFEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearFEModel',)


class ConicalGearFEModel(_1191.GearFEModel):
    """ConicalGearFEModel

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_FE_MODEL

    class _Cast_ConicalGearFEModel:
        """Special nested class for casting ConicalGearFEModel to subclasses."""

        def __init__(self, parent: 'ConicalGearFEModel'):
            self._parent = parent

        @property
        def gear_fe_model(self):
            return self._parent._cast(_1191.GearFEModel)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def conical_gear_fe_model(self) -> 'ConicalGearFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearFEModel._Cast_ConicalGearFEModel':
        return self._Cast_ConicalGearFEModel(self)
