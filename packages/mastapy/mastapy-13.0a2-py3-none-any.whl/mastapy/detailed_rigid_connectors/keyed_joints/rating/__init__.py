﻿"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1429 import KeywayHalfRating
    from ._1430 import KeywayRating
