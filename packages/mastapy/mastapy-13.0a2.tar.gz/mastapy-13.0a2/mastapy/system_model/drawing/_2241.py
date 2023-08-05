"""_2241.py

SystemDeflectionViewable
"""
from mastapy.system_model.drawing import _2224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'SystemDeflectionViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('SystemDeflectionViewable',)


class SystemDeflectionViewable(_2224.AbstractSystemDeflectionViewable):
    """SystemDeflectionViewable

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_VIEWABLE

    class _Cast_SystemDeflectionViewable:
        """Special nested class for casting SystemDeflectionViewable to subclasses."""

        def __init__(self, parent: 'SystemDeflectionViewable'):
            self._parent = parent

        @property
        def abstract_system_deflection_viewable(self):
            return self._parent._cast(_2224.AbstractSystemDeflectionViewable)

        @property
        def part_analysis_case_with_contour_viewable(self):
            from mastapy.system_model.drawing import _2234
            
            return self._parent._cast(_2234.PartAnalysisCaseWithContourViewable)

        @property
        def system_deflection_viewable(self) -> 'SystemDeflectionViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SystemDeflectionViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SystemDeflectionViewable._Cast_SystemDeflectionViewable':
        return self._Cast_SystemDeflectionViewable(self)
