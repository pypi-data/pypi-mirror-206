"""_1052.py

LinearBacklashSepcification
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1034
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_BACKLASH_SEPCIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'LinearBacklashSepcification')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearBacklashSepcification',)


class LinearBacklashSepcification(_0.APIBase):
    """LinearBacklashSepcification

    This is a mastapy class.
    """

    TYPE = _LINEAR_BACKLASH_SEPCIFICATION

    class _Cast_LinearBacklashSepcification:
        """Special nested class for casting LinearBacklashSepcification to subclasses."""

        def __init__(self, parent: 'LinearBacklashSepcification'):
            self._parent = parent

        @property
        def linear_backlash_sepcification(self) -> 'LinearBacklashSepcification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LinearBacklashSepcification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_name(self) -> 'str':
        """str: 'FlankName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankName

        if temp is None:
            return ''

        return temp

    @property
    def circumferential_backlash_pitch_circle(self) -> '_1034.CylindricalMeshLinearBacklashSpecification':
        """CylindricalMeshLinearBacklashSpecification: 'CircumferentialBacklashPitchCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CircumferentialBacklashPitchCircle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def circumferential_backlash_reference_circle(self) -> '_1034.CylindricalMeshLinearBacklashSpecification':
        """CylindricalMeshLinearBacklashSpecification: 'CircumferentialBacklashReferenceCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CircumferentialBacklashReferenceCircle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def normal_backlash(self) -> '_1034.CylindricalMeshLinearBacklashSpecification':
        """CylindricalMeshLinearBacklashSpecification: 'NormalBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalBacklash

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_backlash(self) -> '_1034.CylindricalMeshLinearBacklashSpecification':
        """CylindricalMeshLinearBacklashSpecification: 'RadialBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialBacklash

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_backlash(self) -> 'List[_1034.CylindricalMeshLinearBacklashSpecification]':
        """List[CylindricalMeshLinearBacklashSpecification]: 'LinearBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearBacklash

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'LinearBacklashSepcification._Cast_LinearBacklashSepcification':
        return self._Cast_LinearBacklashSepcification(self)
