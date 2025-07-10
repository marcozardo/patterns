
Biologically sound formal model of Hsp70 heat induction

A B S T R A C T
A proper response to rapid environmental changes is essential for cell survival and requires efficient modifications in the pattern of gene expression. In this respect, a prominent example is Hsp70, a chaperone protein whose synthesis is dynamically regulated in stress conditions. In this paper, we expand a formal model of Hsp70 heat induction originally proposed in previous articles. To accurately capture various modes of heat shock effects, we not only introduce temperature dependencies in transcription to Hsp70 mRNA and in dissociation of transcriptional complexes, but we also derive a new formal expression for the temperature dependence in protein denaturation. We calibrate our model using comprehensive sets of both previously published experimental data and also biologically justified constraints. Interestingly, we obtain a biologically plausible temperature dependence of the transcriptional complex dissociation, despite the lack of biological constraints imposed in the calibration process. Finally, based on a sensitivity analysis of the model carried out in both deterministic and stochastic settings, we suggest that the regulation of the binding of transcriptional complexes plays a key role in Hsp70 induction upon heat shock. In conclusion, we provide a model that is able to capture the essential dynamics of the Hsp70 heat induction whilst being biologically sound in terms of temperature dependencies, description of protein denaturation and imposed calibration constraints. <!-- text, from page 0 (l=0.326,t=0.376,r=0.935,b=0.585), with ID 8628931d-c9f3-4ec3-9449-3947ef55fe56 -->

2. Biochemical model

    Chaperone HSP, as a large family of proteins, consists of members with notably different activity profiles. The family members are classified into sub-families according to their molecular mass (110, 90, 70, 65, 40, 27 kDa and the small HSP). Recently, two of them gained a lot of attention: Hsp90, a highly abundant and ubiquitous chaperone, which has become an important therapeutic target for cancer; and the highly heat-inducible chaperone Hsp70. There are 13 members of the Hsp70 family discovered in human genome. Both Hsp70 and Hsp90 are stable with respect to thermal stress with denaturation starting above human tissue temperatures (Banecki et al., 1992; Palleros et al., 1991; Garnier et al., 1998). <!-- text, from page 0 (l=0.521,t=0.426,r=0.950,b=0.609), with ID 7408bad1-2a2f-4a9c-86d4-4261f192d90b -->

In this section we propose a biochemical model of Hsp70 induction under heat shock conditions, extending the model from Szymańska and Żylicz (2009) and Rybiński et al. (2013). The heat shock response in eukaryotic cells is regulated by a transcription factor known as heat-shock factor 1 (HSF; usually referred in the literature as HSF1). We assume that in unstressed cells HSF is maintained in the non-active monomeric form due to its complexation with various HSPs. Among the most abundant HSP, the complexation with HSF was experimentally confirmed for Hsp70; it is constitutive form Hsc70; and Hsp90 (Nunes and Calderwood, 1995; Baler et al., 1996; Shi et al., 1998; Zou et al., 1998; Ahn et al., 2005). Therefore, for modelling purposes, we assume that Hsp70, Hsc70 and Hsp90 form the HSP family. Although these three proteins all sequester HSF, they differ in their properties. Hsp70 is a stress-inducible protein whereas Hsc70 is constitutively expressed (Dworniczak and Mirault, 1987), meaning that its expression remains almost unchanged in stress conditions. The synthesis of Hsp90 upon stress increases more than that of Hsc70, still the Hsp90 excitation is small compared to Hsp70 (Fortugno et al., 2003). We hence assume that Hsp90, similarly as Hsc70, is a constitutive protein. In consequence, we split the description of HSP synthesis in our model into two components. The first one, which is of major interest for us, represents the synthesis of Hsp70 and encompasses direct modelling of its signalling pathway, subject to stress response. The second one is the synthesis of Hsc70 and <!-- text, from page 0 (l=0.522,t=0.612,r=0.948,b=0.939), with ID a4b1674b-cb01-4661-b984-91d5f2cc7902 -->

76 <!-- marginalia, from page 0 (l=0.051,t=0.043,r=0.071,b=0.055), with ID e5e2fb9f-fbd3-4553-8f80-b8126fed99a0 -->

G. Dudziuk, W. Wronowska and A. Gambin et al./Journal of Theoretical Biology 478 (2019) 74–101 <!-- marginalia, from page 0 (l=0.249,t=0.042,r=0.736,b=0.057), with ID 70545537-6a82-4991-a03b-322e30a7dd99 -->

Table 1  
Species of the biochemical model (2.1)–(2.12). The ODE model proposed in Section 3.1 describes dynamics of each of the species. The column “Initial condition” gives values for the initial concentration of each of the species, for homeostasis at 37°C, resulting from parameter estimation described in Section 3.2. All values are given in μM. The column “Formula” provides references to formulas used to establish the initial values of the species in the run of parameter estimation. <!-- text, from page 0 (l=0.056,t=0.068,r=0.477,b=0.157), with ID e26bb404-9347-4b7c-9de7-8fbb89bcd2d2 -->

<table><thead><tr><th>Species</th><th>Description</th><th>Initial condition</th><th>Formula</th></tr></thead><tbody><tr><td>HSP</td><td>Heat shock proteins</td><td>5.206e+01</td><td>(B.3)</td></tr><tr><td>HSF</td><td>Heat shock factor 1</td><td>1.363e-03</td><td>(C.12.3)</td></tr><tr><td>S</td><td>Denatured proteins (substrate)</td><td>8.122e-08</td><td>(B.5)</td></tr><tr><td>HSP:HSF</td><td>HSP:HSF complexes</td><td>1.429e-02</td><td>(B.9)</td></tr><tr><td>HSP:S</td><td>HSP:S complexes</td><td>5.268e-04</td><td>(B.6)</td></tr><tr><td>HSF₃</td><td>HSF trimers (active HSF)</td><td>9.082e-06</td><td>(B.1)</td></tr><tr><td>HSE</td><td>Heat shock elements</td><td>3.996e-06</td><td>(B.10)</td></tr><tr><td>HSE:HSF₃</td><td>Transcriptional complexes</td><td>4.484e-09</td><td>(C.13.1)</td></tr><tr><td>mRNA</td><td>mRNA of Hsp70</td><td>4.946e-04</td><td>(B.2)</td></tr><tr><td>P</td><td>Native proteins</td><td>1.297e+03</td><td>(B.4)</td></tr></tbody></table> <!-- table, from page 0 (l=0.058,t=0.159,r=0.474,b=0.292), with ID b98b1f3e-23e9-4391-8f0e-00d1ed36e087 -->

Hsp90, assumed to be constant upon stress, which we represent by
a source with constant flux. Separate paths for heat-induced and
constitutive HSP synthesis were not taken into account in many
previous models, see e.g. Rybiński et al. (2013), Szymańska and
Żylicz (2009), and Scheff et al. (2015), despite the fact that the
presence of constitutively expressed HSP may affect HSR dynam-
ics. <!-- text, from page 0 (l=0.052,t=0.323,r=0.481,b=0.415), with ID c0321e7e-71f2-4240-a48b-3139dd1df4f6 -->

Different types of environmental stress, including heat shock,
affect cells mainly by the denaturation of key proteins (we fur-
ther refer the denatured proteins also as substrate). One of the HSP
roles in cellular maintenance is to assist in substrate refolding or
degradation (Lanneau et al., 2010). In the present work, similarly as
in e.g. Szymańska and Żylicz (2009) and Rybiński et al. (2013), we
focus only on the refolding, neglecting the HSP-mediated degra-
dation. For a model taking both refolding and degradation of sub-
strate into account see Sivéry et al. (2016). We also do not take
the denaturation of HSP into account, due to its stability in the
temperature range characteristic for human tissue. To describe con-
secutive stress-induced events, we base on the conceptual model
discussed in Morimoto (1993). Namely, we assume that in stress
conditions cellular HSP pools are insufficient to handle elevated
substrate levels and thus excessive substrate displace HSF from the
HSP:HSF complexes. The released HSF molecules activate by as-
sembly into trimers; bind to heat shock elements (HSE), the pro-
moter sites of the Hsp70 genes, forming transcriptional complexes;
and so trigger the Hsp70 mRNA transcription, leading to elevated
Hsp70 synthesis. When the amount of Hsp70 is sufficiently in-
creased to handle substrate, the excessive Hsp70 sequesters HSF
again, inactivating it and closing the negative feedback loop. We
represent HSF inactivation in our model by trimer breakdown in
the presence of HSP. Note also that actual formation of active tran-
scriptional complexes involving HSF requires activation and bind-
ing of various other proteins (see Section 2.1). However, for the
sake of simplicity, we represent the transcriptional complexes as
active HSF bound to HSE. Moreover, evidences indicate that the
total amount of intracellular HSF molecules (Sarge et al., 1993),
and the course of heat shock experiments (Gamer et al., 1992) <!-- text, from page 0 (l=0.052,t=0.416,r=0.481,b=0.824), with ID 5d80e547-7a3a-4e98-a81b-f9394d1e7d23 -->

Given the above, we formulate the following biochemical model
with 10 species (cf. Table 1) and 12 reactions, among which 3 are
reversible: <!-- text, from page 0 (l=0.053,t=0.823,r=0.481,b=0.864), with ID 58739e3a-5355-4d3c-9c9b-2329fa34b822 -->

$ \text{HSF activation (trimerisation)} \qquad 3 \cdot \text{HSF} \xrightarrow{k_3} \text{HSF}_3, \qquad (2.1) $

$ \text{HSF}_3\text{-to-DNA interactions} \qquad \text{HSF}_3 + \text{HSE} \underset{k_{-7}}{\overset{k_7}{\rightleftharpoons}} \text{HSE:HSF}_3, \qquad (2.2) $ <!-- text, from page 0 (l=0.053,t=0.879,r=0.480,b=0.931), with ID 853b4b47-0e6e-435f-b1c6-36d56b21c3a6 -->

