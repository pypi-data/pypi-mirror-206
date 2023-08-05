"""_652.py

VirtualPlungeShaverOutputs
"""
from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _710
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _646
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_PLUNGE_SHAVER_OUTPUTS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving', 'VirtualPlungeShaverOutputs')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualPlungeShaverOutputs',)


class VirtualPlungeShaverOutputs(_646.PlungeShaverOutputs):
    """VirtualPlungeShaverOutputs

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_PLUNGE_SHAVER_OUTPUTS

    class _Cast_VirtualPlungeShaverOutputs:
        """Special nested class for casting VirtualPlungeShaverOutputs to subclasses."""

        def __init__(self, parent: 'VirtualPlungeShaverOutputs'):
            self._parent = parent

        @property
        def plunge_shaver_outputs(self):
            return self._parent._cast(_646.PlungeShaverOutputs)

        @property
        def virtual_plunge_shaver_outputs(self) -> 'VirtualPlungeShaverOutputs':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualPlungeShaverOutputs.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_modification_on_conjugate_shaver_chart_left_flank(self) -> 'Image':
        """Image: 'LeadModificationOnConjugateShaverChartLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadModificationOnConjugateShaverChartLeftFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def lead_modification_on_conjugate_shaver_chart_right_flank(self) -> 'Image':
        """Image: 'LeadModificationOnConjugateShaverChartRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadModificationOnConjugateShaverChartRightFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def shaver(self) -> '_710.CylindricalGearShaver':
        """CylindricalGearShaver: 'Shaver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'VirtualPlungeShaverOutputs._Cast_VirtualPlungeShaverOutputs':
        return self._Cast_VirtualPlungeShaverOutputs(self)
