"""_5495.py

DynamicForceVector3DResult
"""
from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5494
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_VECTOR_3D_RESULT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting', 'DynamicForceVector3DResult')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceVector3DResult',)


class DynamicForceVector3DResult(_0.APIBase):
    """DynamicForceVector3DResult

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_VECTOR_3D_RESULT

    class _Cast_DynamicForceVector3DResult:
        """Special nested class for casting DynamicForceVector3DResult to subclasses."""

        def __init__(self, parent: 'DynamicForceVector3DResult'):
            self._parent = parent

        @property
        def dynamic_force_vector_3d_result(self) -> 'DynamicForceVector3DResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicForceVector3DResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude(self) -> '_5494.DynamicForceResultAtTime':
        """DynamicForceResultAtTime: 'Magnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Magnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def magnitude_xy(self) -> '_5494.DynamicForceResultAtTime':
        """DynamicForceResultAtTime: 'MagnitudeXY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnitudeXY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def x(self) -> '_5494.DynamicForceResultAtTime':
        """DynamicForceResultAtTime: 'X' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.X

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def y(self) -> '_5494.DynamicForceResultAtTime':
        """DynamicForceResultAtTime: 'Y' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Y

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def z(self) -> '_5494.DynamicForceResultAtTime':
        """DynamicForceResultAtTime: 'Z' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Z

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DynamicForceVector3DResult._Cast_DynamicForceVector3DResult':
        return self._Cast_DynamicForceVector3DResult(self)
