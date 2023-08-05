"""_4005.py

ShaftForcedComplexShape
"""
from mastapy.system_model.analyses_and_results.rotor_dynamics import _4004
from mastapy.utility.units_and_measurements.measurements import _1659, _1604
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_FORCED_COMPLEX_SHAPE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'ShaftForcedComplexShape')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftForcedComplexShape',)


class ShaftForcedComplexShape(_4004.ShaftComplexShape['_1659.LengthVeryShort', '_1604.AngleSmall']):
    """ShaftForcedComplexShape

    This is a mastapy class.
    """

    TYPE = _SHAFT_FORCED_COMPLEX_SHAPE

    class _Cast_ShaftForcedComplexShape:
        """Special nested class for casting ShaftForcedComplexShape to subclasses."""

        def __init__(self, parent: 'ShaftForcedComplexShape'):
            self._parent = parent

        @property
        def shaft_complex_shape(self):
            return self._parent._cast(_4004.ShaftComplexShape)

        @property
        def shaft_forced_complex_shape(self) -> 'ShaftForcedComplexShape':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftForcedComplexShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftForcedComplexShape._Cast_ShaftForcedComplexShape':
        return self._Cast_ShaftForcedComplexShape(self)
