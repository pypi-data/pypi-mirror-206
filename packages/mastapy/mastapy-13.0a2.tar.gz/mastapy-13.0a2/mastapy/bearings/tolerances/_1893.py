"""_1893.py

InterferenceDetail
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.materials import _265
from mastapy.bearings.tolerances import _1886
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_DETAIL = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InterferenceDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceDetail',)


class InterferenceDetail(_1886.BearingConnectionComponent):
    """InterferenceDetail

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_DETAIL

    class _Cast_InterferenceDetail:
        """Special nested class for casting InterferenceDetail to subclasses."""

        def __init__(self, parent: 'InterferenceDetail'):
            self._parent = parent

        @property
        def bearing_connection_component(self):
            return self._parent._cast(_1886.BearingConnectionComponent)

        @property
        def mounting_sleeve_diameter_detail(self):
            from mastapy.bearings.tolerances import _1896
            
            return self._parent._cast(_1896.MountingSleeveDiameterDetail)

        @property
        def race_detail(self):
            from mastapy.bearings.tolerances import _1899
            
            return self._parent._cast(_1899.RaceDetail)

        @property
        def support_detail(self):
            from mastapy.bearings.tolerances import _1905
            
            return self._parent._cast(_1905.SupportDetail)

        @property
        def interference_detail(self) -> 'InterferenceDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterferenceDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_tolerance_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DiameterToleranceFactor' is the original name of this property."""

        temp = self.wrapped.DiameterToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @diameter_tolerance_factor.setter
    def diameter_tolerance_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DiameterToleranceFactor = value

    @property
    def temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Temperature' is the original name of this property."""

        temp = self.wrapped.Temperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @temperature.setter
    def temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Temperature = value

    @property
    def material(self) -> '_265.Material':
        """Material: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterferenceDetail._Cast_InterferenceDetail':
        return self._Cast_InterferenceDetail(self)
