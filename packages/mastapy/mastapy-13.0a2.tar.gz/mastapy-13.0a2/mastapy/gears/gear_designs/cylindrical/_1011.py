"""_1011.py

CylindricalGearDesignConstraintSettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_CONSTRAINT_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearDesignConstraintSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesignConstraintSettings',)


class CylindricalGearDesignConstraintSettings(_0.APIBase):
    """CylindricalGearDesignConstraintSettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_CONSTRAINT_SETTINGS

    class _Cast_CylindricalGearDesignConstraintSettings:
        """Special nested class for casting CylindricalGearDesignConstraintSettings to subclasses."""

        def __init__(self, parent: 'CylindricalGearDesignConstraintSettings'):
            self._parent = parent

        @property
        def cylindrical_gear_design_constraint_settings(self) -> 'CylindricalGearDesignConstraintSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearDesignConstraintSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearDesignConstraintSettings._Cast_CylindricalGearDesignConstraintSettings':
        return self._Cast_CylindricalGearDesignConstraintSettings(self)
