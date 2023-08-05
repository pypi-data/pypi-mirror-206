"""_722.py

CylindricalGearShaverTangible
"""
from mastapy.gears.manufacturing.cylindrical.cutters import _710
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _718
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAVER_TANGIBLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CylindricalGearShaverTangible')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearShaverTangible',)


class CylindricalGearShaverTangible(_718.CutterShapeDefinition):
    """CylindricalGearShaverTangible

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAVER_TANGIBLE

    class _Cast_CylindricalGearShaverTangible:
        """Special nested class for casting CylindricalGearShaverTangible to subclasses."""

        def __init__(self, parent: 'CylindricalGearShaverTangible'):
            self._parent = parent

        @property
        def cutter_shape_definition(self):
            return self._parent._cast(_718.CutterShapeDefinition)

        @property
        def cylindrical_gear_shaver_tangible(self) -> 'CylindricalGearShaverTangible':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearShaverTangible.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self) -> '_710.CylindricalGearShaver':
        """CylindricalGearShaver: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearShaverTangible._Cast_CylindricalGearShaverTangible':
        return self._Cast_CylindricalGearShaverTangible(self)