Summary : This diagram illustrates the Heat Shock Response (HSR) model, showing the interactions and reactions among various molecular species (such as HSP, HSF, mRNA, and HSE) involved in the cellular response to stress, with arrows indicating the flow of reactants and products, and different arrow styles representing transcription, translation, and constant inflow.

flowchart:
# Nodes :
  • P (rectangle, bottom left)
  • S (black square, top left and middle left)
  • HSP (blue square, top center and middle center)
  • HSF (orange square, top center-right)
  • HSF₃ (yellow square, middle right)
  • HSE (green square, bottom right)
  • HSF₃·HSE (yellow-green square, middle right)
  • mRNA (green square, top right)
  • Black dots (representing reactions, various locations)

# Connectors :
  • Solid arrows indicate flow of reactants and products, with stoichiometric numbers (e.g., 2, 3) labeled where not equal to 1.
  • Dashed arrows represent transcription and translation reactions.
  • Dotted arrow represents the constant inflow of HSP.
  • Arrows connect nodes in the following ways:
    – P → S (solid arrow)
    – S → HSP (solid arrow)
    – HSP ↔ HSF (solid arrow, bidirectional)
    – HSP + HSF → HSP·HSF (solid arrow, with black dot)
    – HSP·HSF → HSP + HSF (solid arrow, with black dot)
    – HSF → HSF₃ (solid arrow, stoichiometry 3)
    – HSF₃ + HSE → HSF₃·HSE (solid arrow, stoichiometry 2)
    – HSF₃·HSE → HSE + HSF₃ (solid arrow)
    – HSF₃·HSE → mRNA (dashed arrow)
    – mRNA → HSP (dashed arrow)
    – Dotted arrow from outside into HSP (constant inflow)

# Layout :
  • The diagram is organized with species (squares) and reactions (black dots) arranged in a network, with arrows indicating the direction of molecular transformations.
  • The flow generally moves from left (P, S) to right (mRNA, HSE), with feedback loops and bidirectional reactions.
  • Color coding distinguishes different molecular species: S (black), HSP (blue), HSF (orange), HSF₃ (yellow), HSE (green), HSF₃·HSE (yellow-green), mRNA (green).

# Analysis :
  • The diagram captures the complexity of the HSR model, including feedback loops (e.g., HSP and HSF interactions), multimerization (HSF to HSF₃), and the role of transcription and translation in producing HSP.
  • The use of different arrow styles clarifies the types of reactions (chemical, transcriptional, translational, and constant inflow).
  • The network structure highlights the central role of HSP and HSF in regulating the heat shock response, with mRNA and HSE as key downstream products. <!-- figure, from page 0 (l=0.504,t=0.071,r=0.933,b=0.337), with ID d90a6780-2116-405b-992a-a220b657f895 -->

<table>
  <tr>
    <td>transcription</td>
    <td>HSE:HSF<sub>3</sub> <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightarrow{k_7}$</span> HSE:HSF<sub>3</sub> + mRNA,</td>
    <td>(2.3)</td>
  </tr>
  <tr>
    <td>HSF inactivation</td>
    <td>HSP + HSF<sub>3</sub> <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightarrow{l_3}$</span> HSP:HSF + 2 · HSF,</td>
    <td>(2.4)</td>
  </tr>
  <tr>
    <td>HSP-to-substrate interactions</td>
    <td>HSP + S <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightleftharpoons[k_1]{k_1}$</span> HSP:S,</td>
    <td>(2.5)</td>
  </tr>
  <tr>
    <td>HSP-to-HSF interactions</td>
    <td>HSP + HSF <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightleftharpoons[k_2]{k_2}$</span> HSP:HSF,</td>
    <td>(2.6)</td>
  </tr>
  <tr>
    <td>HSP degradation</td>
    <td>HSP <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightarrow{k_9}$</span> ∅,</td>
    <td>(2.7)</td>
  </tr>
  <tr>
    <td>protein refolding</td>
    <td>HSP:S <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightarrow{k_{10}}$</span> HSP + P,</td>
    <td>(2.8)</td>
  </tr>
  <tr>
    <td>protein denaturation</td>
    <td>P <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightleftharpoons[k_{11}]{k_{11}}$</span> S,</td>
    <td>(2.9)</td>
  </tr>
  <tr>
    <td>translation</td>
    <td>mRNA <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightarrow{k_4}$</span> mRNA + HSP,</td>
    <td>(2.10)</td>
  </tr>
  <tr>
    <td>Hsp70 mRNA degradation</td>
    <td>mRNA <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightarrow{k_5}$</span> ∅,</td>
    <td>(2.11)</td>
  </tr>
  <tr>
    <td>constitutive HSP production</td>
    <td>∅ <span style="display:inline-block; transform: translateY(-0.2em);">$\xrightarrow{k_6}$</span> HSP.</td>
    <td>(2.12)</td>
  </tr>
</table> <!-- table, from page 0 (l=0.503,t=0.369,r=0.933,b=0.672), with ID d29f4eb4-b2bc-42de-9682-55040e55a1ec -->

The scheme of the model is depicted in Fig. 1. For the reaction (2.12), describing constitutive HSP production, we assume a constant rate, given by the parameter $k_6$. For the remaining reactions, i.e. (2.1)–(2.11), we assume mass action kinetics. The parameters given alongside the arrows in (2.1)–(2.11) denote rate constants of particular reactions. The superscript “T” at some reaction rate constants indicates dependence on temperature, which we will discuss now. <!-- text, from page 0 (l=0.505,t=0.673,r=0.934,b=0.781), with ID 78215081-6f09-4582-945f-a379e3a2942c -->

2.1. Temperature-dependent reaction rate constants

In our model, we assume temperature dependence in the rate constants for dissociation of HSF trimer from DNA ($I_1^T$ in Eq. (2.2)), HSP transcription ($k_8^T$ in Eq. (2.3)) and protein denaturation ($k_{11}^T$ in Eq. (2.9)). We specify these temperature dependencies as follows. <!-- text, from page 0 (l=0.504,t=0.794,r=0.932,b=0.885), with ID 3f4ebd12-6230-4648-9b59-268a799673c0 -->

Model for HSF3 dissociation from DNA. According to estimates
based on mFCS measurements in U87 cells, the dissociation rate
constant of activated HSF and DNA binding is higher in 37°C than
in a 43°C heat shock, while the forward binding rate constant <!-- text, from page 0 (l=0.506,t=0.887,r=0.932,b=0.941), with ID 8f1f42eb-7a07-4f72-8ba9-beb6356662d9 -->

G. Dudziuk, W. Wronowska and A. Gambin et al./Journal of Theoretical Biology 478 (2019) 74–101 <!-- marginalia, from page 0 (l=0.265,t=0.041,r=0.753,b=0.057), with ID 65c1aea4-3f75-4b62-9b73-21bce9858274 -->

77 <!-- marginalia, from page 0 (l=0.929,t=0.042,r=0.950,b=0.056), with ID 55deb7c9-8c0c-4b25-81bc-3ba5d2cfe71f -->

Table 2  
Summary of the data used for the parameter estimation of the system (3.1)–(3.10). All listed data concern HeLa cells. We quantified the data from Abravaya et al. (1991a) with the use of DataThief III. The data from Theodorakis and Morimoto (1987) are already presented as numerical values in that work. For the rest of the data, we used the quantification from MATLAB scripts attached to Scheff et al. (2015) as supporting material. The “Observable” column presents the interpretation of data assumed in this work. In this column, the notation is as in the system (3.1)–(3.10). Additionally, Hsp70tot denotes the total amount of Hsp70 molecules and HSF3tot denotes the total amount of HSF3, both free and bound to DNA at HSE site, see caption of Fig. D.1 in Appendix D for details. The “Heat shock” column lists distinct heat shock protocols for which measurements were presented in the corresponding papers. Different heat shock protocols reported within a source correspond to separate data series. The “R” column indicates data series for which at least a part of measurements was performed during recovery, i.e. after the heat shock was terminated and the temperature was set back at 37°C. The “No. m.” column specifies the number of measurements in particular data series. In Table 1 in Theodorakis and Morimoto (1987) and Figures 5A and 5B in Abravaya et al. (1991a), there are measurements shared between data series, i.e. performed for times t such that heat shock conditions in particular data series coincide. Qualification of these measurements to specific data series is arbitrary. These measurements are indicated by the extra “+n” entry in the “No. m.” column. **Remark:** In the parameter estimation, we assumed that some data series are given in the same scale. The groups of data series for which distinct scales were assumed are separated in the table by horizontal lines. <!-- text, from page 0 (l=0.200,t=0.068,r=0.817,b=0.265), with ID 1285f859-890d-4156-8f0e-d4e6e70d110c -->

