"""_2225.py

AdvancedSystemDeflectionViewable
"""
from mastapy.system_model.drawing import _2224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'AdvancedSystemDeflectionViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedSystemDeflectionViewable',)


class AdvancedSystemDeflectionViewable(_2224.AbstractSystemDeflectionViewable):
    """AdvancedSystemDeflectionViewable

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION_VIEWABLE

    class _Cast_AdvancedSystemDeflectionViewable:
        """Special nested class for casting AdvancedSystemDeflectionViewable to subclasses."""

        def __init__(self, parent: 'AdvancedSystemDeflectionViewable'):
            self._parent = parent

        @property
        def abstract_system_deflection_viewable(self):
            return self._parent._cast(_2224.AbstractSystemDeflectionViewable)

        @property
        def part_analysis_case_with_contour_viewable(self):
            from mastapy.system_model.drawing import _2234
            
            return self._parent._cast(_2234.PartAnalysisCaseWithContourViewable)

        @property
        def advanced_system_deflection_viewable(self) -> 'AdvancedSystemDeflectionViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdvancedSystemDeflectionViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AdvancedSystemDeflectionViewable._Cast_AdvancedSystemDeflectionViewable':
        return self._Cast_AdvancedSystemDeflectionViewable(self)
