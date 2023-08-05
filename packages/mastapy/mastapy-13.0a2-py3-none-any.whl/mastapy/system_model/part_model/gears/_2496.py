"""_2496.py

BevelDifferentialPlanetGear
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2494
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialPlanetGear')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGear',)


class BevelDifferentialPlanetGear(_2494.BevelDifferentialGear):
    """BevelDifferentialPlanetGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR

    class _Cast_BevelDifferentialPlanetGear:
        """Special nested class for casting BevelDifferentialPlanetGear to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGear'):
            self._parent = parent

        @property
        def bevel_differential_gear(self):
            return self._parent._cast(_2494.BevelDifferentialGear)

        @property
        def bevel_gear(self):
            from mastapy.system_model.part_model.gears import _2498
            
            return self._parent._cast(_2498.BevelGear)

        @property
        def agma_gleason_conical_gear(self):
            from mastapy.system_model.part_model.gears import _2492
            
            return self._parent._cast(_2492.AGMAGleasonConicalGear)

        @property
        def conical_gear(self):
            from mastapy.system_model.part_model.gears import _2502
            
            return self._parent._cast(_2502.ConicalGear)

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
        def bevel_differential_planet_gear(self) -> 'BevelDifferentialPlanetGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_planets(self) -> 'int':
        """int: 'NumberOfPlanets' is the original name of this property."""

        temp = self.wrapped.NumberOfPlanets

        if temp is None:
            return 0

        return temp

    @number_of_planets.setter
    def number_of_planets(self, value: 'int'):
        self.wrapped.NumberOfPlanets = int(value) if value else 0

    @property
    def cast_to(self) -> 'BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear':
        return self._Cast_BevelDifferentialPlanetGear(self)
