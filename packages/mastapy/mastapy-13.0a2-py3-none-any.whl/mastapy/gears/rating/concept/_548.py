"""_548.py

ConceptGearSetRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.concept import _1172
from mastapy.gears.rating.concept import _546, _545
from mastapy.gears.rating import _359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Concept', 'ConceptGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetRating',)


class ConceptGearSetRating(_359.GearSetRating):
    """ConceptGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_RATING

    class _Cast_ConceptGearSetRating:
        """Special nested class for casting ConceptGearSetRating to subclasses."""

        def __init__(self, parent: 'ConceptGearSetRating'):
            self._parent = parent

        @property
        def gear_set_rating(self):
            return self._parent._cast(_359.GearSetRating)

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def concept_gear_set_rating(self) -> 'ConceptGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> 'str':
        """str: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return ''

        return temp

    @property
    def concept_gear_set(self) -> '_1172.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ConceptGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_546.ConceptGearRating]':
        """List[ConceptGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
    def concept_mesh_ratings(self) -> 'List[_545.ConceptGearMeshRating]':
        """List[ConceptGearMeshRating]: 'ConceptMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetRating._Cast_ConceptGearSetRating':
        return self._Cast_ConceptGearSetRating(self)
