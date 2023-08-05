"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._527 import DIN3990GearSingleFlankRating
    from ._528 import DIN3990MeshSingleFlankRating
