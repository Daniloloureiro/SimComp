import os
import subprocess
import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def generate_plot(csv_path):
    # Carregar o arquivo CSV
    df = pd.read_csv(csv_path)

    # Converter colunas para o tipo numérico
    colunas_numericas = ['Resource', 'OSNR', 'Crosstalk', 'nli', 'Allocted', 'Load']
    df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors='coerce')

    # Calcular as métricas normalizadas por "Allocated"
    df['Resource_pb'] = df['Resource'] / df['Allocted']
    df['OSNR_pb'] = df['OSNR'] / df['Allocted']
    df['Crosstalk_pb'] = df['Crosstalk'] / df['Allocted']
    df['Total_pb'] = (df['Resource'] + df['OSNR'] + df['Crosstalk']) / df['Allocted']

    # Substituir zeros para evitar problemas ao usar escala logarítmica
    df.replace(0, 1e-6, inplace=True)

    # Transformar o DataFrame para formato longo para plotagem
    df_melted = df.melt(
        id_vars=['Load'],
        value_vars=['Resource_pb', 'OSNR_pb', 'Crosstalk_pb', 'Total_pb'],
        var_name='Metric',
        value_name='pb'
    )

    # Criar figura
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df_melted,
        x='Load',
        y='pb',
        hue='Metric',
        marker='o',
        palette='husl',
        linewidth=2
    )

    # Configurações do gráfico
    plt.xlabel('Load [Erlang]', fontsize=12)
    plt.ylabel('pb (Métrica / Allocated)', fontsize=12)
    plt.yscale('log')  # Escala logarítmica no eixo Y
    plt.title('Load vs pb (Resource, OSNR, Crosstalk)', fontsize=14)
    plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
    plt.legend(title='Métrica', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Salvar o gráfico em um buffer de memória
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    
    # Converter para base64
    plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return plot_base64

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
        result = subprocess.run(
            ["python3", script_path],
            capture_output=True,
            text=True,
            check=True,
            env=env,
            cwd=current_dir
        )
        
        # After simulation completes, generate the plot
        csv_path = os.path.join(current_dir, "Result", "new_FF_est2.csv")
        plot_base64 = generate_plot(csv_path)
        
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "plot": plot_base64
        }
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error running simroel.py: {e.stderr}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
