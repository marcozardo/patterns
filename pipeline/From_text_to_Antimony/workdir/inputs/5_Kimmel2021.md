

The roles of T cell competition and stochastic extinction events in chimeric antigen receptor T cell therapy <!-- text, from page 0 (l=0.400,t=0.045,r=0.907,b=0.144), with ID 1d5022de-e475-4870-a6d1-774135c22170 -->

Gregory J. Kimmel¹, Frederick L. Locke²,† and Philipp M. Altrock¹,²,³,† <!-- text, from page 0 (l=0.404,t=0.156,r=0.888,b=0.179), with ID 27aa7425-d689-4fef-8b6f-c33fcc01bc53 -->

¹Department of Integrated Mathematical Oncology, ²Department of Blood and Marrow Transplant and Cellular Immunotherapy, and ³Department of Malignant Hematology, H. Lee Moffitt Cancer Center and Research Institute, Tampa, FL, USA <!-- text, from page 0 (l=0.402,t=0.186,r=0.931,b=0.228), with ID 661d60fb-57ff-4876-8991-6ff08331a1a6 -->

logo: ORCID

GJK, 0000-0001-9766-5399; PMA, 0000-0001-7731-3345 <!-- text, from page 0 (l=0.402,t=0.231,r=0.697,b=0.250), with ID 7105b387-4497-43c6-a553-7e4228e070a2 -->

Chimeric antigen receptor (CAR) T cell therapy is a remarkably effective
immunotherapy that relies on in vivo expansion of engineered CAR T cells,
after lymphodepletion (LD) by chemotherapy. The quantitative laws under-
lying this expansion and subsequent tumour eradication remain unknown.
We develop a mathematical model of T cell–tumour cell interactions and
demonstrate that expansion can be explained by immune reconstitution
dynamics after LD and competition among T cells. CAR T cells rapidly
grow and engage tumour cells but experience an emerging growth rate dis-
advantage compared to normal T cells. Since tumour eradication is
deterministically unstable in our model, we define cure as a stochastic event,
which, even when likely, can occur at variable times. However, we show
that variability in timing is largely determined by patient variability. While
cure events impacted by these fluctuations occur early and are narrowly dis-
tributed, progression events occur late and are more widely distributed in
time. We parameterized our model using population-level CAR T cell and
tumour data over time and compare our predictions with progression-free sur-
vival rates. We find that therapy could be improved by optimizing the tumour-
killing rate and the CAR T cells’ ability to adapt, as quantified by their carrying
capacity. Our tumour extinction model can be leveraged to examine why
therapy works in some patients but not others, and to better understand the
interplay of deterministic and stochastic effects on outcomes. For example,
our model implies that LD before a second CAR T injection is necessary. <!-- text, from page 0 (l=0.407,t=0.259,r=0.929,b=0.580), with ID 9c9556d2-b2db-4ac3-9089-8c9c7ff2180f -->

## 2. Methods
We model dynamics and interactions among normal T cells, CAR T cells and tumour cells. The model considers three cell populations in the form of continuous-time birth and death stochastic processes and their deterministic mean-field equations: normal T cells, *N*, CAR T cells, *C*, both given in cells μl⁻¹, and antigen-presenting tumour cells, *B*, given in ml. These measurements can be converted to cell counts. A more detailed overview of the methods can be found in the electronic supplementary material, sections 1 and 2. <!-- text, from page 0 (l=0.067,t=0.359,r=0.481,b=0.501), with ID 64992745-c167-4e3a-95ab-1793a4514af0 -->

We define the following two scenarios. Complete response
(CR) is achieved when the tumour is eradicated. Progressive
disease (PD) is counted when the tumour has reached 120% of
its initial size. Note that the clinical definition of progression
typically is less quantitatively tractable [16], as clinical pro-
gression can occur whenever the disease worsens in relation to
its nadir size, which could be markedly less than the value at
baseline [17]. <!-- text, from page 0 (l=0.067,t=0.501,r=0.480,b=0.605), with ID 84fb8052-8099-4cc3-b0ac-33d5fb9b8a3a -->

We consider the case of lymphodepleting chemotherapy
prior to infusion of autologous CAR T cells. We set time to 0 at
the time of CAR infusion. Normal and CAR T cell populations
then grow towards their respective carrying capacities but influ-
ence each other. This mutual influence gives rise to selection. <!-- text, from page 0 (l=0.068,t=0.605,r=0.480,b=0.670), with ID c7c809c0-f95b-43a8-8f80-b426440a9e7a -->

