"""_1702.py

StiffnessPerUnitFaceWidth
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STIFFNESS_PER_UNIT_FACE_WIDTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'StiffnessPerUnitFaceWidth')


__docformat__ = 'restructuredtext en'
__all__ = ('StiffnessPerUnitFaceWidth',)


class StiffnessPerUnitFaceWidth(_1594.MeasurementBase):
    """StiffnessPerUnitFaceWidth

    This is a mastapy class.
    """

    TYPE = _STIFFNESS_PER_UNIT_FACE_WIDTH

    class _Cast_StiffnessPerUnitFaceWidth:
        """Special nested class for casting StiffnessPerUnitFaceWidth to subclasses."""

        def __init__(self, parent: 'StiffnessPerUnitFaceWidth'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def stiffness_per_unit_face_width(self) -> 'StiffnessPerUnitFaceWidth':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StiffnessPerUnitFaceWidth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StiffnessPerUnitFaceWidth._Cast_StiffnessPerUnitFaceWidth':
        return self._Cast_StiffnessPerUnitFaceWidth(self)
