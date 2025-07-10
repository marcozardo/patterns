
Simulation of coronavirus disease 2019 (COVID-19) scenarios with
possibility of reinfection <!-- text, from page 0 (l=0.059,t=0.207,r=0.771,b=0.255), with ID 2b81c8b0-d41b-4dce-ac41-b125fe2c7608 -->

Egor Malkovᵃ,ᵇ  
ᵃ Department of Economics, University of Minnesota, 1925 Fourth Street South, Minneapolis, MN 55455, USA  
ᵇ Federal Reserve Bank of Minneapolis, 90 Hennepin Ave, Minneapolis, MN 55401, USA <!-- text, from page 0 (l=0.058,t=0.263,r=0.590,b=0.312), with ID 991f8842-9c0f-407b-ab26-0de5c4e3d449 -->

A R T I C L E   I N F O

Article history:
Received 6 June 2020
Revised 4 September 2020
Accepted 12 September 2020
Available online 18 September 2020

Keywords:
SEIRS model
Epidemiological dynamics
COVID-19
Reinfection
Mitigation <!-- text, from page 0 (l=0.058,t=0.339,r=0.290,b=0.494), with ID 517e91ec-4236-4b91-90cf-b008452ba1f7 -->

A B S T R A C T

Epidemiological models of COVID-19 transmission assume that recovered individuals have a fully protected immunity. To date, there is no definite answer about whether people who recover from COVID-19 can be reinfected with the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). In the absence of a clear answer about the risk of reinfection, it is instructive to consider the possible scenarios. To study the epidemiological dynamics with the possibility of reinfection, I use a Susceptible-Exposed-Infectious-Resistant-Susceptible model with the time-varying transmission rate. I consider three different ways of modeling reinfection. The crucial feature of this study is that I explore both the difference between the reinfection and no-reinfection scenarios and how the mitigation measures affect this difference. The principal results are the following. First, the dynamics of the reinfection and no-reinfection scenarios are indistinguishable before the infection peak. Second, the mitigation measures delay not only the infection peak, but also the moment when the difference between the reinfection and no-reinfection scenarios becomes prominent. These results are robust to various modeling assumptions. <!-- text, from page 0 (l=0.334,t=0.339,r=0.943,b=0.512), with ID ea295819-c80b-4fab-8917-4f39018b8449 -->

© 2020 Elsevier Ltd. All rights reserved. <!-- text, from page 0 (l=0.707,t=0.514,r=0.940,b=0.528), with ID 0c1f89f1-9c20-4660-8a13-a48891621c1b -->

## 2. Model

Consider a SEIRS model with constant population $N$ normalized to one. Each period of time, the population consists of four classes: susceptible (S), exposed (E), infected (I), and resistant (recovered) (R):
susceptible (S), exposed (E), infected (I), and resistant (recovered) (R):

$S(t) + E(t) + I(t) + R(t) = N, \qquad \forall t \geq 0 \qquad$ (1) <!-- text, from page 0 (l=0.059,t=0.528,r=0.488,b=0.631), with ID 185ccd22-70bd-4aa3-98d0-826ede497dd0 -->

Since $N = 1$, variables $S$, $E$, $I$, and $R$ correspond to the fractions of the population. I assume that recovered individuals can become susceptible to infection again at rate $\omega$. The compartmental model is formulated by the following set of ordinary differential equations:

$dS(t)/dt = -\beta(t)\dfrac{S(t)}{N}I(t) + \omega R(t)$  (2)

$dE(t)/dt = \beta(t)\dfrac{S(t)}{N}I(t) - \sigma E(t)$  (3)

$dI(t)/dt = \sigma E(t) - \gamma I(t)$  (4)

$dR(t)/dt = \gamma I(t) - \omega R(t)$  (5) <!-- text, from page 0 (l=0.061,t=0.633,r=0.488,b=0.834), with ID 071b74f3-721c-4e6d-9b76-f8197c93fd30 -->

The transmission rate, $\beta(t)$, accounts for the rate at which infected individuals interact with others and transmit the disease and is given by <!-- text, from page 0 (l=0.061,t=0.836,r=0.487,b=0.877), with ID a01a324d-14a6-48e7-a01f-40a751e73664 -->

$\beta(t) = \gamma \tilde{R}(t)$ <!-- text, from page 0 (l=0.061,t=0.878,r=0.486,b=0.899), with ID 9d07243f-9159-4e1b-b63a-a2485478dc50 -->

where $\tilde{R}(t)$ is the time-varying reproduction number. Absent mitigation measures, $\tilde{R}$ corresponds to the basic reproduction number, $R_0$. To simplify notation, here and thereafter I omit explicit <!-- text, from page 0 (l=0.061,t=0.901,r=0.486,b=0.941), with ID d7ecfcba-0ff7-414c-b975-115cc7282d1e -->

dependence of $\tilde{R}$ on time whenever it does not cause confusion.
The transmission rate, $\beta(t)$, captures the impact of all mitigation
measures such as quarantine, travel restrictions, or social distancing. To study scenarios under different mitigation policies, I adapt a flexible functional form for the time-varying reproduction number. Following [3], I parameterize $\tilde{R}(t)$ as follows: <!-- text, from page 0 (l=0.513,t=0.070,r=0.941,b=0.152), with ID 8f581d38-c1c9-47fe-a2fb-4bee666eaf21 -->

$\tilde{R}_1(t) = \exp(-\eta_1 t) \tilde{R}_1(0) + (1 - \exp(-\eta_1 t)) R_1^*$ <!-- text, from page 0 (l=0.513,t=0.159,r=0.939,b=0.182), with ID 3d1378ab-bbb2-4328-991c-0dfed962a886 -->

$\tilde{R}_2(t) = \exp(-\eta_2 t)\tilde{R}_2(0) + (1 - \exp(-\eta_2 t))R_2^*$ <!-- text, from page 0 (l=0.513,t=0.189,r=0.938,b=0.211), with ID af92ab93-18cb-4bba-ad86-66bc4fa2156c -->

$\tilde{R}(t) = \frac{1}{2} \left( \tilde{R}_1(t) + \tilde{R}_2(t) \right)$ <!-- text, from page 0 (l=0.513,t=0.220,r=0.938,b=0.245), with ID 03b27bfc-19f1-4d3f-9cff-a427b63546c1 -->

where $\tilde{R}_1(0)$ and $\tilde{R}_2(0)$ ($R_1^*$ and $R_2^*$) are the initial (long-run) values
for $\tilde{R}_1$ and $\tilde{R}_2$. Parameter $\eta_1$ determines the rate at which $\tilde{R}_1$ con-
verges to $R_1^*$. In turn, parameter $\eta_2$ governs the rate at which $\tilde{R}_2$
converges to $R_2^*$. By appropriately choosing the parameter values, I
can capture different scenarios of the mitigation policies. In partic-
ular, in the simulations in Section 3, I vary the speed of imposing
the mitigation measures and also consider the scenario when ex-
tremely severe mitigation measures at the beginning of the pan-
demic are followed by their gradual relaxation. From (7)-(9), the
dynamics of $\tilde{R}_1$, $\tilde{R}_2$, and $\tilde{R}$ is described by the following equations: <!-- text, from page 0 (l=0.513,t=0.255,r=0.940,b=0.389), with ID b0b81526-8e8e-4cb0-9944-4ff7b4d4f6d0 -->