We exclude possible influences by other sources of CD19, such as normal B cells, based on the following observations. Patients have effectively zero normal B cells following lympho-depleting chemotherapy and prior/concurrent to CAR T cell infusion. Furthermore, the reconstitution of normal B cells is extremely slow, such that only 50% of patients have recovered any normal B cells by 1 year after therapy. While it is possible that normal B cells activate CD19 directed CAR T cells, at this scale the dynamics of CAR T are probably not impacted by normal B cells. Thus, in the patient population we are interested in, normal sources of CD19 do not seem to play a significant role. Meanwhile, the tumour cell population $B$ grows autonomously at a net growth rate $r_B$ and experiences tumour killing at rate $\gamma_{B}$, proportional to the number of CAR T cells. <!-- text, from page 0 (l=0.068,t=0.670,r=0.479,b=0.852), with ID 96fbd9da-f9db-4f23-a17c-4b1d9040748b -->

These biological mechanisms could manifest themselves in
multiple ways in a mathematical model. A carrying capacity
for T cells could emerge due to predation, resource or spatial
limitations, birth and death rate balance through exogeneous
effects (e.g. paracrine signalling [18]), or any combination of
the above. We investigated different functional forms (a general-
ized logistic, Gompertz, and an explicit interaction model, <!-- text, from page 0 (l=0.068,t=0.853,r=0.479,b=0.946), with ID 3dfe90da-6d82-4ad9-b5a5-e31a8a741e75 -->

discussed in the electronic supplementary material, section 3).
Using an information criterion, we elected to use a Gompertz
model approach. The corresponding dynamical system in the
mean-field limit is <!-- text, from page 0 (l=0.521,t=0.046,r=0.931,b=0.101), with ID bb4030f8-1a00-49a9-8a5e-79a0b31cac87 -->

$
\frac{\mathrm{d}N}{\mathrm{d}t} = -r_N\, N \ln \left[ \frac{N + C}{K_N} \right], \tag{2.1}
$

$
\frac{\mathrm{d}C}{\mathrm{d}t} = -r_C(T)\, C \ln \left[ \frac{N + C}{K_C} \right] \tag{2.2}
$

$
\text{and} \qquad \frac{\mathrm{d}B}{\mathrm{d}t} = r_B B - \gamma_B\, B \frac{C}{k_B + C}. \tag{2.3}
$ <!-- text, from page 0 (l=0.522,t=0.106,r=0.931,b=0.192), with ID 508c647a-b126-4d08-8e4a-b81760fdb396 -->

Here $T = N + C$ is the total lymphocyte count, and $r_C(T) = \rho_C + b(T - K_N)^2 / (a / (T^2 + (T - K_N)^2))$, where $\rho_C$ is a background expansion rate and the second term reflects that growth can be muted when the overall (largely normal) T cell population reaches capacity, modulated by the two parameters $a$ and $b$. We introduced feedback of total lymphocyte count on CAR expansion because the CAR T cell population expands at a faster rate initially and contracts slower after peak, which has been a challenge in several of the recent quantitative modelling approaches [6,11]. A generalized logistic or Gompertz form cannot alone capture this behaviour. Thus, we chose to include additional feedback into the intrinsic growth rate function $\rho_C$, which becomes a function of the total T cell count $T$, the tumour mass $B$, or both (see electronic supplementary material, section 3). For a deeper discussion on the assumptions and details of the system of equations (2.1)-(2.3), which can be based on a stochastic birth and death process, see the electronic supplementary material, section 3, where we also present a linear stability analysis. Figure 1a shows a schematic of the dynamical system. Figure 1b shows the associated cellular events, which can be interpreted deterministically or stochastically. The deterministic system’s *qualitative* behaviour aligns with clinical observations (figure 1d–f). <!-- text, from page 0 (l=0.521,t=0.202,r=0.932,b=0.489), with ID 26153a58-3ab8-4958-8a27-d7aee1db431d -->

Tumour killing by CAR T cells is modelled as a result of contact, thus is proportional to $B \times C$ and includes a saturation factor, motivated by the assumption that there exists an upper limit at which CAR T cells can interact and kill the tumour cells. <!-- text, from page 0 (l=0.523,t=0.490,r=0.931,b=0.541), with ID 01d1392c-d53e-4517-9f92-b85b23d612e4 -->

Altogether, these assumptions lead to seven parameters to be
fitted by optimization, based on 11 data points from clinical
observations—five for CAR T and five for absolute lymphocyte
count (ALC), excluding the initial conditions, and one measure-
ment for the tumour state at day 30 (for further details see
electronic supplementary material, section 4). <!-- text, from page 0 (l=0.522,t=0.542,r=0.932,b=0.620), with ID 1b317730-168b-4f30-8536-3369b646832d -->

