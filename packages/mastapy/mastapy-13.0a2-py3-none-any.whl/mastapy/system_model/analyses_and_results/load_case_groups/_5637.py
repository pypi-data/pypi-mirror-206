"""_5637.py

SubGroupInSingleDesignState
"""
from mastapy.system_model.analyses_and_results.static_loads import _6769
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.load_case_groups import _5628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUB_GROUP_IN_SINGLE_DESIGN_STATE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'SubGroupInSingleDesignState')


__docformat__ = 'restructuredtext en'
__all__ = ('SubGroupInSingleDesignState',)


class SubGroupInSingleDesignState(_5628.AbstractDesignStateLoadCaseGroup):
    """SubGroupInSingleDesignState

    This is a mastapy class.
    """

    TYPE = _SUB_GROUP_IN_SINGLE_DESIGN_STATE

    class _Cast_SubGroupInSingleDesignState:
        """Special nested class for casting SubGroupInSingleDesignState to subclasses."""

        def __init__(self, parent: 'SubGroupInSingleDesignState'):
            self._parent = parent

        @property
        def abstract_design_state_load_case_group(self):
            return self._parent._cast(_5628.AbstractDesignStateLoadCaseGroup)

        @property
        def abstract_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5630
            
            return self._parent._cast(_5630.AbstractStaticLoadCaseGroup)

        @property
        def abstract_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5629
            
            return self._parent._cast(_5629.AbstractLoadCaseGroup)

        @property
        def sub_group_in_single_design_state(self) -> 'SubGroupInSingleDesignState':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SubGroupInSingleDesignState.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def remove_static_load(self, static_load: '_6769.StaticLoadCase'):
        """ 'RemoveStaticLoad' is the original name of this method.

        Args:
            static_load (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
        """

        self.wrapped.RemoveStaticLoad(static_load.wrapped if static_load else None)

    @property
    def cast_to(self) -> 'SubGroupInSingleDesignState._Cast_SubGroupInSingleDesignState':
        return self._Cast_SubGroupInSingleDesignState(self)
