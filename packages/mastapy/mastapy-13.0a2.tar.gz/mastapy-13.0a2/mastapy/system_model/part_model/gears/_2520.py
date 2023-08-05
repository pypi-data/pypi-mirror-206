"""_2520.py

KlingelnbergCycloPalloidSpiralBevelGearSet
"""
from typing import List

from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _970
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2519, _2516
from mastapy.system_model.connections_and_sockets.gears import _2301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSet',)


class KlingelnbergCycloPalloidSpiralBevelGearSet(_2516.KlingelnbergCycloPalloidConicalGearSet):
    """KlingelnbergCycloPalloidSpiralBevelGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSet:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSet to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearSet'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(self):
            return self._parent._cast(_2516.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2503
            
            return self._parent._cast(_2503.ConicalGearSet)

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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_conical_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergCycloPalloidSpiralBevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears(self) -> 'List[_2519.KlingelnbergCycloPalloidSpiralBevelGear]':
        """List[KlingelnbergCycloPalloidSpiralBevelGear]: 'KlingelnbergCycloPalloidSpiralBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes(self) -> 'List[_2301.KlingelnbergCycloPalloidSpiralBevelGearMesh]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMesh]: 'KlingelnbergCycloPalloidSpiralBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet(self)
