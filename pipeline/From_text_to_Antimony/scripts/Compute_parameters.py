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

        gen_matrix, orig_matrix = getStechiometricMatrices(gen_file, orig_file)

        gen_ordered_matrix = Ordering_by_original_rownames(gen_matrix, orig_matrix)

        x, y, z, hamming = order_matrices_by_original_columns(gen_ordered_matrix, orig_matrix)
       

    else:
        x = np.nan
        y = np.nan
        z = np.nan
        hamming = np.nan

        # write the ratios on a CSV:

    csv_out_1=pd.DataFrame({"success based on sources&target":[x]})
    csv_out_1.to_csv("success_Source&Target_aguda.csv", index=False)

    csv_out_2= pd.DataFrame({"success based on real coeff": [y]})
    csv_out_2.to_csv("Success_Real_coeff_aguda.csv", index=False)

    csv_out_3 = pd.DataFrame({"Rmse-norm": [z]})
    csv_out_3.to_csv("Rmse_aguda.csv", index=False)

   
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

            #print(f"generated_matrix:{gen_df}")
 
    # Loading the original model and extracting its stechiometric matrix
        
        with open(orig_file, "r") as file2:
            
            original = file2.read()
            
            orig_model = te.loadAntimonyModel(original)

            depen_or_sp = orig_model.getFloatingSpeciesIds()
            
            orig_matrix = orig_model.getFullStoichiometryMatrix()

            orig_df = pd.DataFrame(orig_matrix, index=depen_or_sp)

            #print(f"original_matrix:{orig_df}")
        
        return gen_df, orig_df
    
    except Exception:

        return None, None
    

def Ordering_by_original_rownames(df1,df2):

    gen_reordered = df1.reindex(df2.index)

    missing_rows = gen_reordered[gen_reordered.isna().all(axis=1)].index

    for row in missing_rows:
        gen_reordered.loc[row] = np.zeros(df1.shape[1])

        print(f"\nMatrice ordinata per il nome delle specie:{gen_reordered}")

    return gen_reordered

def percentage_matching_rownames(data_1, data_2):

    original = te.loada(data_2)

    generated = te.loada(data_1)

    original_sp = original.getFloatingSpeciesIds()

    print(f"lista original species: {original_sp}")

    generated_sp = generated.getFloatingSpeciesIds()

    print(f"lista generated species: {generated_sp}")

    orig_species = set(original_sp)

    print(f"Original species from original model: {orig_species}")
    
    gen_species = set(generated_sp)

    print(f"generated species from generated model: {gen_species}")

    common = orig_species.intersection(gen_species)

    average_common_names = len(common) / len(orig_species)

    print(f"average of species names in common between the two matrices: {average_common_names}")

    return average_common_names

