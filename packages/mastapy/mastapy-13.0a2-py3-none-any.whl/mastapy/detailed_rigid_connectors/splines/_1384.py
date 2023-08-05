"""_1384.py

GBT3478SplineHalfDesign
"""
from mastapy.detailed_rigid_connectors.splines import _1387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GBT3478_SPLINE_HALF_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'GBT3478SplineHalfDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('GBT3478SplineHalfDesign',)


class GBT3478SplineHalfDesign(_1387.ISO4156SplineHalfDesign):
    """GBT3478SplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _GBT3478_SPLINE_HALF_DESIGN

    class _Cast_GBT3478SplineHalfDesign:
        """Special nested class for casting GBT3478SplineHalfDesign to subclasses."""

        def __init__(self, parent: 'GBT3478SplineHalfDesign'):
            self._parent = parent

        @property
        def iso4156_spline_half_design(self):
            return self._parent._cast(_1387.ISO4156SplineHalfDesign)

        @property
        def standard_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1407
            
            return self._parent._cast(_1407.StandardSplineHalfDesign)

        @property
        def spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1402
            
            return self._parent._cast(_1402.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(self):
            from mastapy.detailed_rigid_connectors import _1376
            
            return self._parent._cast(_1376.DetailedRigidConnectorHalfDesign)

        @property
        def gbt3478_spline_half_design(self) -> 'GBT3478SplineHalfDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GBT3478SplineHalfDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign':
        return self._Cast_GBT3478SplineHalfDesign(self)
