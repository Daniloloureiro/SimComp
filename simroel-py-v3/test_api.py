#!/usr/bin/env python3
"""
Test script for SimROEL FastAPI endpoints
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(method, endpoint, data=None):
    """Test an API endpoint"""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json=data)
        
        print(f"{method} {endpoint}: {response.status_code}")
        if response.status_code == 200:
            print(f"  Response: {response.json()}")
        else:
            print(f"  Error: {response.text}")
        print()
    except requests.exceptions.ConnectionError:
        print(f"ERROR: Could not connect to {url}")
        print("Make sure the server is running with: python start_server.py")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    return True

def main():
    print("Testing SimROEL API endpoints...\n")
    
    # Test network endpoints
    print("=== Network Endpoints ===")
    test_endpoint("GET", "/network/get_bandwidth")
    test_endpoint("GET", "/network/get_node_loss")
    test_endpoint("GET", "/network/get_fiber_loss_coefficient")
    test_endpoint("GET", "/network/get_noise_figure")
    test_endpoint("GET", "/network/get_core_pitch")
    test_endpoint("GET", "/network/get_wavelength")
    test_endpoint("GET", "/network/get_bending_radius")
    test_endpoint("GET", "/network/get_coupling_coeff")
    test_endpoint("GET", "/network/get_port_isolation")
    
    # Test traffic endpoints
    print("=== Traffic Endpoints ===")
    test_endpoint("GET", "/traffic/get_traffic_lambda")
    test_endpoint("GET", "/traffic/get_route_algorithm")
    test_endpoint("GET", "/traffic/get_pcc_holding_time")
    test_endpoint("GET", "/traffic/get_guard_band")
    test_endpoint("GET", "/traffic/get_conn_holding_time")
    test_endpoint("GET", "/traffic/get_modulation")
    test_endpoint("GET", "/traffic/get_span_length")
    test_endpoint("GET", "/traffic/get_confidence_interval")
    test_endpoint("GET", "/traffic/get_thread_number")
    test_endpoint("GET", "/traffic/get_pcc_time_threshold")
    
    # Test simulation endpoints
    print("=== Simulation Endpoints ===")
    test_endpoint("GET", "/simulation/get_n_connections")
    test_endpoint("GET", "/simulation/get_n_simulations")
    test_endpoint("GET", "/simulation/load_params")
    test_endpoint("GET", "/simulation/get_n_cores")
    test_endpoint("GET", "/simulation/get_cores")
    
    # Test the simulation runner
    print("=== Simulation Runner ===")
    test_endpoint("POST", "/run_simulation")

if __name__ == "__main__":
    main() 