def order_matrices_by_original_columns(gen_df, orig_df):

    ordered_generated_cols = []
    generated2original = OrderedDict()
    
    correct_pattern = 0
    correct_coeff = 0
    
    errors = []
    hamming_dist = []

    for orig_col in orig_df.columns:

        orig_vec = orig_df[orig_col].values

        sources = orig_vec < 0
        targets = orig_vec > 0

        generated2original[orig_col] = []
        
        for gen_col in gen_df.columns:
            
            gen_vec = gen_df[gen_col].values
            g_sources = gen_vec < 0
            g_targets = gen_vec > 0
        
            if np.array_equal(sources,g_sources) and np.array_equal(targets,g_targets):
                
                generated2original[orig_col].append(gen_col)        

        if len(generated2original[orig_col]) > 0:
            correct_pattern += 1   
   
        print("dizionatio riordinato\n")
        print(generated2original)
    # selection of the closest candidates

    for i, (orig_col, gcandidates) in enumerate(generated2original.items()):

        o_vector = orig_df[orig_col].values

        if len(gcandidates) == 0:
            zero_vec = pd.Series(
                np.zeros(orig_df.shape[0]),
                index=orig_df.index
            )
            ordered_generated_cols.append(zero_vec)

            error_vec = np.zeros_like(o_vector, dtype=float)
            mask = (o_vector != 0) | (zero_vec.values != 0)
            den_zero = np.where(o_vector == 0, 1, o_vector)
            error_vec[mask] = ((o_vector[mask] - zero_vec[mask]) / den_zero[mask])**2
            errors.append(error_vec)
            
            hamming_dist.append(distance.hamming(o_vector, zero_vec))

            continue
        
        distances = []

        for candidate in gcandidates:
            g_vector = gen_df[candidate].values
            dist = np.linalg.norm(o_vector - g_vector)
            distances.append(dist)
        
        best_idx = np.argmin(distances)
        best_gen_col = gcandidates[best_idx]

        best_vec = gen_df[best_gen_col].values

        ordered_generated_cols.append(gen_df[best_gen_col])
        
        if np.array_equal(o_vector,best_vec):

            correct_coeff += 1
        else:
            
            error_vec = np.zeros_like(o_vector, dtype=float)
            mask = (o_vector != 0) | (best_vec != 0)
            den = np.where(o_vector == 0, 1, o_vector)
            error_vec[mask] = ((o_vector[mask] - best_vec[mask]) / den[mask])**2
            #error_vec = (o_vector != best_vec).astype(float)

            print(error_vec)
            errors.append(error_vec)

            hamming_dist.append(distance.hamming(o_vector, best_vec))

    total = len(orig_df.columns)

    percent_pattern = correct_pattern/total

    percent_coeff = correct_coeff/total

    if len(errors) > 0:

        errors = np.array(errors)

        print(f"errors:\n{errors}")

        rmse_per_reaction = np.sqrt(np.mean(errors, axis=1))

        for i, ev in enumerate(errors):
            print(f"Errore reazione {i+1}: {ev}, RMSE per reazione: {rmse_per_reaction[i]}")

        rmse_avg = np.mean(rmse_per_reaction)

    else:

        rmse_avg = 0

    hamming_avg = np.mean(hamming_dist) if hamming_dist else 0

    return percent_pattern, percent_coeff, rmse_avg, hamming_avg



# test:

d_orig = {
    "R1": [-1, 1, 0, 0],
    "R2": [0, -1, 1, 0],
    "R3": [0, 0, -1, 1]
}

df_orig = pd.DataFrame(d_orig, index=["A", "B", "C", "D"])

d_gen = {
    "G1": [-1, 1, 0, 0],   # R1 perfetta
    "G2": [0, -2, 0, 0],   # R2 parzialmente sbagliata (B sbagliata)
    "G3": [0, 0, -1, 0]    # R3 parzialmente sbagliata (D mancante)
}

df_gen = pd.DataFrame(d_gen, index=["A", "B", "C", "D"])

print(df_orig)
print(df_gen)

#original_file = "orAguda1999.txt"

#generated_file = "Aguda1999_tested.txt"

#result_1 = checking_simulation(generated_file, original_file)


#gen_matrix, orig_matrix = getStechiometricMatrices(df1, df2)

gen_ordered_matrix = Ordering_by_original_rownames(df_gen, df_orig)
x, y, z, hamming = order_matrices_by_original_columns(gen_ordered_matrix, df_orig)

#csv_out_1=pd.DataFrame({"success based on sources&target":[x]})
#csv_out_1.to_csv("Source&Target.csv", index=False)

#csv_out_2= pd.DataFrame({"success based on real coeff": [y]})
#csv_out_2.to_csv("Success_Real_coeff.csv", index=False)

#csv_out_3 = pd.DataFrame({"Rmse-norm": [z]})
#csv_out_3.to_csv("Rmse.csv", index=False)

#csv_out_4 = pd.DataFrame({"hamming": [hamming]})
#csv_out_4.to_csv("hamming.csv", index=False)

print(f"source_target:{x},\nreal_coeff:{y},\nhamming_ratio:{hamming},\nrmse_ratio:{z}")