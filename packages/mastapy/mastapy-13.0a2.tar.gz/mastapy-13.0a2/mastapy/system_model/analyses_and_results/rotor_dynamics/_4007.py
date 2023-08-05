"""_4007.py

ShaftModalComplexShapeAtSpeeds
"""
from mastapy.system_model.analyses_and_results.rotor_dynamics import _4006
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_COMPLEX_SHAPE_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'ShaftModalComplexShapeAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftModalComplexShapeAtSpeeds',)


class ShaftModalComplexShapeAtSpeeds(_4006.ShaftModalComplexShape):
    """ShaftModalComplexShapeAtSpeeds

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_COMPLEX_SHAPE_AT_SPEEDS

    class _Cast_ShaftModalComplexShapeAtSpeeds:
        """Special nested class for casting ShaftModalComplexShapeAtSpeeds to subclasses."""

        def __init__(self, parent: 'ShaftModalComplexShapeAtSpeeds'):
            self._parent = parent

        @property
        def shaft_modal_complex_shape(self):
            return self._parent._cast(_4006.ShaftModalComplexShape)

        @property
        def shaft_complex_shape(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4004
            from mastapy.utility.units_and_measurements.measurements import _1677
            
            return self._parent._cast(_4004.ShaftComplexShape)

        @property
        def shaft_modal_complex_shape_at_speeds(self) -> 'ShaftModalComplexShapeAtSpeeds':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftModalComplexShapeAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftModalComplexShapeAtSpeeds._Cast_ShaftModalComplexShapeAtSpeeds':
        return self._Cast_ShaftModalComplexShapeAtSpeeds(self)
