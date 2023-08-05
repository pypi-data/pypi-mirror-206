"""_4006.py

ShaftModalComplexShape
"""
from mastapy.system_model.analyses_and_results.rotor_dynamics import _4004
from mastapy.utility.units_and_measurements.measurements import _1677
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_COMPLEX_SHAPE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'ShaftModalComplexShape')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftModalComplexShape',)


class ShaftModalComplexShape(_4004.ShaftComplexShape['_1677.Number', '_1677.Number']):
    """ShaftModalComplexShape

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_COMPLEX_SHAPE

    class _Cast_ShaftModalComplexShape:
        """Special nested class for casting ShaftModalComplexShape to subclasses."""

        def __init__(self, parent: 'ShaftModalComplexShape'):
            self._parent = parent

        @property
        def shaft_complex_shape(self):
            return self._parent._cast(_4004.ShaftComplexShape)

        @property
        def shaft_modal_complex_shape_at_speeds(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4007
            
            return self._parent._cast(_4007.ShaftModalComplexShapeAtSpeeds)

        @property
        def shaft_modal_complex_shape_at_stiffness(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4008
            
            return self._parent._cast(_4008.ShaftModalComplexShapeAtStiffness)

        @property
        def shaft_modal_complex_shape(self) -> 'ShaftModalComplexShape':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftModalComplexShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftModalComplexShape._Cast_ShaftModalComplexShape':
        return self._Cast_ShaftModalComplexShape(self)