3. Results  
We calibrated the deterministic model using clinical data (figure 2a,b; electronic supplementary material, sections 2 and 4), which led to the parameters in table 1. To recapitulate and predict progression-free survival over time, we employed the corresponding stochastic formulation (electronic supplementary material, section 5), which is able to capture dynamics of small tumour populations near extinction. <!-- text, from page 0 (l=0.521,t=0.653,r=0.931,b=0.776), with ID 95e707bc-d809-4895-8b07-d52cd8304543 -->

(a) Parameter sensitivity and identifiability  
We conducted a local sensitivity and identifiability analysis  
[21–23] of the fitted parameters. The resulting ranking of  
parameters highlights that the carrying capacities of the CAR  
and normal T cells, respectively, and the maximal tumour-  
killing rate were most sensitive (figure 2c). Note here that low  
sensitivity of a parameter does not imply that the model is  
not sensitive to these parameters. We performed an identifi-  
ability analysis, with a threshold value of 0.9, to indicate  
non-identifiability between parameters pairs. Strong Pearson <!-- text, from page 0 (l=0.522,t=0.799,r=0.931,b=0.945), with ID d0525937-de6b-4cb3-a49c-067252d20f11 -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.001,t=0.299,r=0.030,b=0.700), with ID df814898-9b26-416b-97d3-a177356899f0 -->

2 <!-- marginalia, from page 0 (l=0.940,t=0.047,r=0.975,b=0.067), with ID e145281e-76dd-4103-bff5-8eaee72b1182 -->

royalsocietypublishing.org/journal/rspb

Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.946,t=0.077,r=0.976,b=0.375), with ID 0a52740d-f3d0-4b01-896c-dc77e81ae920 -->

Summary : This figure presents a mechanistic mathematical model of T cell, CAR T cell, and tumor cell dynamics, integrating experimental and clinical data to simulate and predict different response scenarios to CAR T cell therapy in cancer.

flowchart and multi-panel schematic:
# (a) Schematic of the Model :
  • Depicts three main cell populations: normal T cells (N, green), CAR T cells (C, blue), and CD19+ tumor cells (B, pink).
  • Arrows indicate interactions: normal T cell expansion, CAR T cell expansion, competition between T and CAR T cells, tumor killing by CAR T cells, and net tumor growth.

# (b) Individual Cellular Processes :
  • Lists four key processes with associated rates:
    – Normal T cell expansion: R_N(N, C)
    – CAR T cell expansion: R_C(N, C, B)
    – Tumor killing by CAR T cells: γ_B
    – Tumor growth: r_B
  • Visual icons represent each process (green, blue, and pink circles).

# (c) Data and Model Integration :
  • Flowchart showing integration of data and modeling:
    – Green box: T cell kinetics over time (lymphocyte counts, Moffitt patients with CAR T).
    – Blue box: CAR T cell kinetics (ZUMA-1, peripheral CAR at days 5, 14, 28, 90, 180).
    – Red box: Tumor size estimates (MTV, CR, PD).
    – Arrows lead to "mechanistic model formulation" and "model calibration," then to "simulate stochastic outcomes."

# (d–f) Model Kinetics: Simulated Response Scenarios :
  • Three line plots (d, e, f) show cell population size vs. time for three cell types:
    – Tumor cells (red line)
    – CAR T cells (blue line)
    – Normal T cells (green dashed line)
  • (d) No response: Tumor cells increase, CAR T cells decline, normal T cells plateau.
  • (e) Transient response: Tumor cells initially decrease, then regrow; CAR T cells peak then decline; normal T cells plateau.
  • (f) Long-term response: Tumor cells decrease and remain low; CAR T cells decline after initial peak; normal T cells plateau.

# Design Encodings :
  • Distinct colors for each cell type: green (normal T), blue (CAR T), red (tumor).
  • Solid and dashed lines differentiate cell types.
  • Schematic arrows and flowchart boxes use color-coding matching cell types.

# Analysis :
  • The model integrates experimental and clinical data to simulate T cell and tumor dynamics.
  • Three kinetic scenarios illustrate possible patient responses to CAR T therapy: no response, transient response, and long-term response.
  • The model highlights the importance of CAR T cell expansion and persistence for durable tumor control, and the competitive dynamics between normal and CAR T cells.
  • The flowchart demonstrates a systematic approach to model calibration and simulation using real patient data. <!-- figure, from page 0 (l=0.090,t=0.044,r=0.904,b=0.440), with ID 9f9604d3-bb82-446b-8e5c-dde1212b0d82 -->

