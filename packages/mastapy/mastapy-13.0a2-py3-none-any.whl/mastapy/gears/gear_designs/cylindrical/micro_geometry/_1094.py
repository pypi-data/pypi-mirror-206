"""_1094.py

CylindricalGearMicroGeometry
"""
from typing import List

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1089, _1115, _1095
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometry',)


class CylindricalGearMicroGeometry(_1095.CylindricalGearMicroGeometryBase):
    """CylindricalGearMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY

    class _Cast_CylindricalGearMicroGeometry:
        """Special nested class for casting CylindricalGearMicroGeometry to subclasses."""

        def __init__(self, parent: 'CylindricalGearMicroGeometry'):
            self._parent = parent

        @property
        def cylindrical_gear_micro_geometry_base(self):
            return self._parent._cast(_1095.CylindricalGearMicroGeometryBase)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_micro_geometry(self) -> 'CylindricalGearMicroGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank(self) -> '_1089.CylindricalGearFlankMicroGeometry':
        """CylindricalGearFlankMicroGeometry: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_1089.CylindricalGearFlankMicroGeometry':
        """CylindricalGearFlankMicroGeometry: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def flanks(self) -> 'List[_1089.CylindricalGearFlankMicroGeometry]':
        """List[CylindricalGearFlankMicroGeometry]: 'Flanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gears(self) -> 'List[_1115.MeshedCylindricalGearMicroGeometry]':
        """List[MeshedCylindricalGearMicroGeometry]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def both_flanks(self) -> '_1089.CylindricalGearFlankMicroGeometry':
        """CylindricalGearFlankMicroGeometry: 'BothFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearMicroGeometry._Cast_CylindricalGearMicroGeometry':
        return self._Cast_CylindricalGearMicroGeometry(self)
