"""_2506.py

CylindricalPlanetGear
"""
from mastapy.system_model.part_model.gears import _2504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalPlanetGear')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGear',)


class CylindricalPlanetGear(_2504.CylindricalGear):
    """CylindricalPlanetGear

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR

    class _Cast_CylindricalPlanetGear:
        """Special nested class for casting CylindricalPlanetGear to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGear'):
            self._parent = parent

        @property
        def cylindrical_gear(self):
            return self._parent._cast(_2504.CylindricalGear)

        @property
        def gear(self):
            from mastapy.system_model.part_model.gears import _2509
            
            return self._parent._cast(_2509.Gear)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2444
            
            return self._parent._cast(_2444.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def cylindrical_planet_gear(self) -> 'CylindricalPlanetGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalPlanetGear._Cast_CylindricalPlanetGear':
        return self._Cast_CylindricalPlanetGear(self)
