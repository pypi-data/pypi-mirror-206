"""_228.py

ModalCMSResults
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.component_mode_synthesis import _229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_CMS_RESULTS = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'ModalCMSResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalCMSResults',)


class ModalCMSResults(_229.RealCMSResults):
    """ModalCMSResults

    This is a mastapy class.
    """

    TYPE = _MODAL_CMS_RESULTS

    class _Cast_ModalCMSResults:
        """Special nested class for casting ModalCMSResults to subclasses."""

        def __init__(self, parent: 'ModalCMSResults'):
            self._parent = parent

        @property
        def real_cms_results(self):
            return self._parent._cast(_229.RealCMSResults)

        @property
        def cms_results(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _226
            
            return self._parent._cast(_226.CMSResults)

        @property
        def modal_cms_results(self) -> 'ModalCMSResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ModalCMSResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculate_results(self) -> 'bool':
        """bool: 'CalculateResults' is the original name of this property."""

        temp = self.wrapped.CalculateResults

        if temp is None:
            return False

        return temp

    @calculate_results.setter
    def calculate_results(self, value: 'bool'):
        self.wrapped.CalculateResults = bool(value) if value else False

    @property
    def frequency(self) -> 'float':
        """float: 'Frequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @property
    def mode_id(self) -> 'int':
        """int: 'ModeID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModeID

        if temp is None:
            return 0

        return temp

    def calculate_strain_and_kinetic_energy(self):
        """ 'CalculateStrainAndKineticEnergy' is the original name of this method."""

        self.wrapped.CalculateStrainAndKineticEnergy()

    @property
    def cast_to(self) -> 'ModalCMSResults._Cast_ModalCMSResults':
        return self._Cast_ModalCMSResults(self)