Figure 1. Overview of cellular interactions, kinetics, data integration and qualitative dynamics. (a) Model schematic of three cell compartments: CAR T cells, $C$, proliferate and interact with resident (normal) lymphocytes, $N$ (depleted by lymphodepleting chemotherapy). CAR T cells also engage in killing CD19+ tumour and other $B$ cells. (b) The system can be described by four cellular kinetic reactions, with density-dependent feedback (differences in carrying capacities) in the net expansion rates: $R_X = r_X \ln(K_X/(N + C))$, where $X$ stands for $N$ or $C$. The deterministic, large population size limit of these dynamics is given by equations (2.1)–(2.3). (c) Schematic of data integration to parametrize the mathematical model; we used longitudinal data of peripheral absolute lymphocyte count (ALC), peripheral CAR+ cell counts per $\mu$L, and the tumour volume-changes as estimated from patients of the ZUMA-1 trial with complete response (CR) or progressive disease (PD). We assumed that, at days 30, 60 or 90, CRs had no detectable tumour mass, and that PDs had 1.2 times their initial tumour size. Median initial tumour mass was 94.86 ml. The qualitative dynamics of the system, given by equations (2.1)–(2.3): no response to CAR therapy (d), transient response followed by progression/relapse (e) and long-term response (tumour appears to be eradicated) (f). These illustrative examples are not to scale. <!-- text, from page 0 (l=0.067,t=0.441,r=0.932,b=0.574), with ID 756922ed-22e8-4046-942b-a0159b99fd9c -->

correlations between $k_B$ and $r_B$ (0.94), and between $k_B$ and $\gamma_B$ (–0.96) were observed (figure 2d inset), which suggests that these pairs are not identifiable. All other pairs were below the threshold and can be considered identifiable. The sensitivity ranking suggests that the most promising avenues to improve CAR T cell therapy should focus on improving adaptability (carrying capacity) and efficacy (tumour-killing rate) of the engineered CAR T cell product. <!-- text, from page 0 (l=0.067,t=0.607,r=0.480,b=0.723), with ID c06cc0f9-f949-4340-9370-5f31f97c4726 -->

(b) Immune reconstitution and return to homeostasis  
during chimeric antigen receptor T cell therapy  
follows a Gompertz growth law

We initially hypothesized that immune reconstitution follows a generalized logistic growth equation of the form $x'(t) = rx(1 - (x/k)^c)$ [24]. This approach contains the standard logistic model ($c = 1$) and leads to Gompertz growth in the limits $c \to 0$, $r \to \infty$. Our nonlinear optimization routine for data fitting (see electronic supplementary material, section 3) selected Gompertz as the best approach for immune reconstitution dynamics (figure 2a). The optimizer was selecting $r$ at the edge of the upper boundary of its optimization region, while selecting $c$ at the lowest possible (positive) value. We <!-- text, from page 0 (l=0.067,t=0.739,r=0.480,b=0.947), with ID 9778f4d8-dc03-413d-8fc9-ed96435243a2 -->

$x'(t) = -rx\ln[x/k]$ <!-- text, from page 0 (l=0.519,t=0.606,r=0.931,b=0.638), with ID cf34c6f8-652b-4512-99b1-3b79beb7066c -->

(c) Chimeric antigen receptor T cell kinetics can be explained by increased growth rate and lower carrying capacity

We hypothesized that CAR T cells become maladapted during the manufacturing process, lowering their carrying capacity. After lymphodepletion, a complex signalling cascade occurs that results in immune reconstitution towards homeostatic levels [19], driven by stem and progenitor cells [25,26]. Both normal T cells (figure 2a) and CAR T cells (figure 2b) use the changing environment to proliferate and expand, but only normal cells can be reconstituted from stem cells. Although we do not model these signals explicitly, the system’s behaviour can be observed through the interplay of the normal and CAR T cells. As a result, CAR T cells are outcompeted by normal T cells [27] in the long term, resulting in lower carrying capacity. An alternative hypothesis that could explain the kinetics would be predation of CAR T cells by normal T cells. We examined and ultimately discarded this alternative hypothesis <!-- text, from page 0 (l=0.520,t=0.669,r=0.932,b=0.945), with ID b1d1c7b9-e9ee-44a4-9db8-f0893345ca79 -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.001,t=0.299,r=0.029,b=0.701), with ID 79f5049b-6898-47fd-96b2-a1c6f66a3de3 -->

3 <!-- marginalia, from page 0 (l=0.939,t=0.047,r=0.976,b=0.068), with ID 4983d7cb-314c-4e2f-a9ba-e63eef3bb65d -->

royalsocietypublishing.org/journal/rspb  
Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.946,t=0.076,r=0.975,b=0.376), with ID 695c9058-1d78-4c1f-a3ef-ff15e957fc8f -->

