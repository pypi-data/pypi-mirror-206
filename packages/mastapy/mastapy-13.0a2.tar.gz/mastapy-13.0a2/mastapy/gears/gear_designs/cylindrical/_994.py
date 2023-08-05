"""_994.py

BacklashSpecification
"""
from typing import List

from mastapy.gears.gear_designs.cylindrical import _1052, _1031, _1062
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BACKLASH_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'BacklashSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('BacklashSpecification',)


class BacklashSpecification(_1062.RelativeValuesSpecification['BacklashSpecification']):
    """BacklashSpecification

    This is a mastapy class.
    """

    TYPE = _BACKLASH_SPECIFICATION

    class _Cast_BacklashSpecification:
        """Special nested class for casting BacklashSpecification to subclasses."""

        def __init__(self, parent: 'BacklashSpecification'):
            self._parent = parent

        @property
        def relative_values_specification(self):
            from mastapy.gears.gear_designs.cylindrical import _994
            
            return self._parent._cast(_1062.RelativeValuesSpecification)

        @property
        def backlash_specification(self) -> 'BacklashSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BacklashSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank(self) -> '_1052.LinearBacklashSepcification':
        """LinearBacklashSepcification: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_1052.LinearBacklashSepcification':
        """LinearBacklashSepcification: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def angular_backlash(self) -> 'List[_1031.CylindricalMeshAngularBacklash]':
        """List[CylindricalMeshAngularBacklash]: 'AngularBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularBacklash

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flanks(self) -> 'List[_1052.LinearBacklashSepcification]':
        """List[LinearBacklashSepcification]: 'Flanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def both_flanks(self) -> '_1052.LinearBacklashSepcification':
        """LinearBacklashSepcification: 'BothFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BacklashSpecification._Cast_BacklashSpecification':
        return self._Cast_BacklashSpecification(self)