$\frac{d\tilde{R}_1^i(t)}{dt} = -\eta_1 (\tilde{R}_1^i(t) - R_1^i)$ <!-- text, from page 0 (l=0.514,t=0.398,r=0.938,b=0.428), with ID de969a5a-677a-41c2-9389-16c6127248ba -->

$\frac{d\tilde{R}_2(t)}{dt} = -\eta_2 (\tilde{R}_2(t) - R_2^*) \hspace{7cm} (11)$ <!-- text, from page 0 (l=0.516,t=0.434,r=0.938,b=0.461), with ID 0ea1d682-0130-46c4-8cb1-7181d8de9088 -->

$\frac{d\tilde{\mathbf{R}}(t)}{dt} = -\frac{1}{2}\eta_1(\tilde{\mathbf{R}}_1(t) - \mathbf{R}_1^*) - \frac{1}{2}\eta_2(\tilde{\mathbf{R}}_2(t) - \mathbf{R}_2^*) \hspace{2cm} (12)$ <!-- text, from page 0 (l=0.516,t=0.469,r=0.938,b=0.500), with ID 0daa3dfb-4b90-4463-8c06-1ac55d900ec7 -->

Parameters ($\sigma$, $\gamma$, $\omega$) represent the characteristics of COVID-19 and assumed to be constant. For parameters $\sigma$ and $\gamma$, I take the estimates from the literature. The parameter $\sigma$ stands for the mean incubation period of the disease, and its estimates vary from 1/5.2 to 1/3, see [18] and [27]. Following [16] and [27], I adopt a mean latent period of 5.2 days (infection rate, $\sigma = 1/5.2$). Next, I adopt a mean infectious period of 18 days (recovery rate, $\gamma = 1/18$) in line with [7] and [27]. Parameter $\omega$, the immunity waning rate, is of the main interest for this paper, and since, to date, there are no credible estimates of it, I consider the range of different values, $\omega \in \{0, 1/365, 1/183, 1/120, 1/60\}$. To et al. [25] show that the second episode of asymptomatic infection occurred 142 days after the first symptomatic episode in an apparently immunocompetent patient. This period is consistent with considered range of $\omega$. The case $\omega = 0$ corresponds to no reinfection. The value of $\omega$ is driven by immunity waning after the infection or the rate of virus mutation. Next, the initial values for actively infected and exposed population are taken for the United States and set to $I(0) = 1/1000$, i.e. 0.1 percent of the population, and $E(0) = 43.75 \times I(0)$ respectively. I use March 16–17, 2020 as the initial date (March 17, 2020 was a day at which the last U.S. state reported its first case, see [19]). I take $I(0) = 1/1000$ from [5]. Official data reports around 4500 cases in the United States on March 16, and they assume that this represents 1.5 percent of all cases. This rate of underreporting is derived by Hortaçsu et al. [12] for March 9, 2020. $E(0) = 43.75 \times I(0)$ corresponds to the estimates for the United States by Peirlinck et al. [19]. <!-- text, from page 0 (l=0.512,t=0.506,r=0.940,b=0.861), with ID 41ce2667-77c1-41d1-a436-736148680135 -->

Throughout the simulations, I fully acknowledge that only a
fraction of the model-generated cases are reported in reality. Li
et al. [17] study the critical importance of undocumented COVID-
19 cases for understanding the overall prevalence and pandemic
potential of this disease. Lin et al. [18] emphasize that the report-
ing rate is time-varying. <!-- text, from page 0 (l=0.514,t=0.861,r=0.939,b=0.941), with ID f600bc8e-e810-498a-a65a-f06be3281457 -->

2 <!-- marginalia, from page 0 (l=0.493,t=0.956,r=0.506,b=0.966), with ID 1345d75b-be2e-41fb-83a9-7ae609fdc3b7 -->

*E. Malkov* <!-- marginalia, from page 0 (l=0.059,t=0.043,r=0.114,b=0.056), with ID 9553f66e-d1cf-4650-bd0b-ef56de632730 -->

*Chaos, Solitons and Fractals* 139 (2020) 110296 <!-- marginalia, from page 0 (l=0.705,t=0.042,r=0.940,b=0.057), with ID d1f1e5fd-bf42-4e70-b3ad-b2a4dc44846e -->

3. Model simulations

   In this section, I use the assumptions about the time paths for $\tilde{R}$ from [3]. This allows me to clearly compare the outcomes under reinfection with his conclusions from the simulations without reinfection. In the first model experiment, I assume that $\tilde{R}$ is fixed over time. This reflects the scenarios when mitigation efforts do not change over time. <!-- text, from page 0 (l=0.058,t=0.070,r=0.489,b=0.175), with ID b6d60037-0251-4f14-a937-470c935db499 -->

In the first model experiment, I consider a range
of values of the basic reproduction number $\hat{R} = R_0 \in \{1.6, 1.8, 2.0, 2.2, 2.5, 2.8, 3.0\}$. The upper bound of this range
captures the estimates from the literature discussed in Section 1.
Lower values of $R_0$ correspond to lower levels of the disease
transmission. The mitigation measures — quarantine, travel re-
strictions, or social distancing — can reduce the basic reproduction
number. Anderson et al. [2] provide a thorough discussion of this
question. Critically, in my simulations, I vary both $\omega$ and
$R_0$. By comparing the simulated series under different values
of $\omega$ and $R_0$, I follow two goals. First, given $R_0$, I compare the
outcomes of the reinfection and no-reinfection scenarios. Second,
given $\omega$, I demonstrate the effects of the mitigation measures
(expressed through the lower values of $R_0$) under the reinfection
and no-reinfection scenarios. <!-- text, from page 0 (l=0.059,t=0.175,r=0.489,b=0.373), with ID 16262cc0-0280-4bce-8871-22f0b5de9e83 -->

Fig. 1 shows the time paths for the simulated fraction of the actively infected population with (solid lines) and without (dashed lines) reinfection under different values of $R_0$. This model experiment implies that lower $R_0$ leads to delaying the infection peak both with and without reinfection. Second, under the reinfection scenario, the size of the peak is greater than without reinfection. The difference in the peak values is decreasing in $R_0$. Third, with reinfection, the fraction of the actively infected population exhibits asymmetric dynamics around the peak. Crucially, before the peak, the time paths with and without reinfection are indistinguishable. However, after the peak, the reinfection series is unambiguously above the no-reinfection series. Therefore, by reducing the transmission rate with the mitigation measures, we delay the infection peak, and hence delay the moment when the difference between the reinfection and no-reinfection scenarios becomes sizeable. Finally, notice that, with reinfection, there can be multiple-wave disease outbreaks. In a related study, [6] discuss the role of homologous reinfection in driving multiple-wave influenza outbreaks. Next, Fig. 1e contains the phase diagram where I plot the fraction of the susceptible population against the fraction of the actively infected population. The solution of the model under both reinfection and no-reinfection scenarios starts in the bottom right corner where $I(0)$ is close to zero and $S(0)$ is close to one. This phase diagram also illustrates that before the peak two scenarios – with and without reinfection – are almost indistinguishable. <!-- text, from page 0 (l=0.059,t=0.373,r=0.489,b=0.698), with ID f15e271d-60b0-4b9b-a218-108ee998146b -->

