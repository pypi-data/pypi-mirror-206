"""_1389.py

JISB1603SplineJointDesign
"""
from mastapy.detailed_rigid_connectors.splines import _1388
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_JISB1603_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'JISB1603SplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('JISB1603SplineJointDesign',)


class JISB1603SplineJointDesign(_1388.ISO4156SplineJointDesign):
    """JISB1603SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _JISB1603_SPLINE_JOINT_DESIGN

    class _Cast_JISB1603SplineJointDesign:
        """Special nested class for casting JISB1603SplineJointDesign to subclasses."""

        def __init__(self, parent: 'JISB1603SplineJointDesign'):
            self._parent = parent

        @property
        def iso4156_spline_joint_design(self):
            return self._parent._cast(_1388.ISO4156SplineJointDesign)

        @property
        def standard_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1408
            
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
        def jisb1603_spline_joint_design(self) -> 'JISB1603SplineJointDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'JISB1603SplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'JISB1603SplineJointDesign._Cast_JISB1603SplineJointDesign':
        return self._Cast_JISB1603SplineJointDesign(self)
