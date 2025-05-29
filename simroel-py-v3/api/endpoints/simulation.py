from fastapi import APIRouter, HTTPException
from .models import ConnectionModel, SimulationsModel, ParamsModel
from files.file_manager import FileManager

router = APIRouter()
file_manager = FileManager()

@router.get("/get_n_connections")
def get_n_connections():
    try:
        connections = file_manager.get_n_connections()
        return {"connections": connections}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_n_simulations")
def get_n_simulations():
    try:
        simulations = file_manager.get_n_simulations()
        return {"simulations": simulations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/load_params")
def load_params():
    try:
        params = file_manager.load_params()
        return {"params": params}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_n_cores")
def get_n_cores():
    try:
        params = file_manager.get_params()
        return {"n_cores": params["n_cores"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_cores")
def get_cores():
    try:
        cores = file_manager.get_cores()
        return {"cores": cores}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_allocation_type")
def get_allocation_type():
    try:
        params = file_manager.get_params()
        return {"allocation_type": params["allocation_type"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_allocation_fn")
def get_allocation_fn():
    try:
        params = file_manager.get_params()
        return {"allocation_fn": params["allocation_fn"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_tracer")
def get_tracer():
    try:
        params = file_manager.get_params()
        return {"tracer": params["tracer"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_osnr")
def get_osnr():
    try:
        params = file_manager.get_params()
        return {"osnr": params["osnr"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_lambda")
def get_lambda():
    try:
        params = file_manager.get_params()
        return {"lambda": params["lambda"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_fn")
def get_fn():
    try:
        params = file_manager.get_params()
        return {"fn": params["fn"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_p")
def get_p():
    try:
        params = file_manager.get_params()
        return {"p": params["p"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_band_ref")
def get_band_ref():
    try:
        params = file_manager.get_params()
        return {"band_ref": params["band_ref"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_limit_single_carrier")
def get_limit_single_carrier():
    try:
        params = file_manager.get_params()
        return {"limit_single_carrier": params["limit_single_carrier"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_crosstalk_reason")
def get_crosstalk_reason():
    try:
        params = file_manager.get_params()
        return {"crosstalk_reason": params["crosstalk_reason"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_calculate_crosstalk")
def get_calculate_crosstalk():
    try:
        params = file_manager.get_params()
        return {"calculate_crosstalk": params["calculate_crosstalk"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 