In the second model experiment, I assume that $\tilde{R}$ gradually de-
creases at different speed. To capture the scenarios under differ-
ent speed of implementation, following [3], I set $\tilde{R}_1(0) = \tilde{R}_2(0) = 
3$, $R_1^* = R_2^* = 1.6$, and vary parameters $\eta_1$ and $\eta_2$ with $\eta_1 = \eta_2 \equiv 
\eta$. There are five scenarios: very fast $(\eta = 1/5)$, fast $(\eta = 1/10)$,
moderate $(\eta = 1/20)$, slow $(\eta = 1/50)$, and very slow
$(\eta = 1/100)$. Higher values of $\eta$ govern higher rate of convergence of $\tilde{R}$ to the
long-run value of 1.6. Fig. 2 shows the time paths for $\tilde{R}$ and the
simulated fraction of the actively infected population with (solid
lines) and without (dashed lines) reinfection. This model experi-
ment implies that the speed of implementation affects the tim-
ing of the peak and its size. Faster implementation of mitigation
measures leads to delaying the infection peak both with and with-
out reinfection. Next, similarly to the simulation from Fig. 1, under
the reinfection scenario, the fraction of the actively infected popu-
lation exhibits asymmetric dynamics around the peak. Relative to
the no-reinfection scenario, reinfection affects the epidemic dura-
tion, the size of the infection peak, and the timing of the infection <!-- text, from page 0 (l=0.060,t=0.700,r=0.489,b=0.941), with ID dbabf112-fdc1-45a5-b04b-262faa37cf26 -->

peak. Furthermore, to provide additional evidence to the dynam-
ics of the solution, in Fig. 2b I show the phase diagram where plot
the fraction of the susceptible population against the fraction of
the actively infected population. <!-- text, from page 0 (l=0.513,t=0.070,r=0.941,b=0.123), with ID a12e1ea4-996d-4c66-a32e-506d07799f07 -->

In the third model experiment, I assume that $\bar{R}$ significantly
drops at the beginning, as a result of extremely severe mitigation
measures, and then gradually goes up, as the mitigation measures
are relaxed. Following [3], I set $\bar{R}_1(0) = 10$, $\bar{R}_2(0) = -4$, $R_1^*_1 = -10$,
$R_2^*_1 = 4$, $\eta_1 = 1/35$, and $\eta_2 = 1/100$. Given the initial and long-run
values of the reproduction number and $\eta_1 > \eta_2$, $\bar{R}_1(t)$ is rapidly
decreasing function while $\bar{R}_2(t)$ is slowly increasing function. As a
result, the time path for $\bar{R}(t)$ has a U-shaped form, see Fig. 3a. The
other two panels of Fig. 3 show the simulated fraction of the ac-
tively infected population with and without reinfection. Under the
temporary and extremely severe mitigation measures, in the first
four months, as shown in Fig. 3b, the fraction of the actively in-
fected population substantially goes down. Moreover, the dynam-
ics is identical for the scenarios with and without the possibility of
reinfection. Turning to the first 15 months of the pandemic, shown
in Fig. 3c, we see that gradual relaxation that follows the initial
extremely severe mitigation measures, leads to a subsequent peak.
Therefore, relaxation of the mitigation measures, driven by the op-
timistic dynamics in the first months, eventually leads to the epi-
demic. Motivated by the observation that early mitigation mea-
sures delay the peak but not its size, because the population does
not acquire herd immunity, Toda [26] studies the optimal mitiga-
tion policy. He shows that it is optimal to initiate the mitigation
measures once the number of cases reaches some threshold frac-
tion of the population. <!-- text, from page 0 (l=0.512,t=0.123,r=0.941,b=0.454), with ID 5c5a77d6-420f-4d62-a1ae-abbd325b7bd0 -->

4. Alternative reinfection assumptions

4.1. Milder disease after reinfection

I consider two alternative ways of modeling reinfection. First, I assume that individuals, once being reinfected, have a milder form of the disease. This is in line with [1] who discuss the clinical characteristics of the recovered COVID-19 patients with re-detectable positive RNA test. When readmitted to the hospital, these patients showed no obvious clinical symptoms or disease progression. In the model, I assume that the individuals who become susceptible after being recovered, have lower transmission rate and higher recovery rate. At each point in time, the population, normalized to one, consists of seven classes: primary-susceptible ($S_p$), secondary-susceptible ($S_s$), primary-exposed ($E_p$), secondary-exposed ($E_s$), primary-infected ($I_p$), secondary-infected ($I_s$), and resistant (recovered) ($R$): <!-- text, from page 0 (l=0.511,t=0.465,r=0.941,b=0.690), with ID 74798f8f-92ed-4473-a969-7b522a91b510 -->

$S_p(t) + S_s(t) + E_p(t) + E_s(t) + I_p(t) + I_s(t) + R(t) = N, \quad \forall t \geq 0 \tag{13}$ <!-- text, from page 0 (l=0.512,t=0.697,r=0.941,b=0.734), with ID c475e15b-3569-47e6-9a58-2a0c2c385175 -->

Individuals belong to $S_p$, $E_p$, or $I_p$ if they were not infected before. Individuals belong to $S_s$, $E_s$, or $I_s$ after being recovered. The compartmental model is formulated as follows:

$dS_p(t)/dt = -(\beta_p I_p(t) + \beta_s I_s(t)) \dfrac{S_p(t)}{N}$  (14)

$dS_s(t)/dt = -(\beta_p I_p(t) + \beta_s I_s(t)) \dfrac{S_s(t)}{N} + \omega R(t)$  (15)

$dE_p(t)/dt = (\beta_p I_p(t) + \beta_s I_s(t)) \dfrac{S_p(t)}{N} - \sigma_p E_p(t)$  (16)

$dE_s(t)/dt = (\beta_p I_p(t) + \beta_s I_s(t)) \dfrac{S_s(t)}{N} - \sigma_s E_s(t)$  (17)

$dI_p(t)/dt = \sigma_p E_p(t) - \gamma_p I_p(t)$  (18) <!-- text, from page 0 (l=0.513,t=0.736,r=0.942,b=0.945), with ID c56a9555-e0c4-4133-9915-e952dcd69885 -->

3 <!-- marginalia, from page 0 (l=0.494,t=0.955,r=0.506,b=0.966), with ID 35fc239c-fa02-4188-b0d3-04e994165007 -->

