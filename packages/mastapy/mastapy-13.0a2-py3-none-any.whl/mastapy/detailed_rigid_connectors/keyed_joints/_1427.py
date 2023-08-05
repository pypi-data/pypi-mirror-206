"""_1427.py

KeywayJointHalfDesign
"""
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.interference_fits import _1434
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KEYWAY_JOINT_HALF_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints', 'KeywayJointHalfDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('KeywayJointHalfDesign',)


class KeywayJointHalfDesign(_1434.InterferenceFitHalfDesign):
    """KeywayJointHalfDesign

    This is a mastapy class.
    """

    TYPE = _KEYWAY_JOINT_HALF_DESIGN

    class _Cast_KeywayJointHalfDesign:
        """Special nested class for casting KeywayJointHalfDesign to subclasses."""

        def __init__(self, parent: 'KeywayJointHalfDesign'):
            self._parent = parent

        @property
        def interference_fit_half_design(self):
            return self._parent._cast(_1434.InterferenceFitHalfDesign)

        @property
        def detailed_rigid_connector_half_design(self):
            from mastapy.detailed_rigid_connectors import _1376
            
            return self._parent._cast(_1376.DetailedRigidConnectorHalfDesign)

        @property
        def keyway_joint_half_design(self) -> 'KeywayJointHalfDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KeywayJointHalfDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_keyway_depth(self) -> 'float':
        """float: 'EffectiveKeywayDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveKeywayDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_factor(self) -> 'float':
        """float: 'HardnessFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HardnessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def is_case_hardened(self) -> 'bool':
        """bool: 'IsCaseHardened' is the original name of this property."""

        temp = self.wrapped.IsCaseHardened

        if temp is None:
            return False

        return temp

    @is_case_hardened.setter
    def is_case_hardened(self, value: 'bool'):
        self.wrapped.IsCaseHardened = bool(value) if value else False

    @property
    def keyway_chamfer_depth(self) -> 'float':
        """float: 'KeywayChamferDepth' is the original name of this property."""

        temp = self.wrapped.KeywayChamferDepth

        if temp is None:
            return 0.0

        return temp

    @keyway_chamfer_depth.setter
    def keyway_chamfer_depth(self, value: 'float'):
        self.wrapped.KeywayChamferDepth = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def support_factor(self) -> 'float':
        """float: 'SupportFactor' is the original name of this property."""

        temp = self.wrapped.SupportFactor

        if temp is None:
            return 0.0

        return temp

    @support_factor.setter
    def support_factor(self, value: 'float'):
        self.wrapped.SupportFactor = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'KeywayJointHalfDesign._Cast_KeywayJointHalfDesign':
        return self._Cast_KeywayJointHalfDesign(self)
