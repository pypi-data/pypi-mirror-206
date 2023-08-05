"""_1019.py

CylindricalGearPinionTypeCutterFlank
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1018, _1002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PINION_TYPE_CUTTER_FLANK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearPinionTypeCutterFlank')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPinionTypeCutterFlank',)


class CylindricalGearPinionTypeCutterFlank(_1002.CylindricalGearAbstractRackFlank):
    """CylindricalGearPinionTypeCutterFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PINION_TYPE_CUTTER_FLANK

    class _Cast_CylindricalGearPinionTypeCutterFlank:
        """Special nested class for casting CylindricalGearPinionTypeCutterFlank to subclasses."""

        def __init__(self, parent: 'CylindricalGearPinionTypeCutterFlank'):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_rack_flank(self):
            return self._parent._cast(_1002.CylindricalGearAbstractRackFlank)

        @property
        def cylindrical_gear_pinion_type_cutter_flank(self) -> 'CylindricalGearPinionTypeCutterFlank':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearPinionTypeCutterFlank.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def residual_fillet_undercut(self) -> 'float':
        """float: 'ResidualFilletUndercut' is the original name of this property."""

        temp = self.wrapped.ResidualFilletUndercut

        if temp is None:
            return 0.0

        return temp

    @residual_fillet_undercut.setter
    def residual_fillet_undercut(self, value: 'float'):
        self.wrapped.ResidualFilletUndercut = float(value) if value else 0.0

    @property
    def cutter(self) -> '_1018.CylindricalGearPinionTypeCutter':
        """CylindricalGearPinionTypeCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearPinionTypeCutterFlank._Cast_CylindricalGearPinionTypeCutterFlank':
        return self._Cast_CylindricalGearPinionTypeCutterFlank(self)
