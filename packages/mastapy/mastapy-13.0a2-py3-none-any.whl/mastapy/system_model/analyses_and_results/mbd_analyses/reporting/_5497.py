"""_5497.py

DynamicTorqueVector3DResult
"""
from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5496
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_TORQUE_VECTOR_3D_RESULT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting', 'DynamicTorqueVector3DResult')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicTorqueVector3DResult',)


class DynamicTorqueVector3DResult(_0.APIBase):
    """DynamicTorqueVector3DResult

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_TORQUE_VECTOR_3D_RESULT

    class _Cast_DynamicTorqueVector3DResult:
        """Special nested class for casting DynamicTorqueVector3DResult to subclasses."""

        def __init__(self, parent: 'DynamicTorqueVector3DResult'):
            self._parent = parent

        @property
        def dynamic_torque_vector_3d_result(self) -> 'DynamicTorqueVector3DResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicTorqueVector3DResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude(self) -> '_5496.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'Magnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Magnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_magnitude(self) -> '_5496.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'RadialMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialMagnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def x(self) -> '_5496.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'X' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.X

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def y(self) -> '_5496.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'Y' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Y

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def z(self) -> '_5496.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'Z' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Z

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DynamicTorqueVector3DResult._Cast_DynamicTorqueVector3DResult':
        return self._Cast_DynamicTorqueVector3DResult(self)
