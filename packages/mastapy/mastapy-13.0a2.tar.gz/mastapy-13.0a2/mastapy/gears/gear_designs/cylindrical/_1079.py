"""_1079.py

ToothThicknessSpecification
"""
from mastapy.gears.gear_designs.cylindrical import _1080
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_THICKNESS_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ToothThicknessSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothThicknessSpecification',)


class ToothThicknessSpecification(_1080.ToothThicknessSpecificationBase):
    """ToothThicknessSpecification

    This is a mastapy class.
    """

    TYPE = _TOOTH_THICKNESS_SPECIFICATION

    class _Cast_ToothThicknessSpecification:
        """Special nested class for casting ToothThicknessSpecification to subclasses."""

        def __init__(self, parent: 'ToothThicknessSpecification'):
            self._parent = parent

        @property
        def tooth_thickness_specification_base(self):
            return self._parent._cast(_1080.ToothThicknessSpecificationBase)

        @property
        def readonly_tooth_thickness_specification(self):
            from mastapy.gears.gear_designs.cylindrical import _1060
            
            return self._parent._cast(_1060.ReadonlyToothThicknessSpecification)

        @property
        def tooth_thickness_specification(self) -> 'ToothThicknessSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ToothThicknessSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ToothThicknessSpecification._Cast_ToothThicknessSpecification':
        return self._Cast_ToothThicknessSpecification(self)
