"""_1027.py

CylindricalGearSetMicroGeometrySettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearSetMicroGeometrySettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetMicroGeometrySettings',)


class CylindricalGearSetMicroGeometrySettings(_0.APIBase):
    """CylindricalGearSetMicroGeometrySettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_SETTINGS

    class _Cast_CylindricalGearSetMicroGeometrySettings:
        """Special nested class for casting CylindricalGearSetMicroGeometrySettings to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetMicroGeometrySettings'):
            self._parent = parent

        @property
        def cylindrical_gear_set_micro_geometry_settings(self) -> 'CylindricalGearSetMicroGeometrySettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetMicroGeometrySettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearSetMicroGeometrySettings._Cast_CylindricalGearSetMicroGeometrySettings':
        return self._Cast_CylindricalGearSetMicroGeometrySettings(self)