<table><thead><tr><th>Source</th><th>Method</th><th>Observable</th><th>Heat shock</th><th>R</th><th>No. m.</th></tr></thead><tbody><tr><td rowspan="3">(Abravaya et al., 1991a, Figure 8A)</td><td rowspan="3">gel-shift assay</td><td rowspan="3">HSE:HSF₃</td><td>41°C, 285 min</td><td></td><td>10</td></tr><tr><td>42°C, 285 min</td><td></td><td>10</td></tr><tr><td>43°C, 285 min</td><td></td><td>10</td></tr><tr><td rowspan="2">(Abravaya et al., 1991a, Figure 5A)</td><td rowspan="2">run-on assay</td><td rowspan="2">kg↑·HSE:HSF₃</td><td>42°C, 240 min</td><td></td><td>10</td></tr><tr><td>42°C, 40 min</td><td>+</td><td>3</td></tr><tr><td rowspan="2">(Abravaya et al., 1991a, Figure 5B)</td><td rowspan="2">gel-shift assay</td><td rowspan="2">HSE:HSF₃</td><td>42°C, 240 min</td><td></td><td>10</td></tr><tr><td>42°C, 40 min</td><td>+</td><td>3</td></tr><tr><td>(Andrews et al., 1987, Figure 1A)</td><td>Northern blot</td><td>mRNA</td><td>42°C, 360 min</td><td></td><td>7</td></tr><tr><td>(Andrews et al., 1987, Figure 1B)</td><td>Northern blot</td><td>mRNA</td><td>42°C, 120 min</td><td>+</td><td>8</td></tr><tr><td>(Mosser et al., 1988, Figure 3)</td><td>S1 nuclease</td><td>mRNA</td><td>42°C, 240 min</td><td></td><td>6</td></tr><tr><td rowspan="2">(Theodorakis and Morimoto, 1987, Table 1)</td><td rowspan="2">Northern blot</td><td rowspan="2">mRNA</td><td>42°C, 120 min</td><td></td><td>2</td></tr><tr><td>43°C, 120 min</td><td></td><td>2</td></tr><tr><td rowspan="2">(Theodorakis and Morimoto, 1987, Table 1)</td><td rowspan="2">S1 nuclease</td><td rowspan="2">mRNA</td><td>42°C, 120 min</td><td></td><td>2</td></tr><tr><td>43°C, 120 min</td><td></td><td>2</td></tr><tr><td>(Stege et al., 1995, Figure 2C)</td><td>Western blot</td><td>Hsp70tot</td><td>44°C, 15 min</td><td>+</td><td>14</td></tr><tr><td>(Baler et al., 1996, Figure 3)</td><td>gel-shift assay</td><td>HSE:HSF₃</td><td>45°C, 10 min</td><td></td><td>6</td></tr><tr><td>(Baler et al., 1996, Figure 3)</td><td>PAGE</td><td>HSF</td><td>45°C, 10 min</td><td></td><td>6</td></tr><tr><td>(Baler et al., 1996, Figure 3)</td><td>PAGE</td><td>HSP:HSF</td><td>45°C, 10 min</td><td></td><td>6</td></tr><tr><td>(Baler et al., 1996, Figure 3)</td><td>PAGE</td><td>HSF₃tot</td><td>45°C, 10 min</td><td></td><td>6</td></tr></tbody></table> <!-- table, from page 0 (l=0.202,t=0.267,r=0.815,b=0.538), with ID 18f98306-852c-45e2-8356-d2b29af2c1fc -->

is unaffected (Kloster-Landsberg et al., 2012). It is worth a re-
mark, however, that the mFCS-based estimates for association and
dissociation are likely to measure directly only transient inter-
actions of HSF with chromatin (Herbomel et al., 2013). Never-
theless, we assume that the HSF interactions with HSE follow a
model analogous to HSF-chromatin interactions, with temperature-
dependent dissociation, described in our model by I$_T^*$. Moreover,
formation of active HSF-involving transcriptional complexes require
the activation and recruitment of many proteins including replica-
tion protein A (RPA), chromatin-remodelling complex BRG1, gen-
eral transcription factors (GTFs), RNA polymerase II (PolII), histone
chaperones, FACT proteins and others (Fujimoto, 2016; Fujimoto
et al., 2012). Temperature-dependent reorganisation of these multi-
protein complexes and their posttranslational modifications are also
important for the HSE:HSF$_3$ dissociation (Nakai, 2016). Given this,
above a certain threshold temperature the decreasing model of I$_T^*$
suggested by the results of Kloster-Landsberg et al. (2012) may
be not applicable. <!-- text, from page 0 (l=0.068,t=0.569,r=0.499,b=0.806), with ID 40cfeb9c-bbb2-405c-a099-8a1de33c0003 -->

We thus expect that the temperature dependence in $I_T^j$ may be relatively complex. For this reason, we do not propose an explicit mathematical formula as a model of $I_T^j$. Instead, we assume that dependence of $I_T^j$ on T is given by linear interpolation with nodes T = 37, 41, 42, 43, 44, 45 °C and we denote corresponding $I_T^j$ values by $I_{j37}$, $I_{j41}$, $I_{j42}$, $I_{j43}$, $I_{j44}$ and $I_{j45}$, respectively. These constitute additional model parameters to be estimated along with other parameters of our model. The temperature nodes for $I_T^j$ correspond to the heat shock data used for parameter estimation (see Table 2). Note that the proposed $I_T^j$ temperature dependence is defined only <!-- text, from page 0 (l=0.069,t=0.808,r=0.498,b=0.941), with ID b49c2d08-608a-4b20-b6b0-349db4326d1d -->

within the range T ∈ [37, 45]°C. However, this range covers the
temperature values of practical importance. <!-- text, from page 0 (l=0.521,t=0.570,r=0.950,b=0.596), with ID c30d0710-19f0-43e1-ab7b-dc26390ff5f1 -->

**Model for HSP transcription.** Transcription diminishes at high temperatures (Miguel et al., 2013). We therefore represent the temperature dependence in the transcription rate constant k₈ᵀ with a sigmoid function, suppressing the transcription in high-temperature heat shocks: <!-- text, from page 0 (l=0.522,t=0.597,r=0.948,b=0.664), with ID 0178af79-90b0-4af2-a1f0-f5a589377ca7 -->

$k_8^{\mathrm{T}} = k_8^{\max} \cdot \left( 1 - \frac{1}{1 + \exp(-R_{k_8} \cdot (T - T_{k_8}))} \right). \qquad (2.13)$ <!-- text, from page 0 (l=0.522,t=0.675,r=0.948,b=0.717), with ID b3e61389-7355-4ea2-87d9-5635ff740149 -->

Parameters $k_{\delta}^{\max}$, $R_{k_\delta}$ and $T_{k_\delta}$ are new parameters to be estimated. We impose the following constrains during the estimation procedure:
35 < $T_{k_\delta}$ < 50 °C,  $R_{k_\delta} \in (0.01, 25)$ unitless. <!-- text, from page 0 (l=0.522,t=0.726,r=0.947,b=0.792), with ID 592fe553-9b94-4b58-8a53-3f28e6e3396e -->

**Model for the denaturation rate constant.** Previously, this task was only superficially treated in the literature. Many authors assumed that the denaturation rate constant is proportional to the fraction of denatured proteins determined from experimental data (Mizera and Gambin, 2010; Peper et al., 1998; Petre et al., 2011; Rybiński et al., 2013; Sivéry et al., 2016; Scheff et al., 2015). This assumption entails units incompatibility, since the units of the denaturation rate constant are reciprocal time units and the fraction of denatured proteins is unitless. Here we address this issue more rigorously and justify that the denaturation rate constant $k_T^1$ in the <!-- text, from page 0 (l=0.522,t=0.803,r=0.949,b=0.936), with ID 4ee6ca4f-f130-4445-95ce-52c5ea446ccd -->

78 <!-- marginalia, from page 0 (l=0.050,t=0.042,r=0.072,b=0.055), with ID 4ffede11-4fff-4fd6-9038-7e2517e1ff84 -->

G. Dudziuk, W. Wronowska and A. Gambin et al./Journal of Theoretical Biology 478 (2019) 74–101 <!-- marginalia, from page 0 (l=0.248,t=0.041,r=0.737,b=0.057), with ID ec4a5dd1-dfc1-4009-b098-f7ef81071958 -->

model (2.1)–(2.12) may be assumed to follow the formula

$k_{11}^{T} = k_{10} \cdot \frac{V_{\text{den}}^{T}}{1 - V_{\text{den}}^{T}}, \hspace{2cm} (2.14)$

which we use in our model, where $k_{10}$ is the refolding rate constant from the reaction (2.8) and $V_{\text{den}}^{T}$ denotes the fraction of denaturation-susceptible proteins denatured at the temperature T. Note that Eq. (2.14) imposes correct time units. <!-- text, from page 0 (l=0.050,t=0.067,r=0.483,b=0.174), with ID 3d3ae7a4-e75b-45ae-93fe-50f9f91ed6e6 -->

To this end, we introduce the following simplistic model of pro-
tein denaturation and refolding: <!-- text, from page 0 (l=0.051,t=0.172,r=0.480,b=0.203), with ID 1d70b329-9eba-4a03-922a-8f00e06d92a5 -->

$ \mathrm{P} \xrightarrow{a_1} \mathrm{S} \underset{b_1^{'}}{\overset{a_2^{'}}{\rightleftharpoons}} \mathrm{HSP}:\mathrm{S} \xrightarrow{b_1} \mathrm{P}, \qquad (2.15) $ <!-- text, from page 0 (l=0.052,t=0.204,r=0.481,b=0.235), with ID cbec2522-9396-4078-a28a-9b54537e55f6 -->

where rates $a_1^T$, $a_2^T$ and $b_2^T$ depend on the temperature T. Let $\mathrm{P}_*^T$, $\mathrm{S}_*^T$, $\mathrm{HSP:S}_*^T$ and $\mathrm{HSP:HSF}_*^T$ denote equilibrium concentrations of P, S, HSP:S, and HSP:HSF, respectively, at a given temperature T. In addition, denote
$\mathrm{S}_{\mathrm{tot}}^T := \mathrm{S}_*^T + \mathrm{HSP:S}_*^T$,
$\mathrm{P}_{\mathrm{tot}}^T := \mathrm{S}_*^T + \mathrm{HSP:S}_*^T + \mathrm{P}_*^T$. <!-- text, from page 0 (l=0.053,t=0.238,r=0.480,b=0.332), with ID ce78634a-5182-4f43-8582-99f62c90ab4f -->

$V_{\text{den}}^{\text{T}} := \frac{\mathbf{S}_{\text{tot}}^{\text{T}}}{\mathbf{P}_{\text{tot}}^{\text{T}}}.$ <!-- text, from page 0 (l=0.053,t=0.334,r=0.479,b=0.395), with ID e86d747b-ef54-483a-8972-5e02863f1d2f -->

