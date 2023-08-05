"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1335 import DynamicForceAnalysis
    from ._1336 import DynamicForceLoadCase
    from ._1337 import EfficiencyMapAnalysis
    from ._1338 import EfficiencyMapLoadCase
    from ._1339 import ElectricMachineAnalysis
    from ._1340 import ElectricMachineBasicMechanicalLossSettings
    from ._1341 import ElectricMachineControlStrategy
    from ._1342 import ElectricMachineEfficiencyMapSettings
    from ._1343 import ElectricMachineFEAnalysis
    from ._1344 import ElectricMachineFEMechanicalAnalysis
    from ._1345 import ElectricMachineLoadCase
    from ._1346 import ElectricMachineLoadCaseBase
    from ._1347 import ElectricMachineLoadCaseGroup
    from ._1348 import ElectricMachineMechanicalLoadCase
    from ._1349 import EndWindingInductanceMethod
    from ._1350 import LeadingOrLagging
    from ._1351 import LoadCaseType
    from ._1352 import LoadCaseTypeSelector
    from ._1353 import MotoringOrGenerating
    from ._1354 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1355 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1356 import OperatingPointsSpecificationMethod
    from ._1357 import SingleOperatingPointAnalysis
    from ._1358 import SlotDetailForAnalysis
    from ._1359 import SpecifyTorqueOrCurrent
    from ._1360 import SpeedPointsDistribution
    from ._1361 import SpeedTorqueCurveAnalysis
    from ._1362 import SpeedTorqueCurveLoadCase
    from ._1363 import SpeedTorqueLoadCase
    from ._1364 import SpeedTorqueOperatingPoint
    from ._1365 import Temperatures
