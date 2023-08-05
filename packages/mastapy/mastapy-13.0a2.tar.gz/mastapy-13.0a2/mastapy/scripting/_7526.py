"""_7526.py

SMTBitmap
"""
from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy import _7515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SMT_BITMAP = python_net_import('SMT.MastaAPIUtility.Scripting', 'SMTBitmap')


__docformat__ = 'restructuredtext en'
__all__ = ('SMTBitmap',)


class SMTBitmap(_7515.MarshalByRefObjectPermanent):
    """SMTBitmap

    This is a mastapy class.
    """

    TYPE = _SMT_BITMAP

    class _Cast_SMTBitmap:
        """Special nested class for casting SMTBitmap to subclasses."""

        def __init__(self, parent: 'SMTBitmap'):
            self._parent = parent

        @property
        def smt_bitmap(self) -> 'SMTBitmap':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SMTBitmap.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def to_image(self) -> 'Image':
        """ 'ToImage' is the original name of this method.

        Returns:
            Image
        """

        return conversion.pn_to_mp_image(self.wrapped.ToImage())

    def to_bytes(self) -> 'bytes':
        """ 'ToBytes' is the original name of this method.

        Returns:
            bytes
        """

        return conversion.pn_to_mp_bytes(self.wrapped.ToBytes())

    @property
    def cast_to(self) -> 'SMTBitmap._Cast_SMTBitmap':
        return self._Cast_SMTBitmap(self)
