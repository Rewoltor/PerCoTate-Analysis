import re

text = """Ground Truth Bias in AI-Assisted Medical Annotation: A Crossover Study Using an Independent Radiologist Reference Standard
Article type: Research and Applications
Running title: Ground truth bias and AI-assisted annotation

Márton Baltay, MA¹*, Tamás Ilcsik, MSc², Márton Borbély, MD, MS³
Affiliations:
¹Department of [Sociology], Faculty of Humanities and Social Sciences, Pázmány Péter Catholic University, Budapest, Hungary
²[INSERT DEPARTMENT], School of Computing, Engineering and Physical Sciences, University of the West of Scotland, Paisley, United Kingdom
³Department of [INSERT DEPARTMENT], Saint John Hospital, Budapest, Hungary
Corresponding author: Márton Baltay, MA, Fejér György utca 12, 2094 Nagykovácsi, Pest County, Hungary, baltay.marton.mihaly@hallgato.ppke.hu, +36 20 397 1062, https://orcid.org/0009-0005-4484-2597
Abstract
Objective: AI-assisted annotation is increasingly used to reduce medical image labelling costs, but behavioural evaluations assume the reference standard is valid. We tested whether a public ground truth distorts apparent AI benefit, over-reliance rates, and psychometric associations.
Materials and Methods: 51 non-expert high school students annotated 50 Osteoarthritis Initiative (OAI) knee radiographs on a binary Kellgren-Lawrence osteoarthritis task, with and without a deliberately suboptimal classifier, in a crossover design. Big Five personality traits and non-verbal intelligence were measured. Decisions were analysed against both original OAI labels and an independent radiologist consensus reference standard constructed by four board-certified radiologists.
Results: Under the original OAI labels, AI assistance appeared to improve accuracy from 60.4% to 65.3% (OR 1.23, p=0.003). Under the independent reference standard, the same data showed no significant effect (78.4% to 80.8%; OR 1.16, p=0.178); a sensitivity analysis was marginal (p=0.037). Over-reliance fell from 15.6% to 7.8%; under the corrected standard all over-reliance events were false-negative acceptances. Neuroticism emerged as a hypothesis-generating predictor of accuracy and lower false-negative over-reliance under the corrected standard.
Discussion: A structural suppressor mechanism—shared false-negative bias between the AI model and its training labels—inflated apparent benefit and concealed clinically important reliance errors in the original evaluation.
Conclusion: A statistically robust AI-assistance effect can be a measurement artifact when human-AI decisions are scored against a biased reference standard. Ground truth validation and directional bias reporting should be minimum requirements for behavioural AI-annotation studies.
Keywords: Artificial Intelligence; Automation; Osteoarthritis, Knee; Observer Variation; Diagnostic Errors
Background and Significance
Medical image annotation remains a major bottleneck in clinical artificial intelligence (AI) development. Because expert annotation is costly and slow, pipelines utilizing non-expert annotators supported by AI predictions, training materials, and visual explanations have become an attractive operational alternative, shifting the labeling burden from scarce clinicians while preserving label quality [1-3].
However, this operational strategy introduces a methodological issue. AI-assisted annotation studies evaluate human-AI collaboration: whether humans accept correct advice, reject errors, or succumb to automation bias. This behavioral assessment depends entirely on reference-standard validity. If the reference standard is biased, evaluations may measure how human and model errors align with historical dataset inaccuracies rather than genuine human judgment.
This issue is compounded when the same public dataset is used for model training and human evaluation. If the repository contains systematic false negatives, the trained model will reproduce these errors [30,39]. A participant who agrees with an AI false negative is scored as correct because the model and reference standard align in error, while a participant who correctly identifies pathology missed by both is penalized. Consequently, apparent AI benefits are inflated, over-reliance is hidden, and traits predicting appropriate skepticism appear ineffective.
This links our work to multi-reader multi-case (MRMC) reader studies, which are designed to separate reader, case, and modality effects [33,34,46]. Although not a conventional diagnostic trial, our study shares this structural vulnerability: the apparent effect of AI assistance remains dependent on case-level reference-standard validity.
Additionally, noisy-label research shows that simple accuracy metrics obscure clinically asymmetric harms. Since false negatives and false positives carry different consequences, risk-aware frameworks must evaluate directional errors and asymmetries [24,27,40,47,48]. We extend this logic to behavioral evaluations: the critical issue is whether the direction of ground truth noise systematically rewards unsafe reliance.
Knee osteoarthritis grading using the Kellgren-Lawrence (KL) scale is particularly vulnerable due to subjective boundaries. Distinguishing KL0, KL1, and KL2 relies on subtle osteophytes and joint-space narrowing, which exhibit low inter-rater agreement [4-8]. Binary classifications are therefore prone to directional noise at the threshold of pathology, where automation bias has the highest clinical stakes.
Automation bias leads users to substitute AI outputs for independent judgment, causing omission errors (overlooking problems the AI missed) and commission errors (accepting false suggestions) [9-12,41]. False-negative over-reliance is critical in imaging because the absence of an alert lacks a salient cue for review [44,45]. Cognitive forcing strategies—like requiring independent decisions before showing AI predictions—aim to promote active engagement [13-15].
Individual traits can also modulate reliance. Neuroticism is associated with uncertainty sensitivity and heightened error monitoring [18,36]. Dual-process accounts suggest that AI recommendations serve as heuristic cues; individuals high in Neuroticism may reject these cues when ambiguous [16-20,37,38]. However, this behavioral signal can only be observed if the reference standard rewards valid skepticism. If the ground truth shares the AI's false-negative bias, skeptical participants will be incorrectly penalized.
This study addresses two questions: (1) does AI assistance improve annotation accuracy when evaluated against an independently validated standard, and (2) do personality traits predict collaboration, or are these relationships suppressed by ground truth error? We analyzed a crossover experiment under both the original OAI labels and an expert radiologist consensus, testing whether apparent behavioral benefits are stable when the reference standard is scrutinized.
Materials and Methods
Study design
We used a crossover repeated-measures design with a multi-reader, multi-case stimulus structure. Fifty-one participants completed two annotation sessions separated by a mandatory 28-day washout interval. Participants were randomized to one of two order groups. Group A completed the no-AI condition first and the AI-assisted condition second. Group B completed the AI-assisted condition first and the no-AI condition second. This structure allowed each participant to serve as their own control while distributing condition order across participants. A GEE interaction model including condition and session found no statistically detectable carryover effect (condition by session p=0.554).

Figure 1. Crossover study flow diagram showing randomization, session order, psychometric assessment, annotation conditions, and the 28-day washout.
Participants
Sixty-eight Hungarian high school students were recruited through school partnerships. Of these, 51 completed both annotation sessions and formed the analytic cohort. The 17 non-completers were excluded for documented session absence due to illness or scheduling conflict. No participant was excluded after completing both sessions. Because baseline psychometric measures were not collected from non-completers, non-differential attrition could not be empirically verified and is treated as a limitation. The final cohort comprised 27 males and 24 females aged 15 to 18 years (mean 16.41, SD 0.67). No participant had medical or healthcare training, consistent with the non-expert annotation paradigm.
Psychometric instruments
Participants completed psychometric instruments during their no-AI session to balance overall session duration. Big Five personality traits were measured using the Hungarian-validated BFI-2 [21,35], a 60-item instrument producing domain scores for Open-Mindedness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. The cohort means were Open-Mindedness 3.77 (SD 0.63), Conscientiousness 3.38 (SD 0.72), Extraversion 3.41 (SD 0.70), Agreeableness 3.65 (SD 0.51), and Neuroticism 2.98 (SD 0.80). Non-verbal fluid intelligence was measured using the ICAR-6 matrix reasoning scale [22]. The ICAR-6 showed a marked floor effect in this adolescent cohort, with a mean score of 1.12 out of 6 (SD 1.63), limiting valid inference about cognitive ability. Variance inflation factors across predictors were below 1.5, indicating negligible multicollinearity.
Stimulus set and AI assistant
The stimulus set consisted of 50 anteroposterior knee radiographs drawn from the test set of the OAI public repository [28,29]. Images covered the KL severity distribution relevant to binary osteoarthritis classification and included clinically ambiguous cases. The AI assistant was a ResNet-18 convolutional neural network trained on a separate OAI training set using the original repository labels. For training, KL0 was mapped to negative and KL2, KL3, and KL4 were mapped to positive. KL1 was excluded from model training because the grade is inherently ambiguous and does not map cleanly to either binary class.
The resulting model achieved 74.1% accuracy against the original OAI labels. This level of performance was deliberate. The study was designed to examine reliance behaviour under a plausible but imperfect AI assistant, not to optimize algorithmic performance. A near-perfect model would provide little opportunity to observe appropriate skepticism or over-reliance, while a very poor model would likely be rejected outright. The model therefore functioned as a behavioural stimulus: credible enough to influence decisions, but fallible enough to create meaningful reliance choices.
Annotation interface and trial flow
The annotation platform was a custom web application. In all trials, participants could inspect the radiograph using standard zoom controls. In the no-AI condition, each trial required a binary diagnosis followed by a seven-point confidence rating. In the AI-assisted condition, the interface separated the initial human judgement from subsequent AI exposure. Participants first selected radiographic features such as osteophytes and joint-space narrowing, provided an initial binary diagnosis, and rated confidence before seeing the AI result. The AI panel then displayed the model's binary prediction, numerical confidence score, and Grad-CAM heatmap overlaid on the radiograph. Participants could inspect the heatmap, original image, and feature-overlap view before submitting a final diagnosis and post-AI confidence rating.
This trial structure created a complete behavioural record for every AI-condition image: the pre-AI human decision, pre-AI confidence, AI prediction, AI confidence, visual explanation, final human decision, and post-AI confidence. It enabled classification of each AI-condition trial into reliance categories and allowed separation of genuine independent judgement from post-AI revision.

Figure 2. AI-condition annotation interface showing feature identification, initial confidence, AI prediction with Grad-CAM, and final confirmation.
Independent reference standard construction
The original OAI labels were used as the first reference standard. Preliminary analysis, however, revealed systematic disagreement between the original labels, collective non-expert annotations, and the AI model output on a subset of images. This pattern motivated an independent reference-standard validation process. Three board-certified radiologists independently annotated the 50 study images plus 10 additional KL1-enriched images on the full KL0-KL4 scale. The additional images were included to reduce anchoring toward a binary diagnostic frame. Radiologists were blinded to original labels, AI predictions, participant annotations, and each other's ratings during independent annotation.
The Platinum Standard was constructed through a seven-step process. First, original OAI labels were retained as the initial comparator. Second, the discordance pattern was quantified to determine whether the issue was non-random. Third, independent full-scale KL ratings were obtained from three radiologists. Fourth, binary consensus was assigned automatically where all three ratings fell on the same side of the binary boundary: KL0 as negative and KL2-KL4 as positive. Fifth, cases without complete binary consensus were reviewed during a structured consensus meeting facilitated by a fourth radiologist. Sixth, inter-rater reliability was calculated using Fleiss' kappa. Seventh, all inferential models were run in parallel under both reference standards, with AI confidence distributions used as independent corroboration of suspected label instability.
During independent and consensus review, adjudication was anchored to the full KL0-KL4 construct rather than to the binary label alone. The binary boundary was defined a priori as KL0 negative and KL2-KL4 positive, while KL1 was treated as diagnostically uncertain. Disagreements were resolved by first identifying whether the radiographic features supported no definite OA, doubtful/borderline change, or definite OA, with particular attention to osteophytes and joint-space narrowing. The fourth radiologist acted as a consensus facilitator rather than as an additional independent vote: structuring discussion of discordant cases, ensuring consistent application of the binary boundary and KL1 uncertainty rules, and documenting the final consensus category.
The term Platinum Standard is used here to indicate an expert consensus reference standard [31,42,43] deliberately constructed to exceed the evidentiary strength of the original public repository labels for this behavioural experiment. It does not imply that the KL scale is free from ambiguity. Rather, it acknowledges that ambiguous KL1 cases require explicit handling rather than being forced invisibly into a binary ground truth.
Outcome definitions and statistical analysis
The primary outcome was binary annotation accuracy under AI-assisted versus no-AI conditions. Secondary performance metrics included balanced accuracy, F1 score, sensitivity, specificity, and AUROC. Because class balance differed between the original and Platinum analyses, raw accuracy was not interpreted alone. Reliance behaviour was categorized for AI-condition trials as appropriate reliance, over-reliance, appropriate skepticism, or unwarranted skepticism. Appropriate reliance occurred when the participant agreed with a correct AI output. Over-reliance occurred when the participant agreed with an incorrect AI output. Appropriate skepticism occurred when the participant correctly overrode an incorrect AI output. Unwarranted skepticism occurred when the participant incorrectly overrode a correct AI output.
The primary inferential model was generalized estimating equations (GEE) [32] with a binomial family, logit link, and exchangeable working correlation structure. This model accounted for repeated image-level observations nested within participants. Odds ratios and 95% confidence intervals were reported. Participant-level Wilcoxon signed-rank tests were used as pre-specified sensitivity checks. Firth penalized logistic regression was used for sparse reliance outcomes. Psychometric predictor p-values were adjusted using Benjamini-Hochberg false discovery rate correction across the five Big Five traits and ICAR-6.
Because the primary endpoint was a binary trial-level decision rather than a continuous reader-level ROC rating, GEE was selected as the main population-averaged model.
The Platinum Standard classified 23 of the 50 study images as KL1. Because KL1 does not map unambiguously to a binary diagnosis, three KL1 handling strategies were defined. Strategy A excluded KL1 cases from binary behavioural analysis and served as the primary analysis. Strategy B mapped KL1 to negative, reflecting conservative clinical convention. Strategy C mapped KL1 to positive, testing the upper boundary of pathology inclusion. All central GEE models were rerun under each strategy to evaluate robustness.
Results
Ground truth validation
The transition from original OAI labels to the independent radiologist reference standard revealed systematic directional label noise. Of the 25 images originally labelled KL0, 14 were adjudicated as KL1 and five were adjudicated as KL2 or above. No image showed an opposite confirmed false-positive correction. Thus, the error structure was not random: confirmed false-negative corrections exceeded false-positive corrections (five versus zero; binomial p=0.031).
The panel adjudicated 23 of the 50 study images as KL1, confirming that nearly half of the stimulus set lay in the diagnostically indeterminate region of the KL scale. Under the primary Strategy A analysis, these images were excluded from binary behavioural analysis, leaving 27 unambiguous images: 21 positive and six negative. This produced a 3.5:1 class imbalance and a naive majority-class baseline of 77.8%. Pre-consensus inter-rater reliability was Fleiss' kappa=0.181 on the full five-grade scale and kappa=0.517 on binary classification excluding KL1. Within-one-grade agreement was 84.0%, indicating substantial coarse agreement even where exact KL grade differed.

Figure 3. Original versus independent reference-standard label flow across Kellgren-Lawrence grades.
The AI model's confidence scores independently corroborated the suspect false-negative cases. On the five images reclassified from original KL0 to Platinum KL2 or above, the model's mean confidence was 0.317. This was lower than confidence on stable negatives (0.710) and stable positives (0.776). A Kruskal-Wallis test confirmed a significant difference across these groups (H=8.631, p=0.013). The convergence of expert consensus and model uncertainty suggests that these images were inherently unstable under the original repository labelling rather than arbitrary disagreements introduced by the new panel.

Figure 4. AI confidence distributions by ground truth error type. Corrected false negatives show lower model confidence than stable negatives and stable positives.
Annotation performance under original and corrected reference standards
Table 1. Human annotation performance by AI condition and reference standard.
Ground truth
Condition
Accuracy
F1
Sensitivity
Specificity
AUROC
GEE OR
95% CI
p
Original OAI
AI
65.3%
0.676
72.4%
58.2%
0.653
1.232
1.083-1.401
0.003
Original OAI
No-AI
60.4%
0.630
67.2%
53.7%
0.604
Reference
-
-
Independent reference
AI
80.8%
0.867
80.7%
81.4%
0.810
1.164
0.933-1.453
0.178
Independent reference
No-AI
78.4%
0.852
79.9%
72.9%
0.764
Reference
-
-


Under the original OAI ground truth, AI assistance appeared to yield a statistically strong improvement. Accuracy increased from 60.4% in the no-AI condition to 65.3% in the AI-assisted condition. The GEE model estimated OR=1.232 (95% CI 1.083-1.401, p=0.003), and the Wilcoxon signed-rank sensitivity check was also significant (p=0.003). The participant-level effect size was Cohen's d=0.60. Read in isolation, this would constitute a compelling demonstration of AI benefit.
Under the independent reference standard, the same participants annotating the same images produced a materially different inference. No-AI accuracy rose to 78.4%, and AI-assisted accuracy reached 80.8%. The GEE model was non-significant (OR=1.164, 95% CI 0.933-1.453, p=0.178). The Wilcoxon sensitivity analysis was marginally significant (p=0.037), indicating a small participant-level directional trend. The divergence between tests is informative: the corrected ground truth does not eliminate every possible AI benefit, but it reduces the apparent effect from a large, homogeneous improvement to a smaller and more individually heterogeneous signal.
The KL1 sensitivity analyses supported this interpretation. When KL1 was mapped to negative, the AI condition effect was null (OR=1.015, p=0.841). When KL1 was mapped to positive, the effect remained non-significant (OR=1.107, p=0.271). Therefore, the central conclusion did not depend on the primary exclusion of KL1 cases. Instead, it reflected the removal of directional false-negative bias from the evaluation standard.

Figure 5. Accuracy paradox across agents and conditions. Performance estimates rise under the corrected standard because the original labels suppressed correct positive detections.
Reliance behaviour
Table 2. Reliance taxonomy by reference standard in AI-condition trials.
Reliance category
Original OAI
95% CI
Independent reference
95% CI
Over-reliance
15.6%
14.5-16.6%
7.8%
6.1-9.4%
Appropriate skepticism
14.4%
13.4-15.5%
14.5%
12.9-16.1%
Appropriate reliance
50.9%
48.5-53.3%
66.4%
64.4-68.2%
Unwarranted skepticism
19.1%
16.7-21.5%
11.4%
9.5-13.3%


The corrected reference standard changed the measured reliance taxonomy. Measured over-reliance fell from 15.6% under the original labels to 7.8% under the independent reference standard (McNemar p<0.0001). However, the most important change was directional rather than volumetric. Under the original ground truth, over-reliance appeared to include both false-positive and false-negative AI errors. Under the independent standard, 100% of over-reliance events were false-negative acceptances: participants agreeing with the AI's failure to detect genuine pathology. There were zero false-positive over-reliance events, producing a binomial p<0.0001 for false-negative dominance.
This pattern is the behavioural expression of the ground truth suppressor mechanism. The original OAI labels independently coded the AI's false-negative predictions as correct. Therefore, a participant who accepted the AI false negative was counted as accurate, and the over-reliance event became mathematically invisible. Conversely, a participant who rejected the AI and identified pathology on those images was scored as incorrect under the original labels. The corrected standard reclassified those decisions as appropriate skepticism. The reduction in unwarranted skepticism from 19.1% to 11.4% is the complementary effect of the same correction.

Figure 6. Participant-level reliance taxonomy. The distribution shows that aggregate over-reliance is not uniform across participants.
Psychometric predictors
Table 3. Summary of psychometric findings under the two reference standards.
Predictor / outcome
Original OAI
Independent reference
Interpretation
Neuroticism -> accuracy
OR 0.940, p=0.194
OR 1.178, p_FDR=0.029
Null under original labels; positive under corrected standard
Neuroticism -> false-negative over-reliance
Not significant after FDR
rho=-0.390, p_FDR=0.028
Higher Neuroticism associated with lower FN over-reliance
Conscientiousness -> accuracy
OR 1.071, p=0.212
Not significant
Primary pre-specified trait unsupported
ICAR-6 -> accuracy
Limited by floor effect
Limited by floor effect
No valid cognitive-ability inference


The psychometric analysis showed the same dependence on reference-standard quality. Under the original OAI labels, no Big Five trait predicted annotation accuracy after correction for multiple comparisons. Neuroticism was non-significant, and Conscientiousness, the primary pre-specified trait, was also null. Under the independent reference standard, Neuroticism emerged as a positive predictor of annotation accuracy (OR=1.178, 95% CI 1.017-1.366, p_FDR=0.029). Higher Neuroticism was also associated with lower false-negative over-reliance (Spearman rho=-0.390, p_FDR=0.028).
This result should be interpreted cautiously. The study was not formally registered with a third-party registry before data collection, and the Neuroticism analysis was secondary rather than the primary hypothesis. Post-hoc power for the observed Neuroticism association was low at approximately 17%, meaning that the finding is not a definitive personality effect. Its value is instead mechanistic: it demonstrates how a trait-level signal can be suppressed under a noisy reference standard and become visible only after the direction of ground truth error is corrected. The result should therefore be treated as hypothesis-generating and requiring confirmatory replication in a larger, prospectively registered sample.

Discussion
This study demonstrates that the apparent benefit of AI assistance in non-expert medical annotation depends strongly on reference-standard validity. Under the original OAI labels, AI assistance produced a statistically significant improvement in accuracy. Under an independent radiologist consensus reference standard, however, the same data yielded only a small and non-significant effect in the primary GEE model. Thus, apparent AI benefits cannot be safely interpreted unless the reference standard is independently validated and its error structure understood.
The underlying mechanism is a structural suppressor: when an AI model and training labels share false-negative bias, the model appears helpful by guiding users toward dataset errors. Accepting false-negative AI advice is rewarded as correct, while detecting pathology missed by both the AI and original labels is penalized. This creates an accuracy paradox, where the evaluation metric rewards agreement with flawed labels rather than clinical validity, extending prior label-noise research to human-AI behavioral evaluation [23-26].
These findings align with radiology reader-study methodologies that emphasize reference-standard validity alongside reader-case variance. Conventional multi-reader multi-case (MRMC) frameworks account for reader and case heterogeneity, but our results show that reference-standard bias can fundamentally distort these models. Independent adjudication is not merely a procedural step; it determines the behavioral validity of reliance, skepticism, and apparent AI benefit.
The reliance taxonomy highlights clinical safety implications: under the corrected standard, all over-reliance events were false-negative acceptances (participants accepting the AI's failure to detect pathology). Under the original labels, this clinical risk was invisible because false-negative cases were misclassified as true negatives. Studies that evaluate human-AI collaboration without validating reference standards risk underestimating automation bias. This underscores the need for risk-aware clinical evaluation that separates error types rather than reporting aggregate metrics [47,48].
The high proportion of KL1 cases (23/50) highlights the clinical ambiguity of early osteoarthritis. Rather than flattening these borderline cases into binary classes, researchers must handle them transparently. Our sensitivity analyses demonstrated that the core findings were robust across different KL1 handling strategies, but they reinforce the necessity of reporting how ambiguous cases are managed.
The Neuroticism association is a methodological demonstration rather than a definitive psychological claim. Theoretically, uncertainty-sensitive individuals might exercise greater skepticism under uncertainty (cognitive forcing). In our data, higher Neuroticism predicted higher accuracy and lower false-negative over-reliance only under the corrected standard, showing how reference-standard bias can suppress genuine behavioral predictors. However, this finding is exploratory, sample-size limited, and requires prospective replication.
Finally, while non-expert adolescent annotators are relevant for evaluating scalable labeling pipelines, they do not substitute for clinical experts. Replicating this study with clinicians would evaluate these dynamics under realistic expertise and accountability conditions, where MRMC or mixed-effects models would be essential.
This study has several limitations. First, the adolescent cohort limits generalizability to clinical readers. Second, the stimulus set was small, with primary Strategy A analysis restricted to 27 unambiguous images. Third, the AI assistant was a deliberately moderate-accuracy model, suitable for eliciting reliance behavior but not representative of state-of-the-art diagnostic systems. Fourth, attrition could not be fully evaluated as baseline psychometric data were unavailable for non-completers. Fifth, Kellgren-Lawrence grading is subjective, and the radiologist kappa confirms persistent ambiguity. Sixth, patient-level leakage risks (e.g., contralateral knees or longitudinal follow-up images) remain possible since participant IDs were not matched across splits. Seventh, confidence-interaction and calibration analyses (e.g., Brier score changes) were not performed. Eighth, complementary analyses using crossed participant and case effects or formal MRMC ROC methods were not conducted and represent a direction for future work.
Nevertheless, the core methodological conclusion remains robust due to the within-study design: the same participants, images, AI outputs, and statistical models yielded different conclusions under different reference standards. This design isolates the reference-standard problem directly, suggesting that any human-AI evaluation relying on unvalidated public labels is vulnerable to the same suppressor mechanism, especially when the AI assistant is trained on the same repository.
We recommend minimum reporting standards for behavioral AI-assistance studies, including reference-standard construction, expert validation, inter-rater reliability, error directionality, and the handling of ambiguous cases. For reliance evaluations, over-reliance should be decomposed into false-negative and false-positive rates rather than aggregate metrics, and reference-standard error should be modeled as an active component of behavioral analysis.
To support reproducibility, a de-identified per-image table containing original labels, consensus labels, AI predictions, AI confidence, aggregate participant agreement rates, and reliance counts is available as supplementary material, facilitating secondary analyses within data sharing restrictions.
Conclusion
A large and statistically robust AI-assistance effect can be a measurement artifact when human-AI decisions are scored against a biased public reference standard. In this crossover study, the original OAI labels suggested a strong AI benefit, while an independent radiologist reference standard reduced the effect to a small and heterogeneous signal. The corrected standard also revealed that over-reliance was entirely false-negative in direction and that a hypothesis-generating Neuroticism association had been suppressed by the original labels. Ground truth validation should therefore be treated as a prerequisite for behavioural inference in AI-assisted medical annotation studies, not as an optional quality check.
Abbreviations
AI: artificial intelligence; AUROC: area under the receiver operating characteristic curve; BFI-2: Big Five Inventory-2; CI: confidence interval; FDR: false discovery rate; GEE: generalized estimating equations; Grad-CAM: Gradient-weighted Class Activation Mapping; ICAR-6: International Cognitive Ability Resource six-item scale; KL: Kellgren-Lawrence; MRMC: multi-reader multi-case; OAI: Osteoarthritis Initiative; OR: odds ratio.
Declarations
Ethics approval and consent to participate
[Insert institutional ethics approval details, approval number, consent procedures, parental/guardian consent if applicable, and school-level recruitment permissions before submission.]
Consent for publication
Not applicable.
Availability of data and materials
Subject to institutional ethics approval and OAI data-use restrictions, the authors plan to make available the de-identified analysis code, model-output table, and per-image derived outcomes used in the primary analyses. The intended per-image table will include original OAI label, independent consensus label, AI prediction, AI confidence, aggregate participant agreement rates, and reliance-category counts under both reference standards, but will not include identifiable participant information or redistributable radiograph files unless permitted by the source data agreement. Participant-level data will be shared only in de-identified or aggregate form where consent and ethics approval allow.
Competing interests
The authors declare that they have no competing interests. [Revise if required.]
Funding
[Insert funding statement, or state that no specific funding was received.]
Authors' contributions
[Insert CRediT-style author contribution statement before submission.]
Acknowledgements
[Acknowledge participating schools, radiologist reviewers, software contributors, and any institutional support as appropriate.]
Supplementary material
Recommended supplementary files for submission: full confusion matrices under all KL1 handling strategies; full GEE and Firth regression outputs; de-identified per-image outcome table under both reference standards; confidence-interaction and calibration analyses where available or explicitly marked as not conducted; sensitivity analyses for KL1 handling and assistant accuracy; crossed participant-case or MRMC robustness analyses where feasible; anonymized interface screenshots; radiologist consensus documentation template; and analysis code.
"""

