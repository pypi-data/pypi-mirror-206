"""_2806.py

SystemDeflectionOptions
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7498
from mastapy.system_model.analyses_and_results.static_loads import _6769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SystemDeflectionOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('SystemDeflectionOptions',)


class SystemDeflectionOptions(_7498.AbstractAnalysisOptions['_6769.StaticLoadCase']):
    """SystemDeflectionOptions

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_OPTIONS

    class _Cast_SystemDeflectionOptions:
        """Special nested class for casting SystemDeflectionOptions to subclasses."""

        def __init__(self, parent: 'SystemDeflectionOptions'):
            self._parent = parent

        @property
        def abstract_analysis_options(self):
            return self._parent._cast(_7498.AbstractAnalysisOptions)

        @property
        def system_deflection_options(self) -> 'SystemDeflectionOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SystemDeflectionOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ground_shaft_if_rigid_body_rotation_is_large(self) -> 'bool':
        """bool: 'GroundShaftIfRigidBodyRotationIsLarge' is the original name of this property."""

        temp = self.wrapped.GroundShaftIfRigidBodyRotationIsLarge

        if temp is None:
            return False

        return temp

    @ground_shaft_if_rigid_body_rotation_is_large.setter
    def ground_shaft_if_rigid_body_rotation_is_large(self, value: 'bool'):
        self.wrapped.GroundShaftIfRigidBodyRotationIsLarge = bool(value) if value else False

    @property
    def maximum_number_of_unstable_rigid_body_rotation_iterations(self) -> 'int':
        """int: 'MaximumNumberOfUnstableRigidBodyRotationIterations' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfUnstableRigidBodyRotationIterations

        if temp is None:
            return 0

        return temp

    @maximum_number_of_unstable_rigid_body_rotation_iterations.setter
    def maximum_number_of_unstable_rigid_body_rotation_iterations(self, value: 'int'):
        self.wrapped.MaximumNumberOfUnstableRigidBodyRotationIterations = int(value) if value else 0

    @property
    def maximum_rigid_body_rotation_change_in_system_deflection(self) -> 'float':
        """float: 'MaximumRigidBodyRotationChangeInSystemDeflection' is the original name of this property."""

        temp = self.wrapped.MaximumRigidBodyRotationChangeInSystemDeflection

        if temp is None:
            return 0.0

        return temp

    @maximum_rigid_body_rotation_change_in_system_deflection.setter
    def maximum_rigid_body_rotation_change_in_system_deflection(self, value: 'float'):
        self.wrapped.MaximumRigidBodyRotationChangeInSystemDeflection = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'SystemDeflectionOptions._Cast_SystemDeflectionOptions':
        return self._Cast_SystemDeflectionOptions(self)
