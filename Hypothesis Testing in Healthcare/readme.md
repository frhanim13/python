<h1>Hypothesis Testing in Healthcare: Drug Safety</h1>

The dataset drug_safety.csv was obtained from Hbiostat courtesy of the Vanderbilt University Department of Biostatistics. It contained five adverse effects: headache, abdominal pain, dyspepsia, upper respiratory infection, chronic obstructive airway disease (COAD), demographic data, vital signs, lab measures, etc. The ratio of drug observations to placebo observations is 2 to 1.

<h1>Goals </h1>

1)Determine if the proportion of adverse effects differs significantly between the Drug and Placebo groups, saving the p-value as a variable called two_sample_p_value.

2)Find out if the number of adverse effects is independent of the treatment and control groups, saving as a variable called num_effects_p_value containing a p-value.

3)Examine if there is a significant difference between the ages of the Drug and Placebo groups, storing the p-value of your test in a variable called age_group_effects_p_value.
<H1>Result</H1>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/a3b1fede-e5da-4b93-94f0-b84b796b53a2" />

**1. Proportion of Adverse Effects Between Drug and Placebo Groups**

1. A high p-value like 0.9639 suggests that the observed proportions of adverse effects between the Drug and Placebo groups are very similar.

2. This result suggests that the drug under investigation does not significantly alter the likelihood of experiencing adverse effects compared to the placebo.

3. For the pharmaceutical company (GlobalXYZ), this could indicate that the drug is generally safe concerning the adverse effects measured in this study.

**2. Independence of Number of Adverse Effects and Treatment Groups** <br>
 num_effects_p_value= 0.6150
 
1. The number of adverse effects appears to be similar across the Drug and Placebo groups.
This suggests that taking the drug does not significantly increase or decrease the likelihood of experiencing multiple adverse effects compared to taking the placebo.

2. If the drug does not cause more adverse effects than the placebo, this supports the safety of the drug.
However, other safety metrics (e.g., severity of effects, long-term outcomes) should also be considered.

3. A high p-value does not confirm that the drug has no adverse effects; it only suggests that any observed differences in the number of adverse effects are likely due to random variation.
Further studies with larger sample sizes might be necessary to detect smaller effects, if any.

**3.Difference in Ages Between Drug and Placebo Groups** <br>
age_group_effects_p_value = 0.2569 (from Mann-Whitney U test)

1. Participants in the Drug and Placebo groups likely have a similar age distribution.
This is an important finding because it suggests that the randomization process was effective in equally distributing ages across both groups.

2. In RCTs, it's crucial to have balanced demographics (like age) to ensure that any differences in outcomes are due to the treatment and not confounding variables.
Since there is no significant age difference, we can be more confident that the trial outcomes won't be biased by age-related factors.

3. If certain adverse effects or outcomes are age-dependent, a lack of significant age differences ensures that these effects won't disproportionately affect one group over the other.
This result supports the fairness and reliability of the trial.





 




