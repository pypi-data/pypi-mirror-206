from dataclasses import dataclass
from typing import Literal, Optional

from ..common import AnnotationID, AnnotationKind, SensorID
from ..paths import PosePath
"""
The LocalizationAdjustmentAnnotation represents a PosePath applied a scene to fix localization issues or convert from ego to world coordinates.
"""


@dataclass
class LocalizationAdjustmentAnnotation:
    id: AnnotationID
    poses: PosePath
    type: Literal[AnnotationKind.LocalizationAdjustment] = AnnotationKind.LocalizationAdjustment
    parent_id: Optional[AnnotationID] = None
