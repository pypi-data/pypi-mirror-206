"""_885.py

ConceptMeshLoadCase
"""
from mastapy.gears.load_case import _870
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Concept', 'ConceptMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptMeshLoadCase',)


class ConceptMeshLoadCase(_870.MeshLoadCase):
    """ConceptMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_MESH_LOAD_CASE

    class _Cast_ConceptMeshLoadCase:
        """Special nested class for casting ConceptMeshLoadCase to subclasses."""

        def __init__(self, parent: 'ConceptMeshLoadCase'):
            self._parent = parent

        @property
        def mesh_load_case(self):
            return self._parent._cast(_870.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def concept_mesh_load_case(self) -> 'ConceptMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptMeshLoadCase._Cast_ConceptMeshLoadCase':
        return self._Cast_ConceptMeshLoadCase(self)
