from fastapi import APIRouter, HTTPException
from .models import (
    TrafficLambdaModel, RouteAlgorithmModel, PccHoldingTimeModel,
    GuardBandModel, ConnectionHoldingTimeModel, ModulationModel,
    SpanLengthModel, ConfidenceIntervalModel, ThreadNumberModel,
    PccTimeThresholdModel
)
from files.file_manager import FileManager

router = APIRouter()
file_manager = FileManager()

@router.post("/set_traffic_lambda")
def set_traffic_lambda(traffic_lambda: TrafficLambdaModel):
    try:
        success = file_manager.set_traffic_lambda(traffic_lambda.traffic_lambda)
        if success:
            return {"message": "Traffic lambda updated successfully", "new_value": traffic_lambda.traffic_lambda}
        else:
            raise HTTPException(status_code=500, detail="Failed to update traffic lambda")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_traffic_lambda")
def get_traffic_lambda():
    try:
        params = file_manager.get_params()
        return {"traffic_lambda": params["traffic_lambda"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_traffic_refresh")
def get_traffic_refresh():
    try:
        params = file_manager.get_params()
        return {"traffic_refresh": params["traffic_refresh"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_traffic_file")
def get_traffic_file():
    try:
        params = file_manager.get_params()
        return {"traffic_file": params["traffic_file"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_traffic_conn_types")
def get_traffic_conn_types():
    try:
        params = file_manager.get_params()
        return {"traffic_conn_types": params["traffic_conn_types"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_route_algorithm")
def set_route_algorithm(route_algorithm: RouteAlgorithmModel):
    try:
        success = file_manager.set_route_algorithm(route_algorithm.route_algorithm)
        if success:
            return {"message": "Route algorithm updated successfully", "new_value": route_algorithm.route_algorithm}
        else:
            raise HTTPException(status_code=500, detail="Failed to update route algorithm")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_route_algorithm")
def get_route_algorithm():
    try:
        params = file_manager.get_params()
        return {"route_algorithm": params["route_algorithm"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_k_routes")
def get_k_routes():
    try:
        params = file_manager.get_params()
        return {"k_routes": params["k_routes"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_route_selection")
def get_route_selection():
    try:
        params = file_manager.get_params()
        return {"route_selection": params["route_selection"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_pcc_holding_time")
def set_pcc_holding_time(pcc_holding_time: PccHoldingTimeModel):
    try:
        success = file_manager.set_pcc_holding_time(pcc_holding_time.pcc_holding_time)
        if success:
            return {"message": "PCC holding time updated successfully", "new_value": pcc_holding_time.pcc_holding_time}
        else:
            raise HTTPException(status_code=500, detail="Failed to update PCC holding time")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_pcc_holding_time")
def get_pcc_holding_time():
    try:
        params = file_manager.get_params()
        return {"pcc_holding_time": params["pcc_holding_time"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_guard_band")
def set_guard_band(guard_band: GuardBandModel):
    try:
        success = file_manager.set_guard_band(guard_band.guard_band)
        if success:
            return {"message": "Guard band updated successfully", "new_value": guard_band.guard_band}
        else:
            raise HTTPException(status_code=500, detail="Failed to update guard band")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_guard_band")
def get_guard_band():
    try:
        params = file_manager.get_params()
        return {"guard_band": params["guard_band"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_conn_holding_time")
def set_conn_holding_time(conn_holding_time: ConnectionHoldingTimeModel):
    try:
        success = file_manager.set_conn_holding_time(conn_holding_time.conn_holding_time)
        if success:
            return {"message": "Connection holding time updated successfully", "new_value": conn_holding_time.conn_holding_time}
        else:
            raise HTTPException(status_code=500, detail="Failed to update connection holding time")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_conn_holding_time")
def get_conn_holding_time():
    try:
        params = file_manager.get_params()
        return {"conn_holding_time": params["conn_holding_time"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_modulation")
def set_modulation(modulation: ModulationModel):
    try:
        success = file_manager.set_modulation(modulation.modulation)
        if success:
            return {"message": "Modulation updated successfully", "new_value": modulation.modulation}
        else:
            raise HTTPException(status_code=500, detail="Failed to update modulation")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_modulation")
def get_modulation():
    try:
        params = file_manager.get_params()
        return {"modulation": params["modulation"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_span_length")
def set_span_length(span_length: SpanLengthModel):
    try:
        success = file_manager.set_span_length(span_length.span_length)
        if success:
            return {"message": "Span length updated successfully", "new_value": span_length.span_length}
        else:
            raise HTTPException(status_code=500, detail="Failed to update span length")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_span_length")
def get_span_length():
    try:
        params = file_manager.get_params()
        return {"span_length": params["span_length"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_confidence_interval")
def set_confidence_interval(confidence_interval: ConfidenceIntervalModel):
    try:
        success = file_manager.set_confidence_interval(confidence_interval.confidence_interval)
        if success:
            return {"message": "Confidence interval updated successfully", "new_value": confidence_interval.confidence_interval}
        else:
            raise HTTPException(status_code=500, detail="Failed to update confidence interval")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_confidence_interval")
def get_confidence_interval():
    try:
        params = file_manager.get_params()
        return {"confidence_interval": params["confidence_interval"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_thread_number")
def set_thread_number(thread_number: ThreadNumberModel):
    try:
        success = file_manager.set_thread_number(thread_number.thread_number)
        if success:
            return {"message": "Thread number updated successfully", "new_value": thread_number.thread_number}
        else:
            raise HTTPException(status_code=500, detail="Failed to update thread number")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_thread_number")
def get_thread_number():
    try:
        params = file_manager.get_params()
        return {"thread_number": params["thread_number"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_pcc_time_threshold")
def set_pcc_time_threshold(pcc_time_threshold: PccTimeThresholdModel):
    try:
        success = file_manager.set_pcc_time_threshold(pcc_time_threshold.pcc_time_threshold)
        if success:
            return {"message": "PCC time threshold updated successfully", "new_value": pcc_time_threshold.pcc_time_threshold}
        else:
            raise HTTPException(status_code=500, detail="Failed to update PCC time threshold")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_pcc_time_threshold")
def get_pcc_time_threshold():
    try:
        params = file_manager.get_params()
        return {"pcc_time_threshold": params["pcc_time_threshold"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 