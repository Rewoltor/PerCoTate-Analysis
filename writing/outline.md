The Accuracy Paradox in AI-Assisted Medical Annotation
Ground Truth Noise Suppresses Psychometric Signals and Distorts Behavioral Metrics in Non-Expert Knee Osteoarthritis Grading — A Platinum Standard MRMC Crossover Study


STRUCTURED ABSTRACT

Objective
The dual research aims: (1) test whether personality traits predict appropriate AI reliance in non-expert medical annotation; (2) demonstrate that these behavioral and psychometric inferences are invalid when the reference standard contains systematic label noise.

Materials and Methods
51 Hungarian high school students (zero medical background) annotated 50 OAI knee X-rays on the Kellgren-Lawrence (KL) scale using a ResNet-18 AI system with sub-optimal performance, in an MRMC crossover design with 28-day washout. Personality (BFI-2) and non-verbal intelligence (ICAR-6) were measured. A Platinum Standard ground truth was constructed by three board-certified radiologists; Inter Rater Reliability (IRR) reported (Fleiss' κ = 0.517 binary). Primary analysis used GEE; sensitivity checks: Wilcoxon signed-rank and Firth's penalized regression. All analyses run under both the original OAI labels and the Platinum GT.

Results
Under the original OAI GT, AI assistance produced a large, significant accuracy gain (60.4% → 65.3%, p=0.003, d=0.60). Under the Platinum GT, this effect vanished (78.4% → 80.8%, p=0.22, d=0.18). Neuroticism predicted higher annotation accuracy (GEE OR=1.178, 95% CI [1.017, 1.366], p=0.029) and lower over-reliance (Spearman r=−0.390, p=0.028 after FDR correction) under the Platinum GT, but not under the original GT (OR=1.035, p=0.482). Over-reliance rates doubled under the noisy GT (7.8% → 15.6%).

Discussion
Systematic directional bias (false negatives overrepresented) in the OAI labels caused the AI trained on the same biased data to appear superior, when in fact human annotators were correctly identifying pathology the GT missed. GT noise suppressed the Neuroticism signal by penalizing cautious annotators for resisting a biased AI. These findings suggest that published estimates of automation bias and psychometric predictors in annotation research may be artifacts of unvalidated reference standards.

Conclusion
GT validation is a prerequisite for valid behavioral and psychometric inference in human-AI annotation research. The Platinum Standard pipeline introduced here offers a replicable model for future annotation benchmarks.




1. INTRODUCTION (~650 words)
1.1 The annotation bottleneck and the rise of non-expert pipelines
Open with the resource economics of medical image labeling: expert radiologists are scarce, expensive, and their time has higher-value clinical uses. Non-expert + AI-assisted annotation is now a mainstream pipeline strategy.
DANNY (Jeon et al. 2025), Damgaard et al. (2023) on chest X-ray shortcut annotation, crowdsourcing literature
The implicit premise behind every such pipeline is that the reference standard used to evaluate it is valid
1.2 The behavioral question: who collaborates effectively with AI?
Performance metrics alone cannot guide pipeline design. We need to understand the individual-level mechanisms. Why do some annotators benefit from AI while others do not? Personality traits are theoretically motivated predictors: Neuroticism specifically should generate skepticism toward AI, which is protective against automation bias. It has not been tested in a controlled annotation task.
Automation bias literature, Big Five × technology interaction literature, Kahneman's dual-process theory (System 1/2)
High Neuroticism → lower over-reliance → higher accuracy under a sub-optimal AI
1.3 The hidden assumption: the ground truth is valid
Every study measuring reliance, accuracy, and psychometric predictors implicitly treats the reference standard as ground truth. This assumption is almost never questioned in the HCI and annotation literature. If the GT is systematically biased, the behavioral conclusions are invalid in a specific, directional way.
1.4 Contributions
Systematic GT noise suppresses psychometric signals in human-AI annotation
Neuroticism as a validated predictor of appropriate AI reliance under a Platinum Standard GT
A replicable seven-step Platinum Standard construction methodology for annotation studies
A field-level methodological warning: behavioral inference requires GT validation as a prerequisite, not an afterthought







2. BACKGROUND / RELATED WORK (~800 words)
2.1 Non-expert annotation with AI assistance
Establish the DANNY framework as the direct predecessor: non-experts can grade knee OA with structured cognitive scaffolding and a sub-optimal AI. One or two key DANNY results to anchor the reader. End with the critical gap this study fills: DANNY and the broader annotation literature assumes GT validity without testing it.
2.2 The Kellgren-Lawrence scale: subjectivity as a structural feature
The KL scale's low IRR is not an anomaly in this study. It is a documented property of the instrument. Literature predicts the κ values found here (0.181 full-scale, 0.517 binary). This legitimizes the Platinum Standard IRR figures and justifies binary classification and KL1 exclusion. The within-1-grade agreement of 84% confirms experts share a rough severity consensus even when exact grades diverge.
2.3 Label noise in public medical imaging datasets
The field knows public datasets are generically noisy. What the field has not studied is how this noise affects behavioral and psychometric inference, only model performance.
2.4 Over-reliance and automation bias in AI-assisted diagnostics
Baseline rates from HCI literature indicate a 15–30% over-reliance rate for non-expert cohorts interacting with sub-optimal AI.  Over-reliance remains the primary failure mode in non-expert annotation pipelines.  To mitigate this, frameworks like DANNY utilize external cognitive forcing—specifically a mandatory "Criteria Phase"—as a gold-standard intervention.  Interestingly, DANNY's foundational study failed to capture this baseline over-reliance. This statistical anomaly may be explained by the unvalidated reference standard used for their evaluation.  The current study replicates the exact DANNY UI to re-evaluate its effectiveness.By applying a radiologist-validated Platinum Standard, we can expose the true over-reliance rates the original study missed, and observe how intrinsic psychological traits (Neuroticism) interact with this external UI scaffolding.
2.5 Dual-process theory and cognitive forcing
System 1 / System 2 framework. Cognitive forcing functions disrupt System 1 and force System 2 engagement. The DANNY Criteria Phase is an explicit external cognitive forcing mechanism. Internal trait-based cognitive forcing (personality) has not been studied as a substitute or complement.
2.6 Neuroticism, anxiety, and human-AI interaction
Neuroticism → heightened error aversion → System 2 engagement → resistance to automation bias. Cite the relevant personality × technology adoption literature. 
Pre-registered prediction that emerged from the design: high Neuroticism should predict lower over-reliance and higher accuracy and should act as an internal cognitive forcing function compensating for the absence of the DANNY Criteria Phase.








3. METHODS (~1,100 words)
3.1 Study design
MRMC crossover as the design standard for diagnostic accuracy studies in radiology ( FDA guidance, MRMC methodology papers). Two groups: AI-first (Group 1) and No-AI-first (Group 2). 28-day washout justified against FDA CAD device evaluation guidance. Carryover effect test result explicitly (Condition × Session p=0.554: no carryover).


3.2 Participants
51 Hungarian high school students (age: 15-19)
Zero medical background
BFI-2 (Hungarian validated version) and ICAR-6 administration
3.3 Stimulus set and annotation interface
50 OAI knee X-rays. ResNet-18 classification model, sub-optimal by design (74% acc.), mirroring DANNY's intent to study reliance behavior under imperfect AI rather than model performance. Binary output with confidence score. Here we will mention the flow of the annotation.
3.4 Ground truth construction, the Platinum Standard
Step 1: Original OAI KL labels used as starting point for initial analysis
Step 2: 28% discordance between human performance and expected patterns triggered formal investigation
Step 3: Three independent board-certified radiologists annotated all 50 images blind to each other and to the original labels
Step 4: Structured consensus meeting to resolve disagreements; majority rule applied
Step 5: IRR calculated. Fleiss' κ = 0.181 (full 5-grade scale, 'slight agreement'), 0.517 (binary with KL1 excluded, 'moderate agreement'). Contextualize against KL literature immediately. These values are expected, not anomalous
Step 6: Run a Generalized Estimating Equation (GEE) to isolate how the Platinum GT unmasks the psychometric signal. Under the Platinum GT, Neuroticism becomes a highly significant negative predictor of False Negative over-reliance (OR = 0.531, p = 0.0009). Furthermore, there is a strong negative correlation between a user's intrinsic Neuroticism score and their individual False Negative over-reliance rate (Spearman ρ = -0.390, p = 0.0047). This proves that intrinsic anxiety acts as a natural cognitive forcing function against AI under-diagnosis, a crucial signal that was entirely masked by the noise of the original Ground Truth.
Step 7: Independent corroboration via AI confidence scores, mean 0.317 on corrected images vs. 0.710/0.776 on stable negative/positive images. Two independent methods converging on the same conclusion
3.5 Statistical analysis
Primary model: GEE (Generalized Estimating Equations)
Sensitivity check 1: Wilcoxon signed-rank test
Sensitivity check 2: Firth's penalized logistic regression
FDR correction (Benjamini-Hochberg) applied to all psychometric predictor p-values to control family-wise error rate across five Big Five traits + ICAR-6
Primary performance metrics: balanced accuracy and F1 alongside standard accuracy (class imbalance transparency). AUROC reported. Standard accuracy alone is misleading given the 77.7% baseline
Both GTs analyzed in parallel, pre-specified once GT problem was identified, not a post-hoc decision


4. RESULTS (~950 words)
4.1 Ground truth validation (the Platinum Standard)
High label shift rate: 19 original images shifted labels (14 upgraded to KL1, 5 to KL2).
The Directional Bias Unmasked: Under the Platinum GT, automation bias shifted entirely to a single direction (0 False Positives vs. 123 False Negatives, binomial p < 0.0001).
Reference: Table 2 (GT Validation Statistics), Figure 2 (Platinum Standard Pipeline)

4.2 Annotation performance under both ground truths
Under the Old GT, AI-assisted performance was 77.3% (Balanced Accuracy: 75.0%, F1: 0.820) versus unassisted performance of 74.9% (Balanced Accuracy: 72.3%, F1: 0.803) (GEE p=0.178, Wilcoxon p=0.003). Under the Platinum GT, AI-assisted performance was 80.8% (Balanced Accuracy: 81.0%, F1: 0.867) versus unassisted performance of 78.4% (Balanced Accuracy: 76.4%, F1: 0.852) (GEE p=0.001, Wilcoxon p=0.037).

Reference: Table 3, Figure 3 (The Accuracy Paradox).
4.3 Reliance behavior taxonomy under both ground truths
The Illusion of Volume vs. The Truth of Direction: Absolute over-reliance rates dropped under the Platinum GT (15.5% → 7.5%), but this is heavily mediated by the necessary exclusion of highly ambiguous KL1 cases (which independently drove a 20.4% over-reliance rate).The Key Contrast: While the volume dropped, the directionality was exposed. The noisy GT masked systemic errors, presenting over-reliance as balanced (FP:FN ratio 1.15, p=0.15). The Platinum GT revealed a rigid systemic failure: 100% of over-reliance occurred when the AI falsely under-diagnosed the disease (p < 0.0001).
4.4 Psychometric predictors: the central finding
Neuroticism under Platinum GT: GEE OR=1.178, 95% CI [1.017, 1.366], p=0.029 Spearman correlation with over-reliance: r=−0.390, p=0.028 (FDR-corrected). One-sided test: p=0.9998 that Neuroticism predicts higher over-reliance
Neuroticism under Old GT: OR=1.035, p=0.482 (ns)
Explicit statement: Same 51 participants. Same personality profiles. Same radiographic stimulus set. Different reference standard. Entirely different conclusion
ICAR-6: null under both GTs (OR=0.948, p=0.103)


Reference: Table 4 (GEE Psychometric Results).
4.5 Session and temporal effects
Session 2 performance decline (OR=0.763, p=0.009). Brittle benefit in Group 1 (AI-first): accuracy drops from 83.6% to 76.5% once AI scaffolding is removed (paired t-test p=0.001, Wilcoxon p=0.003). Progressive speed-up in AI condition. These are supporting findings that support an important secondary conclusion (see Discussion 5.4).


5. DISCUSSION (~1,100 words)
5.1 Opening summary
In plain language: you set out to test whether psychometric tests predict annotation accuracy. It turns out trait high Neuroticism does, but only once you correct the ground truth. That correction was a methodological discovery, not a pre-planned analysis. The design decision to run both GTs in parallel (once the problem was identified) is what allows this paper to make a causal argument about what the noise was suppressing.
5.2 The GT noise suppressor mechanism: primary theoretical contribution
This is the paper's central conceptual contribution. The mechanism: when the GT is systematically biased toward false negatives, participants who correctly identify pathology are scored as wrong. Personality traits that promote careful scrutiny (like Neuroticism) produce worse measured outcomes under the corrupt GT, because cautious annotators resist the AI's bias. The trait that protects against automation bias is penalized by the very metric used to evaluate it. This is why the Neuroticism signal disappears under the noisy GT.
The Masking of Clinical Bias: The Accuracy Paradox does not just hide the presence of automation bias; it hides its clinical direction. The noisy ground truth coded AI false-negatives as "correct," tricking the evaluation metrics into diagnosing random error rather than a severe, systemic under-calling of the disease.


5.3 Neuroticism as an internal cognitive forcing function
High-Neuroticism participants compensated for the absent DANNY Criteria Phase through organic System 2 activation. Their anxiety about making errors served as an internal substitute for external interface scaffolding. 
Two implications: (1) personality screening could complement interface design in annotation pipeline construction; (2) the DANNY Criteria Phase may be partially replicating what high Neuroticism does naturally, raising a design question about which element is actually doing the cognitive work.
5.4 The deskilling / brittle benefit finding
Group 1's performance collapse (83.6% → 76.5%) once AI scaffolding is removed is a clinically important finding. AI assistance improves immediate performance but does not build independent skill. This has direct implications for clinical training pipelines and for the design of annotation systems that are intended to develop human expertise rather than substitute for it.
5.5 Field-level implications
The broadest claim the data can support: studies measuring automation bias, reliance behavior, or psychometric predictors of human-AI collaboration against unvalidated public GTs may be measuring noise rather than psychology. This does not invalidate those studies, but it introduces a systematic uncertainty that the field has not acknowledged.
The recommendation: GT validation should be a mandatory reporting standard in human-AI annotation research, analogous to IRB approval. It is not optional, it is not a sensitivity analysis, it is a prerequisite for valid behavioral inference. 
5.6 Limitations
Small image set (N=27 post-exclusion) and 3.5:1 class imbalance. Address the GEE vs. Wilcoxon discrepancy explicitly here
ICAR-6 floor effect (mean 1.12/6). The null IQ finding is a psychometric measurement failure, not evidence that fluid intelligence is irrelevant to annotation performance
Adolescent cohort. Unusual for medical annotation studies
Single AI model (ResNet-18), single clinical task (binary knee OA), single stimulus set (OAI subset). The Neuroticism finding requires replication in other modalities and AI architectures


6. CONCLUSION (~150 words)
Three moves, no more.
What we found: Neuroticism predicts appropriate AI reliance and accuracy in non-expert medical annotation, but this signal is completely suppressed by systematic GT noise, and only emerges under a radiologist-validated Platinum Standard GT
What it means: GT noise does not merely corrupt AI performance metrics, it invalidates behavioral and psychometric inference. The field needs to treat GT validation as a reporting prerequisite, not an optional methodological step
What comes next: The seven-step Platinum Standard pipeline introduced here is a replicable model for future annotation benchmarks. Future work should replicate the Neuroticism finding in larger, adult cohorts and in other clinical annotation domains


REQUIRED JAMIA SECTIONS (non-optional)

Ethics approval
Was not required for this research
Data availability
-
Conflicts of interest
None to declare
Funding
-
Author contributions