"""_4362.py

ParametricStudyStaticLoad
"""
from mastapy.system_model.analyses_and_results.static_loads import _6769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_STATIC_LOAD = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ParametricStudyStaticLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('ParametricStudyStaticLoad',)


class ParametricStudyStaticLoad(_6769.StaticLoadCase):
    """ParametricStudyStaticLoad

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_STATIC_LOAD

    class _Cast_ParametricStudyStaticLoad:
        """Special nested class for casting ParametricStudyStaticLoad to subclasses."""

        def __init__(self, parent: 'ParametricStudyStaticLoad'):
            self._parent = parent

        @property
        def static_load_case(self):
            return self._parent._cast(_6769.StaticLoadCase)

        @property
        def load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6768
            
            return self._parent._cast(_6768.LoadCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2629
            
            return self._parent._cast(_2629.Context)

        @property
        def parametric_study_static_load(self) -> 'ParametricStudyStaticLoad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParametricStudyStaticLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad':
        return self._Cast_ParametricStudyStaticLoad(self)