Assuming mass action kinetics for the model (2.15), it is easy to prove that, in its steady state, the following relations hold: <!-- text, from page 0 (l=0.053,t=0.397,r=0.480,b=0.425), with ID 5aae892e-f3f2-42f6-9230-4093206fe4f2 -->

$a_1^{\mathrm{T}} = \delta \cdot \mathbf{b}_1 \cdot \frac{V_{\mathrm{den}}^{\mathrm{T}}}{1 - V_{\mathrm{den}}^{\mathrm{T}}} \quad \mathrm{min}^{-1} \qquad \text{and} \qquad \frac{\mathbf{S}_*^{\mathrm{T}}}{\mathrm{HSP} \cdot \mathbf{S}_*^{\mathrm{T}}} = \frac{1}{\delta} - 1,$

\[(2.16)\] <!-- text, from page 0 (l=0.053,t=0.431,r=0.479,b=0.482), with ID 82346103-c0e3-47fa-a043-4e2518d9ab0c -->

$ \delta := \frac{a_2^1}{a_2^1 + (b_1^1 + b_2^1)} $ <!-- text, from page 0 (l=0.053,t=0.484,r=0.319,b=0.513), with ID 19aaae49-f794-4c04-8794-cba012713dab -->

1. (i) Kinetics of denaturation and refolding in the model (2.1)–(2.12) can be approximated by those in the model (2.15), i.e. $k_{11}^{\mathrm{T}} \approx a_1^{\mathrm{T}}$ and $k_{10} \approx b_1$.
2. (ii) In cellular conditions, and in the model (2.15) as well, for any viable temperature T, in the equilibrium, the vast majority of remaining misfolded proteins is chaperoned, i.e. for some small $\epsilon$ we have $\frac{S_1^{\mathrm{T}}}{\mathrm{HSP} \cdot S_1^{\mathrm{T}}} < \epsilon$. <!-- text, from page 0 (l=0.073,t=0.514,r=0.481,b=0.614), with ID cf916098-d307-4257-a452-e6787ff5f49e -->

Using the first part of (2.16) and the assumption (i) we have <!-- text, from page 0 (l=0.053,t=0.617,r=0.440,b=0.635), with ID 1f05b156-6b72-41f6-b64d-91fc424d8b9a -->

$ \mathbf{k}_{11}^{\mathrm{T}} \approx \delta \cdot \mathbf{k}_{10} \cdot \frac{V_{\mathrm{den}}^{\mathrm{T}}}{1 - V_{\mathrm{den}}^{\mathrm{T}}}. $ <!-- text, from page 0 (l=0.053,t=0.637,r=0.214,b=0.669), with ID d971badb-e8df-4cd0-b16b-d024d798f2ad -->

Finally, by the second part of (2.16), the assumption (ii) and from
the definition of $\delta$, it follows that $\frac{1}{1+\epsilon} < \delta < 1$ and, consequently, <!-- text, from page 0 (l=0.053,t=0.670,r=0.479,b=0.699), with ID 54fcac9d-361a-4671-8953-a599ffcde640 -->

$\delta \approx 1$. Assuming that the resulting approximation for $k_{11}^{\mathrm{T}}$ is sufficiently accurate for modelling purposes, we obtain (2.14), <!-- text, from page 0 (l=0.054,t=0.700,r=0.479,b=0.734), with ID 536ddec3-feb4-4395-89be-63b2b11f95fb -->

As a model of the fraction of denatured proteins $V_{\text{den}}^{\text{fr}}$ we choose
the Hill function, given by <!-- text, from page 0 (l=0.054,t=0.731,r=0.478,b=0.756), with ID e4dc0277-69a0-41e9-bf9b-cd5c556ace0d -->

$V_{\text{den}}^{T} = 1 - \left( 1 + \left( \frac{T - T_0}{T_{0.5} - T_0} \right)^{n_v} \right)^{-1}, \qquad\qquad\qquad\qquad\qquad\qquad\qquad (2.17)$ <!-- text, from page 0 (l=0.053,t=0.763,r=0.480,b=0.794), with ID 8e031982-b6e6-48a3-b26a-6aba5c1ad857 -->

where T₀, T₀.₅ and nₙᵥ are new parameters of the model, subject
to parameter estimation along with other model parameters. This
function was chosen because it has enough flexibility to reproduce
real fractional denaturation data, and is in this respect superior
to the power-exponential function used in previous works on HSR
modelling (see Appendix A). The following constrains are assumed
for the optimization purpose: <!-- text, from page 0 (l=0.053,t=0.797,r=0.480,b=0.888), with ID aaa93f3e-de76-48d0-afec-47574fbcf767 -->

$30 < T_0 < 37 - T_\epsilon\ \degree\mathrm{C}, \qquad 37 + T_\epsilon < T_{0.5} < 62\ \degree\mathrm{C}, \qquad n_v \in (1, 100)\ \text{unitless},$ <!-- text, from page 0 (l=0.053,t=0.891,r=0.383,b=0.925), with ID 1593a798-4a20-420b-8081-947c1220692d -->

where we fix T$_\epsilon$ as 0.01. <!-- text, from page 0 (l=0.054,t=0.927,r=0.209,b=0.942), with ID 52fadb97-d2fc-4c18-aeaf-f98dd17fdfd0 -->

3. Mathematical model and parameter estimation

    In the following Section we introduce the mathematical model composed of ordinary differential equations (ODE) and we describe the procedure of parameter estimation of the model. The data involved in parameter estimation concern both HSR dynamics and constraints for model parameters, including reaction rate constants, conserved concentrations and some other quantities. To calibrate the model to the human cells, all dynamical data concern HeLa cell line. The constraints data have diverse origins but we made an attempt to base on HeLa data whenever they were available. <!-- text, from page 0 (l=0.504,t=0.070,r=0.933,b=0.216), with ID 57488449-d8fd-47b8-8908-e9cf2f1ffde3 -->

3.1. Mathematical model

    Assuming mass action kinetics for reactions (2.1)–(2.11) and constant production rate for the reaction (2.12), we transform the biochemical model (2.1)–(2.12) into the system of ten ODEs: <!-- text, from page 0 (l=0.505,t=0.228,r=0.932,b=0.297), with ID 04e3e536-3e80-42c4-a837-ece281cc028c -->

$ \mathrm{HSP}' = -l_3 \cdot \mathrm{HSF}_3 \cdot \mathrm{HSP} - k_1 \cdot \mathrm{HSP} \cdot S + l_1 \cdot \mathrm{HSP}\!:\!S \\
\qquad\qquad\quad - k_2 \cdot \mathrm{HSF} \cdot \mathrm{HSP} + l_2 \cdot \mathrm{HSP}\!:\!\mathrm{HSF} \\
\qquad\qquad\quad - k_9 \cdot \mathrm{HSP} + k_{10} \cdot \mathrm{HSP}\!:\!S + k_4 \cdot \mathrm{mRNA} + k_6, $ <!-- text, from page 0 (l=0.506,t=0.306,r=0.930,b=0.359), with ID 0e73c946-28ab-4b96-b254-b156b7ea3e04 -->

$ \mathrm{HSF}' = -3 \cdot k_3 \cdot \mathrm{HSF}^3 + 2 \cdot l_3 \cdot \mathrm{HSF}_3 \cdot \mathrm{HSP} \\
\qquad\qquad\ - k_2 \cdot \mathrm{HSF} \cdot \mathrm{HSP} + l_2 \cdot \mathrm{HSP}:\mathrm{HSF}, \tag{3.2} $ <!-- text, from page 0 (l=0.506,t=0.370,r=0.930,b=0.404), with ID 69672482-dd55-41e4-9a1b-782a1d99c111 -->

$S' = -k_1 \cdot \mathrm{HSP} \cdot S + l_1 \cdot \mathrm{HSP}\!:\!S + k_{11}^{T} \cdot P,$ <!-- text, from page 0 (l=0.506,t=0.411,r=0.930,b=0.430), with ID ac61416e-264b-4240-92ff-784de2a8fa12 -->

$ \text{HSP:HSF}' = +k_2 \cdot \text{HSF} \cdot \text{HSP} - l_2 \cdot \text{HSP:HSF} + l_3 \cdot \text{HSF}_3 \cdot \text{HSP},\ \ (3.4) $ <!-- text, from page 0 (l=0.506,t=0.440,r=0.931,b=0.456), with ID 42c9024f-eab8-4ab5-b68d-5a03e2fb3b54 -->

$ \mathrm{HSP:S}' = +k_1 \cdot \mathrm{HSP} \cdot \mathrm{S} - l_1 \cdot \mathrm{HSP:S} - k_{10} \cdot \mathrm{HSP:S}, \qquad (3.5) $ <!-- text, from page 0 (l=0.506,t=0.469,r=0.929,b=0.486), with ID 549beb70-9c49-41d6-b76c-9de9b980bc10 -->

$ 
\begin{align*}
\mathrm{HSF}_3' =\ &+k_3 \cdot \mathrm{HSF}^2 - l_3 \cdot \mathrm{HSF}_3 \cdot \mathrm{HSP} \\
&- k_7 \cdot \mathrm{HSE} \cdot \mathrm{HSF}_3 + I_7^t \cdot \mathrm{HSE}:\mathrm{HSF}_3, \tag{3.6}
\end{align*}
$ <!-- text, from page 0 (l=0.507,t=0.501,r=0.930,b=0.527), with ID 5991be53-efc5-4d6a-84e3-1e1bd2fddfd6 -->

$ \text{HSE}' = -k_7 \cdot \text{HSE} \cdot \text{HSF}_3 + l_7^T \cdot \text{HSE:HSF}_3, \qquad\qquad\qquad\qquad\qquad (3.7) $ <!-- text, from page 0 (l=0.506,t=0.546,r=0.930,b=0.563), with ID 3882313c-9598-460f-b9a3-3518fa90e900 -->

