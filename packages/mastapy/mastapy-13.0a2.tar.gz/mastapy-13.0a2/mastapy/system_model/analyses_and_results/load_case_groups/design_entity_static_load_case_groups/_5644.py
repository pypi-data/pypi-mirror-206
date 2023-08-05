"""_5644.py

ConnectionStaticLoadCaseGroup
"""
from typing import List, TypeVar, Generic

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5645
from mastapy.system_model.connections_and_sockets import _2253
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'ConnectionStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionStaticLoadCaseGroup',)


TConnection = TypeVar('TConnection', bound='_2253.Connection')
TConnectionStaticLoad = TypeVar('TConnectionStaticLoad', bound='_6813.ConnectionLoadCase')


class ConnectionStaticLoadCaseGroup(_5645.DesignEntityStaticLoadCaseGroup, Generic[TConnection, TConnectionStaticLoad]):
    """ConnectionStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TConnection
        TConnectionStaticLoad
    """

    TYPE = _CONNECTION_STATIC_LOAD_CASE_GROUP

    class _Cast_ConnectionStaticLoadCaseGroup:
        """Special nested class for casting ConnectionStaticLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'ConnectionStaticLoadCaseGroup'):
            self._parent = parent

        @property
        def design_entity_static_load_case_group(self):
            return self._parent._cast(_5645.DesignEntityStaticLoadCaseGroup)

        @property
        def connection_static_load_case_group(self) -> 'ConnectionStaticLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection(self) -> 'TConnection':
        """TConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(TConnection)(temp) if temp is not None else None

    @property
    def connection_load_cases(self) -> 'List[TConnectionStaticLoad]':
        """List[TConnectionStaticLoad]: 'ConnectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionStaticLoadCaseGroup._Cast_ConnectionStaticLoadCaseGroup':
        return self._Cast_ConnectionStaticLoadCaseGroup(self)