Summary : This figure presents two panels: (a) a time-course plot of normal T cell dynamics in patients, comparing model fit to empirical data, and (c) a parameter sensitivity and correlation analysis for the model parameters.

line and scatter plots with heatmap inset:
# (a) Normal T cell dynamics
Title & Axes :
  • Title: "normal T cell dynamics"
  • X-axis: "time (days)", tick labels: 0, 50, 100, 150, 200
  • Y-axis: "normal T cell ml⁻¹", tick labels: 0, 100, 200, 300, 400, 500
Data Points :
  • Data (grey circles): (0, 0), (10, ~200), (20, ~350), (40, ~450), (100, ~500), (200, ~500)
  • Model fit (green solid line): rises steeply from (0, 0) to plateau near (50, 500)
  • Model equation: 𝑁̇ = r_N N ln [K_N / (N + C)]
Design Encodings :
  • Grey filled circles for data points
  • Green solid line for model fit
  • Legend: "model fit" (green line), "data" (grey circle)
  • Inset text: "medians from 55 patients; calculated from ALC, subtracting CAR"
Distribution & Trends :
  • Rapid initial increase in T cell count, plateauing near 500 normal T cells/ml after ~50 days

# (c) Parameter sensitivity and correlation
Title & Axes :
  • Title: "parameter sensitivity and correlation"
  • X-axis: "model parameter", labels: K_C, K_N, γ_B, r_N, k_B, ρ_C, a, r_B, b
  • Y-axis: "relative sensitivity", log scale, tick labels: 0.005, 0.010, 0.050, 0.100, 0.500, 1
Data Points :
  • Blue circles for each parameter, showing relative sensitivity values (exact y-values not specified)
Design Encodings :
  • Blue filled circles for sensitivity values
  • Logarithmic y-axis
  • Inset: heatmap matrix of parameter correlations, with green (positive), red (negative), and white (near zero) cells, values ranging from -0.14 to 0.14
  • Correlation matrix labels: r_N, ρ_C, k_C, K_N, k_B, γ_B, a, b, r_B
Distribution & Trends :
  • Sensitivity decreases from left (K_C) to right (b)
  • Correlation matrix shows most values near zero, with a few moderate positive/negative correlations

Analysis :
  • The model accurately fits the empirical T cell data, capturing the rapid rise and plateau in cell counts.
  • Parameter sensitivity analysis reveals that K_C and K_N are the most sensitive parameters, while b and r_B are least sensitive.
  • The parameter correlation matrix indicates generally low correlations, suggesting parameter identifiability, with a few moderate correlations (both positive and negative) between specific pairs. <!-- figure, from page 0 (l=0.099,t=0.043,r=0.886,b=0.241), with ID dd50134a-5bf0-44f9-9921-d16c0c40fc46 -->

Summary : This figure presents the dynamics of CAR T cell concentrations in blood over time, comparing a mathematical model fit to median patient data.

line plot:
Title & Axes :
  • Title: “CAR T cell dynamics” (panel label: (b)).
  • X-axis: “time (days)”, range: 0 to 200.
  • Y-axis: “CAR+ T cell ml⁻¹”, range: 0 to 40.
  • Tick marks: X-axis at 0, 50, 100, 150, 200; Y-axis at 0, 10, 20, 30, 40.

Data Points :
  • Data (grey circles): Median CAR+ T cell concentrations at approximately (0, 0.36), (5, ~35), (20, ~5), (50, ~2), (100, ~1), (200, ~0.5) cells ml⁻¹.
  • Model fit (blue line): Smooth curve peaking sharply near day 5, then declining rapidly and flattening toward zero by day 200.

Design Encodings :
  • Model fit: solid blue line.
  • Data: large grey filled circles.
  • Legend: “model fit” (blue line), “data” (grey circle).
  • Mathematical model equations shown on plot:
    - \(\hat{C} = r_C(N, C)C \ln\left[\frac{K_C}{N + C}\right]\)
    - \(r_C(N, C) = \rho_C + \frac{b(N + C - K_N)^2}{a(N + C)^2 + (N + C - K_N)^2}\)
  • Text box: “medians from 101 patients [5]; initial condition: 0.36 cells ml⁻¹ at t = 0”.

Distribution & Trends :
  • The CAR+ T cell count rises sharply to a peak near day 5, then declines rapidly, approaching a low steady value by day 200.
  • Data points closely follow the model fit.

Analysis :
  • The model accurately captures the rapid expansion and subsequent contraction of CAR+ T cells post-infusion, as observed in patient medians.
  • The initial condition and model equations are explicitly provided, supporting reproducibility.
  • The data show a pronounced early peak followed by a long, low plateau, indicating a transient expansion phase. <!-- figure, from page 0 (l=0.098,t=0.249,r=0.500,b=0.429), with ID 4fb60093-b2fb-4ce1-9314-c0002bcbad36 -->