*E. Malkov* <!-- marginalia, from page 0 (l=0.059,t=0.042,r=0.114,b=0.057), with ID 66b6cc39-855a-4935-8c12-97c1969d6b00 -->

*Chaos, Solitons and Fractals* 139 (2020) 110296 <!-- marginalia, from page 0 (l=0.705,t=0.042,r=0.940,b=0.058), with ID 065f0e0d-9894-45bf-b986-c99f3eba36f5 -->

Summary : This figure presents two line plots comparing the fraction of a population infected over time under different basic reproduction numbers (R₀) and immunity waning rates (ω). The left panel uses ω = 1/365, and the right panel uses ω = 1/183.

line plot:
# Title & Axes :
  • Left plot title: “(a) Immunity waning rate ω = 1/365.”
  • Right plot title: “(b) Immunity waning rate ω = 1/183.”
  • X-axis (both): “Days”, ranging from 0 to 450.
  • Y-axis (both): “Fraction infected”, ranging from 0 to 0.35.

# Data Points :
  • Each plot contains 8 series, each corresponding to a different R₀ value (3.0, 2.8, 2.5, 2.2, 2.0, 1.8, 1.6), with two curves per R₀: one with ω = 0 (solid line), one with the specified ω (dashed line).
  • Legend entries (for both plots) include:
    – R₀ = 3.0, ω = 0
    – R₀ = 3.0, ω = 1/365 (left) or ω = 1/183 (right)
    – R₀ = 2.8, ω = 0
    – R₀ = 2.8, ω = 1/365 (left) or ω = 1/183 (right)
    – R₀ = 2.5, ω = 0
    – R₀ = 2.5, ω = 1/365 (left) or ω = 1/183 (right)
    – R₀ = 2.2, ω = 0
    – R₀ = 2.2, ω = 1/365 (left) or ω = 1/183 (right)
    – R₀ = 2.0, ω = 0
    – R₀ = 2.0, ω = 1/365 (left) or ω = 1/183 (right)
    – R₀ = 1.8, ω = 0
    – R₀ = 1.8, ω = 1/365 (left) or ω = 1/183 (right)
    – R₀ = 1.6, ω = 0
    – R₀ = 1.6, ω = 1/365 (left) or ω = 1/183 (right)

# Design Encodings :
  • Each R₀ value is represented by a unique color.
  • Solid lines: ω = 0 (no waning immunity).
  • Dashed lines: ω = 1/365 (left) or ω = 1/183 (right) (waning immunity).
  • Both plots share the same color and line style scheme for direct comparison.

# Distribution & Trends :
  • All curves show an initial rise to a peak in the fraction infected, followed by a decline.
  • Higher R₀ values produce higher peaks.
  • Dashed lines (waning immunity) show a secondary rise or plateau after the initial decline, more pronounced for higher ω (right plot).
  • For lower R₀, the curves are flatter and peaks are lower.

# Analysis :
  • Increasing the immunity waning rate (from ω = 1/365 to ω = 1/183) leads to a higher and earlier resurgence in the fraction infected after the initial epidemic wave.
  • The effect of waning immunity is more pronounced for higher R₀ values.
  • With no waning immunity (solid lines), the fraction infected drops and remains low; with waning immunity (dashed lines), the fraction infected can rise again, especially for higher R₀ and higher ω.
  • The plots illustrate the importance of immunity duration in epidemic dynamics and the potential for recurrent outbreaks. <!-- figure, from page 0 (l=0.111,t=0.100,r=0.880,b=0.357), with ID c2229b27-06b6-4338-b5f8-e6d9b8f25ac5 -->

Summary : This figure presents two line plots comparing the fraction of a population infected over time (days) under different basic reproduction numbers (R₀) and immunity waning rates (ω). The left plot uses ω = 1/120, and the right plot uses ω = 1/60.

line chart:
Title & Axes :
  • Left plot title: “(c) Immunity waning rate ω = 1/120.”
  • Right plot title: “(d) Immunity waning rate ω = 1/60.”
  • X-axis (both plots): “Days”, range 0 to 450, tick marks at intervals of 50.
  • Y-axis (both plots): “Fraction infected”, range 0 to 0.35, tick marks at intervals of 0.05.

Data Points :
  • Each plot contains 10 series, each corresponding to a different R₀ value (from 3.0 to 1.6) and two immunity waning scenarios (ω = 0 and ω = 1/120 or 1/60).
  • Legend entries (for both plots) include:
    – R₀ = 3.0, ω = 0
    – R₀ = 3.0, ω = 1/120 (left) or ω = 1/60 (right)
    – R₀ = 2.8, ω = 0
    – R₀ = 2.8, ω = 1/120 (left) or ω = 1/60 (right)
    – ... (continues for R₀ = 2.6, 2.4, 2.2, 2.0, 1.8, 1.6)
  • Each series shows the fraction infected as a function of days, with a visible initial peak and subsequent decline or secondary rise.

Design Encodings :
  • Solid lines represent ω = 0; dashed lines represent ω = 1/120 (left) or ω = 1/60 (right).
  • Each R₀ value is assigned a unique color, consistent across both plots.
  • Legends are placed within the plot area, listing all series with corresponding color and line style.

Distribution & Trends :
  • All series show a rapid rise to a peak in fraction infected, followed by a decline.
  • For ω > 0 (dashed lines), a secondary rise or plateau is visible after the initial decline, more pronounced at higher R₀.
  • The peak fraction infected is higher for larger R₀.
  • The secondary rise is more pronounced in the right plot (ω = 1/60) than the left (ω = 1/120).

Analysis :
  • Increasing the immunity waning rate (from ω = 1/120 to ω = 1/60) leads to a more pronounced secondary rise in infections, especially for higher R₀.
  • For all R₀, the initial peak is higher when ω = 0 (solid lines), but the long-term fraction infected is higher when immunity wanes (dashed lines).
  • The effect of immunity waning is more significant at higher R₀ values.
  • The time to secondary rise shortens as ω increases. <!-- figure, from page 0 (l=0.108,t=0.365,r=0.880,b=0.662), with ID 303cdb87-2fd5-47ea-9039-57b367b4ce13 -->

Summary : This figure shows S-I (Susceptible-Infected) phase diagrams for different values of the basic reproduction number (R₀) and frequency parameter (ω), illustrating how the fraction of infected individuals varies with the fraction of susceptible individuals under different epidemiological scenarios.

line plot:
Title & Axes :
  • Title: “(e) S-I phase diagram, ω = 1/183.”
  • X-axis: “Fraction susceptible” (range: 0 to 1).
  • Y-axis: “Fraction infected” (range: 0 to 0.3).
  • Tick labels: X-axis (0, 0.1, ..., 1), Y-axis (0, 0.05, ..., 0.3).

Data Points :
  • Four series, as indicated by the legend:
    – R₀ = 3.0, ω = 0 (blue dashed line)
    – R₀ = 3.0, ω = 1/183 (blue solid line)
    – R₀ = 1.6, ω = 0 (red dashed line)
    – R₀ = 1.6, ω = 1/183 (red solid line)
  • Each series traces a curve in the susceptible-infected (S-I) plane, showing the trajectory of the epidemic for the given parameters.

