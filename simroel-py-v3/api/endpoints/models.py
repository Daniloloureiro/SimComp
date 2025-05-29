from pydantic import BaseModel

class SlotSizeModel(BaseModel):
    slot_size: float

class CorePitchModel(BaseModel):
    core_pitch: float

class NodeLossModel(BaseModel):
    node_loss: float

class FiberLossCoefficientModel(BaseModel):
    fiber_loss_coefficient: float

class NoiseFigureModel(BaseModel):
    noise_figure: float

class ConnectionModel(BaseModel):
    connections: int

class SimulationsModel(BaseModel):
    simulations: int

class ParamsModel(BaseModel):
    params: dict

class CoresModel(BaseModel):
    cores: list

class AllocationTypeModel(BaseModel):
    allocation_type: str

class FiberLossModel(BaseModel):
    fiber_loss_coefficient: float

class TrafficLambdaModel(BaseModel):
    traffic_lambda: float

class RouteAlgorithmModel(BaseModel):
    route_algorithm: str

class PccHoldingTimeModel(BaseModel):
    pcc_holding_time: float

class GuardBandModel(BaseModel):
    guard_band: float

class ConnectionHoldingTimeModel(BaseModel):
    conn_holding_time: float

class ModulationModel(BaseModel):
    modulation: str

class WavelengthModel(BaseModel):
    wavelength: float

class SpanLengthModel(BaseModel):
    span_length: float

class ConfidenceIntervalModel(BaseModel):
    confidence_interval: float

class ThreadNumberModel(BaseModel):
    thread_number: int

class PccTimeThresholdModel(BaseModel):
    pcc_time_threshold: float

class BendingRadiusModel(BaseModel):
    bending_radius: float

class CouplingCoeffModel(BaseModel):
    coupling_coeff: float

class BandRefModel(BaseModel):
    band_ref: float

class BandwidthModel(BaseModel):
    bandwidth: int 