$ \mathrm{HSE}:\mathrm{HSF}_3' = +k_7 \cdot \mathrm{HSE} \cdot \mathrm{HSF}_3 - I_7^T \cdot \mathrm{HSE}:\mathrm{HSF}_3, \qquad\qquad (3.8) $ <!-- text, from page 0 (l=0.507,t=0.577,r=0.930,b=0.593), with ID 317a5df6-152e-476e-9611-19f446aa2e6d -->

$m\text{RNA}' = +k_8^T \cdot \text{HSE:HSF}_3 - k_5 \cdot m\text{RNA}, \hspace{3cm} (3.9)$ <!-- text, from page 0 (l=0.507,t=0.607,r=0.930,b=0.623), with ID ce8328d8-a9fb-4768-be86-326fe9b42999 -->

$P' = +k_{10} \cdot \text{HSP:S} - k_{11}^{T} \cdot P.$

$(3.10)$ <!-- text, from page 0 (l=0.506,t=0.637,r=0.930,b=0.653), with ID 08dca0eb-d665-4325-b330-e2c335782a9c -->

For the system (3.1)–(3.10), we have the following 3 independent linear conservation laws: <!-- text, from page 0 (l=0.508,t=0.661,r=0.930,b=0.685), with ID b2bf01d6-4a1f-4a48-acad-b67258661e41 -->

$ \mathrm{P}_{\mathrm{tot}} := \mathrm{P}(t) + \mathrm{S}(t) + \mathrm{HSE} : \mathrm{S}(t), \hspace{4cm} (3.11) $ <!-- text, from page 0 (l=0.506,t=0.693,r=0.931,b=0.709), with ID 1c62535d-79e9-44f7-86de-ff685409c3ed -->

$ \mathrm{HSF}_{\mathrm{tot}} := \mathrm{HSF}(t) + \mathrm{HSP} : \mathrm{HSF}(t) + 3 \cdot \mathrm{HSF}_3(t) + 3 \cdot \mathrm{HSE} : \mathrm{HSF}_3(t), \qquad\qquad\qquad\qquad\qquad\qquad\qquad (3.12) $ <!-- text, from page 0 (l=0.507,t=0.720,r=0.930,b=0.751), with ID 77de13e6-4f8e-4bb9-9f09-cbfbd7ef493b -->

$ \mathrm{HSE}_{\mathrm{tot}} \; := \; \mathrm{HSE}(t) + \mathrm{HSE} : \mathrm{HSF}_3(t), \qquad (3.13) $ <!-- text, from page 0 (l=0.506,t=0.763,r=0.931,b=0.807), with ID e764eb49-9f44-461e-b452-cbc7e4c73a40 -->

3.2. *Parameter estimation*

In order to estimate parameters of the model, we fitted the solutions of the system (3.1)–(3.10) to experimental data on the dynamics of cellular HSP-associated species under temperature stress. Table 2 summarizes used datasets together with the informations on applied heat shock protocols and experimental methods. Additionally, Fig. D.1 in Appendix D presents the data along with fitted curves of model observables. <!-- text, from page 0 (l=0.505,t=0.823,r=0.931,b=0.939), with ID 285de411-cd7a-4df3-8e83-c4b64443face -->

G. Dudziuk, W. Wronowska and A. Gambin et al./Journal of Theoretical Biology 478 (2019) 74–101 <!-- marginalia, from page 0 (l=0.265,t=0.042,r=0.754,b=0.059), with ID 4a34ec8f-42cc-4ccc-8462-68938090d628 -->

79 <!-- marginalia, from page 0 (l=0.931,t=0.043,r=0.949,b=0.055), with ID 1f4dc5c0-ce98-48d7-a315-d49e7c0d208b -->

Since the data concern experiments starting at homeostasis in
unstressed conditions, we set the initial conditions for the system
(3.1)–(3.10) to a stationary state for T = 37°C, i.e. <!-- text, from page 0 (l=0.069,t=0.069,r=0.500,b=0.111), with ID cbabf5ee-6093-46b9-b95f-5b7bcb22e97c -->

$\mathbf{f}(\mathbf{x}_0, \mathbf{k}^{\mathrm{T}}) = \mathbf{0} \quad \text{for T} = 37^\circ \mathrm{C}, \qquad \hspace{4cm} (3.14)$ <!-- text, from page 0 (l=0.068,t=0.111,r=0.500,b=0.134), with ID badacd6c-34b3-4432-8f7e-307e25dbdacc -->

where $\mathbf{x}_0$ represents initial conditions and $\mathbf{f} = \mathbf{f}(\mathbf{x}, \mathbf{k}^{\mathrm{T}})$ represents the right-hand side of (3.1)–(3.10), for species concentrations $\mathbf{x}$ and kinetic parameters $\mathbf{k}^{\mathrm{T}}$, some of which depend on temperature T. We were able to explicitly resolve the condition (3.14) augmented with the conservation laws (3.11)–(3.13), obtaining an explicit parametrization of the model, see Appendix B. This allowed us to avoid including (3.14) to the parameter estimation problem as a nonlinear equality constraint and reduced the number of free parameters to estimate. These free parameters of parametrization, denote them $\mathbf{q}$, determine both $\mathbf{x}_0$ and $\mathbf{k}^{\mathrm{T}}$. <!-- text, from page 0 (l=0.067,t=0.135,r=0.500,b=0.268), with ID 6e4c0875-6207-47d5-94ff-b32fd5f66c5c -->

To ensure biological adequacy of kinetic parameters subject to the optimization process, we performed an exhaustive literature search for biologically justified parameters values. As a result, we were able to impose constraints for most of the reaction rate constants of the model (3.1)–(3.10) as well as for the conserved concentrations P_tot, HSF_tot and HSE_tot and some other characteristic quantities, see Appendix C. In summary, there were more constrained parameters than necessary to determine the parametrization parameters **q**. Consequently, it was necessary to derive some of the constrained parameters from others instead of optimizing them directly. This resulted in an optimization problem with both box and nonlinear constraints: <!-- text, from page 0 (l=0.067,t=0.267,r=0.499,b=0.428), with ID 7d7b8aee-33c1-40cd-9f36-759d1b0adbb9 -->

$
\begin{array}{ll}
\min_{\mathbf{p}} J(\mathbf{p}) \\
\mathbf{p}_{low} < \mathbf{p} < \mathbf{p}_{high} \\
\mathbf{C}(\mathbf{p}) < 0
\end{array}
\hspace{3cm} (3.15)
$ <!-- text, from page 0 (l=0.069,t=0.428,r=0.499,b=0.470), with ID 29c1eed4-e17c-4dd3-8bef-8e285ce3a316 -->

where C is a nonlinear function. Above, the vector of optimized pa-
rameters **p** does not coincide with the model parameters **x₀** and
**k**ᵀ, however allows to derive the parametrization parameters **q**
and, subsequently, **x₀** and **k**ᵀ; see Appendix C for details. <!-- text, from page 0 (l=0.069,t=0.473,r=0.499,b=0.526), with ID 4db0281c-508e-4eed-a5fb-9e054e07714b -->

We now specify the target function J. We minimized the weighted sum of squared residuals (RSS) between the data and respective observables of the system (3.1)–(3.10). Since our data are given on arbitrary scales, the observables were scaled by suitable scale factors s. We resolved the scale factors explicitly, avoiding adding them as free parameters for optimization. To explain how this was done, we start with an auxiliary target function J₀ with unresolved scale factors s and next we show how these factors were resolved in J. The auxiliary target function J₀ is as follows: <!-- text, from page 0 (l=0.069,t=0.525,r=0.498,b=0.645), with ID e32ffa9d-8e58-44d2-81d2-8d9db1d9d909 -->

$ 
J_0(\mathbf{p}, \mathbf{s}) := \sum_{j=1}^{J} \sum_{k=1}^{K_j} \left( \frac{\tilde{y}_{j,k} - s_{l(j)} \cdot \mathbf{y}_{j,k}(\mathbf{p})}{\sigma_{j,k}} \right)^2,
$ <!-- text, from page 0 (l=0.068,t=0.645,r=0.497,b=0.691), with ID bceaac2f-710d-4f75-9cfe-b004e38704d9 -->

$y_{j,k}(\mathbf{p}) := \overline{y}_{j}(\mathbf{p}, T_j, t_{j,k}, \mathbf{x}(\mathbf{p}, T_j, t_{j,k})). \hspace{2cm} (3.16)$

where $\overline{y}_{j,k}$ are measurements from data series $j = 1, \ldots, J$ in given time points $t_{j,k}$, for $k = 1, \ldots, K_j$. The value $\sigma_{j,k}$ denotes the standard deviation of the $k$-th point in the $j$-th data series. The function $y_j$ denotes model observable corresponding to the $j$-th data series (see Table 2). The values of $y_j$ are multiplied by the scale factor $s_{l(j)}$, where $l(j)$ denotes the index of the scale factor in the vector $\mathbf{s}$ corresponding to the $j$-th data series. The indices $l(j)$ are necessary because some of the data series share the same scale factor (see Table 2). In the functions of observables $y_j$, $T_j = T_j(t)$ is the time-dependent heat shock corresponding to the $j$-th data series (see Table 2) and $\mathbf{x}(\mathbf{p}, T_j, t)$ is the solution to the model (3.1)–(3.10) corresponding to the temperature input $T_j$ and parameters $\mathbf{p}$. <!-- text, from page 0 (l=0.068,t=0.692,r=0.499,b=0.870), with ID 50af6008-3024-4c57-9fd9-85e890850bb8 -->

Instead of directly minimizing the function J₀, we resolve the scales **s** in a way that leads to an equivalent minimization problem. Namely, the new problem is to minimize the target function **J** defined as <!-- text, from page 0 (l=0.068,t=0.869,r=0.499,b=0.923), with ID e1ea7f33-a476-406e-8d17-3c454b876798 -->

