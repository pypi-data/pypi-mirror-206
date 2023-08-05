"""_2048.py

MaxStripLoadStressObject
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAX_STRIP_LOAD_STRESS_OBJECT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'MaxStripLoadStressObject')


__docformat__ = 'restructuredtext en'
__all__ = ('MaxStripLoadStressObject',)


class MaxStripLoadStressObject(_0.APIBase):
    """MaxStripLoadStressObject

    This is a mastapy class.
    """

    TYPE = _MAX_STRIP_LOAD_STRESS_OBJECT

    class _Cast_MaxStripLoadStressObject:
        """Special nested class for casting MaxStripLoadStressObject to subclasses."""

        def __init__(self, parent: 'MaxStripLoadStressObject'):
            self._parent = parent

        @property
        def max_strip_load_stress_object(self) -> 'MaxStripLoadStressObject':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaxStripLoadStressObject.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_strip_load(self) -> 'float':
        """float: 'MaximumStripLoad' is the original name of this property."""

        temp = self.wrapped.MaximumStripLoad

        if temp is None:
            return 0.0

        return temp

    @maximum_strip_load.setter
    def maximum_strip_load(self, value: 'float'):
        self.wrapped.MaximumStripLoad = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'MaxStripLoadStressObject._Cast_MaxStripLoadStressObject':
        return self._Cast_MaxStripLoadStressObject(self)
