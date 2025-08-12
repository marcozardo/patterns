import os
import shutil
import pandas as pd
import traceback
import tellurium as te
from pathlib import Path

### Snakemake I/O ###
in_file = snakemake.third_simulation.input[0]
out_file = snakemake.third_simulation.output.result
final_model = snakemake.third_simulation.output.final_model
sample = snakemake.third_simulation.params.file

### generating_csv function to obtain the final csv for each model ###

def generating_csv(input_file, model_name):
    file_name = os.path.basename(input_file)
    simulation_success = False
    error_msg = ""

    try:
        with open(input_file, "r") as f:
                antimony_str = f.read()

                rr = te.loadAntimonyModel(antimony_str)
                rr.simulate(0, 100, 200)

                return {
                      "filename": model_name,
                      "simulation": True,
                      "error": ""
                }
        
    except Exception:
            error_msg = traceback.format_exc()
            return {
                  "filename": model_name,
                  "simulation": True,
                  "error": error_msg 
            }
    df = pd.DataFrame()
    df.to_csv(out_file, index=False)
    
validation = generating_csv(in_file, sample)

# copy the final models in the last repo.

for model in in_file:
    filename = os.path.basename(model)
    destination = os.path.join(final_model, filename)
    shutil.copy(model, destination)