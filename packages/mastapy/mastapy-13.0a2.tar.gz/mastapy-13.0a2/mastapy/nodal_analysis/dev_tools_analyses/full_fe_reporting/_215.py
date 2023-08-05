"""_215.py

NodeDetailsForFEModel
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_DETAILS_FOR_FE_MODEL = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'NodeDetailsForFEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('NodeDetailsForFEModel',)


class NodeDetailsForFEModel(_0.APIBase):
    """NodeDetailsForFEModel

    This is a mastapy class.
    """

    TYPE = _NODE_DETAILS_FOR_FE_MODEL

    class _Cast_NodeDetailsForFEModel:
        """Special nested class for casting NodeDetailsForFEModel to subclasses."""

        def __init__(self, parent: 'NodeDetailsForFEModel'):
            self._parent = parent

        @property
        def node_details_for_fe_model(self) -> 'NodeDetailsForFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodeDetailsForFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def external_ids(self) -> 'List[int]':
        """List[int]: 'ExternalIDs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExternalIDs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)
        return value

    @property
    def node_positions(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'NodePositions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePositions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'NodeDetailsForFEModel._Cast_NodeDetailsForFEModel':
        return self._Cast_NodeDetailsForFEModel(self)
