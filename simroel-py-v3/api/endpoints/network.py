from fastapi import APIRouter, HTTPException
from .models import (
    BandwidthModel, NodeLossModel, FiberLossCoefficientModel,
    NoiseFigureModel, CorePitchModel, WavelengthModel,
    BendingRadiusModel, CouplingCoeffModel
)
from files.file_manager import FileManager

router = APIRouter()
file_manager = FileManager()

@router.post("/set_bandwidth")
def set_bandwidth(bandwidth: BandwidthModel):
    try:
        success = file_manager.set_bandwidth(bandwidth.bandwidth)
        if success:
            return {"message": "Bandwidth updated successfully", "new_value": bandwidth.bandwidth}
        else:
            raise HTTPException(status_code=500, detail="Failed to update bandwidth")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_bandwidth")
def get_bandwidth():
    try:
        params = file_manager.get_params()
        return {"bandwidth": params["bandwidth"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_node_loss")
def set_node_loss(node_loss_data: NodeLossModel):
    try:
        success = file_manager.set_node_loss(node_loss_data.node_loss)
        if success:
            return {"message": "Node loss updated successfully", "new_value": node_loss_data.node_loss}
        else:
            raise HTTPException(status_code=500, detail="Failed to update node loss")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_node_loss")
def get_node_loss():
    try:
        params = file_manager.get_params()
        return {"node_loss": params["node_loss"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_fiber_loss_coefficient")
def set_fiber_loss_coefficient(fiber_loss_data: FiberLossCoefficientModel):
    try:
        success = file_manager.set_fiber_loss_coefficient(fiber_loss_data.fiber_loss_coefficient)
        if success:
            return {"message": "Fiber loss coefficient updated successfully", "new_value": fiber_loss_data.fiber_loss_coefficient}
        else:
            raise HTTPException(status_code=500, detail="Failed to update fiber loss coefficient")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_fiber_loss_coefficient")
def get_fiber_loss_coefficient():
    try:
        params = file_manager.get_params()
        return {"fiber_loss_coefficient": params["fiber_loss_coefficient"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_noise_figure")
def set_noise_figure(noise_figure_data: NoiseFigureModel):
    try:
        success = file_manager.set_noise_figure(noise_figure_data.noise_figure)
        if success:
            return {"message": "Noise figure updated successfully", "new_value": noise_figure_data.noise_figure}
        else:
            raise HTTPException(status_code=500, detail="Failed to update noise figure")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_noise_figure")
def get_noise_figure():
    try:
        params = file_manager.get_params()
        return {"noise_figure": params["noise_figure"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_core_pitch")
def set_core_pitch(core_pitch_data: CorePitchModel):
    try:
        success = file_manager.set_core_pitch(core_pitch_data.core_pitch)
        if success:
            return {"message": "Core pitch updated successfully", "new_value": core_pitch_data.core_pitch}
        else:
            raise HTTPException(status_code=500, detail="Failed to update core pitch")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_core_pitch")
def get_core_pitch():
    try:
        params = file_manager.get_params()
        return {"core_pitch": params["core_pitch"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_wavelength")
def set_wavelength(wavelength: WavelengthModel):
    try:
        success = file_manager.set_wavelength(wavelength.wavelength)
        if success:
            return {"message": "Wavelength updated successfully", "new_value": wavelength.wavelength}
        else:
            raise HTTPException(status_code=500, detail="Failed to update wavelength")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_wavelength")
def get_wavelength():
    try:
        params = file_manager.get_params()
        return {"wavelength": params["wavelength"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_bending_radius")
def set_bending_radius(bending_radius: BendingRadiusModel):
    try:
        success = file_manager.set_bending_radius(bending_radius.bending_radius)
        if success:
            return {"message": "Bending radius updated successfully", "new_value": bending_radius.bending_radius}
        else:
            raise HTTPException(status_code=500, detail="Failed to update bending radius")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_bending_radius")
def get_bending_radius():
    try:
        params = file_manager.get_params()
        return {"bending_radius": params["bending_radius"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_coupling_coeff")
def set_coupling_coeff(coupling_coeff: CouplingCoeffModel):
    try:
        success = file_manager.set_coupling_coeff(coupling_coeff.coupling_coeff)
        if success:
            return {"message": "Coupling coefficient updated successfully", "new_value": coupling_coeff.coupling_coeff}
        else:
            raise HTTPException(status_code=500, detail="Failed to update coupling coefficient")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_coupling_coeff")
def get_coupling_coeff():
    try:
        params = file_manager.get_params()
        return {"coupling_coeff": params["coupling_coeff"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_port_isolation")
def get_port_isolation():
    try:
        params = file_manager.get_params()
        return {"port_isolation": params["port_isolation"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 