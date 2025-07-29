import os
import pandas as pd
import traceback
import tellurium as te
from pathlib import Path

# Snakemake I/O
input_file = snakemake.simulation.input.model
output_file = snakemake.simulation.output.result
attempt_file = snakemake.simulation.output.attempt 
sample = snakemake.simulation.params.file

def read_Simulation_count(attempt_file):
    try:
        if os.path.exists(attempt_file):
            with open(attempt_file, "r") as f:
                return int(f.read().strip())
    except FileNotFoundError:
        pass
    return 0

def write_Simulation_Count(attempt_file, count):
    with open(attempt_file, "w") as f:
        f.write(str(count))
                      

def simulate_and_check(input_file):
    file_name = os.path.basename(input_file)
    simulation_success = False
    error_msg = ""
    
    
    number_of_simulation = read_Simulation_count(attempt_file)
    
    if number_of_simulation < 4:

        try:
            with open(input_file, "r") as f:
                antimony_str = f.read()

                rr = te.loadAntimonyModel(antimony_str)
                rr.simulate(0, 100, 200)

                simulation_success = True
                print(f"Simulation succeeded for {input_file}")

        except Exception as e:
            error_msg = traceback.format_exc()
            print(f"Simulation failed for {input_file}:\n{error_msg}")


            # write csv
            df = pd.DataFrame({
                "filename": [sample],
                "simulation": [simulation_success],
                "error": [error_msg if not simulation_success else ""]
                })
            df.to_csv(output_file, index=False)

        write_Simulation_Count(attempt_file, number_of_simulation + 1)


    else:
        print("max number of simulation covered")

    return simulation_success
 
simulate_and_check(input_file)
