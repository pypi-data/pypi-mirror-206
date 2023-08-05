"""_518.py

ISO6336RateableMesh
"""
from mastapy.gears.rating.cylindrical import _474, _467
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO6336RateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336RateableMesh',)


class ISO6336RateableMesh(_467.CylindricalRateableMesh):
    """ISO6336RateableMesh

    This is a mastapy class.
    """

    TYPE = _ISO6336_RATEABLE_MESH

    class _Cast_ISO6336RateableMesh:
        """Special nested class for casting ISO6336RateableMesh to subclasses."""

        def __init__(self, parent: 'ISO6336RateableMesh'):
            self._parent = parent

        @property
        def cylindrical_rateable_mesh(self):
            return self._parent._cast(_467.CylindricalRateableMesh)

        @property
        def rateable_mesh(self):
            from mastapy.gears.rating import _363
            
            return self._parent._cast(_363.RateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _488
            
            return self._parent._cast(_488.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493
            
            return self._parent._cast(_493.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494
            
            return self._parent._cast(_494.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _495
            
            return self._parent._cast(_495.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _517
            
            return self._parent._cast(_517.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(self) -> 'ISO6336RateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336RateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def misalignment_contact_pattern_enhancement(self) -> '_474.MisalignmentContactPatternEnhancements':
        """MisalignmentContactPatternEnhancements: 'MisalignmentContactPatternEnhancement' is the original name of this property."""

        temp = self.wrapped.MisalignmentContactPatternEnhancement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _474.MisalignmentContactPatternEnhancements)
        return constructor.new_from_mastapy_type(_474.MisalignmentContactPatternEnhancements)(value) if value is not None else None

    @misalignment_contact_pattern_enhancement.setter
    def misalignment_contact_pattern_enhancement(self, value: '_474.MisalignmentContactPatternEnhancements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _474.MisalignmentContactPatternEnhancements.type_())
        self.wrapped.MisalignmentContactPatternEnhancement = value

    @property
    def cast_to(self) -> 'ISO6336RateableMesh._Cast_ISO6336RateableMesh':
        return self._Cast_ISO6336RateableMesh(self)
