"""_942.py

GearDesign
"""
from mastapy._internal import constructor
from mastapy.gears.fe_model import _1191
from mastapy.gears.gear_designs import _943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('GearDesign',)


class GearDesign(_943.GearDesignComponent):
    """GearDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN

    class _Cast_GearDesign:
        """Special nested class for casting GearDesign to subclasses."""

        def __init__(self, parent: 'GearDesign'):
            self._parent = parent

        @property
        def gear_design_component(self):
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _947
            
            return self._parent._cast(_947.ZerolBevelGearDesign)

        @property
        def worm_design(self):
            from mastapy.gears.gear_designs.worm import _951
            
            return self._parent._cast(_951.WormDesign)

        @property
        def worm_gear_design(self):
            from mastapy.gears.gear_designs.worm import _952
            
            return self._parent._cast(_952.WormGearDesign)

        @property
        def worm_wheel_design(self):
            from mastapy.gears.gear_designs.worm import _955
            
            return self._parent._cast(_955.WormWheelDesign)

        @property
        def straight_bevel_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _956
            
            return self._parent._cast(_956.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _960
            
            return self._parent._cast(_960.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _964
            
            return self._parent._cast(_964.SpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _968
            
            return self._parent._cast(_968.KlingelnbergCycloPalloidSpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _972
            
            return self._parent._cast(_972.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _976
            
            return self._parent._cast(_976.KlingelnbergConicalGearDesign)

        @property
        def hypoid_gear_design(self):
            from mastapy.gears.gear_designs.hypoid import _980
            
            return self._parent._cast(_980.HypoidGearDesign)

        @property
        def face_gear_design(self):
            from mastapy.gears.gear_designs.face import _984
            
            return self._parent._cast(_984.FaceGearDesign)

        @property
        def face_gear_pinion_design(self):
            from mastapy.gears.gear_designs.face import _989
            
            return self._parent._cast(_989.FaceGearPinionDesign)

        @property
        def face_gear_wheel_design(self):
            from mastapy.gears.gear_designs.face import _992
            
            return self._parent._cast(_992.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1007
            
            return self._parent._cast(_1007.CylindricalGearDesign)

        @property
        def cylindrical_planet_gear_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1036
            
            return self._parent._cast(_1036.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1148
            
            return self._parent._cast(_1148.ConicalGearDesign)

        @property
        def concept_gear_design(self):
            from mastapy.gears.gear_designs.concept import _1170
            
            return self._parent._cast(_1170.ConceptGearDesign)

        @property
        def bevel_gear_design(self):
            from mastapy.gears.gear_designs.bevel import _1174
            
            return self._parent._cast(_1174.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1187
            
            return self._parent._cast(_1187.AGMAGleasonConicalGearDesign)

        @property
        def gear_design(self) -> 'GearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_shaft_inner_diameter(self) -> 'float':
        """float: 'AbsoluteShaftInnerDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

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
    def mass(self) -> 'float':
        """float: 'Mass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def names_of_meshing_gears(self) -> 'str':
        """str: 'NamesOfMeshingGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NamesOfMeshingGears

        if temp is None:
            return ''

        return temp

    @property
    def number_of_teeth(self) -> 'int':
        """int: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'int'):
        self.wrapped.NumberOfTeeth = int(value) if value else 0

    @property
    def number_of_teeth_maintaining_ratio(self) -> 'int':
        """int: 'NumberOfTeethMaintainingRatio' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethMaintainingRatio

        if temp is None:
            return 0

        return temp

    @number_of_teeth_maintaining_ratio.setter
    def number_of_teeth_maintaining_ratio(self, value: 'int'):
        self.wrapped.NumberOfTeethMaintainingRatio = int(value) if value else 0

    @property
    def shaft_inner_diameter(self) -> 'float':
        """float: 'ShaftInnerDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_outer_diameter(self) -> 'float':
        """float: 'ShaftOuterDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tifffe_model(self) -> '_1191.GearFEModel':
        """GearFEModel: 'TIFFFEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearDesign._Cast_GearDesign':
        return self._Cast_GearDesign(self)
