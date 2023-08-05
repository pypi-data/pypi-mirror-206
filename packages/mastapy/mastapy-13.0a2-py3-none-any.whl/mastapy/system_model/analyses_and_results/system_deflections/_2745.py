"""_2745.py

InformationForContactAtPointAlongFaceWidth
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INFORMATION_FOR_CONTACT_AT_POINT_ALONG_FACE_WIDTH = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'InformationForContactAtPointAlongFaceWidth')


__docformat__ = 'restructuredtext en'
__all__ = ('InformationForContactAtPointAlongFaceWidth',)


class InformationForContactAtPointAlongFaceWidth(_0.APIBase):
    """InformationForContactAtPointAlongFaceWidth

    This is a mastapy class.
    """

    TYPE = _INFORMATION_FOR_CONTACT_AT_POINT_ALONG_FACE_WIDTH

    class _Cast_InformationForContactAtPointAlongFaceWidth:
        """Special nested class for casting InformationForContactAtPointAlongFaceWidth to subclasses."""

        def __init__(self, parent: 'InformationForContactAtPointAlongFaceWidth'):
            self._parent = parent

        @property
        def information_for_contact_at_point_along_face_width(self) -> 'InformationForContactAtPointAlongFaceWidth':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InformationForContactAtPointAlongFaceWidth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def force_per_unit_length(self) -> 'float':
        """float: 'ForcePerUnitLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForcePerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_per_unit_length(self) -> 'float':
        """float: 'StiffnessPerUnitLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessPerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_penetration(self) -> 'float':
        """float: 'SurfacePenetration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfacePenetration

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'InformationForContactAtPointAlongFaceWidth._Cast_InformationForContactAtPointAlongFaceWidth':
        return self._Cast_InformationForContactAtPointAlongFaceWidth(self)
