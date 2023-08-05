"""_2821.py

CylindricalGearMeshMisalignmentValue
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MISALIGNMENT_VALUE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting', 'CylindricalGearMeshMisalignmentValue')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshMisalignmentValue',)


class CylindricalGearMeshMisalignmentValue(_0.APIBase):
    """CylindricalGearMeshMisalignmentValue

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MISALIGNMENT_VALUE

    class _Cast_CylindricalGearMeshMisalignmentValue:
        """Special nested class for casting CylindricalGearMeshMisalignmentValue to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshMisalignmentValue'):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_misalignment_value(self) -> 'CylindricalGearMeshMisalignmentValue':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshMisalignmentValue.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_name(self) -> 'str':
        """str: 'GearName' is the original name of this property."""

        temp = self.wrapped.GearName

        if temp is None:
            return ''

        return temp

    @gear_name.setter
    def gear_name(self, value: 'str'):
        self.wrapped.GearName = str(value) if value else ''

    @property
    def misalignment(self) -> 'float':
        """float: 'Misalignment' is the original name of this property."""

        temp = self.wrapped.Misalignment

        if temp is None:
            return 0.0

        return temp

    @misalignment.setter
    def misalignment(self, value: 'float'):
        self.wrapped.Misalignment = float(value) if value else 0.0

    @property
    def misalignment_due_to_tilt(self) -> 'float':
        """float: 'MisalignmentDueToTilt' is the original name of this property."""

        temp = self.wrapped.MisalignmentDueToTilt

        if temp is None:
            return 0.0

        return temp

    @misalignment_due_to_tilt.setter
    def misalignment_due_to_tilt(self, value: 'float'):
        self.wrapped.MisalignmentDueToTilt = float(value) if value else 0.0

    @property
    def misalignment_due_to_twist(self) -> 'float':
        """float: 'MisalignmentDueToTwist' is the original name of this property."""

        temp = self.wrapped.MisalignmentDueToTwist

        if temp is None:
            return 0.0

        return temp

    @misalignment_due_to_twist.setter
    def misalignment_due_to_twist(self, value: 'float'):
        self.wrapped.MisalignmentDueToTwist = float(value) if value else 0.0

    @property
    def tilt_x(self) -> 'float':
        """float: 'TiltX' is the original name of this property."""

        temp = self.wrapped.TiltX

        if temp is None:
            return 0.0

        return temp

    @tilt_x.setter
    def tilt_x(self, value: 'float'):
        self.wrapped.TiltX = float(value) if value else 0.0

    @property
    def tilt_y(self) -> 'float':
        """float: 'TiltY' is the original name of this property."""

        temp = self.wrapped.TiltY

        if temp is None:
            return 0.0

        return temp

    @tilt_y.setter
    def tilt_y(self, value: 'float'):
        self.wrapped.TiltY = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CylindricalGearMeshMisalignmentValue._Cast_CylindricalGearMeshMisalignmentValue':
        return self._Cast_CylindricalGearMeshMisalignmentValue(self)
