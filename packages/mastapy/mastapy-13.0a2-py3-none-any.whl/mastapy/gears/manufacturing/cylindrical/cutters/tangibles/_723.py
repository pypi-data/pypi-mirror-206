"""_723.py

CylindricalGearWormGrinderShape
"""
from mastapy.gears.manufacturing.cylindrical.cutters import _703
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _725
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_WORM_GRINDER_SHAPE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CylindricalGearWormGrinderShape')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearWormGrinderShape',)


class CylindricalGearWormGrinderShape(_725.RackShape):
    """CylindricalGearWormGrinderShape

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_WORM_GRINDER_SHAPE

    class _Cast_CylindricalGearWormGrinderShape:
        """Special nested class for casting CylindricalGearWormGrinderShape to subclasses."""

        def __init__(self, parent: 'CylindricalGearWormGrinderShape'):
            self._parent = parent

        @property
        def rack_shape(self):
            return self._parent._cast(_725.RackShape)

        @property
        def cutter_shape_definition(self):
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _718
            
            return self._parent._cast(_718.CutterShapeDefinition)

        @property
        def cylindrical_gear_worm_grinder_shape(self) -> 'CylindricalGearWormGrinderShape':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearWormGrinderShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self) -> '_703.CylindricalGearGrindingWorm':
        """CylindricalGearGrindingWorm: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearWormGrinderShape._Cast_CylindricalGearWormGrinderShape':
        return self._Cast_CylindricalGearWormGrinderShape(self)
