"""_2433.py

FEPart
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.fe import _2363
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility import _1487
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2416
from mastapy._internal.cast_exception import CastException

_STRING = python_net_import('System', 'String')
_FE_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FEPart')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPart',)


class FEPart(_2416.AbstractShaftOrHousing):
    """FEPart

    This is a mastapy class.
    """

    TYPE = _FE_PART

    class _Cast_FEPart:
        """Special nested class for casting FEPart to subclasses."""

        def __init__(self, parent: 'FEPart'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing(self):
            return self._parent._cast(_2416.AbstractShaftOrHousing)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def fe_part(self) -> 'FEPart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def three_d_node_size(self) -> 'float':
        """float: 'ThreeDNodeSize' is the original name of this property."""

        temp = self.wrapped.ThreeDNodeSize

        if temp is None:
            return 0.0

        return temp

    @three_d_node_size.setter
    def three_d_node_size(self, value: 'float'):
        self.wrapped.ThreeDNodeSize = float(value) if value else 0.0

    @property
    def default_fe_substructure(self) -> 'list_with_selected_item.ListWithSelectedItem_FESubstructure':
        """list_with_selected_item.ListWithSelectedItem_FESubstructure: 'DefaultFESubstructure' is the original name of this property."""

        temp = self.wrapped.DefaultFESubstructure

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_FESubstructure)(temp) if temp is not None else None

    @default_fe_substructure.setter
    def default_fe_substructure(self, value: 'list_with_selected_item.ListWithSelectedItem_FESubstructure.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_FESubstructure.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_FESubstructure.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.DefaultFESubstructure = value

    @property
    def knows_scalar_mass(self) -> 'bool':
        """bool: 'KnowsScalarMass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KnowsScalarMass

        if temp is None:
            return False

        return temp

    @property
    def local_coordinate_system(self) -> '_1487.CoordinateSystem3D':
        """CoordinateSystem3D: 'LocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_fe_substructure(self) -> '_2363.FESubstructure':
        """ 'CreateFESubstructure' is the original name of this method.

        Returns:
            mastapy.system_model.fe.FESubstructure
        """

        method_result = self.wrapped.CreateFESubstructure()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_fe_substructure_with_name(self, name: 'str') -> '_2363.FESubstructure':
        """ 'CreateFESubstructure' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.fe.FESubstructure
        """

        name = str(name)
        method_result = self.wrapped.CreateFESubstructure.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_fe_substructure(self, fe_substructure: '_2363.FESubstructure') -> 'bool':
        """ 'RemoveFESubstructure' is the original name of this method.

        Args:
            fe_substructure (mastapy.system_model.fe.FESubstructure)

        Returns:
            bool
        """

        method_result = self.wrapped.RemoveFESubstructure(fe_substructure.wrapped if fe_substructure else None)
        return method_result

    def select_fe_substructure(self, fe_substructure: '_2363.FESubstructure'):
        """ 'SelectFESubstructure' is the original name of this method.

        Args:
            fe_substructure (mastapy.system_model.fe.FESubstructure)
        """

        self.wrapped.SelectFESubstructure(fe_substructure.wrapped if fe_substructure else None)

    @property
    def cast_to(self) -> 'FEPart._Cast_FEPart':
        return self._Cast_FEPart(self)
