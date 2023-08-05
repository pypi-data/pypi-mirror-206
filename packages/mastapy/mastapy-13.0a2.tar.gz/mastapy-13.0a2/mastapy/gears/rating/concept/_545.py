"""_545.py

ConceptGearMeshRating
"""
from typing import List

from mastapy.gears.gear_designs.concept import _1171
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.concept import _546
from mastapy.gears.rating import _356
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Concept', 'ConceptGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshRating',)


class ConceptGearMeshRating(_356.GearMeshRating):
    """ConceptGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_RATING

    class _Cast_ConceptGearMeshRating:
        """Special nested class for casting ConceptGearMeshRating to subclasses."""

        def __init__(self, parent: 'ConceptGearMeshRating'):
            self._parent = parent

        @property
        def gear_mesh_rating(self):
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
        def concept_gear_mesh_rating(self) -> 'ConceptGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concept_gear_mesh(self) -> '_1171.ConceptGearMeshDesign':
        """ConceptGearMeshDesign: 'ConceptGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gear_ratings(self) -> 'List[_546.ConceptGearRating]':
        """List[ConceptGearRating]: 'ConceptGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearMeshRating._Cast_ConceptGearMeshRating':
        return self._Cast_ConceptGearMeshRating(self)