Design Encodings :
  • Colour: Blue for R₀ = 3.0, Red for R₀ = 1.6.
  • Linestyle: Dashed for ω = 0, Solid for ω = 1/183.
  • All lines are smooth curves; some exhibit spiral or looping behaviour.

Distribution & Trends :
  • For R₀ = 3.0 (blue), the infected fraction peaks higher (~0.26) than for R₀ = 1.6 (red, peak ~0.11).
  • For both R₀ values, ω = 1/183 (solid lines) introduces a spiral or oscillatory pattern in the S-I plane, not present for ω = 0 (dashed lines).
  • All curves start at high susceptible, low infected fractions and move toward lower susceptible, higher infected fractions before returning toward lower infected values.

Analysis :
  • The introduction of ω = 1/183 (solid lines) leads to oscillatory or spiral epidemic trajectories, indicating possible recurrent outbreaks or damped oscillations in the infected fraction.
  • Higher R₀ (3.0) results in a larger maximum infected fraction and a broader trajectory in the S-I plane compared to lower R₀ (1.6).
  • For ω = 0 (dashed lines), the epidemic follows a single-peaked trajectory without oscillations.
  • The phase diagram visually distinguishes the impact of both R₀ and ω on epidemic dynamics, with both parameters significantly altering the shape and extent of the S-I trajectory. <!-- figure, from page 0 (l=0.306,t=0.616,r=0.696,b=0.864), with ID 424c0144-b6ba-44cc-9214-ef54645922e8 -->

Fig. 1. Panels (a)–(d) show the fraction of the actively infected population over time under the reinfection (solid) and no-reinfection (dashed) scenarios and with different values of the basic reproduction number, $R_0$. Panels (a)–(d) differ in the size of the immunity waning ratio, $\omega$. Panel (e) contains the phase diagram that shows the evolution of the fraction of the actively infected population against the fraction of the susceptible population with and without reinfection. <!-- text, from page 0 (l=0.058,t=0.870,r=0.941,b=0.906), with ID a6994236-5da7-4814-a7d8-68fefe57898d -->

4 <!-- marginalia, from page 0 (l=0.493,t=0.955,r=0.507,b=0.967), with ID bf108065-4997-4209-aa0d-d7a1b4f27540 -->

*E. Malkov* <!-- marginalia, from page 0 (l=0.059,t=0.043,r=0.114,b=0.056), with ID d0b6008d-6b59-489f-a06f-72542e3c626d -->

*Chaos, Solitons and Fractals* 139 (2020) 110296 <!-- marginalia, from page 0 (l=0.705,t=0.042,r=0.940,b=0.057), with ID a8fd23c2-253c-4178-8dfb-684bd71a60d3 -->

Summary : This figure presents two panels analyzing the dynamics of an epidemic model with time-varying reproduction number and corresponding S-I phase diagrams for different rates of change.

line plots:
# (a) Time-varying \(\tilde{R}\)
Title & Axes :
  • Title: “(a) Time-varying \(\tilde{R}\).”
  • X-axis: “Days” (range: 0 to 450).
  • Y-axis: “\(\tilde{R}(t)\)” (range: 1.6 to 3).
Data Points :
  • Five series, each representing a different rate of change:
    – Very fast (blue)
    – Fast (red)
    – Moderate (orange)
    – Slow (green)
    – Very slow (black)
  • All series start at \(\tilde{R}(t) \approx 3\) and decay toward \(\tilde{R}(t) \approx 1.6\), with faster rates decaying more quickly.
Design Encodings :
  • Colour-coded lines matching legend.
  • No markers; solid lines.
Distribution & Trends :
  • All curves are monotonically decreasing.
  • The “Very fast” curve drops sharply within ~25 days; “Very slow” decays gradually over ~400 days.

# (b) S-I phase diagram, \(\omega = 1/183\)
Title & Axes :
  • Title: “(b) S-I phase diagram, \(\omega = 1/183\).”
  • X-axis: “Fraction susceptible” (range: 0.1 to 1).
  • Y-axis: “Fraction infected” (range: 0 to 0.25).
Data Points :
  • Six series:
    – Very fast, \(\omega = 0\) (blue dashed)
    – Very fast, \(\omega = 1/183\) (blue solid)
    – Moderate, \(\omega = 0\) (orange dashed)
    – Moderate, \(\omega = 1/183\) (orange solid)
    – Very slow, \(\omega = 0\) (black dashed)
    – Very slow, \(\omega = 1/183\) (black solid)
  • Each series traces a trajectory in S-I space, with solid lines for \(\omega = 1/183\) and dashed for \(\omega = 0\).
Design Encodings :
  • Colour and line style encode both rate and \(\omega\) value.
  • Legend present for all series.
Distribution & Trends :
  • All trajectories start at high susceptible, low infected.
  • Dashed lines (\(\omega = 0\)) show larger loops; solid lines (\(\omega = 1/183\)) spiral inward more quickly.
  • “Very slow” series reach higher infected fractions than “Very fast”.

Analysis :
  • Faster decay in \(\tilde{R}(t)\) leads to a more rapid reduction in the effective reproduction number.
  • In the S-I phase diagram, increasing \(\omega\) (solid lines) causes the epidemic trajectory to spiral inward more quickly, indicating faster epidemic resolution.
  • Slower rates of change in \(\tilde{R}(t)\) (black lines) result in higher peaks of infection and longer epidemic duration.
  • The comparison of dashed and solid lines highlights the impact of the parameter \(\omega\) on epidemic dynamics, with higher \(\omega\) dampening oscillations in the S-I plane. <!-- figure, from page 0 (l=0.119,t=0.096,r=0.880,b=0.351), with ID 7dde16bf-d6d5-4c45-b61c-005628af46b6 -->

Summary : This figure presents two line plots comparing the fraction of a population infected over time under different immunity waning rates (ω = 1/365 and ω = 1/183), with multiple transmission speeds and immunity scenarios.

line chart:

# Title & Axes :
  • Left plot title: “(c) Immunity waning rate ω = 1/365.”
  • Right plot title: “(d) Immunity waning rate ω = 1/183.”
  • X-axis: “Days” (range: 0 to 450, tick marks at intervals of 50).
  • Y-axis: “Fraction infected” (range: 0 to 0.25, tick marks at intervals of 0.05).

# Data Series :
  • Each plot contains 8 series, corresponding to combinations of transmission speed (Very fast, Fast, Moderate, Slow, Very slow) and immunity waning (ω = 0 or ω = 1/365 or ω = 1/183).
  • Series names and line styles (as per legend, both plots):
    – Very fast, ω = 0 (blue dashed)
    – Very fast, ω = 1/365 (left, blue solid); ω = 1/183 (right, blue solid)
    – Fast, ω = 0 (red dashed)
    – Fast, ω = 1/365 (left, red solid); ω = 1/183 (right, red solid)
    – Moderate, ω = 0 (orange dashed)
    – Moderate, ω = 1/365 (left, orange solid); ω = 1/183 (right, orange solid)
    – Slow, ω = 0 (green dashed)
    – Slow, ω = 1/365 (left, green solid); ω = 1/183 (right, green solid)
    – Very slow, ω = 0 (black dashed)
    – Very slow, ω = 1/365 (left, black solid); ω = 1/183 (right, black solid)

