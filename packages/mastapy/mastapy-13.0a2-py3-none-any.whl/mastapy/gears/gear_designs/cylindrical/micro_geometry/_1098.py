"""_1098.py

CylindricalGearMicroGeometryPerTooth
"""
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1095
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_PER_TOOTH = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometryPerTooth')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometryPerTooth',)


class CylindricalGearMicroGeometryPerTooth(_1095.CylindricalGearMicroGeometryBase):
    """CylindricalGearMicroGeometryPerTooth

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_PER_TOOTH

    class _Cast_CylindricalGearMicroGeometryPerTooth:
        """Special nested class for casting CylindricalGearMicroGeometryPerTooth to subclasses."""

        def __init__(self, parent: 'CylindricalGearMicroGeometryPerTooth'):
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
        def cylindrical_gear_micro_geometry_per_tooth(self) -> 'CylindricalGearMicroGeometryPerTooth':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometryPerTooth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearMicroGeometryPerTooth._Cast_CylindricalGearMicroGeometryPerTooth':
        return self._Cast_CylindricalGearMicroGeometryPerTooth(self)
