"""_2631.py

DesignEntityGroupAnalysis
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_GROUP_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'DesignEntityGroupAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignEntityGroupAnalysis',)


class DesignEntityGroupAnalysis(_0.APIBase):
    """DesignEntityGroupAnalysis

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_GROUP_ANALYSIS

    class _Cast_DesignEntityGroupAnalysis:
        """Special nested class for casting DesignEntityGroupAnalysis to subclasses."""

        def __init__(self, parent: 'DesignEntityGroupAnalysis'):
            self._parent = parent

        @property
        def rigidly_connected_component_group_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2827
            
            return self._parent._cast(_2827.RigidlyConnectedComponentGroupSystemDeflection)

        @property
        def rigidly_connected_design_entity_group_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4697
            
            return self._parent._cast(_4697.RigidlyConnectedDesignEntityGroupModalAnalysis)

        @property
        def design_entity_group_analysis(self) -> 'DesignEntityGroupAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DesignEntityGroupAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'DesignEntityGroupAnalysis._Cast_DesignEntityGroupAnalysis':
        return self._Cast_DesignEntityGroupAnalysis(self)