$ \mathbf{J}(\mathbf{p}) \; := \; \min_{\mathbf{s}} \mathbf{J}_0(\mathbf{p}, \mathbf{s}), $ <!-- text, from page 0 (l=0.065,t=0.925,r=0.224,b=0.945), with ID 425a06d2-30da-4c34-91c8-5ece9a3035a4 -->

$(3.17)$ <!-- marginalia, from page 0 (l=0.454,t=0.925,r=0.500,b=0.944), with ID 43317c25-9ed3-4ee2-9766-42e6e6d057f4 -->

$ \mathbf{J}(\mathbf{p}) \; := \; \mathbf{J}_0(\mathbf{p}, \mathbf{s}^*(\mathbf{p})), \qquad\qquad\qquad\qquad\qquad\qquad\qquad (3.18) $ <!-- text, from page 0 (l=0.518,t=0.071,r=0.952,b=0.107), with ID e5139a23-9a82-4303-8365-8f19b1695045 -->

where $\mathbf{s}^*(\mathbf{p})$ is the vector of scale factors solving the minimization problem on the right hand side of (3.17) for given $\mathbf{p}$, i.e. we express the scale factors as functions of the model parameters. Note that from the positivity of $y_{j,k}(\mathbf{p})$ (which can be shown for our model given positive kinetic parameters and conserved quantities) it follows that $J_0(\mathbf{p}, \mathbf{s})$ is quadratic and positive-definite w.r.t. scale factors $\mathbf{s}$. In consequence, for a given $\mathbf{p}$, the vector of optimal scales $\mathbf{s}^*(\mathbf{p})$ exists and is unique, making $J(\mathbf{p})$ well-defined. An arbitrary local minimum $(\mathbf{p}_1, \mathbf{s}_1)$ of $J_0$ determines a local minimum $\mathbf{p}_2$ of $J$ by the assignment $\mathbf{p}_2 := \mathbf{p}_1$. *Vice versa*, a local minimum $\mathbf{p}_2$ of $J$ gives a minimum $(\mathbf{p}_1, \mathbf{s}_1)$ of $J_0$ by assignments $\mathbf{p}_1 := \mathbf{p}_2$ and $\mathbf{s}_2 := \mathbf{s}^*(\mathbf{p}_2)$. Thus, the minimization of $J$ is indeed equivalent to the minimization of $J_0$. <!-- text, from page 0 (l=0.520,t=0.109,r=0.951,b=0.279), with ID 1d247a24-b461-431d-b28f-e577d88d530a -->

As $J_0(\mathbf{p}, \mathbf{s})$ is quadratic and positive-definite w.r.t. $\mathbf{s}$, the vector of optimal scales $\mathbf{s}^*(\mathbf{p})$ is the solution of

$\nabla_{\mathbf{s}} J_0(\mathbf{p}, \mathbf{s}) \ = \ 0.$
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <!-- text, from page 0 (l=0.520,t=0.280,r=0.951,b=0.330), with ID de8cdda1-67fe-465c-9c61-2e457cf005d5 -->

By solving the Eq. (3.19) for s, we derive the vector s*(p) of optimal scale factors: <!-- text, from page 0 (l=0.519,t=0.331,r=0.950,b=0.362), with ID 6c82b9a0-324c-4915-8d62-46521b6de39b -->

$
\mathbf{s}_l^i(\mathbf{p}) = 
\frac{
    \sum_{j=1}^J N_{j,l} \cdot \sum_{k=1}^{K_j} \sigma_{j,k}^{-2} \cdot \tilde{y}_{j,k} \cdot \mathbf{y}_{j,k}(\mathbf{p})
}{
    \sum_{j=1}^J N_{j,l}^2 \cdot \sum_{k=1}^{K_j} \sigma_{j,k}^{-2} \cdot \mathbf{y}_{j,k}(\mathbf{p})^2
}
\quad \text{for } l = 1, \ldots, L,
\qquad (3.20)
$ <!-- text, from page 0 (l=0.520,t=0.364,r=0.951,b=0.426), with ID a82552d5-ab72-4636-90dd-67a4064ea5e7 -->

where $s^l_i(\mathbf{p})$ denotes the $l$-th component of $\mathbf{s}^*(\mathbf{p})$ and $N_{j,l}$ equals 1 for $l = l(j)$ and 0 otherwise. Substituting (3.20) to (3.18), we obtain a more explicit form of $\mathbf{J}$: <!-- text, from page 0 (l=0.521,t=0.428,r=0.951,b=0.470), with ID 7edd4da3-43fe-4c84-a4c6-b75c269855df -->

$ \mathbf{J}(\mathbf{p}) = \sum_{j=1}^{J} \sum_{k=1}^{K_j} \left( \frac{ \widetilde{y}_{j,k} - \mathbf{S}_{l(j)}^{\mathrm{T}}(\mathbf{p}) \cdot \mathbf{y}_{j,k}(\mathbf{p}) }{ \sigma_{j,k} } \right)^2. \hspace{2cm} (3.21) $ <!-- text, from page 0 (l=0.520,t=0.472,r=0.951,b=0.513), with ID f2cfe882-d1b9-4d8a-ab6b-6bf169dc0e62 -->

The above method of removing scale factors from the parame-
ter estimation problem was already presented in Weber et al.
(2011) and, in a more general setting, in Loos et al. (2018). <!-- text, from page 0 (l=0.520,t=0.516,r=0.950,b=0.561), with ID 92d315a9-9287-40ac-a71e-60ba56992e08 -->

To fully specify $J$, it is necessary to define the standard devia-
tions $\sigma_{jk}$. We assumed that the standard deviation $\sigma_{jk}$ of the $k$-th
data point in the $j$-th data series is a sum of absolute and relative
error components, i.e. <!-- text, from page 0 (l=0.520,t=0.558,r=0.951,b=0.612), with ID 8095cb54-80d9-4729-ba6d-3662e8030680 -->

$\sigma_{j,k} := \sigma_{j,\mathrm{rel}} \cdot \widetilde{y}_{j,k} + \sigma_{\mathrm{abs}} \cdot PV_j,$ <!-- text, from page 0 (l=0.520,t=0.614,r=0.950,b=0.634), with ID 442e6adf-73e3-42be-b6ce-ce0622dce785 -->

where $PV_j$ is the peak value computed for the $j$-th data series and $\sigma_{j,rel}$, $\sigma_{abs}$ are relative and absolute error parameters, respectively. The $\sigma_{abs}$ parameter value was assumed to be 3%, independently of the data series, and the value of $\sigma_{j,rel}$ was assumed to be one of 15%, 20% or 25%, depending on the experimental method corresponding to particular data series (see Table 2): <!-- text, from page 0 (l=0.520,t=0.636,r=0.950,b=0.718), with ID 28476b76-85fa-4d92-b893-c7340c1d4b77 -->

- • 25% relative error – gel-shift assay experiments,
- • 20% relative error – Northern blot, Western blot and PAGE experiments,
- • 15% relative error – nuclear run-on and S1 nuclease experiments. <!-- text, from page 0 (l=0.525,t=0.721,r=0.950,b=0.790), with ID daebe93f-a69d-40cd-9d08-297bb13c0d29 -->

To compute the peak values $PV_{j}$, we assumed that the standard deviations $\sigma_{j,k}$ for measurements with the same observable and conditions should be computed using the same peak value. We thus grouped the data series corresponding to the same model curves, at least until some time $t > 0$. Next, we normalized the data series in each group to have a common mean value for the measurements repeated in all series in the group (i.e. measurements at the same time and temperature). After the normalization, we computed the peak value $PV_{j}$ for each data series as the maximal value of all data series in the corresponding group. Details are available upon request. Moreover, as the data from Fig. 2C <!-- text, from page 0 (l=0.520,t=0.794,r=0.951,b=0.941), with ID becd6f52-75ad-454c-9eee-7a45472c5e8c -->

80 <!-- marginalia, from page 0 (l=0.050,t=0.042,r=0.072,b=0.055), with ID a6d86e6d-1939-4fbe-8691-61336d5be789 -->

G. Dudziuk, W. Wronowska and A. Gambin et al./Journal of Theoretical Biology 478 (2019) 74–101 <!-- marginalia, from page 0 (l=0.249,t=0.042,r=0.736,b=0.056), with ID 588ae0cf-9f8d-4b00-8dd8-1c631f0b553f -->

Summary : This figure presents three plots showing the temperature dependence of three reaction rate constants in a biochemical model: HSE:HSF3 dissociation rate constant (labeled as \( l_7^T \)), transcription rate constant (\( k_8^T \)), and denaturation rate constant (\( k_{11}^T \)), each as a function of temperature (in degrees Celsius).

line charts:
# Left Plot: HSE:HSF3 Dissociation Rate Constant (\( l_7^T \))
Title & Axes :
  • No explicit title; y-axis labeled “\( l_7^T \) (1/min)”, x-axis labeled “Temperature (C deg)”.
  • X-axis tick labels: 38, 40, 42, 44.
  • Y-axis range: 0 to 1.0 × 10² (i.e., 0 to 100).
Data Points :
  • Blue diamonds at (38, ~0.6×10²), (39, ~0.4×10²), (40, ~0.2×10²), (41, ~0.1×10²), (42, ~0.1×10²), (44, ~0.9×10²).
Design Encodings :
  • Blue line connecting blue diamond markers.
Distribution & Trends :
  • Decreases from 38°C to 42°C, then sharply increases at 44°C, forming a U-shaped curve.

# Middle Plot: Transcription Rate Constant (\( k_8^T \))
Title & Axes :
  • No explicit title; y-axis labeled “\( k_8^T \) (1/min)”, x-axis labeled “Temperature (C deg)”.
  • X-axis tick labels: 38, 40, 42, 44.
  • Y-axis range: 0 to 1.0 × 10² (i.e., 0 to 100).
Data Points :
  • Single blue line, no markers; appears constant at ~0.9×10² from 38°C to ~43°C, then drops sharply to zero by 44°C.
