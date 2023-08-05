"""_1040.py

FinishToothThicknessDesignSpecification
"""
from mastapy.gears.gear_designs.cylindrical import _1080
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_TOOTH_THICKNESS_DESIGN_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'FinishToothThicknessDesignSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('FinishToothThicknessDesignSpecification',)


class FinishToothThicknessDesignSpecification(_1080.ToothThicknessSpecificationBase):
    """FinishToothThicknessDesignSpecification

    This is a mastapy class.
    """

    TYPE = _FINISH_TOOTH_THICKNESS_DESIGN_SPECIFICATION

    class _Cast_FinishToothThicknessDesignSpecification:
        """Special nested class for casting FinishToothThicknessDesignSpecification to subclasses."""

        def __init__(self, parent: 'FinishToothThicknessDesignSpecification'):
            self._parent = parent

        @property
        def tooth_thickness_specification_base(self):
            return self._parent._cast(_1080.ToothThicknessSpecificationBase)

        @property
        def finish_tooth_thickness_design_specification(self) -> 'FinishToothThicknessDesignSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FinishToothThicknessDesignSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FinishToothThicknessDesignSpecification._Cast_FinishToothThicknessDesignSpecification':
        return self._Cast_FinishToothThicknessDesignSpecification(self)
