"""_2367.py

FESubstructureNodeModeShapes
"""
from typing import List

from mastapy.system_model.fe import _2365, _2366
from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1487
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_NODE_MODE_SHAPES = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FESubstructureNodeModeShapes')


__docformat__ = 'restructuredtext en'
__all__ = ('FESubstructureNodeModeShapes',)


class FESubstructureNodeModeShapes(_0.APIBase):
    """FESubstructureNodeModeShapes

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_NODE_MODE_SHAPES

    class _Cast_FESubstructureNodeModeShapes:
        """Special nested class for casting FESubstructureNodeModeShapes to subclasses."""

        def __init__(self, parent: 'FESubstructureNodeModeShapes'):
            self._parent = parent

        @property
        def fe_substructure_node_mode_shapes(self) -> 'FESubstructureNodeModeShapes':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FESubstructureNodeModeShapes.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def condensation_node(self) -> '_2365.FESubstructureNode':
        """FESubstructureNode: 'CondensationNode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CondensationNode

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connected_component_local_coordinate_system(self) -> '_1487.CoordinateSystem3D':
        """CoordinateSystem3D: 'ConnectedComponentLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponentLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mode_shapes_at_condensation_node(self) -> 'List[_2366.FESubstructureNodeModeShape]':
        """List[FESubstructureNodeModeShape]: 'ModeShapesAtCondensationNode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModeShapesAtCondensationNode

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FESubstructureNodeModeShapes._Cast_FESubstructureNodeModeShapes':
        return self._Cast_FESubstructureNodeModeShapes(self)
