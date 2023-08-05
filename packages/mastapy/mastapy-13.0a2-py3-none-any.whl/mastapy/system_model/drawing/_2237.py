"""_2237.py

ShaftDeflectionDrawingNodeItem
"""
from mastapy._internal import constructor
from mastapy.math_utility.measured_vectors import _1549
from mastapy.system_model.analyses_and_results.system_deflections import _2782
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_DEFLECTION_DRAWING_NODE_ITEM = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'ShaftDeflectionDrawingNodeItem')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftDeflectionDrawingNodeItem',)


class ShaftDeflectionDrawingNodeItem(_0.APIBase):
    """ShaftDeflectionDrawingNodeItem

    This is a mastapy class.
    """

    TYPE = _SHAFT_DEFLECTION_DRAWING_NODE_ITEM

    class _Cast_ShaftDeflectionDrawingNodeItem:
        """Special nested class for casting ShaftDeflectionDrawingNodeItem to subclasses."""

        def __init__(self, parent: 'ShaftDeflectionDrawingNodeItem'):
            self._parent = parent

        @property
        def shaft_deflection_drawing_node_item(self) -> 'ShaftDeflectionDrawingNodeItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftDeflectionDrawingNodeItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_deflection(self) -> 'float':
        """float: 'AxialDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_deflection(self) -> 'float':
        """float: 'RadialDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def node_detail(self) -> '_1549.ForceAndDisplacementResults':
        """ForceAndDisplacementResults: 'NodeDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def section_to_the_left_side(self) -> '_2782.ShaftSectionSystemDeflection':
        """ShaftSectionSystemDeflection: 'SectionToTheLeftSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectionToTheLeftSide

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def section_to_the_right_side(self) -> '_2782.ShaftSectionSystemDeflection':
        """ShaftSectionSystemDeflection: 'SectionToTheRightSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectionToTheRightSide

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftDeflectionDrawingNodeItem._Cast_ShaftDeflectionDrawingNodeItem':
        return self._Cast_ShaftDeflectionDrawingNodeItem(self)
