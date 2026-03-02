from scipy.spatial import distance
import pandas as pd
import numpy as np
import tellurium as te
from collections import OrderedDict

# Snakemake inputs & output

#generated_model = snakemake.input[0]
#original_model = snakemake.input[1]
#hamming_percentage = snakemake.output[0]


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

        x, y = Hamming_dist(gen_file, orig_file)
       

    else:
        x = np.nan
        y = np.nan

        # write the ratios on a CSV:

    csv_out_1=pd.DataFrame({"success_ratio":[x]})
    csv_out_1.to_csv(Hamming_ratio_1_csv, index=False)

    csv_out_2= pd.DataFrame({"no_success_ratio": [y]})
    csv_out_2.to_csv(Hamming_ratio_2_csv, index=False)

    
# Function Extraction_matrix: load the models if simulation goes fine and extract the stechiomatric matrix of both (generated vs original)

def getStechiometricMatrices(gen_file, orig_file):

    # Loading the generated model and extracting its stechiometric matrix 
    
    try:
        with open(gen_file, "r") as file1:
        
            generated = file1.read()
        
            gen_model = te.loadAntimonyModel(generated)

            depen_gen_sp = gen_model.getFloatingSpeciesIds()
            
            gen_matrix = gen_model.getFullStoichiometryMatrix()

            gen_df = pd.DataFrame(gen_matrix, index=depen_gen_sp)

            print(f"generated_matrix:{gen_df}")
 
    # Loading the original model and extracting its stechiometric matrix
        
        with open(orig_file, "r") as file2:
            
            original = file2.read()
            
            orig_model = te.loadAntimonyModel(original)

            depen_or_sp = orig_model.getFloatingSpeciesIds()
            
            orig_matrix = orig_model.getFullStoichiometryMatrix()

            orig_df = pd.DataFrame(orig_matrix, index=depen_or_sp)

            print(f"original_matrix:{orig_df}")
        
        return gen_df, orig_df
    
    except Exception:

        return None, None

def Ordering_by_original_rownames(df1,df2):

    gen_reordered = df1.reindex(df2.index)

    missing_rows = gen_reordered[gen_reordered.isna().all(axis=1)].index

    for row in missing_rows:
        gen_reordered.loc[row] = np.zeros(df1.shape[1])

        print(f"\nMatriceordinata per il nome delle specie:{gen_reordered}")

    return gen_reordered

def percentage_matching_rownames(data_1, data_2):

    orig_species = set(data_2.index)
    gen_species = set(data_1.index)

    common = orig_species.intersection(gen_species)

    average_common_names = len(common) / len(orig_species)

    print(f"average of species names in common between the two matrices:{average_common_names}")

    return average_common_names


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

            #if gen_col in used_gen_cols:
            #    continue
            
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

    print(f"\nmatrice ordinata per reazioni:{ordered_generated_df}")

    return ordered_generated_df
    

# Function to compute the Hamming distance and finally the ratio of dissimilar reactions.


def Hamming_dist(generated_file, original_file):

    generated, original = getStechiometricMatrices(generated_file, original_file)

    if generated is None or original is None:
        return np.nan

    matrix_ordered_by_orignal_rownames = Ordering_by_original_rownames(generated,original)
    ordered_matrix = order_matrices_by_original_columns(matrix_ordered_by_orignal_rownames, original)

    original_sign = np.sign(original.to_numpy())
    generated_sign = np.sign(ordered_matrix.to_numpy())

    n_reactions = original_sign.shape[1]

    column_distances = []

    for i in range(n_reactions):
        col_original = original_sign[:,i]
        col_generated = generated_sign[:,i]

        hamming_i = distance.hamming(col_original,col_generated)
        column_distances.append(hamming_i)

    #hamming_ratio = np.mean(column_distances)

    count_zero = 0
    for i in column_distances:
        if i == 0 :
            count_zero += 1
    
    success_ratio = count_zero / len(column_distances)

    hamming_values = []

    for j in column_distances:
        if j != 0:
            hamming_values.append(j)
    
    hamming_ratio = np.mean(hamming_values)

    print(f"\nlista con distaze di Hamming:{column_distances}")
    print(f"rapporto di reazioni uguali all'originale:{success_ratio}")
    print(f"media sulle reazioni incorrette:{hamming_ratio}")

    return success_ratio, hamming_ratio

## Test:

O_file = "orHou2020.txt"

G_file = "Hou2020_tested.txt"

generated, original = getStechiometricMatrices(G_file,O_file)
average_on_rownames = percentage_matching_rownames(generated, original)

Hamming_ratio_1_csv = "valuation_hou2020_success.csv"
Hamming_ratio_2_csv = "valuation_hou2020_failure.csv"
Hamming_ratio_3_csv = "valuation_hou2020_rownames_similarity.csv"

result = checking_simulation(G_file, O_file)

csv_out_3= pd.DataFrame({"Average equal species": [average_on_rownames]})
csv_out_3.to_csv(Hamming_ratio_3_csv, index=False)