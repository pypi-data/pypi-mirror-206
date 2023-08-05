"""_1378.py

CustomSplineJointDesign
"""
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines import _1403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'CustomSplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomSplineJointDesign',)


class CustomSplineJointDesign(_1403.SplineJointDesign):
    """CustomSplineJointDesign

    This is a mastapy class.
    """

    TYPE = _CUSTOM_SPLINE_JOINT_DESIGN

    class _Cast_CustomSplineJointDesign:
        """Special nested class for casting CustomSplineJointDesign to subclasses."""

        def __init__(self, parent: 'CustomSplineJointDesign'):
            self._parent = parent

        @property
        def spline_joint_design(self):
            return self._parent._cast(_1403.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(self):
            from mastapy.detailed_rigid_connectors import _1375
            
            return self._parent._cast(_1375.DetailedRigidConnectorDesign)

        @property
        def custom_spline_joint_design(self) -> 'CustomSplineJointDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomSplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pressure_angle(self) -> 'float':
        """float: 'PressureAngle' is the original name of this property."""

        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    def pressure_angle(self, value: 'float'):
        self.wrapped.PressureAngle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CustomSplineJointDesign._Cast_CustomSplineJointDesign':
        return self._Cast_CustomSplineJointDesign(self)
