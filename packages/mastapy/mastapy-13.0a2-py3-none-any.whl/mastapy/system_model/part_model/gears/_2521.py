"""_2521.py

PlanetaryGearSet
"""
from typing import List

from mastapy.system_model.part_model.gears import _2504, _2506, _2505
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'PlanetaryGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSet',)


class PlanetaryGearSet(_2505.CylindricalGearSet):
    """PlanetaryGearSet

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET

    class _Cast_PlanetaryGearSet:
        """Special nested class for casting PlanetaryGearSet to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSet'):
            self._parent = parent

        @property
        def cylindrical_gear_set(self):
            return self._parent._cast(_2505.CylindricalGearSet)

        @property
        def gear_set(self):
            from mastapy.system_model.part_model.gears import _2511
            
            return self._parent._cast(_2511.GearSet)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2456
            
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
        def planetary_gear_set(self) -> 'PlanetaryGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def annuluses(self) -> 'List[_2504.CylindricalGear]':
        """List[CylindricalGear]: 'Annuluses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Annuluses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planets(self) -> 'List[_2506.CylindricalPlanetGear]':
        """List[CylindricalPlanetGear]: 'Planets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def suns(self) -> 'List[_2504.CylindricalGear]':
        """List[CylindricalGear]: 'Suns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Suns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_annulus(self) -> '_2504.CylindricalGear':
        """ 'AddAnnulus' is the original name of this method.

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGear
        """

        method_result = self.wrapped.AddAnnulus()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_planet(self) -> '_2504.CylindricalGear':
        """ 'AddPlanet' is the original name of this method.

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGear
        """

        method_result = self.wrapped.AddPlanet()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_sun(self) -> '_2504.CylindricalGear':
        """ 'AddSun' is the original name of this method.

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGear
        """

        method_result = self.wrapped.AddSun()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def set_number_of_planets(self, amount: 'int'):
        """ 'SetNumberOfPlanets' is the original name of this method.

        Args:
            amount (int)
        """

        amount = int(amount)
        self.wrapped.SetNumberOfPlanets(amount if amount else 0)

    @property
    def cast_to(self) -> 'PlanetaryGearSet._Cast_PlanetaryGearSet':
        return self._Cast_PlanetaryGearSet(self)
