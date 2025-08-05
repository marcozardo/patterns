
import os
import shutil
import pandas as pd
import traceback
import tellurium as te
from pathlib import Path

### Snakemake I/O ###
input_file = snakemake.third_simulation.input[0]
out_file = snakemake.third_simulation.output.result
final_model = snakemake.third_simulation.output.final_model
sample = snakemake.third_simulation.params.file


results = []

### generating_csv function to obtain the final csv for each model ###

def generating_cvs(input_file, sample):
    file_name = os.path.basename(input_file)
    simulation_success = False
    error_msg = ""

    try:
        with open(input_file, "r") as f:
                antimony_str = f.read()

                rr = te.loadAntimonyModel(antimony_str)
                rr.simulate(0, 100, 200)

                return {
                      "filename": sample,
                      "simulation": True,
                      "error": ""
                }
        
    except Exception:
            error_msg = traceback.format_exc()
            return {
                  "filename": sample,
                  "simulation": True,
                  "error": error_msg 
            }

    source = Path(input_file)
    destination = source.with_stem(last_model)
    destination.write_bytes(source.read_bytes())


#loop over all models

for model, sample_name in zip(input_file, sample):
    result = generating_cvs(model, sample_name)
    results.append(result)

df = pd.DataFrame(results)
df.to_csv(out_file, index=False)

# copy the final models in the last repo.

for model in input_file:
    filename = os.path.basename(model)
    destination = os.path.join(final_model, filename)
    shutil.copy(model, destination)