# Design Encodings :
  • Colour encodes transmission speed: blue (very fast), red (fast), orange (moderate), green (slow), black (very slow).
  • Dashed lines: ω = 0 (no waning immunity).
  • Solid lines: ω > 0 (waning immunity at specified rate).
  • Both plots share the same legend, located centrally between them.

# Distribution & Trends :
  • All series show a single peak in fraction infected, followed by a decline.
  • Peak height and timing vary by transmission speed and immunity waning rate.
  • For each transmission speed, the solid line (waning immunity) peaks higher and/or later than the dashed line (no waning).
  • The right plot (higher waning rate) shows higher and more prolonged infection fractions compared to the left plot.

# Analysis :
  • Increasing the immunity waning rate (from ω = 1/365 to ω = 1/183) results in higher and more sustained infection levels for all transmission speeds.
  • Faster transmission speeds (blue, red) peak earlier and higher, while slower speeds (green, black) peak later and lower.
  • Waning immunity (solid lines) consistently leads to higher infection fractions than permanent immunity (dashed lines), with the effect more pronounced at higher waning rates.
  • The difference between solid and dashed lines increases as the waning rate increases, indicating the importance of immunity duration in epidemic dynamics. <!-- figure, from page 0 (l=0.113,t=0.355,r=0.879,b=0.605), with ID 59983ad8-b3f0-4ab5-b747-bf9546240493 -->

Summary : This figure presents two line plots comparing the fraction of a population infected over time under different immunity waning rates (ω = 1/120 and ω = 1/60), with multiple scenarios for the speed of immunity loss.

line plot:
Title & Axes :
  • Left plot title: “(e) Immunity waning rate ω = 1/120.”
  • Right plot title: “(f) Immunity waning rate ω = 1/60.”
  • X-axis: “Days” (range: 0 to 450, tick marks at 0, 50, 100, 150, 200, 250, 300, 350, 400, 450).
  • Y-axis: “Fraction infected” (range: 0 to 0.25, tick marks at 0, 0.05, 0.10, 0.15, 0.20, 0.25).

Data Points :
  • Each plot contains 8 series, corresponding to combinations of immunity loss speed (Very fast, Fast, Moderate, Slow, Very slow) and waning rate (ω = 0, ω = 1/120 for left; ω = 0, ω = 1/60 for right).
  • Series names and legend (identical in both plots except for ω values):
    – Very fast, ω = 0 (blue dashed)
    – Very fast, ω = 1/120 (left, blue solid); ω = 1/60 (right, blue solid)
    – Fast, ω = 0 (red dashed)
    – Fast, ω = 1/120 (left, red solid); ω = 1/60 (right, red solid)
    – Moderate, ω = 0 (orange dashed)
    – Moderate, ω = 1/120 (left, orange solid); ω = 1/60 (right, orange solid)
    – Slow, ω = 0 (green dashed)
    – Slow, ω = 1/120 (left, green solid); ω = 1/60 (right, green solid)
    – Very slow, ω = 0 (black dashed)
    – Very slow, ω = 1/120 (left, black solid); ω = 1/60 (right, black solid)
  • All series show a rise to a peak fraction infected, then a decline.

Design Encodings :
  • Line colour encodes immunity loss speed: blue (Very fast), red (Fast), orange (Moderate), green (Slow), black (Very slow).
  • Dashed lines: ω = 0; solid lines: ω = 1/120 (left), ω = 1/60 (right).
  • Both plots share the same legend, centrally placed between them.

Distribution & Trends :
  • All curves rise to a peak between 0.15 and 0.22 fraction infected, then decline.
  • Faster immunity loss (darker colours) generally results in higher and earlier peaks.
  • Higher waning rate (right plot, ω = 1/60) leads to higher long-term infection fractions compared to lower waning rate (left plot, ω = 1/120).
  • For ω = 0 (dashed lines), infection fraction drops to near zero after the peak.
  • For nonzero ω (solid lines), infection fraction stabilises at a nonzero value after the initial decline.

Analysis :
  • Increasing the immunity waning rate (from ω = 1/120 to ω = 1/60) results in higher long-term endemic infection levels.
  • Faster immunity loss (Very fast, Fast) produces higher and earlier peaks in infection fraction.
  • When immunity does not wane (ω = 0), the infection dies out after the initial wave; with waning immunity, a persistent endemic state is reached.
  • The effect of immunity loss speed is more pronounced at higher waning rates. <!-- figure, from page 0 (l=0.106,t=0.610,r=0.883,b=0.861), with ID 4532cc64-a679-41ee-8c4e-74a2154d878d -->

Fig. 2. Panel (a) shows the time paths for the time-varying reproduction number, $\hat{R}$. Panel (b) contains the phase diagram that shows the evolution of the fraction of the actively infected population against the fraction of the susceptible population with and without reinfection. Panels (c)–(e) show the fraction of the actively infected population over time under the reinfection (solid) and no-reinfection (dashed) scenarios and with different speed of the change in $\hat{R}$. Panels (c)–(e) differ in the size of the immunity waning ratio, $\omega$. <!-- text, from page 0 (l=0.058,t=0.865,r=0.942,b=0.913), with ID 53d11c53-3c84-4942-80eb-a63a78b8c50e -->

5 <!-- marginalia, from page 0 (l=0.493,t=0.955,r=0.506,b=0.966), with ID 8beaabb6-7b4c-4216-9f1d-0b223dbf821b -->

*E. Malkov* <!-- marginalia, from page 0 (l=0.058,t=0.043,r=0.115,b=0.056), with ID 6608d460-a62f-461a-bc25-01749495d5d2 -->

*Chaos, Solitons and Fractals* 139 (2020) 110296 <!-- marginalia, from page 0 (l=0.705,t=0.042,r=0.941,b=0.057), with ID a67c5f4f-fc9b-4124-945b-9d53be067a4e -->

Summary : This figure presents three panels analyzing the impact of time-varying reproduction numbers and reinfection rates on the fraction of actively infected individuals under different mitigation scenarios over time.

line plots:
# (a) Time-varying 𝑅̃
Title & Axes :
  • No explicit title; panel label: “(a) Time-varying 𝑅̃.”
  • X-axis: “Days” (range: 0 to 450, ticks at 0, 50, 100, 150, 200, 250, 300, 350, 400, 450).
  • Y-axis: “𝑅̃(t)” (range: 0 to 3, ticks at 0, 0.5, 1, 1.5, 2, 2.5, 3).
Data Points :
  • Single black curve showing 𝑅̃(t) decreasing to a minimum near day 100, then rising steadily to day 450.
Design Encodings :
  • Black solid line.
