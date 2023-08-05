"""_404.py

KlingelnbergCycloPalloidHypoidGearMeshRating
"""
from typing import List

from mastapy.gears.rating.klingelnberg_conical.kn3030 import _414
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.klingelnberg_hypoid import _973
from mastapy.gears.rating.klingelnberg_hypoid import _405
from mastapy.gears.rating.klingelnberg_conical import _407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid', 'KlingelnbergCycloPalloidHypoidGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshRating',)


class KlingelnbergCycloPalloidHypoidGearMeshRating(_407.KlingelnbergCycloPalloidConicalGearMeshRating):
    """KlingelnbergCycloPalloidHypoidGearMeshRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_RATING

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMeshRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self):
            return self._parent._cast(_407.KlingelnbergCycloPalloidConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(self):
            from mastapy.gears.rating.conical import _534
            
            return self._parent._cast(_534.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _356
            
            return self._parent._cast(_356.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _349
            
            return self._parent._cast(_349.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def kn3030_pitting_and_bending_klingelnberg_mesh_single_flank_rating(self) -> '_414.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating':
        """KlingelnbergCycloPalloidHypoidMeshSingleFlankRating: 'KN3030PittingAndBendingKlingelnbergMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KN3030PittingAndBendingKlingelnbergMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def kn3030_scuffing_klingelnberg_mesh_single_flank_rating(self) -> '_414.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating':
        """KlingelnbergCycloPalloidHypoidMeshSingleFlankRating: 'KN3030ScuffingKlingelnbergMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KN3030ScuffingKlingelnbergMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_973.KlingelnbergCycloPalloidHypoidGearMeshDesign':
        """KlingelnbergCycloPalloidHypoidGearMeshDesign: 'KlingelnbergCycloPalloidHypoidGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_ratings(self) -> 'List[_405.KlingelnbergCycloPalloidHypoidGearRating]':
        """List[KlingelnbergCycloPalloidHypoidGearRating]: 'KlingelnbergCycloPalloidHypoidGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating(self)
