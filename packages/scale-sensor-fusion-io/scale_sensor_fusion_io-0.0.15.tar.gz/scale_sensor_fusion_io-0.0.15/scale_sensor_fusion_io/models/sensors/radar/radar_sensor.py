from dataclasses import dataclass
from typing import Any, List, Literal, Optional, Union

import numpy as np
import numpy.typing as npt

from ...common import SensorID, SensorKind
from ...paths import PosePath


@dataclass
class RadarSensorPoints:
    positions: npt.NDArray[np.float32]
    directions: Optional[npt.NDArray[np.float32]] = None
    lengths: Optional[npt.NDArray[np.float32]] = None
    timestamps: Optional[Union[npt.NDArray[np.int32], npt.NDArray[np.int64]]] = None


@dataclass
class RadarSensorFrame:
    timestamp: int
    points: RadarSensorPoints


@dataclass
class RadarSensor:
    id: SensorID
    poses: PosePath
    frames: List[RadarSensorFrame]
    type: Literal[SensorKind.Radar] = SensorKind.Radar
    coordinates: Literal["ego", "world"] = "world"
    parent_id: Optional[SensorID] = None