Summary : This figure shows two possible outcomes (cure vs. progression) of CD19+ tumour cell counts over time after CAR infusion, using the same model parameters but different stochastic realizations.

line plot:
Title & Axes :
  • Title: "tumour dynamics: same parameters, different outcomes"
  • X-axis: "days post CAR infusion" (range: 0 to 180, ticks at 0, 30, 60, 90, 120, 150, 180)
  • Y-axis: "CD19+ tumour cell" (log scale, range: 10^0 to 10^12, ticks at 10^0, 10^2, 10^4, 10^6, 10^8, 10^10, 10^12)

Data Points :
  • Series 1 (solid red line, labeled "cure"): Tumour cell count decreases steeply from ~10^10 at day 0 to below 10^2 by day 60, then remains low.
  • Series 2 (dotted red line, labeled "progression"): Tumour cell count decreases similarly at first, but after ~day 60, begins to rise again, reaching above 10^4 by day 180.

Design Encodings :
  • Solid red line for "cure", dotted red line for "progression".
  • Logarithmic Y-axis.
  • Dashed horizontal line at y = 10^2.
  • Equation inset: Ẋ = r_B - γ_B B (C / (k_B + C)), indicating the model for tumour cell dynamics.
  • Legend: "cure" (solid), "progression" (dotted).
  • Caption box: "two realizations of the same stochastic process".

Distribution & Trends :
  • Both series show a rapid initial decline in tumour cell count.
  • "Cure" series remains low after initial decline.
  • "Progression" series rebounds after initial decline, showing tumour regrowth.

Analysis :
  • The figure demonstrates that, even with identical parameters, stochastic effects can lead to divergent outcomes: either sustained tumour clearance (cure) or tumour regrowth (progression).
  • The initial response to CAR infusion is similar in both cases, but long-term fate diverges after ~60 days.
  • The log scale highlights the dramatic changes in tumour cell numbers and the difference in long-term outcomes. <!-- figure, from page 0 (l=0.503,t=0.251,r=0.900,b=0.429), with ID 1a023cf4-be07-4394-81de-6d8f3b2edcd7 -->

