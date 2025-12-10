import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
import tellurium as te
import math


input_1 = snakemake.input[0]
input_2 = snakemake.input[1]
output_1 = snakemake.output[0]
output_2 = snakemake.output[1]


def simulate_and_check(file1, file2):
    
    gen_ok = True
    orig_ok = True

    try:
        with open(file2, "r") as f2:
            original = f2.read()

        or_load = te.loadAntimonyModel(original)
        ts_ground = or_load.simulate(0,100,200)
    except Exception:
        orig_ok = False

    try:
        with open(file1, "r") as f1:
            generated = f1.read()

        gen_load = te.loadAntimonyModel(generated)
        ts_gen = gen_load.simulate(0,100,200)
    except Exception:
        gen_ok = False

    #decision logic
        
    if orig_ok and gen_ok:

        # Compute reproducibility
        aafe_result = partial_reproducibility(ts_ground, ts_gen)

        # plot both
        make_plots(ts_ground, ts_gen, output_2)

        # write CSV
        with open(output_1, "w") as file:
            csv1 = pd.DataFrame({"AAFE evaluation": [aafe_result]})
            csv1.to_csv(output_1, index=False)

    else:
        # Only original works -> plot only that
        make_single_plot(ts_ground, output_2)

        # AAEF not computed --> value = 1
        with open(output_1, "w") as file:
            csv1 = pd.DataFrame({"AAFE evaluation": [1]})
            csv1.to_csv(output_1, index=False)


"""
    Compute AAFE using the formula:
    AAFE = 10^( (1/n) * sum( | log10(gen_i / orig_i) | ) )
"""

def AAFE(ground, gen):
        if not ground or not gen or len(ground) != len(gen):
                return None
        terms = []
        for o, p in zip(ground, gen):
            o = float(o)
            p = float(p)
            if o <= 0 or p <= 0:
                return None
            terms.append(abs(math.log10(p / o)))


        return 10 ** (sum(terms) / len(terms))

def partial_reproducibility(obs_matrix, gen_matrix):
    obs_cols = len(obs_matrix[0]) - 1
    gen_cols = len(gen_matrix[0]) - 1  # -1 since ignore time column

    shared_vars = min(obs_cols, gen_cols) 

    for var_idx in range(1, shared_vars + 1):
        obs_series = [row[var_idx] for row in obs_matrix]
        gen_series = [row[var_idx] for row in gen_matrix]
        
        aafe = AAFE(obs_series, gen_series)
        if aafe is not None and aafe <= 2:
            return 0

    return 1

#def partial_reproducibility(obs_matrix, gen_matrix):
#    num_vars = len(obs_matrix[0]) - 1   # -1 since ignore time column
    
    # var_idx begin from 1, first variable
#    for var_idx in range(1, num_vars + 1):
#        obs_series = [row[var_idx] for row in obs_matrix]
#        gen_series = [row[var_idx] for row in gen_matrix]
        
#        aafe = AAFE(obs_series, gen_series)
        
#        if aafe is not None and aafe <= 2:
#            return 0   # at least one riproducible plot

#    return 1           # no reproducible plot

# Plots:

def make_single_plot(ts_ground, outfile):

    time_col = ts_ground.colnames.index("time")
    time = ts_ground[:,time_col]

    species = [c for c in ts_ground.colnames if c != "time"]
    n = len(species)

    fig, axes = plt.subplots(n,1, figsize=(10, 4*n), sharex=True)

    if n == 1:
         axes = [axes]
    
    for ax, sp in zip(axes, species):
        sp_col = ts_ground.colnames.index(sp)
        # ground-truth (solid)
        ax.plot(time, ts_ground[:, sp_col], label="Ground-truth", linewidth=2)
        ax.set_ylabel(sp)
        ax.legend()

    axes[-1].set_xlabel("Time")

    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()

def make_plots(ts_ground, ts_gen, outfile):
     # --- get column indices ---
    time_col = ts_ground.colnames.index("time")
    
    # species in ground
    species_ground = [c for c in ts_ground.colnames if c != "time"]
    species_gen = [c for c in ts_gen.colnames if c != "time"]
    
    # all species = all columns except "time"
    #species = [c for c in ts_ground.colnames if c != "time"]

    N_ground = len(species_ground)
    N_gen = len(species_gen)

    #final number of species to compare

    N = min(N_ground, N_gen)

    # first species
    species_ground = species_ground[:N]
    species_gen = species_gen[:N]

    # extract time (1D array)
    time = ts_ground[:, time_col]

    #n = len(species)

    n = N
    
    # no variable/species to plot
    if n == 0:
        plt.figure()
        plt.text(0.5,0.5, "No variables to plot", ha="center", va="center")
        plt.savefig(outfile, dpi=300)
        plt.close()
        return

    # --- compute subplot grid: 2 columns ---
    ncols = 2
    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(nrows, ncols, figsize=(10, 4*nrows), sharex=True)

    # if only one species, make axes iterable
    if n == 1:
        axes = [axes]

    # axes might be 2D -> flatten for easy iteration
    axes = axes.flatten()

    for ax, sp_ground, sp_gen in zip(axes, species_ground, species_gen):
        #sp_col = ts_ground.colnames.index(sp)
        sp_col_ground = ts_ground.colnames.index(sp_ground)
        sp_col_gen = ts_gen.colnames.index(sp_gen)

        # ground-truth (solid)
        ax.plot(time, ts_ground[:, sp_col_ground], label="Ground-truth", linewidth=2)
        # generated (dashed)
        ax.plot(time, ts_gen[:, sp_col_gen], '--', label="Generated", linewidth=2)
        ax.set_ylabel(sp_ground)
        ax.legend()
    
    if n>0:
        axes[-1].set_xlabel("Time")

    # turn off any unused axes (if species count is odd)
    for empty_ax in axes[n:]:
        empty_ax.axis("off")

    fig.suptitle("Ground-truth vs Generated Simulation", y=0.995)

    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()

         
simulate_and_check(input_1, input_2)

