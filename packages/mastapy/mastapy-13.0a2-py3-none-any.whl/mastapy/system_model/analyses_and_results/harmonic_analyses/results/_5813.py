"""_5813.py

ExcitationSourceSelectionBase
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCITATION_SOURCE_SELECTION_BASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results', 'ExcitationSourceSelectionBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ExcitationSourceSelectionBase',)


class ExcitationSourceSelectionBase(_0.APIBase):
    """ExcitationSourceSelectionBase

    This is a mastapy class.
    """

    TYPE = _EXCITATION_SOURCE_SELECTION_BASE

    class _Cast_ExcitationSourceSelectionBase:
        """Special nested class for casting ExcitationSourceSelectionBase to subclasses."""

        def __init__(self, parent: 'ExcitationSourceSelectionBase'):
            self._parent = parent

        @property
        def excitation_source_selection(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5812
            
            return self._parent._cast(_5812.ExcitationSourceSelection)

        @property
        def excitation_source_selection_group(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5814
            
            return self._parent._cast(_5814.ExcitationSourceSelectionGroup)

        @property
        def excitation_source_selection_base(self) -> 'ExcitationSourceSelectionBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExcitationSourceSelectionBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def included(self) -> 'bool':
        """bool: 'Included' is the original name of this property."""

        temp = self.wrapped.Included

        if temp is None:
            return False

        return temp

    @included.setter
    def included(self, value: 'bool'):
        self.wrapped.Included = bool(value) if value else False

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
    def cast_to(self) -> 'ExcitationSourceSelectionBase._Cast_ExcitationSourceSelectionBase':
        return self._Cast_ExcitationSourceSelectionBase(self)