Figure 2. Comparison of model fits and data in the T cell compartments, stochastic dynamics in the tumour cell compartment. (a) ALC was used to parameterize normal T cell dynamics, equation (2.1), using ALC-CAR from peripheral blood to estimate normal T cell counts N. (b) CAR positive T cell dynamics, equation (2.2), were parameterized using ZUMA-1 trial data of median peripheral CAR counts, to fit peak and decay of CAR. Nonlinear optimization for data fitting explained in the electronic supplementary material, section 4. (c) Parameters ranked by local relative sensitivity measure (electronic supplementary material, section 4. Inset: parameter correlation matrix (Pearson correlation, see electronic supplementary material). (d) Two example trajectories of tumour burden over time, using identical parameters and initial conditions for the hybrid deterministic-stochastic process in the tumour compartment. Both examples enter the stochastic region (less than 100 tumour cells), but one escapes leading to progression. All parameter values and initial conditions used are given in table 1. Hybrid model simulation procedure described in the electronic supplementary material, section 5. (Online version in colour.) <!-- text, from page 0 (l=0.066,t=0.432,r=0.933,b=0.550), with ID 32f2f374-a7a1-4daa-9f23-4aa4e6f45725 -->

Table 1. Parameter and initial condition values as identified by our machine learning procedure and from the literature (also see electronic supplementary material, section 4). The CAR T cell growth rate function is $r_G$, which depends on parameters $\rho_C$, a, b. <!-- text, from page 0 (l=0.066,t=0.571,r=0.932,b=0.604), with ID 30a69608-b9ee-422f-a9cd-018ee391a328 -->

<table><thead><tr><th>biological parameter</th><th>symbol</th><th>fitted value</th><th>quartile range</th><th>ref.</th></tr></thead><tbody><tr><td>normal T cell carrying capacity</td><td>K<sub>N</sub></td><td>2.50 × 10<sup>11</sup> cells</td><td>n/a</td><td>[19]</td></tr><tr><td>CAR T cell carrying capacity</td><td>K<sub>C</sub></td><td>6.96 × 10<sup>10</sup> cells</td><td>[6.15, 9.65] × 10<sup>10</sup> cells</td><td>this work</td></tr><tr><td>normal T cell net growth rate</td><td>r<sub>N</sub></td><td>1.70 × 10<sup>−1</sup> day<sup>−1</sup></td><td>[1.65, 1.70] × 10<sup>−1</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>baseline CAR T net growth rate</td><td>ρ<sub>C</sub></td><td>2.51 × 10<sup>−2</sup> day<sup>−1</sup></td><td>[2.08, 3.54] × 10<sup>−2</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>signalling inefficiency factor in r<sub>C</sub></td><td>a</td><td>4.23 × 10<sup>−1</sup></td><td>[1.00, 3.02] × 10<sup>−1</sup></td><td>this work</td></tr><tr><td>immune reconstitution impact in r<sub>C</sub></td><td>b</td><td>5.25 × 10<sup>−1</sup> day<sup>−1</sup></td><td>[4.67, 5.22] × 10<sup>−1</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>tumour net growth rate</td><td>r<sub>B</sub></td><td>(1 − 50) × 10<sup>−2</sup> day<sup>−1</sup></td><td>n/a</td><td>[20]</td></tr><tr><td>tumour-killing rate (by effector CAR)</td><td>γ<sub>B</sub></td><td>1.15 × 10<sup>0</sup> day<sup>−1</sup></td><td>[0.64, 1.35] × 10<sup>0</sup> day<sup>−1</sup></td><td>this work</td></tr><tr><td>killing rate saturation parameter</td><td>k<sub>B</sub></td><td>2.024 × 10<sup>9</sup> cells</td><td>[1.40, 3.125] × 10<sup>9</sup> cells</td><td>this work</td></tr><tr><td>initial median normal T cell number</td><td>N(t = 0)</td><td>3.00 × 10<sup>9</sup> cells</td><td>n/a</td><td>[5]</td></tr><tr><td>initial CAR T cell number</td><td>C(0)</td><td>1.80 × 10<sup>8</sup> cells</td><td>n/a</td><td>[5]</td></tr><tr><td>initial median tumour cell number</td><td>B(0)</td><td>9.486 × 10<sup>10</sup> cells</td><td>n/a</td><td>[5]</td></tr></tbody></table> <!-- table, from page 0 (l=0.068,t=0.614,r=0.931,b=0.861), with ID 3423fd0e-e8b1-46c5-ab36-3c1b40ff760b -->

after statistical examination (see electronic supplementary
material, section 3).
  CAR T cell persistence, at least for some time, could result
from CAR T effector memory cells [6]. Currently, it is unclear <!-- text, from page 0 (l=0.067,t=0.888,r=0.480,b=0.947), with ID 09e04339-6d8e-459b-8530-5c583a85b679 -->

whether CAR T persistence plays a role in LBCL treatment
[4]; remarkably, cure is possible without CART cell persistence.
The decline over time of CART cells may occur on a time frame
longer than the expected survival time, even in patients <!-- text, from page 0 (l=0.521,t=0.889,r=0.932,b=0.947), with ID 69a15016-e112-4418-b828-01a2e9fc8042 -->

Downloaded from https://royalsocietypublishing.org/ on 02 July 2025 <!-- marginalia, from page 0 (l=0.000,t=0.297,r=0.031,b=0.703), with ID 794e735c-4696-4ab4-bef6-ca63267354de -->

4 <!-- marginalia, from page 0 (l=0.939,t=0.048,r=0.976,b=0.067), with ID 85967ed4-fa45-469e-b519-6bd210075257 -->

royalsocietypublishing.org/journal/rspb
Proc. R. Soc. B 288: 20210229 <!-- marginalia, from page 0 (l=0.947,t=0.077,r=0.976,b=0.376), with ID 8fcde566-e0e7-46e4-84bc-6eadd69f5397 -->

with tumour extinction. Therefore, the clinical definition of
(temporal) CAR T persistence may be captured by our model.

    CAR T expansion occurs rapidly within the first two weeks.
By contrast, CAR T cells decay on a much slower time scale. For
instance, the median patient still retains levels comparable to
their value at infusion by day 90. Hence, other functional
dependencies need to be placed on the CAR T cell growth
rate (equation (2.2)). The baseline rate ρ_C sets the time scale at
which birth and death events occur on average in the CAR T
cell population. These birth and death rates depend on signals
provided by all T cells, which change during therapy as the
immune system returns to homeostatic levels. Hence, we
expect the overall CAR T cell turnover rate to change during
the course of reconstitution. The dependence on the total lym-
phocyte count T describes these nonlinear dynamics as the
total T cell count approaches a carrying capacity, $T \rightarrow K_N$. <!-- text, from page 0 (l=0.064,t=0.044,r=0.483,b=0.279), with ID e3dc5b4a-c939-4ed4-a6d9-d7ec4198248d -->

(d) Stochastic tumour extinction  
As a consequence of CAR T cell impairment in renewal capacity, tumour eradication is deterministically unstable and not a long-term outcome (see electronic supplementary material, section 3). However, tumour mass often shrinks at least for some time during treatment and can temporarily be brought down to very low levels [4], leading to possible stochastic extinction (figure 2d). We predict that if cure occurs, it does so via a stochastic event in which the malignant B cells are driven to extinction [28]. This stochastic approach leads to the question of whether parameter variability (e.g. patient variability), or stochasticity of the underlying process, or both, are responsible for the broad distributions of the times to cure or progression and probability of cure. Of those ZUMA-1 patients that were treated at Moffitt, we assessed the variability in CAR T cell kinetics, although not all patients had all time points available (figure 3a). The Moffitt ZUMA-1 patient cohort’s (overall n = 23 patients) variability in CAR T count (cells μl–1) were 27.5 (IQR: 16.5,57.5; n = 19), 9.1 (IQR: 3.8,31.1; n = 23), 2.1 (IQR: 0.6,6.1; n = 22) and 0.1 (IQR: 0.01,0.4; n = 22) at days 7, 14, 28 and 90, respectively. <!-- text, from page 0 (l=0.065,t=0.297,r=0.483,b=0.607), with ID c21ff52f-0b37-408a-bcd1-716b9897b273 -->

(e) Probability and time to progression  
To evaluate our model parameterization, we compared the overall progression-free survival (PFS) curve for all patients in the ZUMA-1 [5] trial to a virtual cohort of 1000 simulated patients with varying tumour growth rates (figure 3b). Although we had not used progression-free survival as a goal function to find suitable model parameters (Methods, electronic supplementary material, section 4), our stochastic model recapitulates PFS of the ZUMA-1 trial for reasonable tumour growth rate values, using a hybrid deterministic–stochastic numerical approach (electronic supplementary material, section 5) in which the system is simulated deterministically if the tumour is above a threshold value, and the tumour is simulated stochastically once below this threshold (the outcomes were very weakly impacted by choice of threshold; see electronic supplementary material). As a result, a probability of tumour extinction can be calculated numerically as a function of specific model parameters for a fixed point in time or overall. Treatment success (probability of tumour extinction) critically depends on the ability of the CAR T to survive (figure 3c), and on the effectiveness of lymphodepletion that reduce absolute lymphocyte counts (figure 3d). <!-- text, from page 0 (l=0.065,t=0.625,r=0.484,b=0.947), with ID 4f382062-ad05-421f-9cce-70895fce76bb -->

(f) Variability in outcomes  
A natural question involves whether overall variability in timing to cure or progression is shaped by patient variability (implemented using a hyperparameter that perturbs the parameters, see electronic supplementary material, section 5.3) in contrast with model stochastic effects. We performed additional stochastic simulations of tumour extinction (electronic supplementary material, section 5.4) under controlled parameter variation. We found that the probability of cure changes with overall parameter variability (figure 3e). Similarly, the time to cure distribution for a specific set of parameters widens with increasing parameter variability (figure 3f). Thus, variation in patient-specific conditions and parameter values could be the main determinant of observed variability in timing of cure or progression. <!-- text, from page 0 (l=0.519,t=0.046,r=0.933,b=0.264), with ID 85fe72bf-a6b6-4950-abcd-81689356f122 -->

Most stochastic simulations resulted in cure between days
20 and 80. We rarely found late cure events up to day 140
(figure 4a). Meanwhile, progression times were distributed
over a broader range. Typical progression times, as defined
in our model as 120% of initial tumour burden, occur any-
where between days 200 and 500 (figure 4b). These large
differences in time scales occur because cure, as a stochastic
tumour extinction event, is much more likely to occur
before CAR T cells begin to decline, typically after day 14. <!-- text, from page 0 (l=0.520,t=0.266,r=0.934,b=0.396), with ID 8fe0ef85-6a0c-4a33-90c3-46efaf5c2647 -->

(g) Necessity of lymphodepletion  
In the context of timing of events, our model can be useful to test new treatment strategies in silico, to inform clinical trial design. For example, we used our model to inform the timing of a second infusion, with or without additional lymphodepletion (electronic supplementary material, section 6) [11]. To improve outcomes with a second infusion, lymphodepletion that resets the T cells is necessary. This suggests that a second, lower dose lymphodepletion alone might be sufficient, provided it does not kill all CAR T cell but lowers overall T cell density sufficiently. The temporal suppression of normal lymphocytes is a key driver of CAR expansion, which, together with transient tumour burden data, could be leveraged to further evaluate the benefit of second interventions. <!-- text, from page 0 (l=0.519,t=0.414,r=0.934,b=0.620), with ID 3c191868-ba33-4c6b-be84-1aced6f9ccdf -->