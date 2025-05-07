import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
import subprocess

client = TestClient(app)

def test_run_simulation_success():
    # Mock the subprocess.run to return a successful result
    mock_result = MagicMock()
    mock_result.stdout = "Simulation completed successfully"
    mock_result.stderr = ""
    
    with patch('subprocess.run', return_value=mock_result) as mock_run:
        response = client.post("/run_simulation")
        
        assert response.status_code == 200
        assert response.json() == {
            "stdout": "Simulation completed successfully",
            "stderr": ""
        }
        
        # Verify the subprocess.run was called with correct arguments
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        assert "python" in args[0]
        assert "simroel.py" in args[0]
        assert kwargs["capture_output"] is True
        assert kwargs["text"] is True
        assert kwargs["check"] is True

def test_run_simulation_error():
    # Mock subprocess.run to raise CalledProcessError
    with patch('subprocess.run', side_effect=subprocess.CalledProcessError(
        returncode=1,
        cmd=["python", "simroel.py"],
        stderr="Simulation failed"
    )) as mock_run:
        response = client.post("/run_simulation")
        
        assert response.status_code == 500
        assert "Error running simroel.py" in response.json()["detail"]
        assert "Simulation failed" in response.json()["detail"]

def test_run_simulation_unexpected_error():
    # Mock subprocess.run to raise an unexpected error
    with patch('subprocess.run', side_effect=Exception("Unexpected error")) as mock_run:
        response = client.post("/run_simulation")
        
        assert response.status_code == 500
        assert response.json()["detail"] == "Unexpected error" 