"""_540.py

ConicalMeshedGearRating
"""
from mastapy.gears.gear_designs.conical import _1146
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalMeshedGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshedGearRating',)


class ConicalMeshedGearRating(_0.APIBase):
    """ConicalMeshedGearRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_GEAR_RATING

    class _Cast_ConicalMeshedGearRating:
        """Special nested class for casting ConicalMeshedGearRating to subclasses."""

        def __init__(self, parent: 'ConicalMeshedGearRating'):
            self._parent = parent

        @property
        def straight_bevel_diff_meshed_gear_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _397
            
            return self._parent._cast(_397.StraightBevelDiffMeshedGearRating)

        @property
        def conical_meshed_gear_rating(self) -> 'ConicalMeshedGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshedGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self) -> '_1146.ConicalFlanks':
        """ConicalFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1146.ConicalFlanks)
        return constructor.new_from_mastapy_type(_1146.ConicalFlanks)(value) if value is not None else None

    @property
    def axial_force(self) -> 'float':
        """float: 'AxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_force_type(self) -> 'str':
        """str: 'AxialForceType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialForceType

        if temp is None:
            return ''

        return temp

    @property
    def gleason_axial_factor(self) -> 'float':
        """float: 'GleasonAxialFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonAxialFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor(self) -> 'float':
        """float: 'GleasonSeparatingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonSeparatingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def normal_force(self) -> 'float':
        """float: 'NormalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force(self) -> 'float':
        """float: 'RadialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force_type(self) -> 'str':
        """str: 'RadialForceType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialForceType

        if temp is None:
            return ''

        return temp

    @property
    def tangential_force(self) -> 'float':
        """float: 'TangentialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ConicalMeshedGearRating._Cast_ConicalMeshedGearRating':
        return self._Cast_ConicalMeshedGearRating(self)