Distribution & Trends :
  • U-shaped curve: initial decrease, minimum, then monotonic increase.

# (b) Infected, first 4 months
Title & Axes :
  • No explicit title; panel label: “(b) Infected, first 4 months.”
  • X-axis: “Days” (range: 0 to 140, ticks at 0, 20, 40, 60, 80, 100, 120, 140).
  • Y-axis: “Fraction Infected” (range: 0 to 0.06, ticks at 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06).
Data Points :
  • Five series (legend):
    – “ω = 0 (no reinfection)”
    – “ω = 1/365”
    – “ω = 1/183”
    – “ω = 1/120”
    – “ω = 1/60”
  • All series overlap, showing a single peak near day 60, then decline.
Design Encodings :
  • Black solid line for ω = 0; grey lines for ω > 0.
  • All lines coincide in this panel.
Distribution & Trends :
  • Single peak in fraction infected, then decline.

# (c) Infected, first 15 months
Title & Axes :
  • No explicit title; panel label: “(c) Infected, first 15 months.”
  • X-axis: “Days” (range: 0 to 450, ticks at 0, 50, 100, 150, 200, 250, 300, 350, 400, 450).
  • Y-axis: “Fraction Infected” (range: 0 to 0.3, ticks at 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3).
Data Points :
  • Five series (legend as above).
  • Black solid line (ω = 0) shows a single peak, then a smaller secondary rise.
  • Grey lines (ω > 0) show higher secondary peaks, with magnitude increasing as ω increases.
Design Encodings :
  • Black solid line for ω = 0; grey solid and dashed lines for ω > 0.
Distribution & Trends :
  • For ω = 0: initial peak, then decline, small secondary rise.
  • For ω > 0: initial peak, then larger secondary peaks, with higher ω leading to higher and earlier secondary peaks.

# Design Encodings :
  • Legends in panels (b) and (c) specify ω values and line styles.
  • All axes have labeled ticks and gridlines.
  • Panel (a) uses a single black line; panels (b) and (c) use multiple lines with varying shades/styles.

# Analysis :
  • The time-varying reproduction number 𝑅̃(t) initially decreases, then increases, reflecting changing mitigation measures.
  • In the first 4 months, reinfection rate (ω) has negligible effect on the fraction infected (all lines coincide).
  • Over 15 months, higher reinfection rates (larger ω) lead to higher and earlier secondary peaks in infection fraction, indicating that reinfection can drive subsequent waves even after initial mitigation.
  • The no-reinfection scenario (ω = 0) results in a much smaller secondary rise compared to reinfection scenarios. <!-- figure, from page 0 (l=0.057,t=0.069,r=0.943,b=0.325), with ID 89fa5836-95ea-4fd5-86a9-e72338001efb -->

Summary : This figure presents three line plots showing the fraction of the population infected over time, separated into total infected, primary-infected, and secondary-infected groups. The plots compare the effects of different immunity waning rates (ω) and primary-transmission rates (βₚ).

line plots:
# (a) Infected (total)
Title & Axes :
  • Title: “(a) Infected (total).”
  • X-axis: “Days” (range: 0 to 450).
  • Y-axis: “Fraction infected” (range: 0 to 0.3).
  • Tick labels: X-axis (0, 50, 100, 150, 200, 250, 300, 350, 400, 450); Y-axis (0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30).
Data Points :
  • Four series, as per legend:
    – “ω = 1/365, βₚ = 1/6”
    – “ω = 1/365, βₚ = 1/12”
    – “ω = 1/60, βₚ = 1/6”
    – “ω = 1/60, βₚ = 1/12”
  • Each series shows a curve with a single peak, then decline.
Design Encodings :
  • Solid, dashed, dash-dot, and dotted lines distinguish the four parameter combinations.
  • All series use black/grey lines.
Distribution & Trends :
  • All curves peak between 0.10 and 0.28 fraction infected, with the highest peak for “ω = 1/60, βₚ = 1/6”.
  • Faster waning (ω = 1/60) and higher transmission (βₚ = 1/6) yield higher and earlier peaks.

# (b) Primary-infected
Title & Axes :
  • Title: “(b) Primary-infected.”
  • X-axis: “Days” (range: 0 to 450).
  • Y-axis: “Fraction infected” (range: 0 to 0.2).
  • Tick labels: X-axis (0, 50, 100, 150, 200, 250, 300, 350, 400, 450); Y-axis (0, 0.05, 0.10, 0.15, 0.20).
Data Points :
  • Same four series as above.
  • Each series shows a single peak, lower than in panel (a).
Design Encodings :
  • Same as panel (a).
Distribution & Trends :
  • Peaks are lower than in panel (a), with the highest for “ω = 1/60, βₚ = 1/6”.

# (c) Secondary-infected
Title & Axes :
  • Title: “(c) Secondary-infected.”
  • X-axis: “Days” (range: 0 to 450).
  • Y-axis: “Fraction infected” (range: 0 to 0.05).
  • Tick labels: X-axis (0, 50, 100, 150, 200, 250, 300, 350, 400, 450); Y-axis (0, 0.01, 0.02, 0.03, 0.04, 0.05).
Data Points :
  • Four series as above, but only the “ω = 1/60” lines show visible peaks.
  • “ω = 1/365” lines are nearly flat at zero.
Design Encodings :
  • Same as above.
Distribution & Trends :
  • Only faster waning (ω = 1/60) produces a noticeable secondary-infected fraction, peaking below 0.03.

# Legend :
  • Located in the upper right of each panel.
  • Lists the four parameter combinations, matching line styles.

# Analysis :
  • Higher immunity waning rate (ω = 1/60) and higher primary-transmission rate (βₚ = 1/6) result in higher and earlier peaks in both total and primary-infected fractions.
  • Secondary infections are negligible for slow waning (ω = 1/365), but become visible for fast waning (ω = 1/60), especially with higher βₚ.
  • The majority of infections are primary, with secondary infections contributing only when immunity wanes quickly. <!-- figure, from page 0 (l=0.056,t=0.335,r=0.941,b=0.576), with ID f32ffecd-9394-4b92-a167-289c54bf8dbc -->

$
\frac{dI_s(t)}{dt} = \sigma_s E_s(t) - \gamma_s I_s(t) \hspace{4cm} (19)
$

$
\frac{dR(t)}{dt} = \gamma_p I_p(t) + \gamma_s I_s(t) - \omega R(t) \hspace{3.7cm} (20)
$ <!-- text, from page 0 (l=0.060,t=0.605,r=0.488,b=0.671), with ID b299270f-0538-40a3-a139-08ada6777fb3 -->

