"""_2547.py

CycloidalAssembly
"""
from typing import List

from mastapy.cycloidal import _1441
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.cycloidal import _2549, _2548
from mastapy.system_model.part_model import _2456
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalAssembly')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssembly',)


class CycloidalAssembly(_2456.SpecialisedAssembly):
    """CycloidalAssembly

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY

    class _Cast_CycloidalAssembly:
        """Special nested class for casting CycloidalAssembly to subclasses."""

        def __init__(self, parent: 'CycloidalAssembly'):
            self._parent = parent

        @property
        def specialised_assembly(self):
            return self._parent._cast(_2456.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2414
            
            return self._parent._cast(_2414.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def cycloidal_assembly(self) -> 'CycloidalAssembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cycloidal_assembly_design(self) -> '_1441.CycloidalAssemblyDesign':
        """CycloidalAssemblyDesign: 'CycloidalAssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pins(self) -> '_2549.RingPins':
        """RingPins: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def known_designs(self) -> 'List[_1441.CycloidalAssemblyDesign]':
        """List[CycloidalAssemblyDesign]: 'KnownDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KnownDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_disc(self) -> '_2548.CycloidalDisc':
        """ 'AddDisc' is the original name of this method.

        Returns:
            mastapy.system_model.part_model.cycloidal.CycloidalDisc
        """

        method_result = self.wrapped.AddDisc()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def design_named(self, name: 'str') -> '_1441.CycloidalAssemblyDesign':
        """ 'DesignNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.cycloidal.CycloidalAssemblyDesign
        """

        name = str(name)
        method_result = self.wrapped.DesignNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_disc_from_designs(self, disc_id: 'int'):
        """ 'RemoveDiscFromDesigns' is the original name of this method.

        Args:
            disc_id (int)
        """

        disc_id = int(disc_id)
        self.wrapped.RemoveDiscFromDesigns(disc_id if disc_id else 0)

    def set_active_cycloidal_assembly_design(self, cycloidal_assembly_design: '_1441.CycloidalAssemblyDesign'):
        """ 'SetActiveCycloidalAssemblyDesign' is the original name of this method.

        Args:
            cycloidal_assembly_design (mastapy.cycloidal.CycloidalAssemblyDesign)
        """

        self.wrapped.SetActiveCycloidalAssemblyDesign(cycloidal_assembly_design.wrapped if cycloidal_assembly_design else None)

    def try_remove_design(self, design: '_1441.CycloidalAssemblyDesign') -> 'bool':
        """ 'TryRemoveDesign' is the original name of this method.

        Args:
            design (mastapy.cycloidal.CycloidalAssemblyDesign)

        Returns:
            bool
        """

        method_result = self.wrapped.TryRemoveDesign(design.wrapped if design else None)
        return method_result

    @property
    def cast_to(self) -> 'CycloidalAssembly._Cast_CycloidalAssembly':
        return self._Cast_CycloidalAssembly(self)
