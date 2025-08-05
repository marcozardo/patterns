import os
import pandas as pd
import traceback
from pathlib import Path
import tellurium as te

input_file = snakemake.input[0]
output_file = snakemake.output[0]
output_file2 = snakemake.output[1]

# Simulation and generation of the error for each model

def simulate_and_check(input_file):
    file_name = os.path.basename(input_file)
    success = True
    error_message = ""

    try:
        with open(input_file, "r") as f:
            antimony_str = f.read()

        rr = te.loadAntimonyModel(antimony_str)
        rr.simulate(0,100,200)

        success = True
        error_message = ""


    except Exception as e:
        error_message = traceback.format_exc()
    
        

    if success == True:
            with open(output_file, "w") as no_err:
                no_err.write(error_message)
    else:
        with open(output_file, "w") as err:
             err.write(error_message)
    
# copying the file inside the "simulated" repository, to work on that

    source = Path(input_file)
    destination = source.with_stem(output_file2)
    destination.write_bytes(source.read_bytes())

success = simulate_and_check(input_file)