Note that susceptible individuals, both those who have never
been infected and those who have recovered and are currently
susceptible again, become exposed after contacting with both
primary- and secondary-infected individuals. In the absence of
the parameter estimates for COVID-19, I assume that $\beta_s = \beta_p/2$,
$\gamma_s = 2\gamma_p$, and $\sigma_s = \sigma_p$. Following the previous simulations, I set
$\sigma_p = 1/5.2$ and $\gamma_p = 1/18$. The initial values are $I_p(0) = 1/1000$,
$E_p(0) = 43.75 \times I_p(0)$, as in Section 2, and $S_s(0) = E_s(0) = I_s(0) =
R(0) = 0$. <!-- text, from page 0 (l=0.059,t=0.676,r=0.488,b=0.794), with ID 9b4a409d-a6a4-4815-8c2d-6b34576788a3 -->

Fig. 4 shows the simulated time paths for the fraction of the
actively infected population — total (primary and secondary), pri-
mary, and secondary. In these simulations, I consider several sce-
narios. They are characterized by four combinations of the immunity waning rate and primary-transmission rate, $\beta_P$. The immu-
nity waning rate takes two values, $\omega = 1/365$ and $\omega = 1/60$. Thus,
I use the lower and upper bounds of the range considered in the
previous simulations. The primary-transmission rate also takes two
values, $\beta_P = 1/6$ and $\beta_P = 1/12$. The case $\beta_P = 1/6$ corresponds to
$R_0 = 3.0$ in the baseline SEIRS model from Section 2, while the case
$\beta_P = 1/12$ corresponds to $R_0 = 1.5$. We can see from Fig. 4 that the <!-- text, from page 0 (l=0.059,t=0.796,r=0.489,b=0.942), with ID a88f3559-f3de-4638-a83b-685f49ebd6a0 -->

dynamics of the total fraction of the actively infected population is
almost entirely driven by the primary-infected people. There is a
limited role of reinfection in the general epidemic dynamics. <!-- text, from page 0 (l=0.512,t=0.596,r=0.940,b=0.640), with ID 5b3f2bca-85ff-4cb8-b5bd-0c88f33a409a -->

4.2. *One-time reinfection*

Second, instead of a constant immunity waning rate, I assume that the individuals, that are resistant at date $t^*$ (those who were infected in the past), become susceptible again. In particular, I consider a standard SEIR model, i.e. one described by Eqs. (1)-(5) with $\omega = 0$. Before date $t^*$, the dynamics of the model coincides with the no-reinfection case. At date $t^*$, resistant individuals join the pool of susceptible population. Formally this is described by $S(t^*) = S(t^* - dt) + R(t^* - dt)$ as $dt \to 0$. Therefore, at date $t^*$ the fraction of resistant population goes down to zero, while the fraction of susceptible population discretely goes up. To illustrate the patterns that arise under this modeling approach of reinfection, I choose two time thresholds, $t^* = 120$ and $t^* = 30$. <!-- text, from page 0 (l=0.512,t=0.650,r=0.941,b=0.834), with ID f6ddd39b-9776-49c0-a7d3-f0bcde60f7ba -->

Fig. 5 shows the time paths for the fraction of the actively in-
fected population. For each scenario, I consider a range of the bas-
ic reproduction number values. First, my model simulations imply
that if the infection peak occurs before t*, as in Fig. 5a, then rein-
fection leads to a double peak. Second, if the infection peak occurs
shortly after t*, as in Fig. 5b, then reinfection results in a higher
single peak. Notice that the simulated series are consistent with
the conclusion from Section 3 that the mitigation measures (lower <!-- text, from page 0 (l=0.513,t=0.835,r=0.939,b=0.941), with ID e502d73c-c56b-4d6f-880b-6ec868a22d44 -->

6 <!-- marginalia, from page 0 (l=0.494,t=0.956,r=0.506,b=0.966), with ID c3acb234-289f-46c0-91ef-a537088c6ca5 -->

*E. Malkov* <!-- marginalia, from page 0 (l=0.059,t=0.042,r=0.113,b=0.057), with ID 4ac023bf-88b5-4109-a78b-31080499c832 -->

*Chaos, Solitons and Fractals* 139 (2020) 110296 <!-- marginalia, from page 0 (l=0.704,t=0.041,r=0.941,b=0.058), with ID 5d7a8a77-3e29-46af-bca6-fa1b237a4bd6 -->

Summary : This figure presents two line plots comparing the fraction of the actively infected population over time under reinfection (solid lines) and no-reinfection (dashed lines) scenarios, for different basic reproduction numbers (R₀), with two different reinfection times (t* = 120 and t* = 30 days).

line plots:
# Title & Axes :
  • Left panel title: "(a) Reinfection time t* = 120."
  • Right panel title: "(b) Reinfection time t* = 30."
  • X-axis (both panels): "Days", ranging from 0 to 450.
  • Y-axis (both panels): "Fraction infected", ranging from 0 to 0.3 (left: up to 0.25, right: up to 0.3).
  • Tick labels: X-axis (0, 50, 100, 150, 200, 250, 300, 350, 400, 450); Y-axis (0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30).

# Data Series :
  • Each panel shows 8 series:
    – R₀ = 3.0, no reinf (blue dashed)
    – R₀ = 3.0, reinf (blue solid)
    – R₀ = 2.2, no reinf (red dashed)
    – R₀ = 2.2, reinf (red solid)
    – R₀ = 1.8, no reinf (green dashed)
    – R₀ = 1.8, reinf (green solid)
    – R₀ = 1.6, no reinf (black dashed)
    – R₀ = 1.6, reinf (black solid)
  • All series plot "Fraction infected" vs. "Days".

# Design Encodings :
  • Colour: Blue (R₀ = 3.0), Red (R₀ = 2.2), Green (R₀ = 1.8), Black (R₀ = 1.6).
  • Line style: Solid for "reinf" (reinfection allowed), dashed for "no reinf" (no reinfection).
  • Legend present in both panels, upper right.

# Distribution & Trends :
  • For t* = 120 (left): All "reinf" curves show a second peak in infections, while "no reinf" curves decline after the first peak.
  • For t* = 30 (right): "reinf" curves show a single, higher and earlier peak compared to "no reinf" curves, with no clear second peak.
  • Higher R₀ values correspond to higher and earlier peaks in both panels.
  • The difference between "reinf" and "no reinf" is more pronounced for higher R₀ and longer reinfection time.

# Analysis :
  • Allowing reinfection (solid lines) increases the fraction of infected individuals, especially for higher R₀ and longer reinfection time (t* = 120).
  • For t* = 120, reinfection leads to a pronounced second wave of infections, while for t* = 30, reinfection causes a single, larger initial peak.
  • Lower R₀ values result in lower and later peaks, with less pronounced differences between reinfection and no-reinfection scenarios.
  • The timing of reinfection (t*) critically affects the epidemic dynamics, altering the number and timing of infection peaks. <!-- figure, from page 0 (l=0.058,t=0.067,r=0.941,b=0.388), with ID 9e4eae85-6c37-4ad5-8d72-b28c3ba62fe3 -->

$R_0$) delay not only the infection peak, but also the moment when
the difference between the reinfection and no-reinfection scenarios
becomes prominent. <!-- text, from page 0 (l=0.059,t=0.406,r=0.487,b=0.449), with ID 14439135-c9c4-450d-b921-4d0f739f1e09 -->
