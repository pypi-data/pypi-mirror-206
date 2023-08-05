"""_1466.py

DetailedBoltedJointDesign
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bolts import _1470
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_BOLTED_JOINT_DESIGN = python_net_import('SMT.MastaAPI.Bolts', 'DetailedBoltedJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('DetailedBoltedJointDesign',)


class DetailedBoltedJointDesign(_0.APIBase):
    """DetailedBoltedJointDesign

    This is a mastapy class.
    """

    TYPE = _DETAILED_BOLTED_JOINT_DESIGN

    class _Cast_DetailedBoltedJointDesign:
        """Special nested class for casting DetailedBoltedJointDesign to subclasses."""

        def __init__(self, parent: 'DetailedBoltedJointDesign'):
            self._parent = parent

        @property
        def detailed_bolted_joint_design(self) -> 'DetailedBoltedJointDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DetailedBoltedJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def number_of_bolts(self) -> 'int':
        """int: 'NumberOfBolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfBolts

        if temp is None:
            return 0

        return temp

    @property
    def loaded_bolts(self) -> 'List[_1470.LoadedBolt]':
        """List[LoadedBolt]: 'LoadedBolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DetailedBoltedJointDesign._Cast_DetailedBoltedJointDesign':
        return self._Cast_DetailedBoltedJointDesign(self)
