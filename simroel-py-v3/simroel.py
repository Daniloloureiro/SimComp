import pandas as pd
import os
import json
import time
from core.simulation import Simulation

# Configuração do caminho relativo
base_dir = os.path.dirname(os.path.abspath(__file__))
params_path = os.path.join(base_dir, 'parameters.json')

total = pd.DataFrame()
# loads = [60, 100, 140, 180, 220, 260]
loads = [600] #transformar isso em parametro
n_repeat = 1
n_total = len(loads)*n_repeat
simu = 1

# Caminho relativo para a pasta de resultados
results_dir = os.path.join(base_dir, 'Result')
os.makedirs(results_dir, exist_ok=True)  # Garante que a pasta existe

for erlang in loads:
    with open(params_path, 'r+') as f:
        data = json.load(f)
        data['traffic_lambda'] = 1/erlang
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    for i in range(n_repeat):
        inicio = time.time()
        sim = Simulation()
        sim.simulate(simu, n_total)
        sim.stats.summarize()
        results = sim.stats.results()
        results['Load'] = erlang
        total = pd.concat([total, results])

        # Salva o resultado da simulação atual em um arquivo CSV individual
        current_output_filename = f'Sim{simu}.csv'
        current_output_path = os.path.join(results_dir, current_output_filename)
        results.to_csv(current_output_path, index=False)

        simu += 1
        fim = time.time()
        print(fim - inicio)

print(total)