"""_5725.py

GearMeshMisalignmentExcitationDetail
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5723
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MISALIGNMENT_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'GearMeshMisalignmentExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshMisalignmentExcitationDetail',)


class GearMeshMisalignmentExcitationDetail(_5723.GearMeshExcitationDetail):
    """GearMeshMisalignmentExcitationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MISALIGNMENT_EXCITATION_DETAIL

    class _Cast_GearMeshMisalignmentExcitationDetail:
        """Special nested class for casting GearMeshMisalignmentExcitationDetail to subclasses."""

        def __init__(self, parent: 'GearMeshMisalignmentExcitationDetail'):
            self._parent = parent

        @property
        def gear_mesh_excitation_detail(self):
            return self._parent._cast(_5723.GearMeshExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649
            
            return self._parent._cast(_5649.AbstractPeriodicExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(self) -> 'GearMeshMisalignmentExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshMisalignmentExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMeshMisalignmentExcitationDetail._Cast_GearMeshMisalignmentExcitationDetail':
        return self._Cast_GearMeshMisalignmentExcitationDetail(self)
