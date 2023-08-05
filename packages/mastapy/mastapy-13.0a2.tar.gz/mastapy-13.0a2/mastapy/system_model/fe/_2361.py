"""_2361.py

FEStiffnessGeometry
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_STIFFNESS_GEOMETRY = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FEStiffnessGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FEStiffnessGeometry',)


class FEStiffnessGeometry(_0.APIBase):
    """FEStiffnessGeometry

    This is a mastapy class.
    """

    TYPE = _FE_STIFFNESS_GEOMETRY

    class _Cast_FEStiffnessGeometry:
        """Special nested class for casting FEStiffnessGeometry to subclasses."""

        def __init__(self, parent: 'FEStiffnessGeometry'):
            self._parent = parent

        @property
        def fe_stiffness_geometry(self) -> 'FEStiffnessGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEStiffnessGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    def delete_geometry(self):
        """ 'DeleteGeometry' is the original name of this method."""

        self.wrapped.DeleteGeometry()

    def reduce_file_size(self):
        """ 'ReduceFileSize' is the original name of this method."""

        self.wrapped.ReduceFileSize()

    @property
    def cast_to(self) -> 'FEStiffnessGeometry._Cast_FEStiffnessGeometry':
        return self._Cast_FEStiffnessGeometry(self)
