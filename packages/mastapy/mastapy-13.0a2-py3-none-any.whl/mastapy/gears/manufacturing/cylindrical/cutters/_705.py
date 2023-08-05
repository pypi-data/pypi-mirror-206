"""_705.py

CylindricalGearPlungeShaver
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical import _608
from mastapy.gears.manufacturing.cylindrical.cutters import _710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLUNGE_SHAVER = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearPlungeShaver')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPlungeShaver',)


class CylindricalGearPlungeShaver(_710.CylindricalGearShaver):
    """CylindricalGearPlungeShaver

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLUNGE_SHAVER

    class _Cast_CylindricalGearPlungeShaver:
        """Special nested class for casting CylindricalGearPlungeShaver to subclasses."""

        def __init__(self, parent: 'CylindricalGearPlungeShaver'):
            self._parent = parent

        @property
        def cylindrical_gear_shaver(self):
            return self._parent._cast(_710.CylindricalGearShaver)

        @property
        def involute_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713
            
            return self._parent._cast(_713.InvoluteCutterDesign)

        @property
        def cylindrical_gear_real_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _708
            
            return self._parent._cast(_708.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _701
            
            return self._parent._cast(_701.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def cylindrical_gear_plunge_shaver(self) -> 'CylindricalGearPlungeShaver':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearPlungeShaver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def has_tolerances(self) -> 'bool':
        """bool: 'HasTolerances' is the original name of this property."""

        temp = self.wrapped.HasTolerances

        if temp is None:
            return False

        return temp

    @has_tolerances.setter
    def has_tolerances(self, value: 'bool'):
        self.wrapped.HasTolerances = bool(value) if value else False

    @property
    def left_flank_micro_geometry(self) -> '_608.CylindricalGearSpecifiedMicroGeometry':
        """CylindricalGearSpecifiedMicroGeometry: 'LeftFlankMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_micro_geometry(self) -> '_608.CylindricalGearSpecifiedMicroGeometry':
        """CylindricalGearSpecifiedMicroGeometry: 'RightFlankMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry(self) -> 'List[_608.CylindricalGearSpecifiedMicroGeometry]':
        """List[CylindricalGearSpecifiedMicroGeometry]: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver':
        return self._Cast_CylindricalGearPlungeShaver(self)
