#import sys
import os
import pandas as pd
import tellurium as te

input_file = snakemake.input.generated_model
output_file = snakemake.output.simulated_model
#log_file = snakemake.log[0]

print(input_file, output_file)

def simulate_and_check(input_file):
    try:
        with open(input_file, "r") as f:
            antimony_str = f.read()

        rr = te.loadAntimonyModel(antimony_str)
        rr.simulate(0,100,200)

        print(f"Simulation succeeded for {input_file}") #file=log_file)
        return True

    except Exception as e:
        print(f"Simulation Failed for {input_file}:\n{e}") #file=log_file)
        return False

# Open log file
#with open(output_file, "w") as output_file:

success = simulate_and_check(input_file)

# Create output dataframe
file_name = os.path.basename(input_file)
df = pd.DataFrame({
    "filename": [file_name],
    "simulation": [success]
})
df.to_csv(output_file, index=False)


#if __name__ == "__main__":

#    if len(sys.argv) < 2:
#        print("Usage: python check_sinulation.py with <model_file>")        
#        sys.exit(1)

#   input = sys.argv[1]
#    file_name = os.path.basename(input)

#    success = simulate_and_check(input)

    # creation of the dataframe to see if each Antimony model created by fabric
    # can be simulated

#    df = pd.DataFrame({
#        "filename": [file_name],
#        "simulation":[success]
#   })

#    output_file = input.replace(".txt", "_result.csv")
#    df.to_csv(output_file, index=False)    