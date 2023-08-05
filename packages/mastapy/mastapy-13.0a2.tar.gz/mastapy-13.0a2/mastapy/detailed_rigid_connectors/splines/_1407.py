"""_1407.py

StandardSplineHalfDesign
"""
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines import _1402
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_SPLINE_HALF_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'StandardSplineHalfDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StandardSplineHalfDesign',)


class StandardSplineHalfDesign(_1402.SplineHalfDesign):
    """StandardSplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _STANDARD_SPLINE_HALF_DESIGN

    class _Cast_StandardSplineHalfDesign:
        """Special nested class for casting StandardSplineHalfDesign to subclasses."""

        def __init__(self, parent: 'StandardSplineHalfDesign'):
            self._parent = parent

        @property
        def spline_half_design(self):
            return self._parent._cast(_1402.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(self):
            from mastapy.detailed_rigid_connectors import _1376
            
            return self._parent._cast(_1376.DetailedRigidConnectorHalfDesign)

        @property
        def din5480_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1380
            
            return self._parent._cast(_1380.DIN5480SplineHalfDesign)

        @property
        def gbt3478_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1384
            
            return self._parent._cast(_1384.GBT3478SplineHalfDesign)

        @property
        def iso4156_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1387
            
            return self._parent._cast(_1387.ISO4156SplineHalfDesign)

        @property
        def sae_spline_half_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1395
            
            return self._parent._cast(_1395.SAESplineHalfDesign)

        @property
        def standard_spline_half_design(self) -> 'StandardSplineHalfDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StandardSplineHalfDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def root_fillet_radius_factor(self) -> 'float':
        """float: 'RootFilletRadiusFactor' is the original name of this property."""

        temp = self.wrapped.RootFilletRadiusFactor

        if temp is None:
            return 0.0

        return temp

    @root_fillet_radius_factor.setter
    def root_fillet_radius_factor(self, value: 'float'):
        self.wrapped.RootFilletRadiusFactor = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'StandardSplineHalfDesign._Cast_StandardSplineHalfDesign':
        return self._Cast_StandardSplineHalfDesign(self)