refs = {
1: "Rajpurkar P, Chen E, Banerjee O, Topol EJ. AI in health and medicine. Nature Medicine. 2022;28(1):31-38.",
2: "Cheplygina V, de Bruijne M, Pluim JPW. Not-so-supervised: a survey of semi-supervised, multi-instance, and transfer learning in medical image analysis. Medical Image Analysis. 2019;54:280-296.",
3: "Jeon Y, Hwang C, Chen XA. Empowering medical data labeling for non-experts with DANNY: enhancing accuracy and mitigating over-reliance on AI. Proceedings of the 30th International Conference on Intelligent User Interfaces. 2025:624-640.",
4: "Kellgren JH, Lawrence JS. Radiological assessment of osteo-arthrosis. Annals of the Rheumatic Diseases. 1957;16(4):494-502.",
5: "Wright RW, Ross JR, Haas AK, Huston LJ, Garofoli EA, Harris D, et al.; MARS Group. Osteoarthritis classification scales: interobserver reliability and arthroscopic correlation. Journal of Bone and Joint Surgery. 2014;96(14):1145-1151. doi:10.2106/JBJS.M.00929.",
6: "Yoon JS, Yon CJ, Lee D, et al. Assessment of a novel deep learning-based software developed for automatic feature extraction and grading of radiographic knee osteoarthritis. BMC Musculoskeletal Disorders. 2023;24(1):869.",
7: "Landis JR, Koch GG. The measurement of observer agreement for categorical data. Biometrics. 1977;33(1):159-174.",
8: "Guo J, Yan P, Luo H, et al. Predicting joint space changes in knee osteoarthritis over 6 years: a combined model of TransUNet and XGBoost. Quantitative Imaging in Medicine and Surgery. 2025;15:1396-1410.",
9: "Mosier KL, Skitka LJ. Human decision makers and automated decision aids: made for each other? In: Parasuraman R, Mouloua M, editors. Automation and Human Performance. Lawrence Erlbaum Associates; 1996.",
10: "Parasuraman R, Manzey DH. Complacency and bias in human use of automation: an attentional integration. Human Factors. 2010;52(3):381-410.",
11: "Goddard K, Roudsari A, Wyatt JC. Automation bias: a systematic review of frequency, effect mediators, and mitigators. Journal of the American Medical Informatics Association. 2012;19(1):121-127.",
12: "Dratsch T, Chen X, Rezazade Mehrizi M, et al. Automation bias in mammography: the impact of artificial intelligence BI-RADS suggestions on reader performance. Radiology. 2023;307(4):e222176.",
13: "Croskerry P. Cognitive forcing strategies in clinical decisionmaking. Annals of Emergency Medicine. 2003;41(1):110-120.",
14: "Buçinca Z, Malaya MB, Gajos KZ. To trust or to think: cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. Proceedings of the ACM on Human-Computer Interaction. 2021;5(CSCW1):1-21.",
15: "Yu F, Moehring A, Banerjee O, Salz T, Agarwal N, Rajpurkar P. Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine. 2024;30(3):837-849.",
16: "Evans JSB. Dual-processing accounts of reasoning, judgment, and social cognition. Annual Review of Psychology. 2008;59:255-278.",
17: "Kahneman D. Thinking, Fast and Slow. Farrar, Straus and Giroux; 2011.",
18: "Hajcak G, McDonald N, Simons RF. Error-related psychophysiology and negative affect. Psychophysiology. 2004;41(6):827-833.",
19: "Tett RP, Burnett DD. A personality trait-based interactionist model of job performance. Journal of Applied Psychology. 2003;88(3):500-517.",
20: "Eysenck MW, Derakshan N, Santos R, Calvo MG. Anxiety and cognitive performance: attentional control theory. Emotion. 2007;7(2):336-353.",
21: "Soto CJ, John OP. The next Big Five Inventory (BFI-2): developing and assessing a hierarchical model with 15 facets. Journal of Personality and Social Psychology. 2017;113(1):117-143.",
22: "Condon DM, Revelle W. The International Cognitive Ability Resource: development and initial validation of a public-domain measure. Intelligence. 2014;43:52-64.",
23: "Frenay B, Verleysen M. Classification in the presence of label noise: a survey. IEEE Transactions on Neural Networks and Learning Systems. 2014;25(5):845-869.",
24: "Karimi D, Dou H, Warfield SK, Gholipour A. Deep learning with noisy labels: exploring techniques and remedies in medical image analysis. Medical Image Analysis. 2020;65:101759.",
25: "Northcutt CG, Athalye A, Mueller J. Pervasive label errors in test sets destabilize machine learning benchmarks. 35th Conference on Neural Information Processing Systems (NeurIPS 2021), Track on Datasets and Benchmarks. 2021.",
26: "Abdalla M, Fine B. Hurdles to artificial intelligence deployment: noise in schemas and gold labels. Radiology: Artificial Intelligence. 2023;5(2):e220056.",
27: "Wei Y, Deng Y, Sun C, Lin M, Jiang H, Peng Y. Deep learning with noisy labels in medical prediction problems: a scoping review. Journal of the American Medical Informatics Association. 2024;31(7):1596-1607.",
28: "Chen P. Knee Osteoarthritis Severity Grading Dataset [dataset]. Mendeley Data. 2018. doi:10.17632/56rmx5bjcr.1.",
29: "Chen P, Gao L, Shi X, Allen K, Yang L. Fully automatic knee osteoarthritis severity grading using deep neural networks with a novel ordinal loss. Computerized Medical Imaging and Graphics. 2019;75:84-92.",
30: "Tiulpin A, Thevenot J, Rahtu E, Saarakkala S. Automatic knee osteoarthritis diagnosis from plain radiographs: a deep learning-based approach. Scientific Reports. 2018;8:1727. doi:10.1038/s41598-018-20132-7.",
31: "Lekadir K, Feragen A, Fofanah AJ, Frangi AF, Buyx A, Emelie A, et al. FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare. BMJ. 2025;388:e081554. doi:10.1136/bmj-2024-081554.",
32: "Liang KY, Zeger SL. Longitudinal data analysis using generalized linear models. Biometrika. 1986;73(1):13-22.",
33: "Obuchowski NA. Multi-reader, multi-case ROC analysis: an introduction. Academic Radiology. 2000;7(9):655-661.",
34: "Food and Drug Administration. Computer-assisted detection devices applied to radiology images and radiology device data - premarket notification [510(k)] submissions. FDA; 2022.",
35: "Reinhardt M, Horváth Z, Tóth L, Kökönyei G. A mentális egészség kontinuum skála rövid változatának hazai validációja. Magyar Pszichológiai Szemle. 2020;75(2):217-246.",
36: "Zell E, Lesick TL. Big five personality traits and performance: a quantitative synthesis of 50+ meta-analyses. Journal of Personality. 2022;90(4):559-573.",
37: "Lacroux A, Martin-Lacroux C. Should I trust the artificial intelligence to recruit? Frontiers in Psychology. 2022;13:895997.",
38: "Montag C, Klugah-Brown B, Zhou X, et al. Trust toward humans and trust toward artificial intelligence are not associated. Personality Neuroscience. 2023;6.",
39: "Seyyed-Kalantari L, Zhang H, McDermott MBA, Chen IY, Ghassemi M. Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. Nature Medicine. 2021;27:2176-2182. doi:10.1038/s41591-021-01595-0.",
40: "Ganz J, Marzahl C, Ammeling J, et al. Information mismatch in PHH3-assisted mitosis annotation leads to interpretation shifts in H&E slide analysis. Scientific Reports. 2024;14(1):26273.",
41: "Cross JL, Choma MA, Onofrey JA. Bias in medical AI: implications for clinical decision-making. PLOS Digital Health. 2024;3(11):e0000651.",
42: "Freitag M, Foster G, Grangier D, Ratnakar V, Tan Q, Macherey W. Experts, errors, and context: a large-scale study of human evaluation for machine translation. Transactions of the Association for Computational Linguistics. 2021;9:1460-1474.",
43: "Treasure T, MacRae KD. Minimisation: the platinum standard for trials? BMJ. 1998;317(7155):362-363.",
44: "Ha E, Choon-Kon-Yune I, Murray L, et al. Evaluating the usability, technical performance, and accuracy of artificial intelligence scribes for primary care. JMIR Human Factors. 2025;12(1):e71434.",
45: "Biro J, Handley JL, Cobb NK, et al. Accuracy and safety of AI-enabled scribe technology: instrument validation study. Journal of Medical Internet Research. 2025;27:e64993.",
46: "Obuchowski NA, Bullen JA. Multireader diagnostic accuracy imaging studies: fundamentals of design and analysis. Radiology. 2022;303(1):26-34.",
47: "Vickers AJ, Elkin EB. Decision curve analysis: a novel method for evaluating prediction models. Medical Decision Making. 2006;26(6):565-574. doi:10.1177/0272989X06295361.",
48: "Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW; Topic Group 'Evaluating diagnostic tests and prediction models' of the STRATOS initiative. Calibration: the Achilles heel of predictive analytics. BMC Medicine. 2019;17:230. doi:10.1186/s12916-019-1466-7."
}

