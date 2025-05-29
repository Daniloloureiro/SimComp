# SimROEL FastAPI

FastAPI web service for the SimROEL (Simulador de Redes Ópticas Elásticas) project.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python start_server.py
```

The server will start on `http://127.0.0.1:8000`

### 3. Access the API Documentation
Open your browser and go to:
- **Interactive Docs (Swagger UI)**: http://127.0.0.1:8000/docs
- **Alternative Docs (ReDoc)**: http://127.0.0.1:8000/redoc

### 4. Test the API
```bash
pip install requests  # if not already installed
python test_api.py
```

## API Endpoints

### Network Configuration
- `GET /network/get_bandwidth` - Get current bandwidth setting
- `POST /network/set_bandwidth` - Set bandwidth (requires JSON: `{"bandwidth": value}`)
- `GET /network/get_node_loss` - Get node loss setting
- `POST /network/set_node_loss` - Set node loss
- `GET /network/get_fiber_loss_coefficient` - Get fiber loss coefficient
- `POST /network/set_fiber_loss_coefficient` - Set fiber loss coefficient
- `GET /network/get_noise_figure` - Get noise figure
- `POST /network/set_noise_figure` - Set noise figure
- `GET /network/get_core_pitch` - Get core pitch
- `POST /network/set_core_pitch` - Set core pitch
- `GET /network/get_wavelength` - Get wavelength
- `POST /network/set_wavelength` - Set wavelength
- `GET /network/get_bending_radius` - Get bending radius
- `POST /network/set_bending_radius` - Set bending radius
- `GET /network/get_coupling_coeff` - Get coupling coefficient
- `POST /network/set_coupling_coeff` - Set coupling coefficient
- `GET /network/get_port_isolation` - Get port isolation

### Traffic Configuration
- `GET /traffic/get_traffic_lambda` - Get traffic lambda
- `POST /traffic/set_traffic_lambda` - Set traffic lambda
- `GET /traffic/get_route_algorithm` - Get route algorithm
- `POST /traffic/set_route_algorithm` - Set route algorithm
- `GET /traffic/get_pcc_holding_time` - Get PCC holding time
- `POST /traffic/set_pcc_holding_time` - Set PCC holding time
- `GET /traffic/get_guard_band` - Get guard band
- `POST /traffic/set_guard_band` - Set guard band
- `GET /traffic/get_conn_holding_time` - Get connection holding time
- `POST /traffic/set_conn_holding_time` - Set connection holding time
- `GET /traffic/get_modulation` - Get modulation
- `POST /traffic/set_modulation` - Set modulation
- `GET /traffic/get_span_length` - Get span length
- `POST /traffic/set_span_length` - Set span length
- `GET /traffic/get_confidence_interval` - Get confidence interval
- `POST /traffic/set_confidence_interval` - Set confidence interval
- `GET /traffic/get_thread_number` - Get thread number
- `POST /traffic/set_thread_number` - Set thread number
- `GET /traffic/get_pcc_time_threshold` - Get PCC time threshold
- `POST /traffic/set_pcc_time_threshold` - Set PCC time threshold

### Simulation Control
- `GET /simulation/get_n_connections` - Get number of connections
- `GET /simulation/get_n_simulations` - Get number of simulations
- `GET /simulation/load_params` - Load all parameters
- `GET /simulation/get_n_cores` - Get number of cores
- `GET /simulation/get_cores` - Get core information
- `POST /run_simulation` - Run the simulation (returns stdout, stderr, and plot)

## Example Usage

### Using curl
```bash
# Get bandwidth
curl http://127.0.0.1:8000/network/get_bandwidth

# Set bandwidth
curl -X POST http://127.0.0.1:8000/network/set_bandwidth \
  -H "Content-Type: application/json" \
  -d '{"bandwidth": 100}'

# Run simulation
curl -X POST http://127.0.0.1:8000/run_simulation
```

### Using Python requests
```python
import requests

base_url = "http://127.0.0.1:8000"

# Get current bandwidth
response = requests.get(f"{base_url}/network/get_bandwidth")
print(response.json())

# Set bandwidth
response = requests.post(
    f"{base_url}/network/set_bandwidth",
    json={"bandwidth": 150}
)
print(response.json())

# Run simulation
response = requests.post(f"{base_url}/run_simulation")
result = response.json()
print("Simulation output:", result["stdout"])
print("Plot data:", result["plot"][:100] + "...")  # First 100 chars of base64 plot
```

## File Structure
```
simroel-py-v3/
├── main.py                 # FastAPI application
├── start_server.py         # Server startup script
├── test_api.py            # API test script
├── endpoints.py           # Router aggregation
├── requirements.txt       # Dependencies
├── api/
│   ├── __init__.py
│   └── endpoints/
│       ├── __init__.py
│       ├── models.py      # Pydantic models
│       ├── network.py     # Network endpoints
│       ├── traffic.py     # Traffic endpoints
│       └── simulation.py  # Simulation endpoints
├── files/
│   ├── __init__.py
│   ├── file_manager.py    # Parameter file management
│   ├── parameters.py      # Parameter handling
│   └── properties.py      # Properties handling
└── ... (other project files)
```

## Troubleshooting

### Import Errors
Make sure you're in the correct directory and all `__init__.py` files are present:
```bash
cd simroel-py-v3
python -c "from files.file_manager import FileManager; print('OK')"
```

### Server Won't Start
1. Check if port 8000 is already in use:
   ```bash
   lsof -i :8000
   ```
2. Try a different port:
   ```bash
   uvicorn main:app --port 8001
   ```

### Missing Dependencies
Install all required packages:
```bash
pip install -r requirements.txt
```

## Development

To run the server with auto-reload during development:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The server will automatically restart when you make changes to the code. 