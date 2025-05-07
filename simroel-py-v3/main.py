import os
import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from endpoints import router  # import the single router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.post("/run_simulation")
def run_simulation():
    try:
        # Build an absolute path from this file's directory to 'simroel.py'
        script_path = os.path.join(
            os.path.dirname(__file__),
            "simroel.py"
        )
        
        # Set PYTHONPATH to include the current directory
        env = os.environ.copy()
        current_dir = os.path.dirname(__file__)
        env["PYTHONPATH"] = current_dir
        
        print(f"Script path: {script_path}")
        print(f"PYTHONPATH: {current_dir}")
        
        # Run the script
        # If you need Python 3 specifically, replace "python" with "python3"
        result = subprocess.run(
            ["python3", script_path],  # Changed to python3
            capture_output=True,
            text=True,
            check=True,
            env=env,
            cwd=current_dir  # Added working directory
        )
        
        return {"stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error running simroel.py: {e.stderr}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