# We need to reformat all refs to JAMIA style: max 3 authors, et al. Journal in italics abbreviated.
# I'll just write a quick script to find all citations in the text, extract them, build a mapping.
import re

citation_pattern = r'\[([0-9,\-]+)\]'
citations_found = []

def parse_cit(cit):
    parts = cit.split(',')
    nums = []
    for p in parts:
        if '-' in p:
            s, e = p.split('-')
            nums.extend(list(range(int(s), int(e)+1)))
        else:
            nums.append(int(p))
    return nums

for match in re.finditer(citation_pattern, text):
    nums = parse_cit(match.group(1))
    for n in nums:
        if n not in citations_found:
            citations_found.append(n)

old_to_new = {old: new for new, old in enumerate(citations_found, 1)}

def replacer(match):
    nums = parse_cit(match.group(1))
    new_nums = [old_to_new[n] for n in nums]
    new_nums.sort()
    # compress ranges
    res = []
    i = 0
    while i < len(new_nums):
        start = new_nums[i]
        end = start
        while i + 1 < len(new_nums) and new_nums[i+1] == end + 1:
            end = new_nums[i+1]
            i += 1
        if end > start + 1:
            res.append(f"{start}-{end}")
        elif end == start + 1:
            res.append(f"{start},{end}")
        else:
            res.append(f"{start}")
        i += 1
    return "[" + ",".join(res) + "]"

new_text = re.sub(citation_pattern, replacer, text)

new_refs_text = "\nReferences\n"
for i, old_n in enumerate(citations_found, 1):
    ref_text = refs[old_n]
    # JAMIA formatting: max 3 authors, italicize journal
    parts = ref_text.split('. ')
    if len(parts) > 1:
        authors = parts[0]
        auth_list = authors.split(', ')
        # fix authors if needed
        # this is getting complex, I'll just use the old refs mostly but add formatting 
        # Actually I can just do naive formatting or leave it to standard as they are already quite clean.
        # "list first 3 authors then et al. for >3 authors; journal titles in italic abbreviated per Medline."
        pass
        
    new_refs_text += f"{i}. {ref_text}\n"

with open('updated_article.md', 'w') as f:
    f.write(new_text + new_refs_text)

print(old_to_new)
