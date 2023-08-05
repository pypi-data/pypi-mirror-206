"""_1009.py

CylindricalGearDesignConstraints
"""
from typing import List

from mastapy.gears.gear_designs.cylindrical import _1008
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_CONSTRAINTS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearDesignConstraints')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesignConstraints',)


class CylindricalGearDesignConstraints(_1816.NamedDatabaseItem):
    """CylindricalGearDesignConstraints

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_CONSTRAINTS

    class _Cast_CylindricalGearDesignConstraints:
        """Special nested class for casting CylindricalGearDesignConstraints to subclasses."""

        def __init__(self, parent: 'CylindricalGearDesignConstraints'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def cylindrical_gear_design_constraints(self) -> 'CylindricalGearDesignConstraints':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearDesignConstraints.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_constraints(self) -> 'List[_1008.CylindricalGearDesignConstraint]':
        """List[CylindricalGearDesignConstraint]: 'DesignConstraints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignConstraints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearDesignConstraints._Cast_CylindricalGearDesignConstraints':
        return self._Cast_CylindricalGearDesignConstraints(self)