Design Encodings :
  • Solid blue line.
Distribution & Trends :
  • Plateau at high value, then abrupt drop-off near 44°C.

# Right Plot: Denaturation Rate Constant (\( k_{11}^T \))
Title & Axes :
  • No explicit title; y-axis labeled “\( k_{11}^T \) (1/min)”, x-axis labeled “Temperature (C deg)”.
  • X-axis tick labels: 38, 40, 42, 44.
  • Y-axis range: 0 to 3 × 10⁻² (i.e., 0 to 0.03).
Data Points :
  • Single blue line, no markers; curve starts near zero at 38°C and rises steeply to ~0.03 at 44°C.
Design Encodings :
  • Solid blue line.
Distribution & Trends :
  • Exponential-like increase with temperature.

Analysis :
  • The dissociation rate constant (\( l_7^T \)) shows a U-shaped temperature dependence, decreasing then increasing sharply.
  • The transcription rate constant (\( k_8^T \)) remains high and constant until a critical temperature (~43°C), after which it drops abruptly.
  • The denaturation rate constant (\( k_{11}^T \)) increases rapidly with temperature, especially above 42°C, indicating strong temperature sensitivity.
  • The three plots together illustrate distinct temperature dependencies for each reaction rate, with potential biological implications for heat shock response modeling. <!-- figure, from page 0 (l=0.051,t=0.063,r=0.936,b=0.273), with ID 4bcd96f4-fdd9-465e-a7e6-2bfe53344643 -->

Summary : This figure presents a line plot comparing predictions of fractional denaturation models (overall and critical) and a model-driven curve, against experimental data, as a function of temperature. The plot is used to assess how well the models capture protein denaturation behavior relevant to cell death.

line plot:
# Title & Axes :
  • No explicit title on the plot, but the context is "Predictions of fractional denaturation model versus predictions and experimental data."
  • X-axis: "Temperature" (no units specified, but values suggest degrees Celsius).
  • Y-axis: "Denaturation level" (unitless, normalized).
  • X-axis tick labels: 36, 38, 40, 42, 44, 46.
  • Y-axis tick labels: 0.00, 0.05, 0.10, 0.15, 0.20, 0.25.

# Data Points :
  • Three series are plotted:
    – "Overall" (black dashed line): experimental data for overall protein denaturation in rat liver homogenate.
    – "Critical" (red dash-dot line): model-driven predictions for proteins critical to cell death.
    – "Model" (solid blue line): model-driven predictions for overall denaturation.
  • Data is continuous; exact (x, y) pairs are not individually labeled.

# Design Encodings :
  • "Overall": black dashed line.
  • "Critical": red dash-dot line.
  • "Model": solid blue line.
  • Legend box in upper left, with series names and line styles.
  • No error bars or confidence intervals shown.
  • Grid lines present for both axes.

# Distribution & Trends :
  • All three curves show a low, nearly flat denaturation level from 36°C to about 41°C.
  • Above ~41°C, all curves rise, with the "Critical" (red) curve increasing most steeply, followed by "Overall" (black), and "Model" (blue) rising more gradually.
  • The "Critical" curve surpasses the others at higher temperatures (above 43°C).
  • The "Model" curve remains below the other two across the entire temperature range.

# Analysis :
  • The "Critical" (red) model predicts a sharper increase in denaturation at higher temperatures compared to the "Overall" and "Model" curves.
  • The "Overall" (black) experimental data rises less steeply than the "Critical" model but more than the "Model" prediction.
  • The "Model" (blue) underestimates denaturation relative to both experimental and "Critical" model curves, especially above 42°C.
  • The divergence between curves above 42°C highlights differences in model sensitivity to temperature, with the "Critical" model most responsive to temperature increases. <!-- figure, from page 0 (l=0.050,t=0.291,r=0.481,b=0.606), with ID 2b2795fc-f623-4c76-9b47-fc78a5776e49 -->

in Stege et al. (1995) represent means of $n = 2$ or $n = 3$ repeated
measurements, the respective standard deviations were divided by
$\sqrt{n}$. <!-- text, from page 0 (l=0.051,t=0.645,r=0.480,b=0.684), with ID 8ababe24-de0c-40ca-932f-7a6bc15c9de1 -->

Table 4 summarizes particular vectors and functions introduced
above to set the parameter estimation problem (3.15) up, along
with their dimensions. <!-- text, from page 0 (l=0.052,t=0.685,r=0.480,b=0.724), with ID 41954417-0731-48fc-b74e-da11c1d87954 -->

We performed the parameter estimation by solving the minimization problem (3.15), with the target function J described above. To minimize J, we combined global and local optimization methods. First, we launched 200 runs of global optimization with use of the simulated annealing (SA) algorithm. Second, we fine-tuned the 50 best results with use of the interior point (IP) algorithm for local optimization. Some of the parameters in the vector p were optimized assuming logarithmic scale with base e. The optimization was carried out with use of MATLAB software (simulannealbnd and fmincon functions). <!-- text, from page 0 (l=0.053,t=0.724,r=0.480,b=0.856), with ID c7d9d80e-a3be-4a10-8805-0f9a97af0c42 -->

The IP algorithm is a local optimization method utilizing the
gradient of the target function. The gradient of J was obtained by
differentiation of the formula (3.21), which was possible because
we derived the explicit form of $s_{f_{iN}}^{r}(\mathbf{p})$. The sensitivity coefficients <!-- text, from page 0 (l=0.053,t=0.857,r=0.479,b=0.909), with ID 5f037c93-8a42-40ef-8f99-1a148a00acb6 -->

$\frac{\partial}{\partial p_n} \mathbf{x}(\mathbf{p}, T_j, t)$ resulting from the differentiation, and the solutions $\mathbf{x}$ themselves, were computed with use of the CVODES solver from <!-- text, from page 0 (l=0.053,t=0.911,r=0.479,b=0.940), with ID 398f5a5e-7a63-4869-9089-52beb7edc8ca -->

the SUNDIALS package (Hindmarsh et al., 2005), accessed from
MATLAB via the SUNDIALSTB interface. <!-- text, from page 0 (l=0.504,t=0.295,r=0.933,b=0.321), with ID 899cff17-ea9d-4f03-8165-09e98c95c730 -->

We would like to remark that the IP algorithm exhibited slow
progress and stopped due to either achieving maximal number of
iterations or a very short step. Hence, the 50 resulting sets of pa-
rameters may be suboptimal. Moreover, optimized values of some
parameters were close to the constraints in many optimization
runs, see Appendix E. Nevertheless, we subjected these results to
further examination, as described in Section 4. <!-- text, from page 0 (l=0.504,t=0.321,r=0.932,b=0.414), with ID b603a195-04b8-402c-8111-ee25c6f454ea -->

**4. Model selection and discussion**

_4.1. Fit selection based on temperature dependence in HSE:HSF$_3$ dissociation_ <!-- text, from page 0 (l=0.506,t=0.427,r=0.894,b=0.478), with ID dba9d893-89da-4680-bf2d-7a32cfd8fb84 -->

We considered 50 curve-fits resulting from the optimization
procedure described in Section 3.2 as candidates for further model
selection. In order to select the optimal model, we scrutinize the
biological relevance of the temperature dependence in the tran-
scriptional complexes HSE:HSF₃ dissociation rate constant I₁ᵀ. This
temperature dependence was defined without constraints on its
monotonicity nor number of extrema, potentially allowing non-
biological profiles. Therefore, we find the discrimination of I₁ᵀ pro-
files a reasonable selection criterion. <!-- text, from page 0 (l=0.505,t=0.493,r=0.932,b=0.610), with ID 3e84bd07-9e39-40db-9ef7-429ad2df1261 -->

We assume that the profiles exhibiting complex behaviour, i.e.
with several maxima or minima, are more likely to be biologi-
cally unreliable and just over-fitting results than simple profiles
with clear monotonicity. In none of the considered 50 fits a fully
monotone IT
      p profile was present, neither increasing nor decreas-
ing. However, in 10 fits, the profiles had one local minimum in
the temperature range 37–45 °C. These were the simplest obtained
profiles in the sense that the remaining profiles had more than
one minimum or maximum. We consider one-minimum profiles as
simple enough to be biologically plausible. Moreover, this kind of
temperature-dependent profile is characteristic for many complex
biological phenomena, as cellular respiration or enzymes activity.
We hence hypothesise that it may be the case for the stability of
HSE:HSF3, which is also maintained by a complex molecular mechan-
ism (see Section 2.1). Therefore, we subsequently limited our at-
tention to these 10 fits. <!-- text, from page 0 (l=0.506,t=0.611,r=0.932,b=0.820), with ID 315d6689-d6c6-422c-86f0-02c16942c330 -->

Interestingly, most of the 10 models with one-minimum ITj were
in a group of fits with best target function scores, see Fig. E.1 in
Appendix E. From these 10 alternative models, we choose the one
with the best score as the optimal model. Tables 1 and 3 present
the values of initial conditions and kinetic parameters for the se-
lected model, respectively. Fig. 2 presents the corresponding ITj
profile along with other temperature-dependent reaction rate con-
stants in the model. Fig. D.1 in Appendix D presents the fit of
model curves to all data used for parameter estimation. Below, in <!-- text, from page 0 (l=0.506,t=0.823,r=0.931,b=0.940), with ID f6f73f34-2427-465b-80a0-4bc7b2251af8 -->

G. Dudziuk, W. Wronowska and A. Gambin et al./Journal of Theoretical Biology 478 (2019) 74–101 <!-- marginalia, from page 0 (l=0.265,t=0.042,r=0.753,b=0.057), with ID ee073968-3338-44f7-8211-62a93e5d771c -->

81 <!-- marginalia, from page 0 (l=0.930,t=0.043,r=0.948,b=0.055), with ID 33d06186-521c-4222-805c-ef7a65e6c95f -->

