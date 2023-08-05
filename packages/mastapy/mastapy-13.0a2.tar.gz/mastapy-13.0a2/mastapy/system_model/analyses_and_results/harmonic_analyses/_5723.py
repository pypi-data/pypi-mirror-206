"""_5723.py

GearMeshExcitationDetail
"""
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5674, _5649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'GearMeshExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshExcitationDetail',)


class GearMeshExcitationDetail(_5649.AbstractPeriodicExcitationDetail):
    """GearMeshExcitationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_EXCITATION_DETAIL

    class _Cast_GearMeshExcitationDetail:
        """Special nested class for casting GearMeshExcitationDetail to subclasses."""

        def __init__(self, parent: 'GearMeshExcitationDetail'):
            self._parent = parent

        @property
        def abstract_periodic_excitation_detail(self):
            return self._parent._cast(_5649.AbstractPeriodicExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5725
            
            return self._parent._cast(_5725.GearMeshMisalignmentExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726
            
            return self._parent._cast(_5726.GearMeshTEExcitationDetail)

        @property
        def gear_mesh_excitation_detail(self) -> 'GearMeshExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh(self) -> '_2738.GearMeshSystemDeflection':
        """GearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def get_compliance_and_force_data(self) -> '_5674.ComplianceAndForceData':
        """ 'GetComplianceAndForceData' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.harmonic_analyses.ComplianceAndForceData
        """

        method_result = self.wrapped.GetComplianceAndForceData()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'GearMeshExcitationDetail._Cast_GearMeshExcitationDetail':
        return self._Cast_GearMeshExcitationDetail(self)
