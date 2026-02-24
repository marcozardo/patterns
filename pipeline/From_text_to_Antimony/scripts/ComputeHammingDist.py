from scipy.spatial import distance
import pandas as pd
import numpy as np
import tellurium as te
from collections import OrderedDict

# Snakemake inputs & output

G_model = snakemake.input[0]
O_model = snakemake.input[1]
hamming_ratio = snakemake.output[0]


# Loading the models and extract the stechiometric matrices

def checking_simulation(gen_file, orig_file):
    
    simulation_gen = True

    try:
        with open(gen_file, "r") as f1:
            gen = f1.read()
            
            gen_antimony = te.loadAntimonyModel(gen)
            
    
    except Exception:

        simulation_gen = False

    # decision based on simulation_output

    if simulation_gen:

        # compute Hamming distance for each pair of column vector of generated_model matrix and original_model matrix 
        # and extract the percentage of non-similar vectors (reactions differentiation)

        hamming_percentage = Hamming_dist(gen_file, orig_file)

    else:

        hamming_percentage = np.nan

        # write the ratio on a CSV:

        
    csv_out= pd.DataFrame({"Hamming ratio": [hamming_percentage]})
    csv_out.to_csv(hamming_ratio, index=False)

    
# Function Extraction_matrix: load the models if simulation goes fine and extract the stechiomatric matrix of both (generated vs original)

def getStechiometricMatrices(gen_file, orig_file):

    # Loading the generated model and extracting its stechiometric matrix 
    
    try:
        with open(gen_file, "r") as file1:
        
            generated = file1.read()
        
            gen_model = te.loadAntimonyModel(generated)

            gen_matrix = gen_model.getFullStoichiometryMatrix()

            gen_df = pd.DataFrame(gen_matrix)
 
    # Loading the original model and extracting its stechiometric matrix
        
        with open(orig_file, "r") as file2:
            
            original = file2.read()
            
            orig_model = te.loadAntimonyModel(original)
            
            orig_matrix = orig_model.getFullStoichiometryMatrix()

            orig_df = pd.DataFrame(orig_matrix)
        
        return gen_df, orig_df
    
    except Exception:

        return None, None

# Function of ordering the stechiomatric generated matrix based on the columns of the original one

def order_matrices_by_original_columns(gen_df, orig_df):

    ordered_generated_cols = []
    generated2original = OrderedDict()
    used_gen_cols = set()

    # Building of the original matrix --> candidates dictionary

    for orig_col in orig_df.columns:

        orig_vec = orig_df[orig_col].values

        sources = orig_vec < 0
        targets = orig_vec > 0

        generated2original[orig_col] = []
        
        for gen_col in gen_df.columns:

            if gen_col in used_gen_cols:
                continue
            
            gen_vec = gen_df[gen_col].values
            g_sources = gen_vec < 0
            g_targets = gen_vec > 0
        
            if np.array_equal(sources,g_sources) and np.array_equal(targets,g_targets):
                
                generated2original[orig_col].append(gen_col)

    # selection of the closest candidates

    for i, (orig_col, gcandidates) in enumerate(generated2original.items()):

        if len(gcandidates) == 0:
            zero_cols = pd.Series(
                np.zeros(orig_df.shape[0]),
                index=orig_df.index
            )
            
            ordered_generated_cols.append(zero_cols)

            continue
        
        o_vector = orig_df[orig_col].values
        distances = []

        for candidate in gcandidates:
            g_vector = gen_df[candidate].values
            dist = np.linalg.norm(o_vector - g_vector)
            distances.append(dist)
        
        best_idx = np.argmin(distances)
        best_gen_col = gcandidates[best_idx]

        ordered_generated_cols.append(gen_df[best_gen_col])
        used_gen_cols.add(best_gen_col)

    # Building the new ordered DataFrame:

    ordered_generated_df = pd.concat(ordered_generated_cols, axis=1)
    ordered_generated_df.columns = orig_df.columns
    ordered_generated_df.index = orig_df.index

    
    return ordered_generated_df
    

# Function to compute the Hamming distance and finally the ratio of dissimilar reactions.


def Hamming_dist(generated_file, original_file):

    generated, original = getStechiometricMatrices(generated_file, original_file)

    if generated is None or original is None:
        return np.nan

    ordered_matrix = order_matrices_by_original_columns(generated, original)

    original_sign = np.sign(original.to_numpy())
    generated_sign = np.sign(ordered_matrix.to_numpy())

    n_reactions = original_sign.shape[1]

    column_distances = []

    for i in range(n_reactions):
        col_original = original_sign[:,i]
        col_generated = generated_sign[:,i]

        hamming_i = distance.hamming(col_original,col_generated)
        column_distances.append(hamming_i)

    hamming_ratio = np.mean(column_distances)

    return hamming_ratio

## Computation:

result = checking_simulation(G_model, O_model)