Table 3  
Values of kinetic parameters of the model (2.1)–(2.12) and the total concentrations of conserved species in (3.11)–(3.13), obtained by parameter estimation described in Section 3.2. For those parameters which were subject to optimization constraints, range of values is given. <!-- text, from page 0 (l=0.170,t=0.068,r=0.847,b=0.115), with ID 1ad29667-b4b2-4d23-b709-fe9b6d7893ac -->

<table><thead><tr><th>Parameter</th><th>Description</th><th>Unit</th><th>In-text</th><th>Constraints</th><th>Value</th></tr></thead><tbody><tr><td>k₁</td><td>HSP:S association rate constant</td><td>μM⁻¹min⁻¹</td><td>(C.2.1)</td><td>2.7e-02 - 2.0e+04</td><td>1.260e+01</td></tr><tr><td>l₁</td><td>HSP:S dissociation rate constant</td><td>min⁻¹</td><td>(C.3.1)</td><td>0 - 1.27e+05</td><td>3.028e-03</td></tr><tr><td>k₂</td><td>HSP:HSF association rate constant</td><td>μM⁻¹min⁻¹</td><td>(C.1.1)</td><td>0 - 6.0e+05</td><td>2.180e-01</td></tr><tr><td>l₂</td><td>HSP:HSF dissociation rate constant</td><td>min⁻¹</td><td>(C11.1)</td><td>unconstrained</td><td>1.162e+00</td></tr><tr><td>k₃</td><td>HSF activation rate constant</td><td>μM⁻²min⁻¹</td><td>(B.8)</td><td>unconstrained</td><td>4.465e+05</td></tr><tr><td>l₃</td><td>HSF inactivation rate constant</td><td>μM⁻¹min⁻¹</td><td>(C.1.1)</td><td>0 - 6.0e+05</td><td>2.392e+00</td></tr><tr><td>k₄</td><td>Translation rate constant</td><td>min⁻¹</td><td>(C.7.2)</td><td>7.5e-01 - 5.0e+01</td><td>1.885e+01</td></tr><tr><td>k₅</td><td>Hsp70 mRNA degradation rate constant</td><td>min⁻¹</td><td>(C.4.1)</td><td>1.15e-04 - 2.31e-02</td><td>8.709e-04</td></tr><tr><td>k₆</td><td>Constitutive HSP production rate</td><td>min⁻¹</td><td>(C.8.1)</td><td>unconstrained</td><td>8.899e-02</td></tr><tr><td>k₇</td><td>HSE:HSF₃ association rate constant</td><td>μM⁻¹min⁻¹</td><td>(C.1.1)</td><td>0 - 6.0e+05</td><td>5.892e+03</td></tr><tr><td>l₇ᵖ(l₇,₃₇, l₇,₄₁,...,l₇,₄₅)</td><td>HSE:HSF₃ dissociation rate constant</td><td>min⁻¹</td><td>(C.9.1)</td><td>1.62e-02 - 1.62e+02</td><td>Fig. 2</td></tr><tr><td>l₇,₃₇</td><td>Auxiliary parameter for l₇ᵖ</td><td>min⁻¹</td><td>(C.9.1)</td><td>1.62e-02 - 1.62e+02</td><td>4.768e+01</td></tr><tr><td>l₇,₄₁</td><td>Auxiliary parameter for l₇ᵖ</td><td>min⁻¹</td><td>(C.9.1)</td><td>1.62e-02 - 1.62e+02</td><td>1.233e+00</td></tr><tr><td>l₇,₄₂</td><td>Auxiliary parameter for l₇ᵖ</td><td>min⁻¹</td><td>(C.9.1)</td><td>1.62e-02 - 1.62e+02</td><td>6.628e-01</td></tr><tr><td>l₇,₄₃</td><td>Auxiliary parameter for l₇ᵖ</td><td>min⁻¹</td><td>(C.9.1)</td><td>1.62e-02 - 1.62e+02</td><td>1.639e-02</td></tr><tr><td>l₇,₄₄</td><td>Auxiliary parameter for l₇ᵖ</td><td>min⁻¹</td><td>(C.9.1)</td><td>1.62e-02 - 1.62e+02</td><td>5.001e+01</td></tr><tr><td>l₇,₄₅</td><td>Auxiliary parameter for l₇ᵖ</td><td>min⁻¹</td><td>(C.9.1)</td><td>1.62e-02 - 1.62e+02</td><td>8.427e+01</td></tr><tr><td>k₈ᵖ(k₈ᵐᵃˣ, Rₖ₈, Tₖ₈)</td><td>Transcription rate constant</td><td>min⁻¹</td><td>(2.13)</td><td>unconstrained</td><td>Fig. 2</td></tr><tr><td>k₈ᵐᵃˣ</td><td>Auxiliary parameter for k₈ᵖ</td><td>min⁻¹</td><td>(2.13)</td><td>1.5e-02 - 1.5e+02</td><td>9.607e+01</td></tr><tr><td>Rₖ₈</td><td>Auxiliary parameter for k₈ᵖ</td><td>unitless</td><td>(2.13)</td><td>0.01 - 25.00</td><td>15.93</td></tr><tr><td>Tₖ₈</td><td>Auxiliary parameter for k₈ᵖ</td><td>°C</td><td>(2.13)</td><td>35.0 - 50.0</td><td>42.89</td></tr><tr><td>k₉</td><td>HSP degradation rate constant</td><td>min⁻¹</td><td>(C.5.1)</td><td>1.16e-04 - 5.02e-03</td><td>1.888e-03</td></tr><tr><td>k₁₀</td><td>Proteins refolding rate constant</td><td>min⁻¹</td><td>(C.6.1)</td><td>0 - 1.27e+05</td><td>9.813e-02</td></tr><tr><td>k₁₁ᵖ(k₁₀, Vₚᵈᵉₙᵀ)</td><td>Proteins denaturation rate constant</td><td>min⁻¹</td><td>(2.14)</td><td>> 0 at T = 37°C</td><td>Fig. 2</td></tr><tr><td>T₀</td><td>Auxiliary parameter for Vₚᵈᵉₙᵀ</td><td>°C</td><td>(2.17)</td><td>30.00 - 36.99</td><td>35.81</td></tr><tr><td>T₀.₅</td><td>Auxiliary parameter for Vₚᵈᵉₙᵀ</td><td>°C</td><td>(2.17)</td><td>37.01 - 62.00</td><td>47.13</td></tr><tr><td>nᵥ</td><td>Auxiliary parameter for Vₚᵈᵉₙᵀ</td><td>unitless</td><td>(2.17)</td><td>1.0 - 100.0</td><td>6.522</td></tr><tr><td>Pₜₒₜ</td><td>Total denaturation-susceptible proteins</td><td>μM</td><td>(C.17.1)</td><td>7.67e+02 - 3.07e+03</td><td>1.297e+03</td></tr><tr><td>HSFₜₒₜ</td><td>Total heat shock factor 1</td><td>μM</td><td>(C.18.1)</td><td>1.56e-02 - 2.44e-02</td><td>1.568e-02</td></tr><tr><td>HSEₜₒₜ</td><td>All heat shock elements</td><td>μM</td><td>(C.19.1)</td><td>4.00e-06 - 4.00e-06</td><td>4.00e-06</td></tr></tbody></table> <!-- table, from page 0 (l=0.173,t=0.117,r=0.844,b=0.482), with ID 94095d67-cd1c-488f-ba72-bb448260f18f -->

Table 4
Summary of notation used in the description of the parameter estimation problem in Section 3.2. The column "Dim/No." presents the dimensionality of particular vectors or functions; and numbers of data series and data points. The column "In-text" provides cross-references to locations in the text presenting more detailed specifications of components underlying particular symbols.

<table><thead><tr><th>Symbol</th><th>Description</th><th>Dim/No.</th><th>In-text</th></tr></thead><tbody><tr><td>x</td><td>Vector of species of the model; x = x(t)</td><td>10</td><td>Table 1</td></tr><tr><td>x₀</td><td>Vector of initial conditions of x, i.e. x0</td><td>10</td><td>Table 1</td></tr><tr><td>k<sup>T</sup></td><td>Vector of kinetic parameters of the model</td><td>15</td><td>Table 3</td></tr><tr><td>q</td><td>Vector of parameters of parametrization</td><td>18</td><td>Appendix B</td></tr><tr><td>p</td><td>Vector of directly optimized parameters</td><td>27</td><td>Table C.1</td></tr><tr><td>s</td><td>Vector of scale factors</td><td>13</td><td>Table 2</td></tr><tr><td>J</td><td>Number of data series</td><td>19</td><td>Table 2</td></tr><tr><td>K<sub>j</sub></td><td>Number of data points in each series</td><td>from 2 to 14</td><td>Table 2</td></tr><tr><td>ỹ<sub>j,k</sub></td><td>Data points; j = 1,...,J, k = 1,...,K<sub>j</sub></td><td>total: 127</td><td>Table 2</td></tr><tr><td>C</td><td>Nonlinear inequality constraints function</td><td>C : ℝ<sup>27</sup> → ℝ<sup>17</sup></td><td>Table C.2</td></tr><tr><td>J₀</td><td>Target function</td><td>J₀ : ℝ<sup>27</sup> × ℝ<sup>13</sup> → ℝ</td><td>(3.16)</td></tr><tr><td>J</td><td>Target function</td><td>J : ℝ<sup>27</sup> → ℝ</td><td>(3.21)</td></tr></tbody></table> <!-- table, from page 0 (l=0.262,t=0.504,r=0.754,b=0.730), with ID 8578e4a5-d50c-4296-8daf-787d64b853db -->

Section 4.2, we select and discuss some of the fitting results and model predictions. <!-- text, from page 0 (l=0.068,t=0.751,r=0.497,b=0.781), with ID a18e937e-9d76-4756-9da6-b585af2d10fa -->