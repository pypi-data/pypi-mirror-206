"""_1388.py

ISO4156SplineJointDesign
"""
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines import _1408
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO4156_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'ISO4156SplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO4156SplineJointDesign',)


class ISO4156SplineJointDesign(_1408.StandardSplineJointDesign):
    """ISO4156SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _ISO4156_SPLINE_JOINT_DESIGN

    class _Cast_ISO4156SplineJointDesign:
        """Special nested class for casting ISO4156SplineJointDesign to subclasses."""

        def __init__(self, parent: 'ISO4156SplineJointDesign'):
            self._parent = parent

        @property
        def standard_spline_joint_design(self):
            return self._parent._cast(_1408.StandardSplineJointDesign)

        @property
        def spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1403
            
            return self._parent._cast(_1403.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(self):
            from mastapy.detailed_rigid_connectors import _1375
            
            return self._parent._cast(_1375.DetailedRigidConnectorDesign)

        @property
        def gbt3478_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1385
            
            return self._parent._cast(_1385.GBT3478SplineJointDesign)

        @property
        def jisb1603_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1389
            
            return self._parent._cast(_1389.JISB1603SplineJointDesign)

        @property
        def iso4156_spline_joint_design(self) -> 'ISO4156SplineJointDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO4156SplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def form_clearance(self) -> 'float':
        """float: 'FormClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FormClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_clearance(self) -> 'float':
        """float: 'MaximumEffectiveClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_effective_clearance(self) -> 'float':
        """float: 'MinimumEffectiveClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO4156SplineJointDesign._Cast_ISO4156SplineJointDesign':
        return self._Cast_ISO4156SplineJointDesign(self)
