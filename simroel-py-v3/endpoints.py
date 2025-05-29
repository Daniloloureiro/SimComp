from fastapi import APIRouter
from api.endpoints import network_router, traffic_router, simulation_router

router = APIRouter()

# Include all the routers
router.include_router(network_router, prefix="/network", tags=["network"])
router.include_router(traffic_router, prefix="/traffic", tags=["traffic"])
router.include_router(simulation_router, prefix="/simulation", tags=["simulation"])
