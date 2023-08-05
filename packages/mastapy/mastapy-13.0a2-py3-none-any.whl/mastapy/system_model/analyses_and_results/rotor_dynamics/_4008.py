"""_4008.py

ShaftModalComplexShapeAtStiffness
"""
from mastapy.system_model.analyses_and_results.rotor_dynamics import _4006
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_COMPLEX_SHAPE_AT_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'ShaftModalComplexShapeAtStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftModalComplexShapeAtStiffness',)


class ShaftModalComplexShapeAtStiffness(_4006.ShaftModalComplexShape):
    """ShaftModalComplexShapeAtStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_COMPLEX_SHAPE_AT_STIFFNESS

    class _Cast_ShaftModalComplexShapeAtStiffness:
        """Special nested class for casting ShaftModalComplexShapeAtStiffness to subclasses."""

        def __init__(self, parent: 'ShaftModalComplexShapeAtStiffness'):
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
        def shaft_modal_complex_shape_at_stiffness(self) -> 'ShaftModalComplexShapeAtStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftModalComplexShapeAtStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftModalComplexShapeAtStiffness._Cast_ShaftModalComplexShapeAtStiffness':
        return self._Cast_ShaftModalComplexShapeAtStiffness(self)
