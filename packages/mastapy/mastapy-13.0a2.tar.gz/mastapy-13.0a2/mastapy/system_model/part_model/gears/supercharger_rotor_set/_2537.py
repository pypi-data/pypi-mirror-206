"""_2537.py

RotorSetDataInputFileOptions
"""
from mastapy.utility_gui import _1834
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_SET_DATA_INPUT_FILE_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'RotorSetDataInputFileOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('RotorSetDataInputFileOptions',)


class RotorSetDataInputFileOptions(_1834.DataInputFileOptions):
    """RotorSetDataInputFileOptions

    This is a mastapy class.
    """

    TYPE = _ROTOR_SET_DATA_INPUT_FILE_OPTIONS

    class _Cast_RotorSetDataInputFileOptions:
        """Special nested class for casting RotorSetDataInputFileOptions to subclasses."""

        def __init__(self, parent: 'RotorSetDataInputFileOptions'):
            self._parent = parent

        @property
        def data_input_file_options(self):
            return self._parent._cast(_1834.DataInputFileOptions)

        @property
        def rotor_set_data_input_file_options(self) -> 'RotorSetDataInputFileOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RotorSetDataInputFileOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RotorSetDataInputFileOptions._Cast_RotorSetDataInputFileOptions':
        return self._Cast_RotorSetDataInputFileOptions(self)
