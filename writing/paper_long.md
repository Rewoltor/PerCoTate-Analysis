The Accuracy Paradox in AI-Assisted Medical Annotation 
A Platinum Standard Crossover Study


ABSTRACT
Objective: We ask two questions central to the non-expert annotation literature: does AI assistance genuinely improve annotation accuracy, and do personality traits predict who collaborates appropriately with AI? We demonstrate that both questions — and their published answers — are fundamentally confounded by a single, routinely unexamined variable: whether the reference standard against which human judgments are scored contains systematic directional bias.
Materials and Methods: Fifty-one Hungarian high school students annotated 50 OAI knee radiographs on the Kellgren-Lawrence scale using a sub-optimal ResNet-18 AI (74.1% accuracy) in a multi-reader multi-case crossover design with a 28-day washout. Personality (BFI-2) and non-verbal intelligence (ICAR-6) were assessed. A seven-step Platinum Standard ground truth was constructed by three independent board-certified radiologists (Fleiss' κ = 0.517, binary). All analyses were pre-specified and conducted in parallel under the original OAI labels and the Platinum Standard.
Results: Under the original OAI ground truth, AI assistance produced a large, significant accuracy gain (60.4% → 65.3%; GEE OR = 1.232, p = 0.003; Cohen's d = 0.60) — a result that, read in isolation, constitutes a compelling demonstration of AI benefit. Under the Platinum Standard, the same participants annotating the same images showed no significant primary effect (GEE p = 0.178), with only a marginal, individually heterogeneous signal in the pre-specified Wilcoxon sensitivity check (p = 0.037). Measured over-reliance halved (15.6% → 7.8%), and its direction became structurally unambiguous: 100% of over-reliance events under the Platinum Standard were false-negative acceptances — participants agreeing with the AI's failure to detect genuine pathology — with zero false-positive acceptances (binomial p < 0.0001). The original labels had rendered this clinical asymmetry mathematically invisible. Neuroticism, entirely null under the original ground truth (OR = 1.035, p = 0.482), emerged as a significant positive predictor of annotation accuracy (OR = 1.178, 95% CI [1.017, 1.366], p_FDR = 0.029) and a negative predictor of false-negative over-reliance (Spearman ρ = −0.390, p_FDR = 0.028) under the Platinum Standard only. Given post-hoc power of 17% at N = 51, the Neuroticism association is hypothesis-generating and requires confirmatory replication.
Discussion: The suppressor mechanism has a structural explanation. The original OAI labels independently encoded the same false negatives as the AI model — both derived from the same repository. This alignment had three simultaneous consequences: participants who accepted the AI's erroneous negative predictions were scored correct; participants who correctly identified pathology the AI missed were scored wrong; and the personality trait most protective against automation bias appeared mathematically counterproductive. The effect size of d = 0.60 was not a property of human learning — it was a property of shared error between the model and the labels used to evaluate it. This condition is not a design flaw specific to this study. It describes the current default in the field.
Conclusion: A large, statistically robust AI benefit can be a measurement artifact. The same label noise that inflates apparent AI benefit renders clinical over-reliance invisible, suppresses protective personality signals, and reverses their apparent direction — simultaneously and systematically. Any study that evaluates AI-assisted human annotation against an unvalidated public repository may be documenting the error structure of that repository, not the cognitive behavior of the annotators. The field's empirical literature on AI benefit and personality effects in annotation tasks should be read with this possibility in mind.



1. INTRODUCTION
1.1 The annotation bottleneck and the rise of non-expert pipelines
The annotation of medical imaging data at the scale required by modern AI development is one of the most acute resource problems in clinical informatics. Expert radiologists are scarce, expensive, and their time carries higher-value clinical uses than labeling training sets. The volume of unlabeled data accumulated by population-scale imaging programs vastly exceeds what credentialed specialists can annotate [Rajpurkar et al., 2022]. The field's operational response has been the non-expert annotation pipeline: structured frameworks in which lay annotators, supported by AI predictions, produce labels that approximate expert standards at a fraction of the cost [Cheplygina et al., 2019]. The DANNY (Data ANnotation for Non-experts made easY) framework is a well-studied example of this approach in musculoskeletal radiology, demonstrating that cognitive scaffolding enables non-experts to achieve competitive grading accuracy with a tenfold increase in deliberation time and significantly higher rates of appropriate AI override [Jeon et al., 2025]. Implicit in every such pipeline evaluation is a premise so fundamental that it is rarely stated: that the reference standard used to score annotator performance is valid. If it is not, the conclusions are not merely imprecise, they are systematically distorted in ways the study has no method to detect.
1.2 The behavioral question: who collaborates effectively with AI?
Aggregate accuracy metrics cannot alone guide pipeline design. Knowing that a cohort achieved 80% accuracy with AI assistance reveals nothing about whether that accuracy arose from genuine diagnostic engagement or uncritical algorithmic deference—two mechanisms with completely different implications for pipeline safety [Goddard et al., 2012; Mosier & Skitka, 1996]. Understanding individual-level predictors of appropriate reliance is a prerequisite for informed design, not a secondary research agenda. Personality traits are theoretically motivated predictors of this variation. Dual-process frameworks [Evans, 2008; Kahneman, 2011] position AI assistance as a default System 1 pathway—a heuristic proxy for deliberate judgment. Of the Big Five dimensions, Neuroticism is most theoretically positioned to disrupt this substitution: its established correlation with enhanced error-related negativity (ERN) amplitude generates persistent, trait-level sensitivity to uncertainty and potential failure [Hajcak et al., 2004]. Trait Activation Theory predicts this disposition should produce deliberative, independent behavior specifically in high-ambiguity AI contexts—precisely when a sub-optimal algorithm is most likely to be wrong and most likely to be trusted [Tett & Burnett, 2003]. The prediction is theoretically motivated and, in controlled annotation tasks, empirically untested. While Conscientiousness was pre-registered as the primary predictor, Neuroticism was included as a pre-specified secondary predictor. This study reports a hypothesis-generating association between Neuroticism and appropriate AI reliance that warrants confirmatory investigation in a properly powered sample.
1.3 The hidden assumption
The majority of studies measuring reliance behavior, annotation accuracy, or psychometric predictors in human-AI annotation implicitly treats the reference standard as objective. This assumption is almost never tested. The resulting error distribution is not random; it is systematically directional. When the ground truth's error pattern is correlated with the AI's own systematic errors, as occurs when both derive from the same public training repository, two consequences follow simultaneously. First, over-reliance events become mathematically invisible: the annotator agrees with the AI's error, and the corrupted reference standard registers the outcome as correct. Second, the traits that protect against automation bias are penalized: an annotator who correctly identifies pathology the AI missed is scored as wrong because the noisy ground truth agrees with the false negative. In this environment, protective personality traits appear mathematically counterproductive. This paper provides the first empirical demonstration that this distortion is not theoretical — it is operating in the field's leading annotation paradigm.
1.4 Contributions
This paper reports four contributions:
The Ground Truth (GT) noise suppressor mechanism. Systematic directional label noise in the OAI repository masked a Neuroticism-linked association that was recoverable only after ground truth correction (OR = 1.035, p = 0.482 under original labels; OR = 1.178, p = 0.029 under Platinum Standard).
Neuroticism as a hypothesis-generating predictor of appropriate AI reliance. High-Neuroticism annotators exhibited significantly lower false-negative over-reliance in this sample (ρ = −0.390, p_FDR = 0.028), suggesting that the trait may function as an internal cognitive forcing mechanism. This association is hypothesis-generating: the estimated post-hoc power for this effect was 17% (N = 51), and confirmatory replication in a larger, properly powered sample is required.
A replicable seven-step Platinum Standard construction methodology. For annotation studies requiring independent ground truth validation from ambiguous public imaging repositories.
Proposed minimum reporting standards. Behavioral inference in human-AI annotation requires ground truth validation as a prerequisite. We propose three minimum reporting requirements that should accompany any study measuring human reliance on AI.


2. BACKGROUND / RELATED WORK
2.1 Non-expert annotation with AI assistance
The demand for annotated medical imaging data far exceeds the capacity of expert radiologist labor, creating a well-documented resource bottleneck [Rajpurkar et al., 2022]. Non-expert annotation pipelines augmented by AI assistance have emerged as the mainstream solution [Cheplygina et al., 2019], and hybrid human-AI systems have been shown to outperform either component in isolation, provided the human operator remains actively engaged rather than passively deferring to the algorithm [Rajpurkar et al., 2022]. The DANNY (Data ANnotation for Non-experts made easY) framework represents a prominent instantiation of this paradigm for musculoskeletal radiology. Jeon et al. (2025) demonstrated that non-experts using DANNY's structured cognitive scaffolding achieved significantly higher grading accuracy than control groups (p < 0.001), with a tenfold increase in per-image deliberation time (50.5 vs. 5.7 seconds) and a significantly higher rate of appropriate AI override, providing the operational definition of appropriate reliance against which the present study is benchmarked [Jeon et al., 2025].

Despite these advances, a foundational assumption runs unexamined across the entire non-expert annotation literature: that the reference standard used to evaluate annotator accuracy is valid and free of systematic bias. DANNY and comparable frameworks treat the ground truth as an immutable reality rather than a human-constructed consensus subject to error. However, as Jackson et al. (2026) demonstrated in a comprehensive scoping review, evaluations of AI-assisted decision-making frequently yield mixed or contradictory results because they fail to account for the complex interplay between baseline human attitudes, the intrinsic ambiguity of medical imaging data, and the actual validity of the ground truth used to score collaborative performance [Jackson et al., 2026]. Furthermore, Chen et al. (2021) have explicitly warned that evaluating AI on a reference standard based primarily on subjective human interpretation inherently caps the measurable performance of both the human operator and the algorithm [Chen et al., 2021]. If the reference standard harbors directional bias, evaluating human actions against it does not merely produce noisy data; it systematically distorts the measurement of human cognitive engagement. Ground truth validation is therefore a fundamental prerequisite for valid behavioral and psychometric inference, not a supplementary quality check.

2.2 The Kellgren-Lawrence scale: subjectivity as a structural feature
The Kellgren-Lawrence (KL) scale provides the standard five-grade ordinal assessment of knee osteoarthritis severity based on joint space narrowing, osteophyte formation, and subchondral changes [Kellgren & Lawrence, 1957]. Its low inter-rater reliability (IRR), particularly at the lower grade boundaries, is a documented structural property of the instrument rather than a study-specific anomaly. Kose et al. (2017) conducted comparative evaluations of multiple radiographic grading scales and found that the KL scale consistently failed to achieve acceptable reliability independently [Kose et al., 2017]. Yoon et al. (2023) corroborated this, documenting that the grading system suffers from inferior inter-observer and intra-observer reliability primarily due to the inherent semantic ambiguity characterizing its lower grades, particularly Grade 1 [Yoon et al., 2023].

Estimates of KL reliability vary significantly depending on the clinical context. Full-scale agreement among expert radiologists regularly falls between κ = 0.183 and 0.230—categorized as slight to fair—reflecting the difficulty of evaluating early-stage osteoarthritis [Landis & Koch, 1977]. In contrast, the higher substantial agreement range of κ = 0.500–0.692 is predominantly observed among orthopedic surgeons evaluating advanced stages of the disease or utilizing a collapsed binary categorization [Khela et al., 2026]. This demonstrates that the structural subjectivity of the KL scale is heavily modulated by the specific clinical background and daily operational focus of the human observer. Interestingly, while human experts struggle with this ambiguity, Vaattovaara et al. (2025) demonstrated that highly calibrated AI models can achieve a kappa of 0.820, highlighting a distinct asymmetry in signal-to-noise ratios between human and algorithmic agents when evaluating ambiguous boundaries [Vaattovaara et al., 2025]. Furthermore, Guo et al. (2025) established that while fixed joint space width measurements can achieve exceptionally high reliability (ICC > 0.80), minimum joint space width measurements remain highly vulnerable to positioning variability and perspective effects, illustrating that no single radiographic metric is entirely free from systemic noise [Guo et al., 2025].

The IRR figures produced in the present study are congruent with this literature, validating our analytical decisions to adopt binary outcome classification, exclude KL1 images from the primary behavioral analysis, and construct an independent expert-consensus reference standard. The FUTURE-AI international consensus guidelines mandate rigorous, multi-rater consensus protocols to establish trustworthy ground truths for medical AI deployment [Lekadir et al., 2021]. The operational definition of a "Platinum Standard"—a dataset curated with such exceptional, multi-tiered expert consensus that it rigorously surpasses the traditional "gold standard"—is well-documented in the methodology literature. Originating with Treasure and MacRae (1998), the precise term "platinum standard" has been utilized in foundational machine learning and informatics work, such as large-scale human evaluation studies for artificial intelligence [Freitag et al., 2021], confirming its appropriateness to denote a reference standard subjected to extraordinary human curation.


2.3 Label noise in public medical imaging datasets
The KL scale's structural subjectivity propagates into large-scale public datasets as systematic label noise. Frenay and Verleysen (2014) established that label noise is rarely random; it is feature-dependent and correlated with class-boundary ambiguity—precisely the pattern expected at the KL0/KL1 margin [Frenay & Verleysen, 2014]. In medical imaging, Karimi et al. (2020) showed that deep learning models are acutely sensitive to this variability, actively memorizing annotator heuristics and perceptual biases rather than learning the underlying pathology [Karimi et al., 2020]. The Osteoarthritis Initiative (OAI) dataset used in this study has been specifically implicated: its heavy class skew toward KL0 (~40%) and KL1 (~18%) cases induces trained models to favor negative predictions, amplifying the underdiagnosis bias of the original annotators [Tiulpin et al., 2019]. Northcutt et al. (2021) extended this concern to test sets, demonstrating that label errors in evaluation benchmarks create an accuracy paradox in which more capable models appear to underperform because they correctly identify true pathology that the corrupted reference standard coded as healthy [Northcutt et al., 2021].

The field has studied label noise almost exclusively as a problem of model performance. Its effect on human behavioral and psychometric inference has not been investigated. We extend the accuracy paradox from model evaluation to human psychometric and behavioral inference—a domain where its consequences have not previously been empirically demonstrated. When annotators are evaluated against a biased ground truth, correct human judgments that contradict the reference standard are coded as errors, and psychological traits that promote careful scrutiny appear mathematically counterproductive. The present study addresses this gap directly.

Contemporary research confirms this is a pervasive and escalating challenge. Ma et al. (2026) demonstrated in their LNMBench study that existing algorithmic label-noise mitigation techniques systematically fail under real-world, high-noise clinical conditions, proving that label noise is a structural barrier requiring sociotechnical intervention [Ma et al., 2026]. Furthermore, a 2025 simulation study investigating Large Language Model-generated label noise in radiology revealed that even minute reductions in reference standard specificity in low-prevalence environments result in massive underestimations of true AI sensitivity [Emory University, 2025]. The human-factors dimensions are equally critical: recent research emphasizes that label noise frequently arises from automated extraction pipelines mathematically flattening the nuanced uncertainty and disagreement of clinical experts into collapsed binary labels [Abdalla & Fine, 2023; Wei et al., 2024]. Ganz et al. (2024) documented similar label shifts in histopathology, where features that are borderline identifiable to human experts introduce massive label noise when processed by binary networks [Ganz et al., 2024]. Most alarmingly, Seyyed-Kalantari et al. (2021) established that AI algorithms trained on such noisy, skewed public datasets reliably amplify underdiagnosis biases, heavily and disproportionately penalizing marginalized subpopulations [Seyyed-Kalantari et al., 2021].


2.4 Over-reliance and automation bias in AI-assisted diagnostics
Automation bias — the tendency to substitute automated outputs for independent judgment — is a well-documented failure mode in human-AI systems, including non-expert annotation pipelines [Mosier & Skitka, 1996]. It manifests as omission errors (failures to detect problems the AI did not flag) and commission errors (accepting incorrect AI recommendations). This vulnerability is not restricted to non-experts; Dratsch et al. (2023) provided a striking quantification of this risk within mammography, where highly experienced, board-certified radiologists presented with incorrect AI suggestions saw their diagnostic accuracy plummet catastrophically from 82.3% to 45.5% [Dratsch et al., 2023]. Yu et al. (2024) documented identical vulnerabilities across broader medical imaging modalities, demonstrating that automated labels significantly alter interpreter uncertainty and degrade performance when algorithms make errors [Yu et al., 2024]. These findings demonstrate that even highly trained experts are susceptible to algorithmic deference, rendering our investigation of non-expert vulnerability well-motivated.

The theoretical distinction between omission and commission errors requires critical attention. Recent 2025 research on ambient AI scribes by Ha et al. and Biro et al. revealed that omission errors present a uniquely insidious cognitive safety risk: because missing details provide no salient visual cue, they fail to trigger human error-monitoring cognitive processes, resulting in 70% of such errors remaining undetected during clinical review [Biro et al., 2025; Ha et al., 2025]. Furthermore, recent research has demonstrated that modern high-capacity models seamlessly mimic human expertise, bypassing natural skepticism and inducing significant automation bias [Rodman, 2026; Cross et al., 2024].

Parasuraman and Manzey (2010) demonstrated that complacency is maximized when an automated system is perceived as generally reliable—the condition deliberately induced by the sub-optimal ResNet-18 model (~70% accuracy) deployed here [Parasuraman & Manzey, 2010]. Goddard et al. (2012), in a systematic review published in this journal, established baseline over-reliance rates of 15–30% for non-expert cohorts under these conditions [Goddard et al., 2012]. The DANNY Criteria Phase was designed specifically to counter this risk through mandatory feature identification prior to AI exposure. Yet the foundational DANNY study did not observe the expected baseline over-reliance rates—an anomaly plausibly explained by its unvalidated reference standard. When the ground truth and the AI share the same false-negative error structure, over-reliance events are mathematically invisible: the human agrees with the AI's error, and the biased ground truth scores the outcome as correct. The present study replicates the DANNY interface under a radiologist-validated reference standard independent of the AI's training data, enabling the first unconfounded measurement of true over-reliance rates in this paradigm.

2.5 Dual-process theory and cognitive forcing
Dual-process theories of cognition [Evans, 2008; Kahneman, 2011] provide the architecture underlying both automation bias and its mitigation: System 1 processing is fast and heuristic-driven; System 2 is slow, deliberate, and analytically rigorous. AI assistance creates a default System 1 pathway in which the algorithmic output functions as a low-effort proxy for judgment. Croskerry (2003) established cognitive forcing strategies as the clinical intervention to disrupt this pathway, mandating System 2 engagement before diagnostic closure [Croskerry, 2003]. Buçinca et al. (2021) demonstrated in an AI interface context that requiring users to commit to an independent hypothesis before accessing the model's prediction significantly reduces over-reliance [Buçinca et al., 2021]. The DANNY Criteria Phase is a direct application of this principle. What the literature has not examined is whether an individual's intrinsic psychological disposition can fulfill the same function—whether internal, trait-based friction can substitute for the external friction imposed by interface design.

2.6 Neuroticism, anxiety, and human-AI interaction
Neuroticism is the Big Five trait most theoretically positioned to serve as an internal cognitive forcing function. As operationalized by the BFI-2, it encompasses anxiety, emotional volatility, and negative emotionality [Soto & John, 2017]. Hajcak et al. (2004) established that Neuroticism correlates strongly with an enhanced error-related negativity (ERN)—the electrophysiological signature of the anterior cingulate cortex's error-monitoring system—indicating a chronically hyperactivated sensitivity to uncertainty and potential failure [Hajcak et al., 2004]. Tett and Burnett (2003) formalized how this latent disposition translates into observable behavior through Trait Activation Theory: traits express as behaviors when situationally relevant cues are present [Tett & Burnett, 2003]. An ambiguous radiograph accompanied by a low-confidence AI prediction is precisely such a cue. Eysenck et al. (2007) formalized in Attentional Control Theory that the hyperactivated performance-monitoring system in highly anxious and neurotic individuals is highly sensitive to conflicting informational streams, forcing the continuous recruitment of top-down compensatory cognitive resources—essentially a mandatory System 2 cognitive state—to maintain control [Eysenck et al., 2007].

Empirical support for this pathway in human-AI interaction is robust. While Saini et al. (2026) identified that high Neuroticism systematically induces AI skepticism [Saini et al., 2026], recent empirical work has measured Big Five traits in professionals using AI decision support, demonstrating that specific traits like Neuroticism are associated with a differential reliance on algorithmic recommendations (Lacroux & Martin-Lacroux, 2022). Expanding on this, Montag et al. (2023) demonstrated that the anxiety-driven components of Neuroticism fundamentally rewire the perception of algorithmic competence: high-Neuroticism individuals exhibit heightened fear and significantly reduced trust in AI, approaching the technology with elevated skepticism rather than viewing it as an authoritative oracle (Montag et al., 2023).

The central prediction of the present study follows: high Neuroticism should predict lower over-reliance and higher annotation accuracy, functioning as an internal cognitive forcing function. However, this signal can only be statistically recovered from a reference standard free of systematic directional bias. If the ground truth encodes the same false negatives that trigger appropriate skepticism linked to higher neuroticism as correct outcomes, the trait that protects against automation bias is rendered statistically invisible. Empirically unmasking this interaction is the purpose of the Platinum Standard methodology introduced in this study.



3. METHODS
3.1 Study Design
We employed a crossover repeated-measures design with an MRMC-style stimulus structure, aligning with standard frameworks for evaluating diagnostic accuracy in radiology human factors research and the framework specified by the FDA for evaluating computer-aided detection (CAD) devices [Obuchowski, 2000; FDA, 2022]. Fifty-one participants were randomized at enrollment into two treatment groups: Group A (No-AI first; n = 27) and Group B (AI first; n = 24). Each participant completed two annotation sessions separated by a mandatory 28-day washout period, locked at the application level via server-side timestamp enforcement. In Session 1, Group A annotated the full image set without AI assistance while Group B annotated the same set with AI assistance; conditions were reversed in Session 2, so that every participant served as their own control across both experimental conditions. The 28-day interval was selected to minimize learning and memory carryover from the specific stimulus set, consistent with FDA CAD evaluation guidance [FDA, 2022]. To test for residual carryover, we estimated a GEE interaction model with Condition × Session as predictors; the interaction term was non-significant (p = 0.554), providing no statistically detectable evidence of carryover effects and supporting the validity of the crossover design.

Pre-registration and hypothesis hierarchy. This study was not formally pre-registered with a third-party registry prior to data collection. The original study hypothesis, specified before data collection, posited that Conscientiousness and non-verbal intelligence (ICAR-6) would predict annotation accuracy—a theoretical prediction grounded in published literature on diligence and cognitive ability in structured judgment tasks. These constitute the primary pre-specified hypotheses. Neuroticism was included as a pre-specified secondary predictor, motivated by its theoretical link to error-monitoring and uncertainty aversion (§2.6). Its emergence as a statistically significant predictor should be interpreted strictly within this hierarchy: the primary hypotheses were unsupported, and the Neuroticism finding—while theoretically coherent—is a secondary result from a study that was not formally pre-registered. All characterizations of this finding as hypothesis-generating reflect this epistemic status, not rhetorical hedging.


[Figure 1: MRMC crossover flow diagram]


3.2 Participants
68 Hungarian high school students were recruited through school partnerships. Of 68 enrolled participants, 27 were randomized to Group A (No-AI first) and 41 to Group B (AI first). Of the 68 enrolled, 51 completed both sessions (75.0% completion rate). The 17 non-completers were excluded for the following documented reasons: session absence due to illness (n = 9; Group A: 4, Group B: 5) and session absence due to scheduling conflict (n = 8; Group A: 4, Group B: 4). All 51 completers contributed data to the analytic cohort; no participant was excluded from analysis after completing both sessions. However, because baseline psychometric data were not collected for participants who did not complete the study, non-differential attrition cannot be empirically verified—this is addressed as a limitation in §5.7. The final cohort comprised 27 males (52.9%) and 24 females (47.1%) aged 15 to 18 years (mean = 16.41, SD = 0.67). No participant had any medical or healthcare background, confirmed at enrollment as an explicit inclusion criterion and consistent with the non-expert annotation paradigm [Jeon et al., 2025].

To ensure balanced session duration—as the No-AI session flow was substantially shorter—each group completed the two validated psychometric instruments exclusively during their respective No-AI session (Group A: Session 1; Group B: Session 2), as shown in Figure 1. The Big Five personality traits were assessed using the Hungarian-validated BFI-2 [Reinhardt 2020], a 60-item self-report instrument producing five domain scores on a 1–5 Likert scale. Cohort descriptives were as follows: Open-Mindedness (M = 3.77, SD = 0.63), Conscientiousness (M = 3.38, SD = 0.72), Extraversion (M = 3.41, SD = 0.70), Agreeableness (M = 3.65, SD = 0.51), and Neuroticism (M = 2.98, SD = 0.80). Non-verbal fluid intelligence was assessed using the ICAR-6, a six-item matrix reasoning scale from the International Cognitive Ability Resource [Condon & Revelle, 2014]. The cohort produced a mean ICAR-6 score of 1.12 out of 6 (SD = 1.63)—a floor effect reflecting an instrumentation mismatch: the ICAR-6 is normed for adult populations and proved too difficult to generate meaningful variance in this adolescent cohort. This floor effect eliminates statistical power to detect any association between fluid intelligence and annotation performance; accordingly, no valid inference regarding the role of fluid intelligence can be drawn from these data. The ICAR-6 findings are reported for transparency, not as evidence about cognitive ability. Multicollinearity between all predictors was negligible (all VIF < 1.5).

3.3 Stimulus Set and Annotation Interface
Stimulus set. The 50 radiographic stimuli were anteroposterior knee X-rays drawn exclusively from the test set of the Osteoarthritis Initiative (OAI) public repository [Chen, 2018], ensuring that no image had been seen by the AI model during training. Images spanned the Kellgren-Lawrence grading distribution relevant to binary pathology classification, including cases at the clinically ambiguous (KL1).

AI model. Binary osteoarthritis classification was provided by a ResNet-18 convolutional neural network trained on a separate, train set of the OAI database under the original repository labels, achieving 74.1% accuracy against those labels. The model was trained as a strict binary classifier, with KL1 images excluded from the training set to avoid the label ambiguity inherent in that grade; KL0 was mapped to Negative and KL2+ to Positive. As a consequence, the model had no direct training exposure to diagnostically ambiguous cases. This sub-optimal performance was deliberate, mirroring the DANNY framework's design principle of studying AI reliance behavior under an imperfect algorithm rather than evaluating model performance per se [Jeon et al., 2025]. For each image, the model produced a binary prediction (Positive / Negative for osteoarthritis) and a continuous confidence score (0–1).

Annotation interface and trial flow. The annotation platform was a custom web application delivering a structured, multi-step trial for each of the 50 images. In all steps involving the radiograph, participants could view the image with standard zoom-in and zoom-out controls. The trial images were sequenced in random order for all participants in both sessions to control for case difficulty and order bias.
In the No-AI condition, each trial proceeded in two steps: (1) the participant viewed the knee radiograph with zoom controls, entered a binary diagnosis (Positive / Negative for osteoarthritis); (2) upon submitting the diagnosis, the participant rated their decision confidence on a 7-point Likert scale (1 = Uncertain; 7 = Certain). In the AI condition, the trial extended to four sequential steps designed to capture the pre-AI independent judgment, AI evidence exposure, and post-AI decision separately:

Feature annotation and initial diagnosis: For each of the two radiographic features (osteophytes and narrowed joint space), participants selected one of three options from a dropdown: 'symptom', 'ambiguous', or 'no symptom'. If 'symptom' was selected, drawing a bounding box around the feature was mandatory; if 'ambiguous' was selected, drawing was optional; and if 'no symptom' was selected, drawing was disabled. After completing feature annotation, the participant submitted a binary diagnosis before any AI output was displayed, locking a pre-AI decision into the record.
Initial confidence rating: A modal panel immediately prompted the participant to rate their confidence in the submitted diagnosis on a 7-point scale (1 = Uncertain; 7 = Certain), recorded as the pre-AI confidence.
AI analysis panel: A dedicated panel ("AI Elemzés") was then rendered over the radiograph, presenting three elements simultaneously: the AI's binary classification displayed (Positive / Negative), the AI's prediction confidence expressed as a numerical percentage (e.g., "Az AI magabiztossága: 54%"), and a Gradient-weighted Class Activation Mapping (Grad-CAM) heatmap overlaid on the radiograph to visualize the spatial regions driving the AI's prediction. Participants could navigate among three display states of the AI output (heatmap overlay, original image, and a feature-overlap indicator). A dropdown control allowed revision of the diagnosis prior to final submission ("Végleges döntés").
Final confirmation and post-AI confidence rating: A summary panel ("Végső Megerősítés") displayed the locked final decision and prompted a second 7-point confidence rating, capturing any shift in certainty induced by exposure to the AI output.

This four-step structure yields, for every AI-condition trial, a complete record of: (a) the initial human judgment prior to AI exposure, (b) the AI binary prediction and numerical confidence, (c) the Grad-CAM spatial attention map, (d) the final human decision (which may have been revised following AI review), and (e) post-AI confidence ratings. This design enables the computation of the full AI reliance taxonomy—appropriate reliance, over-reliance, appropriate skepticism, and unwarranted skepticism—at the individual trial level.

Before the annotation sessions, all participants completed a mandatory educational video module corrected by a board-certified radiologist with 20 years of clinical experience (independent from the Platinum Standard panel). The module trained participants on a binary Positive/Negative diagnostic framework based on three specific radiographic features: narrowed joint space, marginal osteophytes, and subchondral sclerosis (explained as bone whitening due to mechanical pressure). To ensure compliance, a front-end mechanism prevented participants from advancing to the scored trials until the video was watched in its entirety. No unscored practice images were provided; participants applied the video instruction directly to the trial stimuli.


[Figure 2: Annotation interface screenshots — AI-condition trial flow, four steps]

3.4 Ground Truth Construction: The Platinum Standard
The original OAI repository labels were utilized as the initial reference standard for the first stage of the experiment. However, preliminary analysis revealed evidence suggesting substantial label noise, which necessitated a formal ground truth validation investigation. Specifically, in five image cases, a significant majority (95%) of non-expert annotations concurred with the AI model's prediction, yet the original OAI label was discordant. This unexpected, systematic disagreement between the collective non-expert judgment, the AI's output, and the repository label—quantified as a 28% overall discordance from theoretically expected accuracy rates—demonstrated non-random error and prompted the construction of the independent Platinum Standard ground truth in seven pre-specified steps.

Step 1. Original OAI KL labels served as the starting point for all preliminary analyses.

Step 2. The discordance pattern was quantified (28% of images were implicated in unexpected decision patterns), confirming its non-random character and motivating expert re-annotation.

Step 3. Three board-certified radiologists independently annotated a set of 60 images on the full KL scale (0–4): the 50 study images annotated by participants, plus 10 additional images carrying original OAI KL1 labels. The 10 supplementary images were added as a blinded enrichment set to prevent cognitive anchoring toward binary classification during annotation—had the set contained only the 50 study images, the distribution of pathology severity might have cued raters toward a binary frame of reference. Images were presented to each radiologist in a randomized order. All three radiologists annotated the full set independently, in separate sessions, with no access to the original OAI labels, to each other's ratings, or to any AI model outputs. Before the session, raters were provided with a short Kellgren-Lawrence grade anchoring image reference. For each image, the annotation platform required them to assign a full KL grade and an associated confidence score, with only image magnification and color inversion available as decision aids.

Step 4. Following independent annotation, the three sets of Kellgren-Lawrence (KL) grades were subjected to a pre-specified consensus protocol. Images were first classified according to a binary scheme: KL grade 0 was defined as Negative, and grades KL 2, 3, and 4 were defined as Positive. A case was automatically assigned to the Platinum Standard without review if all three independent raters unanimously provided a grade within the same binary category (e.g., three grades of KL 3, 4, and 3 resulted in an automatic Positive assignment). Only cases lacking this complete binary consensus—i.e., those with disagreement or mixed ratings across the binary boundary, such as a rating of KL 2, 2, and 1—were selected for the structured consensus meeting. The three radiologists then convened a structured 40-minute consensus meeting, facilitated by a fourth radiologist not involved in the independent annotation phase. These flagged cases were reviewed sequentially in a randomized order, with discrepancies discussed explicitly and resolved by consensus where possible. Majority rule was applied in the rare instances where deliberation did not yield full agreement.

Step 5. Pre-consensus inter-rater reliability (IRR) was calculated using Fleiss' κ across all three independent raters. Critically, the Platinum Standard panel adjudicated 23 of the 50 study images as KL1—14 originally labeled KL0 and 9 originally labeled KL2+ in the OAI repository—images whose diagnostic status is inherently indeterminate and therefore inadmissible as a binary behavioral ground truth. Under the primary analytical strategy (Strategy A, see §3.5), these 23 images were excluded, reducing the behavioral analysis stimulus set from 50 to 27 images. The resulting class distribution was approximately 21 Positive (KL2+) to 6 Negative (KL0), yielding a 3.5:1 imbalance and a naïve majority-class baseline of 77.8%.

Step 6. To quantify the informational value of the Platinum Standard relative to the original OAI labels, GEE models were pre-specified to run in parallel under both ground truths. This parallel analysis was designed to isolate how the corrected reference standard unmasks valid psychometric effects that the original noisy labels suppressed.

Step 7. Independent corroboration of the label noise was pre-specified to be evaluated using the AI model's own confidence scores, under the hypothesis that the model would exhibit significantly lower confidence on false-negative images than on stable negative or positive images.

Radiologist panel characterization. The ground truth construction panel comprised four board-certified radiologists — three independent annotators and one consensus facilitator — each with a minimum of five years of post-certification clinical experience. Direct inquiry at recruitment confirmed that none of the panel members had prior exposure to the OAI dataset or the AI model used in this study.

Blinding mechanism. Structural blinding was enforced at the platform level throughout the independent annotation phase. The annotation interface presented each radiologist with the radiographic image only; no original OAI labels, no AI model predictions, and no other participants' annotations were accessible or displayed at any point during independent annotation. The platform recorded each annotation under a participant anonymization token. When the three independent annotation sets were compiled for the consensus meeting, each radiologist viewed only their own prior responses alongside those of the other two raters; original OAI reference labels were not present in the consensus interface. This constitutes structural, platform-enforced blinding rather than reliance on a verbal instruction.


3.5 Statistical Analysis
All inferential analyses were conducted in parallel under both the original OAI labels and the Platinum Standard to enable direct quantification of how ground truth quality affects downstream behavioral and psychometric inferences. This dual-GT analysis strategy was pre-specified upon identification of the ground truth problem, not applied post-hoc.

Primary model. The primary statistical model was Generalized Estimating Equations (GEE) with an exchangeable working correlation structure and a binomial family (logit link), which appropriately accounts for the within-participant clustering arising from repeated observations across images and two sessions [Liang & Zeger, 1986]. Odds ratios (OR) with 95% confidence intervals are reported throughout.

Sensitivity checks. Two pre-specified sensitivity analyses were conducted: (1) a Wilcoxon signed-rank test on participant-level accuracy pairs (AI vs. No-AI condition) to corroborate GEE estimates without distributional assumptions, and (2) Firth's penalized logistic regression applied to binary reliance outcomes to address potential complete separation arising from the small number of over-reliance events.

KL1 ambiguity strategies. Because the Platinum Standard adjudicated 23 images as KL1—a grade that does not map unambiguously to either binary class—the treatment of these images constitutes an analytical decision with potential influence on all downstream estimates. Three pre-specified strategies were defined and all GEE models were rerun under each: Strategy A (Exclude), the primary analysis, removes all Platinum KL1 images entirely, yielding 27 images with unambiguous binary labels; Strategy B (Clinical Mapping) assigns KL1 to Negative, reflecting the conservative radiological convention that equivocal evidence should not trigger a positive diagnosis; Strategy C (Sensitivity) assigns KL1 to Positive, testing the upper boundary of pathology inclusion. Concordance of findings across all three strategies is reported in the Results as evidence of robustness.

Terminology. We define "appropriate AI reliance" as the behavioral category in which an annotator's final decision agrees with the AI when the AI is correct, or correctly overrides the AI when it is wrong—as operationalized in Table 3. The complementary failure modes are "over-reliance" (accepting AI errors) and "unwarranted skepticism" (overriding correct AI predictions). These definitions follow Goddard et al. (2012) and are consistent throughout the manuscript.

Multiple testing corrections. Benjamini-Hochberg false discovery rate (FDR) correction was applied to all psychometric predictor p-values across the six predictors (five Big Five traits plus ICAR-6); both uncorrected and FDR-corrected p-values are reported.

Performance metrics. Given the 3.5:1 class imbalance in the primary analysis stimulus set (naïve majority-class baseline: 77.8%), raw accuracy alone is an incomplete and potentially misleading summary measure. Balanced accuracy, F1 score, sensitivity, specificity, and AUROC are therefore reported alongside raw accuracy for all condition comparisons and AI model evaluations.

All analyses were conducted in Python 3.9 using statsmodels (GEE, Firth regression), scipy (non-parametric tests), and scikit-learn (performance metrics).


4. RESULTS
4.1 Ground Truth Validation: The Platinum Standard
The transition from the original OAI repository labels to the Platinum Standard revealed systematic and directionally biased label noise across the 50-image stimulus set. Table 1 summarizes the 5×5 grade-level transition matrix. Of the 25 images originally graded KL0 (Negative), the radiologist panel reclassified 14 as KL1 and 5 as KL2+, producing a substantial net false-negative mass in the original dataset. No image was revised in the opposite direction: of the 25 images originally graded KL2 or above (Positive), all remained in the Positive class or moved only into the ambiguous KL1 region (9 images downgraded from KL2 to KL1). The error structure was therefore not random. A binomial test for directional bias confirmed that false-negative label corrections significantly exceeded false-positive corrections (5 images confirmed as genuine false negatives vs. zero false positives; p = 0.031).


Table 1. Ground truth transition matrix (N = 50 images).

The panel adjudicated 23 of the 50 images as KL1—the diagnostically indeterminate grade. Under the primary analysis strategy (Strategy A: Exclude), these images were removed from behavioral analyses, yielding a final stimulus set of 27 images with unambiguous binary labels (21 Positive [KL2+], 6 Negative [KL0]; 3.5:1 class imbalance; naïve majority-class baseline: 77.8%). The pre-consensus inter-rater reliability was Fleiss' κ = 0.181 (95% CI: [0.042, 0.300]; slight agreement) on the full five-grade KL scale, and Fleiss' κ = 0.517 (95% CI: [0.175, 0.752]; moderate agreement) on binary classification excluding KL1. Both values are consistent with the published literature for radiologist agreement on the KL scale [Khela et al., 2024; Landis & Koch, 1977] and confirm the structural subjectivity of the instrument rather than a study-specific limitation. Within-1-grade agreement was 84.0%, indicating that the radiologists reached a coarse severity consensus even where exact grades differed.

Independent corroboration was obtained from the AI model's own confidence scores (Figure 3). On the five images reclassified as false negatives (Original KL0 → Platinum KL2+), the ResNet-18 produced a mean confidence of 0.317, compared with 0.710 on stable negatives and 0.776 on stable positives. A Kruskal-Wallis test confirmed that this difference was statistically significant across the three subgroups (H = 8.631, p = 0.013). Two independent lines of evidence—expert radiologist consensus and AI model uncertainty—converged on the same five images, providing strong corroboration that the original OAI labels on those images were inherently unstable.


Figure 3: AI Confidence on Mislabeled Images — box plots with individual data points for stable negatives (0.710), corrected false negatives (0.317), and stable positives (0.776). Kruskal-Wallis p = 0.013.

4.2 Annotation Performance Under Both Ground Truths
Table 2 presents annotation accuracy stratified by AI condition and ground truth. The two results, read together, constitute the study's primary empirical finding.

Ground Truth
Condition
Accuracy
F1
Sensitivity
Specificity
AUROC
GEE OR (AI vs No-AI)
95% CI
p (GEE)
p (Wilcoxon)
Original OAI
AI
65.3%
0.676
72.4%
58.2%
0.653
1.232
[1.083, 1.401]
0.003
0.003
Original OAI
No-AI
60.4%
0.630
67.2%
53.7%
0.604
Reference
—
—
—
Platinum
AI
80.8%
0.867
80.7%
81.4%
0.810
1.164
[0.933, 1.453]
0.178
0.037
Platinum
No-AI
78.4%
0.852
79.9%
72.9%
0.764
Reference
—
—
—

Table 2. Human annotation performance by condition and ground truth.

GEE with exchangeable working correlation, clustered by participant_id. Wilcoxon signed-rank on participant-level accuracy pairs (n = 51). Original OAI metrics computed over the full 50-image balanced stimulus set (N = 2,550 trials per condition; 1,275 positive, 1,275 negative); for this perfectly class-balanced set, Balanced Accuracy = AUROC = raw Accuracy. Platinum Standard metrics computed over the 27-image Strategy A: Exclude subset (N = 1,377 trials per condition; 1,071 positive, 306 negative). Carryover interaction (Condition × Session) non-significant (p = 0.554) under all strategies.

Under the original OAI ground truth, AI assistance appeared to yield a large and significant accuracy gain of 4.9 percentage points (60.4% → 65.3%). Both the primary GEE model (OR = 1.232, 95% CI [1.083, 1.401], p = 0.003) and the Wilcoxon sensitivity check (W = 314, p = 0.003) were highly significant. A repeated-measures ANOVA confirmed the result (F(1, 50) = 10.03, p = 0.003). The participant-level effect size was Cohen's d = 0.60—a large effect by conventional benchmarks. Read in isolation, this constitutes a compelling demonstration of AI benefit.

Under the Platinum Standard ground truth, the same participants annotating the same images produced a materially different result. Unassisted accuracy rose to 78.4% (Balanced Accuracy: 76.4%; F1: 0.852), substantially higher than estimated under the original GT. AI assistance produced a further 2.4 percentage point increment (80.8%; Balanced Accuracy: 81.0%; F1: 0.867). The primary GEE model was non-significant (OR = 1.164, 95% CI [0.933, 1.453], p = 0.178). The Wilcoxon test was significant (W = 317, p = 0.037). The three-strategy sensitivity analysis confirmed the GEE non-significance regardless of how KL1 images are handled: Strategy B (KL1 → Negative; OR = 1.015, p = 0.841) and Strategy C (KL1 → Positive; OR = 1.107, p = 0.271) were likewise non-significant. Full human annotation confusion matrices for all three strategies are provided in Appendix A, demonstrating that the core performance metrics are directionally consistent across the stimulus set reduction decision.

The divergence between the GEE and Wilcoxon results under the Platinum GT warrants methodological consideration. GEE estimates a marginal, population-averaged odds ratio for the AI condition effect while appropriately accounting for the within-participant clustering arising from 27 image-level observations nested within each of 51 participants across two sessions. This modelling of the correlation structure makes GEE more conservative than participant-level aggregates: it down-weights consistent small effects that appear large when heterogeneous within-person variance is ignored. Wilcoxon operates on participant-level accuracy means—each participant's 27 trials collapsed into a single proportion—and is sensitive to consistent directional trends even when per-participant magnitudes are modest. In the Platinum GT analysis, AI condition accuracy exceeded No-AI accuracy for 29 of 51 participants (versus 18 worse, 4 unchanged), producing a directionally consistent but small-magnitude effect that the Wilcoxon test detected and the GEE's within-person clustering adjustment did not. This divergence carries a specific interpretive message: the AI benefit under the Platinum GT is marginal, individually heterogeneous, and sensitive to the level of aggregation at which it is measured. Under the Original GT, the benefit was large and homogeneous enough to survive both tests simultaneously. Under the Platinum GT, it is not. Both tests were pre-specified; reporting only the significant Wilcoxon result would have constituted selective reporting.


Figure 4: The Accuracy Paradox — four-bar grouped chart showing accuracy under the Original GT (orange) and Platinum GT (blue) for four agents/conditions: AI Model (74.1% / 77.8%), Human Overall (76.1% / 79.6%), Human No-AI (74.9% / 78.4%), and Human AI-Assisted (77.3% / 80.8%). The upward shift of all bars from orange to blue is the visual signature of directional label noise suppressing true performance estimates under the original OAI ground truth.

4.3 Reliance Behavior Taxonomy Under Both Ground Truths
Table 3 presents the four-category reliance taxonomy. The ground truth correction reduced measured over-reliance by half (15.6% → 7.8%; McNemar p < 0.0001), but the interpretive importance of this shift lies in its directionality, not its volume.

Reliance Category
Original GT (50 imgs)
95% CI
Platinum GT (27 imgs)
95% CI
Shift
Over-reliance
15.6%
[14.5%–16.6%]
7.8%
[6.1%–9.4%]
−7.8%
Appropriate skepticism
14.4%
[13.4%–15.5%]
14.5%
[12.9%–16.1%]
+0.1%
Appropriate reliance
50.9%
[48.5%–53.3%]
66.4%
[64.4%–68.2%]
+15.5%
Unwarranted skepticism
19.1%
[16.7%–21.5%]
11.4%
[9.5%–13.3%]
−7.7%

Table 3. Mean reliance rates by ground truth (AI condition trials; N = 51 participants; participant-level bootstrap 95% CIs, 5,000 iterations).

McNemar test for over-reliance shift: p < 0.0001. Over-reliance = participant agrees with AI error; Appropriate skepticism = participant correctly overrides AI error; Appropriate reliance = participant agrees with correct AI; Unwarranted skepticism = participant incorrectly overrides correct AI. Original GT rates computed over the full 50-image stimulus set (N = 51 × 50 = 2,550 AI-condition trials). Platinum GT rates computed over the 27-image Strategy A: Exclude subset (N = 51 × 27 = 1,377 AI-condition trials). The image-set reduction is a consequence of the Platinum Standard construction pipeline and is therefore not held constant across ground truths.

Under the original OAI ground truth, the 15.6% over-reliance rate appeared to be distributed across both false-positive and false-negative AI error directions. This made the over-reliance appear as a relatively balanced calibration problem. Under the Platinum Standard, the error distribution became fully unambiguous: 100% of measured over-reliance events were false-negative acceptances—cases in which a participant agreed with the AI's failure to detect genuine pathology. There were zero false-positive over-reliance events. A binomial test for the null hypothesis that FN and FP over-reliance events are equally common yields p < 0.0001 in the FN-dominant direction. The directional bias is absolute..

This asymmetry has a structural explanation. Because the original OAI GT independently coded the AI's false-negative predictions as correct—it labeled those images KL0; the AI predicted KL0—any participant who accepted the AI's erroneous negative prediction was scored as having annotated correctly. The over-reliance event was mathematically invisible: the human agreed with the AI's error, and the noisy reference standard registered the outcome as accurate. The Platinum GT resolves this alignment, making the AI's systematic clinical failure mode—and the human tendency to accept it—statistically visible.

The large drop in unwarranted skepticism (19.1% → 11.4%) is the complement of this correction. Under the original GT, participants who correctly identified pathology on a false-negative image and rejected the AI's erroneous suggestion were scored as having made an error (they disagreed with both the AI and the noisy GT). The Platinum GT reclassifies these decisions as appropriate skepticism—behavioral signal that had been misidentified as noise. Appendix A presents the full human confusion matrices under all three KL1 handling strategies, confirming that this directional pattern in the reliance taxonomy is not an artifact of the 50→27 image reduction.

Figure 5: Reliance Taxonomy by Participant — stacked bar chart, participants sorted by over-reliance rate. Four categories in distinct colors. Visual demonstration that a minority of participants drives aggregate over-reliance, and that appropriate reliance constitutes the plurality of AI-condition decisions.

4.4 Psychometric Predictors: The Central Finding
Table 4 presents the GEE results for psychometric predictor models under both ground truths. The contrast between the two analytic conditions is the paper's central empirical finding.

Under the original OAI ground truth, no personality trait predicted annotation accuracy at conventional significance thresholds. Neuroticism yielded OR = 0.940 (95% CI [0.857, 1.032], p = 0.194; M3 full model). The parallel GEE model for false-negative over-reliance returned a non-significant Neuroticism coefficient (coefficient = −0.083, p = 0.065). The Spearman correlation between individual Neuroticism scores and personal over-reliance rates was ρ = −0.218 (p_raw = 0.124; p_FDR = 0.441) — directionally consistent with the hypothesis but well below significance after FDR correction. Conscientiousness, the pre-registered primary predictor, was likewise null (M3: OR = 1.071, p = 0.212).

Under the Platinum Standard ground truth, the associations with psychometric predictors changed substantially. Neuroticism emerged as a statistically significant positive predictor of annotation accuracy in both the standalone model (M2: OR = 1.171, 95% CI [1.016, 1.349], p = 0.029) and the fully adjusted model controlling for image difficulty and AI correctness (M3: OR = 1.178, 95% CI [1.017, 1.366], p = 0.029). The near-identical magnitude of the Neuroticism coefficient in M2 and M3 constitutes a direct robustness check: including AI correctness as a covariate — despite its potential circularity under the Platinum Standard — left the Neuroticism estimate substantively unchanged (Δ OR = 0.007), confirming that the psychometric signal is not an artifact of covariance with the AI performance term. The over-reliance model was even stronger: Neuroticism was a highly significant negative predictor of false-negative over-reliance (GEE coefficient = −0.429, p < 0.001). The individual-level Spearman correlation confirmed this relationship (ρ = −0.390; p_raw = 0.005; p_FDR = 0.028). A one-sided test for the reverse hypothesis — that Neuroticism predicts higher over-reliance — yielded p = 0.9998, providing essentially decisive evidence against it. The Neuroticism × Condition interaction term was non-significant (p = 0.828), indicating that the trait's benefit was not specific to the AI condition and reflected genuine individual differences in annotation quality under the valid reference standard.


Predictor
Platinum GT OR
95% CI
p
Original GT OR
95% CI
p
AI condition
1.172
[0.930, 1.477]
0.178
1.253
[1.091, 1.440]
0.001
Neuroticism
1.178
[1.017, 1.366]
0.029
0.940
[0.857, 1.032]
0.194
IQ (ICAR-6)
0.948
[0.890, 1.011]
0.103
1.001
[0.954, 1.050]
0.979
Conscientiousness
0.964
[0.811, 1.147]
0.681
1.071
[0.961, 1.194]
0.212
Image difficulty (KL)
1.397
[1.256, 1.554]
<0.001
1.472
[1.306, 1.660]
<0.001
AI correctness
2.317
[1.819, 2.951]
<0.001
2.129
[1.882, 2.407]
<0.001

Table 4. GEE model comparison: psychometric predictors under both ground truths (M3: full model).

GEE with exchangeable working correlation, clustered by participant_id. N = 2,754 trial-level observations (Platinum, Strategy A). All psychometric p-values are FDR-corrected (Benjamini-Hochberg) within each GT; presented values are uncorrected; Neuroticism survives FDR correction under the Platinum GT (p_FDR = 0.029). Bold: p < 0.05. Table columns are symmetric: Platinum GT (OR | 95% CI | p) followed by Original GT (OR | 95% CI | p) for each predictor, enabling direct side-by-side comparison of the ground truth effect on each coefficient.

No other personality trait reached FDR-corrected significance under either ground truth. The ICAR-6 produced a non-significant coefficient in all models (Platinum: OR = 0.948, p = 0.103; Original: OR = 1.001, p = 0.979). Critically, this output should not be described as a null finding about fluid intelligence. As documented in §3.2, the cohort's near-floor ICAR-6 distribution (M = 1.12/6, SD = 1.63) reflects an instrumentation mismatch: the tool proved too difficult to generate meaningful variance in this adolescent population. The statistical output is therefore an artifact of the instrument, not evidence about whether cognitive ability influences annotation performance. No valid inferences regarding the role of fluid intelligence can be drawn from this study.

4.5 Session and Temporal Effects
Annotation performance declined significantly from Session 1 to Session 2 across the full cohort, independent of condition assignment (GEE OR = 0.763, 95% CI [0.624, 0.934], p = 0.009). This cohort-wide decline likely reflects a combination of reduced novelty engagement and mild cognitive fatigue with the interface over the two-session study. The Condition × Session interaction was non-significant (p = 0.554), confirming the absence of carryover effects and validating the crossover structure.

Within this overall decline, Group 1 participants—those who received AI assistance in Session 1—exhibited a notably larger drop upon transition to the unassisted condition in Session 2. Group 1 mean accuracy fell from 83.6% (Session 1, AI) to 76.5% (Session 2, No-AI; paired t = 3.655, p = 0.001; Wilcoxon p = 0.003 under Platinum GT). Group 0 showed no comparable between-session shift. Critically, the Condition × Session interaction term was non-significant (p = 0.554), which means that while the overall cohort Session 2 decline cannot alone explain the magnitude of the Group 1 drop, we also cannot statistically rule it out as a contributing factor. The observed pattern is consistent with a withdrawal of AI scaffolding upon which performance partially depended, but the non-significant interaction prevents definitive attribution independent of general temporal decline.

Trial duration data are broadly consistent with this interpretation. AI-condition trials required a mean of 25.43 seconds versus 6.85 seconds in the unassisted condition (paired t = 20.781, p < 0.0001)—a nearly fourfold difference attributable to processing the AI output panel, Grad-CAM visualization, and numerical confidence score. A habituation effect was evident: AI-condition trial duration shortened by 6.0 seconds from early to late trials (versus 0.43 seconds in the unassisted condition), indicating that participants learned to process the interface more efficiently. Whether this processing time translated into diagnostic learning that could be retained without the AI panel is an open question; the Session 2 accuracy data are consistent with the possibility that it did not.



5. Discussion
5.1 Opening Summary
We set out to test a theoretically motivated hypothesis regarding psychometric predictors of annotation performance. We must explicitly acknowledge the hierarchy of these predictors, set prior to data collection: our pre-registered primary hypothesis posited that Conscientiousness and non-verbal intelligence would predict annotation accuracy. This primary hypothesis was not supported under either ground truth. Neuroticism was included as a pre-specified secondary hypothesis, positing that its anxiety-linked trait properties (chronically activating error-monitoring circuitry) would predict lower over-reliance on a sub-optimal AI. Under the original OAI ground truth, this secondary hypothesis was also not supported. The GEE model returned a Neuroticism odds ratio of 1.035 (p = 0.482)—a null result unremarkable enough to have ended the inquiry. It did not end it, because the data simultaneously produced a pattern that made the null implausible: a 28% discordance between participant behavior and the expected consequences of automation bias. That discordance triggered a formal ground truth investigation, the results of which became the paper's primary contribution.

The Platinum Standard re-evaluation isolated the effect of label noise while holding participant, image, and AI characteristics constant. Under the radiologist-validated Platinum Standard, Neuroticism was associated with higher annotation accuracy (M3: OR = 1.178, 95% CI [1.017, 1.366], p = 0.029) and lower false-negative over-reliance (GEE coefficient = −0.429, p < 0.001; Spearman ρ = −0.390, p_FDR = 0.028). This association must be interpreted as hypothesis-generating. A post-hoc power calculation revealed that the study had an estimated power of only 17% to detect the observed Neuroticism effect at N = 51. The probability of Winner's Curse—an inflated effect size estimate in an underpowered significant result—is therefore substantial. The Neuroticism signal warrants serious theoretical attention and confirmatory replication in a larger sample; it does not, in isolation, constitute a confirmed psychometric finding.

The sections that follow explain the mechanism by which this suppression operates (§5.2), what the recovered psychometric signal implies for annotation pipeline design (§5.3), what the temporal dynamics of AI scaffolding reveal about knowledge transfer (§5.4), and what the combined findings demand from the field as a methodological standard (§5.5). The limitations of the present evidence are addressed in §5.6.

5.2 The GT noise suppressor mechanism: primary theoretical contribution
The central conceptual contribution of this paper is the identification and empirical demonstration of a phenomenon we term the ground truth noise suppressor mechanism. When the reference standard contains systematic directional bias, it actively masks valid psychometric and behavioral signals in human-AI annotation.

The mechanism originates in the structure of the original OAI ground truth [Chen, 2018]. As established in our results, the label noise in the original dataset was not random; it exhibited a strong false-negative bias. This asymmetry is consistent with the structural subjectivity of the KL scale at lower grades and the documented tendency of AI models to favor negative predictions when trained on highly imbalanced, ambiguous data [Tiulpin et al., 2019]. In the present study, the model's false-negative tendency has a more specific structural explanation: as described in §3.3, KL1 images were excluded from training entirely, meaning the model was never calibrated to the boundary zone where the most diagnostically ambiguous cases reside. When it encountered such cases in the test set, it classified them from the perspective of a model that had only learned what unambiguous negatives and positives look like — a training gap that directly accounts for the low confidence observed on the five false-negative images in §4.1.

It is precisely at this point of ambiguity that annotator personality governs the outcome. Faced with a low-confidence AI signal on a radiographically subtle case, an annotator must decide whether to defer to the algorithm or to maintain an independent judgment. High Neuroticism, through its characteristic error aversion and heightened sensitivity to uncertainty, functions as an internal cognitive forcing mechanism that sustains System 2 deliberative processing [Jeon et al., 2025; Kahneman, 2011; Zell & Lesick, 2022].

However, under the original OAI ground truth, the evaluation metric was structurally inverted. Because the original reference standard and the AI model shared the same false-negative bias, participants who correctly identified subtle pathology and rejected the AI's erroneous negative suggestion were penalized. The behaviors that constitute successful resistance to automation bias were coded as annotation errors, while uncritical AI acceptance was coded as correct performance. Consequently, the analytical framework effectively penalized the protective influence of Neuroticism, rendering the trait statistically invisible.

Ground truth validation resolves these distortions systematically. Validating the reference standard not only unmasks the true magnitude of automation bias but also reveals its clinical direction. Under the original labels, over-reliance appeared as a relatively balanced calibration problem. The Platinum Standard exposed a rigid, systemic failure mode: over-reliance was entirely driven by participants accepting the AI's failure to detect genuine pathology. Directional bias in a reference standard corrupts behavioral evaluation in a manner that tracks the AI's own systematic errors. All these distortions are resolved simultaneously by validating the ground truth.

The suppressor mechanism has an equity dimension that deserves explicit acknowledgment. Seyyed-Kalantari et al. (2021) demonstrated that AI algorithms trained on skewed public datasets — precisely the class-imbalanced OAI repository implicated here — reliably amplify underdiagnosis bias, with the magnitude of the effect falling disproportionately on marginalized subpopulations who are already underrepresented in training data [Seyyed-Kalantari et al., 2021]. When a reference standard carries false-negative bias aligned with this AI error pattern, the suppressor mechanism does not merely produce neutral measurement noise; it renders AI failures on disadvantaged populations statistically invisible in evaluation data. Annotators who correctly identify pathology that the AI missed — and who are more likely doing so on images of underrepresented patients — are penalized by the biased GT and their protective behavior goes undetected. Ground truth validation is therefore not only a methodological requirement for valid psychometric inference but a prerequisite for equitable evaluation of AI-assisted annotation systems.
5.3 Neuroticism as an Internal Cognitive Forcing Function
The signal recovered under the Platinum Standard does more than validate a psychometric prediction—it reopens a design question at the center of the annotation pipeline literature.

The DANNY framework, a well-studied instantiation of the non-expert annotation paradigm for musculoskeletal radiology, achieves its behavioral benefit through what Buçinca et al. (2021) term a cognitive forcing function: a mandatory procedural step that interrupts the default System 1 pathway before the AI output is revealed [Buçinca et al., 2021; Croskerry, 2003]. In DANNY's implementation, this takes the form of a Criteria Phase in which participants are required to identify and annotate specific radiographic features before accessing the algorithmic prediction [Jeon et al., 2025]. The present study deliberately omitted this external scaffolding element. The purpose of that omission was to test whether the absence of the Criteria Phase would be compensated — or only partially compensated — by individual-level psychological differences.

In this sample, participants with high Neuroticism scores exhibited the behavioral signature of System 2 activation without any external prompt to do so. Their false-negative over-reliance rates were substantially and specifically lower (GEE coefficient = −0.429, p < 0.001), and the direction was unambiguous: a one-sided test for the hypothesis that Neuroticism predicts higher over-reliance yielded p = 0.9998. Critically, the protective association was not a blanket expression of caution. The appropriate reliance rate under the Platinum Standard was 66.4%, and Neuroticism did not suppress this; high-Neuroticism annotators were not globally skeptical of the AI — they were specifically resistant to accepting the AI's errors. Trait Activation Theory provides the theoretical account: Neuroticism's latent error-aversion disposition is activated by situationally relevant cues, and a low-confidence AI suggestion on a diagnostically ambiguous image is precisely such a cue [Tett & Burnett, 2003]. In the absence of an external forcing function, the trait itself may have provided cognitive friction [Hajcak et al., 2004; Saini et al., 2026]. These interpretations are, however, hypothesis-generating: with an estimated post-hoc power of 17%, the observed association is substantially underpowered, and the magnitude of the effect should not be taken at face value.

This finding raises a question that the annotation pipeline design literature has not previously confronted: to what degree does the DANNY Criteria Phase achieve its effect by artificially inducing—in all participants—the same internal state that high-Neuroticism individuals enter organically? If the Criteria Phase functionally simulates the cognitive friction associated with high Neuroticism, two testable implications emerge. First, the marginal behavioral benefit of the Criteria Phase should be larger in low-Neuroticism annotators, for whom the internal forcing mechanism is weaker, than in high-Neuroticism annotators who already generate it spontaneously. Second, the overall effectiveness of an external scaffolding interface will depend in part on the personality composition of the annotator cohort it is evaluated against. Both are hypotheses for future work, not assertions from the current data. They are, however, directly motivated by what the present results empirically establish.

The practical implication for pipeline design is immediate. Personality screening need not replace interface scaffolding, but it can complement it as a risk stratification tool. In annotation contexts where external scaffolding is costly or operationally infeasible, selecting for or modeling the distribution of high-Neuroticism annotators may provide a meaningful, measurable reduction in false-negative over-reliance rates. Conversely, in large-scale pipelines where low-Neuroticism annotators predominate, the case for mandatory external forcing mechanisms is strengthened by our data.

While these implications are promising, the generalizability of findings from an adolescent cohort to adult annotation professionals must be considered. Adolescents may exhibit higher baseline variability in task engagement and different baseline distributions of the Big Five traits compared to adult populations. However, the non-expert, crowdsourced pipelines that frameworks like DANNY address frequently employ laypersons without specialized training. We expect the underlying mechanism — trait-based cognitive friction substituting for interface-based friction — to generalize to adult crowdsourced labelers, though the magnitude of the effect may vary based on maturity, financial incentives, and professional accountability.

5.4 Scaffolding Without Knowledge Transfer: The Brittle Benefit
The psychometric and methodological findings discussed above rest on the corrected Platinum Standard ground truth. The finding examined in this section does not. It holds under both reference standards, and that cross-GT consistency is precisely what earns it independent status as a secondary empirical contribution.

Group 1 participants — those who completed the AI-assisted condition in Session 1 — achieved a mean accuracy of 83.6% when AI scaffolding was available. When that scaffolding was removed in Session 2, their accuracy fell to 76.5% (paired t = 3.655, p = 0.001; Wilcoxon p = 0.003 under the Platinum GT; Wilcoxon p = 0.040 under the original GT). The Condition × Session interaction was non-significant (p = 0.554), which means we cannot definitively attribute the Group 1 drop to AI withdrawal as opposed to the general cohort-wide Session 2 decline (OR = 0.763, p = 0.009). The observed pattern is, however, consistent with a partial dependence on the AI scaffold: Group 0, which transitioned from unassisted to AI-assisted, showed no comparable between-session magnitude drop, whereas Group 1's decline was larger and directionally specific. We treat this finding as hypothesis-generating regarding scaffold dependency, not as a confirmed withdrawal effect.

The appropriate characterization of this pattern requires precision. In the medical training literature, "deskilling" refers to the degradation of pre-existing competence through sustained reliance on automation — a phenomenon relevant to credentialed clinicians [Parasuraman & Manzey, 2010]. Our cohort arrived with no prior clinical competence. The more parsimonious interpretation is therefore not deskilling but a possible failure of AI scaffolding to transfer knowledge: the AI may have improved measurable performance within the scaffolded session without producing generalizable cognitive learning that participants could sustain independently. The temporal evidence is broadly consistent with this account. AI-condition trial duration was 25.43 seconds on average versus 6.85 seconds in the unassisted condition (paired t = 20.781, p < 0.0001) — a nearly fourfold investment of time. If that time was spent processing the AI panel's output rather than constructing independent diagnostic representations, the Session 2 accuracy drop becomes plausible on a scaffolding-dependency account. Definitive evidence for this mechanism would require a study designed to disentangle it from temporal fatigue.

This has direct implications for annotation systems deployed in contexts where the goal is not only throughput but also annotator development. A system that improves immediate accuracy while suppressing the error signal necessary for learning produces annotators who are dependent on its continued presence. Future interface designs should consider whether modulating AI availability — for example, progressively withdrawing AI support across sessions, or introducing deliberate periods of unassisted practice — might preserve the throughput benefit while enabling knowledge consolidation [Croskerry, 2003].

These observations should be treated as hypothesis-generating rather than as a confirmed finding of scaffold dependency. The non-significant Condition × Session interaction (p = 0.554) prevents the scaffold-dependency interpretation from being cleanly distinguished from the general cohort-wide Session 2 decline (OR = 0.763, p = 0.009). A dedicated future study — specifically designed to isolate the AI withdrawal effect from temporal fatigue — would require a three-arm design: (a) AI-first/No-AI-second (Group 1 replication), (b) No-AI-only control across both sessions (to quantify the pure Session 2 decline without AI withdrawal), and (c) a delayed AI-introduction arm to establish baseline learning trajectories. Only under such a design could the Group 1 accuracy drop be partitioned into its AI-withdrawal and temporal-fatigue components with sufficient statistical precision.

5.5 Field-Level Implications: Proposed Minimum Reporting Standards
The suppressor mechanism demonstrated in this study is not a property of this particular dataset, this AI model, or this annotator cohort. It is a structural consequence of a general condition: any evaluation framework in which the reference standard's error direction is correlated with the AI system's error direction will suppress behavioral signals in the manner we have documented. This condition arises whenever an AI is evaluated against the same public dataset on which it was trained — and that condition is, at present, the default in the field, not the exception.

The DANNY framework offers the clearest illustration of the risk. Its foundational study evaluated non-expert annotation performance against reference labels derived from the same OAI repository whose systematic false-negative bias we have directly quantified here [Jeon et al., 2025]. The study's anomalous failure to observe expected baseline over-reliance rates — rates that Goddard et al. (2012) established at 15–30% in their systematic review published in this journal — is consistent with the suppressor mechanism and warrants future investigation [Goddard et al., 2012]. When an AI biased toward false negatives is evaluated against a ground truth independently biased toward the same false negatives, true over-reliance events are invisible: the human agrees with the AI's error, and the corrupted ground truth registers the outcome as correct. In the present study, over-reliance measured 15.6% under the original OAI labels — precisely within the Goddard range — and dropped to 7.8% under the Platinum Standard, a shift confirmed as non-random (McNemar p < 0.0001). Studies that evaluate annotator behavior against the OAI repository's original labels — including foundational work in this paradigm — may have encountered the suppressor mechanism we document here. Direct empirical investigation using parallel GT validation would be needed to confirm this.

We also investigated the mechanism through which AI assistance influences accuracy, testing the hypothesis that it operates via user confidence. The hypothesis was not supported: the bootstrap mediation analysis (5,000 iterations) showed that the indirect effect of AI condition on accuracy through final confidence was null (point estimate = 0.024; 95% CI: [−0.049, 0.096]). Path A (Condition → Confidence) was non-significant (p = 0.510), while Path B (Confidence → Accuracy) was strongly significant (p < 0.0001). Confidence shifted following AI exposure (paired t = −10.974, p < 0.0001; mean increase = 0.32 points), but this shift did not mediate the accuracy effect. This is an important negative finding with direct design implications: if AI assistance does not work through increased confidence calibration, then interfaces designed to manipulate confidence — such as ours, which displayed numerical AI confidence percentages — may be solving the wrong problem. Confidence calibration and accuracy improvement are distinct outcomes that require separate empirical validation.

5.6 Minimum Reporting Standards for Behavioral Inference
Against this background, we propose that ground truth validation should be treated as a mandatory methodological checkpoint in human-AI annotation research, not an optional sensitivity analysis or a supplementary appendix item. We suggest three minimum reporting requirements that should accompany any behavioral study in this domain (Table 5). These requirements do not demand the resource-intensive construction of a Platinum Standard for every study. They demand transparency about what is being measured and honesty about what that measurement assumes.

Standard
Operationalized Criterion
Purpose
1. Provenance
Explicit account of how the reference standard was constructed, by whom, and whether it is independent of the AI's training data.
Establishes the baseline validity of the labels.
2. Directional Bias Test
Minimally a binomial test for false-negative versus false-positive asymmetry applied to the evaluation labels.
Identifies systemic error vectors that could mask behavioral signals.
3. Reliability Context
Inter-rater reliability (IRR) calculation among original annotators, contextualized against instrument-specific published benchmarks.
Quantifies the baseline noise level relative to accepted clinical norms.

Table 5. Proposed minimum reporting standards for reference standard validation in human-AI studies.
5.7 Limitations
Stimulus set and class imbalance. The primary behavioral analysis rested on 27 images after exclusion of the Platinum Standard's 23 KL1-adjudicated cases (Strategy A). The resulting class distribution (approximately 21 positive, 6 negative; 3.5:1 ratio; majority-class baseline: 77.8%) created a constrained evaluation environment in which image-level estimates of AI accuracy and over-reliance rates should be treated as illustrative rather than as prevalence estimates for the clinical domain. Individual-level over-reliance rates were estimated from a small number of qualifying events per participant, which limits the reliability of the behavioral outcome variable and may contribute to the width of the confidence intervals observed. We report balanced accuracy, F1, sensitivity, specificity, and AUROC alongside raw accuracy throughout to mitigate the misleading influence of this imbalance, and the three pre-specified KL1 treatment strategies (Exclude, Clinical mapping, Sensitivity) produced directionally consistent findings across all psychometric models, supporting the robustness of the primary conclusions. The GEE psychometric models, estimated at the trial level (N = 2,754 observations), operated with substantially greater statistical power than the image-level counts suggest.

The GEE–Wilcoxon discrepancy. The divergence between the GEE (p = 0.178) and Wilcoxon (p = 0.037) estimates for the AI condition effect under the Platinum Standard reflects differing modeling assumptions rather than contradictory findings, as detailed in §4.2. We report both pre-specified tests to avoid selection bias, acknowledging that the AI benefit under the Platinum Standard is marginal and sensitive to the level of aggregation.

ICAR-6 instrumentation failure. The cohort produced a mean ICAR-6 score of 1.12 out of 6 (SD = 1.63), with a severely restricted variance distribution consistent with a floor effect. This was a preventable design error: the ICAR-6 is normed for adult populations and its difficulty ceiling is inappropriate for an adolescent cohort, rendering meaningful effect detection statistically impossible. The statistical output for fluid intelligence (M3: OR = 0.948, p = 0.103) cannot be characterized as a null finding; it is an instrumentation artifact. No valid inferences about whether cognitive ability influences annotation performance can be drawn from this study. Future studies with adolescent or non-academic populations should substitute an age-validated non-verbal reasoning instrument with appropriate difficulty calibration.

Attrition and potential selection bias. Of the 68 enrolled participants, 17 (25.0%) did not complete both sessions and were excluded from the analytic cohort. Administrative records document their dropout as logistical (illness, scheduling conflicts unrelated to study participation), and the distribution of non-completers across treatment groups showed no apparent pattern. However, because psychometric instruments (BFI-2, ICAR-6) were administered only during the No-AI session of completed participants, no baseline personality or cognitive data exist for the 17 non-completers. Non-differential attrition therefore cannot be empirically verified through a baseline comparison table; it rests solely on the logistical records. If attrition were differential — for example, if participants who found the study too cognitively demanding were more likely to drop out — the completer cohort would be a positively selected sample with systematically higher engagement or cognitive tolerance than the intended target population. This would not alter the internal validity of the within-cohort comparisons, but it would affect the generalizability of the personality effect estimates. Future studies should collect baseline psychometric data at enrollment, prior to any session, to enable formal attrition bias testing.

Cohort and scope. The use of an adolescent, non-clinical Hungarian student cohort is deliberate — it directly replicates the non-expert paradigm established by DANNY — but it limits the generalizability of the psychometric magnitude estimates to clinical annotation populations. The methodological contribution of this paper — the demonstration that GT noise suppresses psychometric signals in a specific, predictable, directional way — does not depend on the cohort's demographic characteristics; it is a structural property of the evaluation framework. The magnitude of the Neuroticism effect, and its applicability to trained radiologists or clinical technicians, requires replication in larger, adult samples. Additionally, because Neuroticism emerged as a significant secondary predictor after the primary pre-registered hypothesis (Conscientiousness) was unsupported, this finding should be treated as hypothesis-generating and requires confirmatory replication. A post-hoc power calculation for the observed Neuroticism effect (OR = 1.178) yielded an estimated power of 17% (N = 51), confirming that this secondary analysis is substantially underpowered and that the point estimate may not be reliable.

While a preliminary sample size calculation guided the initial recruitment target, the study protocol and its primary endpoints were not formally pre-registered — a limitation that must be explicitly acknowledged. The required N for a confirmatory study depends on which effect-size measure is designated as the primary confirmatory endpoint. For the GEE logistic regression estimating the Neuroticism OR (= 1.178 per unit, participant SD = 0.80) against a binary accuracy outcome, achieving 80% power would require approximately 2,800 participants under the Hsieh et al. (1998) participant-level approximation (α = 0.05, two-tailed) — a number that reflects the small per-unit OR relative to the clustered data structure. However, if the primary confirmatory outcome is instead the individual-level Spearman correlation between Neuroticism and over-reliance rate (ρ = −0.390), the required N drops substantially: 80% power requires approximately 49 participants, and 90% power requires approximately 65 participants (Fisher z-transformation method; α = 0.05, two-tailed). Future studies should pre-register one of these as the primary confirmatory endpoint: if the GEE accuracy endpoint is primary, a large multi-site trial is warranted; if the over-reliance correlation is primary, a single-site study with 65–80 participants would be adequately powered. We recommend the latter as the more tractable next confirmatory step, with accuracy as a secondary outcome.

Similarly, the brittle benefit finding is specific to a ResNet-18 model, a binary knee OA task, and a 28-day single-washout crossover. Whether the same pattern of scaffolding without knowledge transfer emerges under different AI architectures, different clinical modalities, or different inter-session intervals is an open empirical question.


6. CONCLUSION
This study set out to investigate whether cognitive ability and the Big Five personality traits predict appropriate reliance and annotation accuracy in AI-assisted medical annotation. While fluid intelligence testing encountered structural limitations and the primary personality hypothesis proved unsupported, Neuroticism emerged as a strong candidate predictor of lower automation bias. Under the original OAI ground truth, however, the empirical answer appeared unambiguous: it did not predict performance. That null result, replicated across GEE, Wilcoxon, and Spearman analyses, would constitute the study's conclusion in any standard reporting pipeline. We report it here as the starting point, not the ending one — because the data simultaneously contained evidence that the null result was not measuring what it claimed to measure.

The ground truth investigation that followed revealed a directionally biased reference standard: a pattern of false-negative label errors in the original OAI repository that was independently corroborated by the AI model's own uncertainty signals. Correcting these errors through a seven-step radiologist-consensus Platinum Standard protocol did not change the participants, the images, or the personality scores. It changed which decisions were scored as correct. Under the corrected reference standard, Neuroticism was associated with higher annotation accuracy (OR = 1.178, p = 0.029) and lower false-negative over-reliance (GEE coefficient = −0.429, p < 0.001), surviving FDR correction. Critically, this finding must be treated as hypothesis-generating: a post-hoc power calculation estimates that the study had only 17% power to detect the observed effect at N = 51, meaning the probability of an inflated effect size (Winner's Curse) is high. The association is theoretically coherent and directionally consistent across multiple analyses, but it requires confirmatory replication in a larger, adequately powered study before it can be treated as an established psychometric signal.

We formalize the primary finding as the ground truth noise suppressor mechanism: when a reference standard's error direction is correlated with an AI system's error direction — as occurs routinely when both are derived from the same public training repository — valid psychometric and behavioral signals in human annotators are rendered statistically invisible. This reflects a systemic measurement design flaw rather than a statistical artifact. The suppressor mechanism is a structural property of how evaluation frameworks are constructed, and it operates silently across any study that deploys a behaviorally noisy ground truth without directional bias testing.

Two secondary contributions reinforce the primary finding. First, in this sample, participants high in Neuroticism showed the behavioral signature of System 2 activation without external prompting, partially substituting for the mandatory procedural friction that frameworks like DANNY impose architecturally. This observation motivates personality screening as a potential complement to interface design in annotation pipeline risk stratification, pending replication in a powered study. Second, the brittle benefit effect — AI assistance improving performance within sessions while failing to generate any transferable diagnostic knowledge — held across both reference standards, confirming that scaffolding without knowledge transfer is an independent hazard for annotation systems deployed in clinical training contexts.

Taken together, the findings converge on a single methodological demand: ground truth validation must become a mandatory, explicitly reported step in every study that purports to measure human behavior in the presence of AI. The three minimum requirements we propose — documented reference standard construction, a directional bias test, and a contextualized inter-rater reliability report — are not burdensome. They are conditions for knowing what was actually measured. Until they are adopted as standard practice, the behavioral and psychometric conclusions of AI-assisted annotation research will remain hostage to the quality of the labels against which human judgment is scored.

Appendix A. Human Annotation Confusion Matrices Under All Three KL1 Handling Strategies

The primary behavioral analysis (Strategy A: Exclude) removed the 23 images adjudicated as KL1 by the radiologist panel, reducing the stimulus set from 50 to 27 images. To ensure that the core performance metrics are robust and not artifacts of this stimulus set reduction, we report full human annotation confusion matrices for all three pre-specified KL1 handling strategies. These are computed against the Platinum Standard ground truth under each strategy's respective KL1 mapping rule. Entries aggregate all N = 51 participants across both conditions (AI-assisted and unassisted).

Metric
Strategy A: Exclude (N = 27 images; 2,754 obs.)
Strategy B: Clinical Mapping (KL1 → Negative) (N = 50 images; 5,100 obs.)
Strategy C: Sensitivity (KL1 → Positive) (N = 50 images; 5,100 obs.)
True Positives (TP)
1,720
1,720
2,764
False Positives (FP)
140
1,184
140
False Negatives (FN)
422
422
1,724
True Negatives (TN)
472
1,774
472
Accuracy
79.6%
68.5%
63.5%
Sensitivity (Recall)
80.3%
80.3%
61.6%
Specificity
77.1%
59.9%
77.1%
Balanced Accuracy
78.7%
70.1%
69.4%
F1 Score
86.0%
68.2%
74.8%

Table A1. Human annotation confusion matrices against Platinum Ground Truth under all three KL1 handling strategies (both conditions combined; N = 51 participants).

Note: TP and FN counts are identical across Strategies A and B (1,720 / 422) because these strategies share the same Positive ground truth pool; they differ only in how KL1 images are classified on the Negative side. Strategy C's lower sensitivity (61.6%) reflects the reclassification of all 23 KL1-adjudicated images as Positive, a conservative bound that substantially increases the denominator of true Positive cases. Specificity is identical across Strategies A and C (77.1%) because both retain the same TN/FP pool. The directional pattern — human annotators exhibiting higher sensitivity than specificity under the Platinum Standard, with the main source of error being false negatives rather than false positives — is consistent across all three strategies. This confirms that the primary finding regarding the direction of over-reliance (100% false-negative in the AI condition) is not an artifact of the 50→27 image reduction. Psychometric GEE models (Table 4) produced directionally consistent Neuroticism coefficients across all three strategies (detailed in Supplementary Table S2), and the AI condition effect remained non-significant under all three strategies.

Bibliography
Ganz, J., Marzahl, C., Ammeling, J., Rosbach, E., Richter, B., Puget, C., ... & Aubreville, M. (2024). Information mismatch in PHH3-assisted mitosis annotation leads to interpretation shifts in H&E slide analysis. Scientific reports, 14(1), 26273.
Biro, J., Handley, J. L., Cobb, N. K., Kottamasu, V., Collins, J., Krevat, S., & Ratwani, R. M. (2025). Accuracy and safety of AI-enabled scribe technology: instrument validation study. Journal of Medical Internet Research, 27, e64993.
Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. Proceedings of the ACM on Human-computer Interaction, 5(CSCW1), 1-21.
Chen, Pingjun (2018), “Knee Osteoarthritis Severity Grading Dataset”, Mendeley Data, V1, doi: 10.17632/56rmx5bjcr.1
Chen, P., Gao, L., Shi, X., Allen, K., & Yang, L. (2019). Fully automatic knee osteoarthritis severity grading using deep neural networks with a novel ordinal loss. Computerized Medical Imaging and Graphics, 75, 84-92.
Chen, X., et al. (2021). Evaluating artificial intelligence on a reference standard based primarily on subjective human interpretation. The Lancet Digital Health.
Cheplygina, V., de Bruijne, M., & Pluim, J. P. (2019). Not-so-supervised: A survey of semi-supervised, multi-instance, and transfer learning in medical image analysis. Medical Image Analysis, 54, 280-296.
Condon, D. M., & Revelle, W. (2014). The International Cognitive Ability Resource: Development and initial validation of a public-domain measure. Intelligence, 43, 52–64.
Croskerry, P. (2003). Cognitive forcing strategies in clinical decisionmaking. Annals of Emergency Medicine, 41(1), 110-120.
Dratsch, T., Chen, X., Rezazade Mehrizi, M., Kloeckner, R., Mähringer-Kunz, A., Püsken, M., ... & Pinto dos Santos, D. (2023). Automation bias in mammography: the impact of artificial intelligence BI-RADS suggestions on reader performance. Radiology, 307(4), e222176.
Emory University. (2025). Impact of Label Noise from Large Language Model-generated Annotations on Evaluation of Diagnostic Model Performance. PubMed.
Evans, J. S. B. (2008). Dual-processing accounts of reasoning, judgment, and social cognition. Annu. Rev. Psychol., 59(1), 255-278.
FDA. (2022). Computer-assisted detection devices applied to radiology images and radiology device data — premarket notification [510(k)] submissions. U.S. Food and Drug Administration.
Frenay, B., & Verleysen, M. (2014). Classification in the presence of label noise: a survey. IEEE Transactions on Neural Networks and Learning Systems, 25(5), 845-869.
Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: a systematic review of frequency, effect mediators, and mitigators. Journal of the American Medical Informatics Association, 19(1), 121-127.
Ha, E., Choon-Kon-Yune, I., Murray, L., Luan, S., Montague, E., Bhattacharyya, O., & Agarwal, P. (2025). Evaluating the usability, technical performance, and accuracy of artificial intelligence scribes for primary care: competitive analysis. JMIR Human Factors, 12(1), e71434.
Hajcak, G., McDonald, N., & Simons, R. F. (2004). Error-related psychophysiology and negative affect. Psychophysiology, 41(6), 827-833.
Jackson, et al. (2026). Factors influencing the effectiveness of artificial intelligence-assisted decision-making in medicine: a scoping review. Journal of the American Medical Informatics Association.
Jeon, Y., Hwang, C., & Chen, X. A. (2025, March). Empowering medical data labeling for non-experts with danny: Enhancing accuracy and mitigating over-reliance on ai. In proceedings of the 30th international conference on intelligent user interfaces (pp. 624-640).
Kahneman, D. (2011). Thinking, fast and slow. Farrar, Straus and Giroux.
Karimi, D., et al. (2020). Deep learning with noisy labels: exploring techniques and remedies in medical image analysis. Medical Image Analysis, 65, 101759.
Kellgren J & Lawrence J. (1957). Radiological Assessment of Osteo-Arthrosis. Ann Rheum Dis. 16(4):494-502. doi:10.1136/ard.16.4.494
Khela, H., et al. (2026). Minimum joint space width demonstrates higher inter- and intra-observer reliability than Kellgren–Lawrence grading in knee osteoarthritis. Knee Surgery, Sports Traumatology, Arthroscopy.
Kose, O., et al. (2017). Osteoarthritis Classification Scales: Interobserver Reliability and Arthroscopic Correlation.
Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 33(1), 159-174.
Lekadir, K., Osuala, R., Gallin, C., Lazrak, N., Kushibar, K., Tsakou, G., ... & Martí-Bonmatí, L. (2021). FUTURE-AI: guiding principles and consensus recommendations for trustworthy artificial intelligence in medical imaging. arXiv preprint arXiv:2109.09658.
Liang, K. Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. Biometrika, 73(1), 13–22.
Mergen, M., et al. (2022). Should I trust the artificial intelligence to recruit? Recruiters' perceptions and behavior when faced with algorithm-based recommendation systems during resume screening. Frontiers in Psychology, 13, 895997.
Mosier, K. L., & Skitka, L. J. (1996). Human decision makers and automated decision aids: Made for each other? In R. Parasuraman & M. Mouloua (Eds.), Automation and human performance. Lawrence Erlbaum Associates Publishers.
Northcutt, C. G., Athalye, A., & Mueller, J. (2021). Pervasive label errors in test sets destabilize machine learning benchmarks. arXiv preprint arXiv:2103.14749.
Obuchowski, N. A. (2000). Multi-reader, multi-case ROC analysis: An introduction. Academic Radiology, 7(9), 655–661.
Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. Human Factors, 52(3), 381-410.
Rajpurkar, P., Chen, E., Banerjee, O., & Topol, E. J. (2022). AI in health and medicine. Nature Medicine, 28(1), 31-38.
Khela, M. S., Lee, T., Mulford, K. L., Yang, L., Brkljac, M., Crossman, D., ... & Wyles, C. C. (2026). Minimum joint space width demonstrates higher inter‐and intra‐observer reliability than Kellgren–Lawrence grading in knee osteoarthritis. Knee Surgery, Sports Traumatology, Arthroscopy.
Reinhardt, M., Horváth, Z., Tóth, L., & Kökönyei, G. (2020). A mentális egészség kontinuum skála rövid változatának hazai validációja. Magyar Pszichológiai Szemle, 75(2), 217-246.
Saini, S., Rabby, F., Bansal, R., Aziz, A. L., & Propheto, A. (2026). Mapping the intersection of artificial intelligence and neuroticism: a bibliometric analysis. Critical Public Health, 36(1). https://doi.org/10.1080/09581596.2025.2598715
Seyyed-Kalantari, L., et al. (2021). Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. Nature Medicine.
Soto, C. J., & John, O. P. (2017). The next Big Five Inventory (BFI-2): Developing and assessing a hierarchical model with 15 facets to enhance bandwidth, fidelity, and predictive power. Journal of Personality and Social Psychology, 113(1), 117.
Tett, R. P., & Burnett, D. D. (2003). A personality trait-based interactionist model of job performance. Journal of Applied Psychology, 88(3), 500.
Tiulpin, A., et al. (2019). Fully automatic knee osteoarthritis severity grading using deep neural networks with a novel ordinal loss. Scientific Reports, 9(1), 1-11.
Treasure, T., & MacRae, K. D. (1998). Minimisation: the platinum standard for trials?: randomisation doesn't guarantee similarity of groups; minimisation does. Bmj, 317(7155), 362-363.
Vaattovaara, et al. (2025). Kellgren-Lawrence Grading of Knee Osteoarthritis using Deep Learning: Diagnostic Performance with External Dataset and Comparison with Four Readers.
Ma, Y., Hou, J., Zhang, C., Zhou, Y., Ge, Z., Xie, H., & Ju, L. (2025). Benchmarking Real-World Medical Image Classification with Noisy Labels: Challenges, Practice, and Outlook. arXiv preprint arXiv:2512.09315.
Yoon, J. S., Yon, C. J., Lee, D., Lee, J. J., Kang, C. H., Kang, S. B., ... & Chang, C. B. (2023). Assessment of a novel deep learning-based software developed for automatic feature extraction and grading of radiographic knee osteoarthritis. BMC musculoskeletal disorders, 24(1), 869.
Zell, E., & Lesick, T. L. (2022). Big five personality traits and performance: A quantitative synthesis of 50+ meta‐analyses. Journal of personality, 90(4), 559-573.
Zhang, X., et al. (2024). CAISR: achieving human-level performance in automated sleep analysis across all clinical sleep metrics.
Ma, Y., Hou, J., Zhang, C., Zhou, Y., Ge, Z., Xie, H., & Ju, L. (2026). Benchmarking Real-World Medical Image Classification with Noisy Labels: Challenges, Practice, and Outlook. Pattern Recognition, 
Hsieh, F. Y., Bloch, D. A., & Larsen, M. D. (1998). A simple method of sample size calculation for linear and logistic regression. Statistics in medicine, 17(14), 1623-1634.
Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30(3), 837-849.
Eysenck, M. W., Derakshan, N., Santos, R., & Calvo, M. G. (2007). Anxiety and cognitive performance: attentional control theory. Emotion, 7(2), 336.
Abdalla, M., & Fine, B. (2023). Hurdles to artificial intelligence deployment: noise in schemas and “gold” labels. Radiology: Artificial Intelligence, 5(2), e220056.
Wei, Y., Deng, Y., Sun, C., Lin, M., Jiang, H., & Peng, Y. (2024). Deep learning with noisy labels in medical prediction problems: a scoping review. Journal of the American Medical Informatics Association, 31(7), 1596-1607.
Lacroux, A., & Martin-Lacroux, C. (2022). Should I trust the artificial intelligence to recruit? Recruiters’ perceptions and behavior when faced with algorithm-based recommendation systems during resume screening. Frontiers in Psychology, 13, 895997.
Freitag, M., Foster, G., Grangier, D., Ratnakar, V., Tan, Q., & Macherey, W. (2021). Experts, errors, and context: A large-scale study of human evaluation for machine translation. Transactions of the Association for Computational Linguistics, 9, 1460-1474.
Montag, C., Klugah-Brown, B., Zhou, X., et al. (2023). Trust toward humans and trust toward artificial intelligence are not associated: Initial insights from self-report and neurostructural brain imaging. Personality Neuroscience, 6. https://doi.org/10.1017/pen.2022.5
Cross, J. L., Choma, M. A., & Onofrey, J. A. (2024). Bias in medical AI: Implications for clinical decision-making. PLOS Digital Health, 3(11), e0000651. https://doi.org/10.1371/journal.pdig.0000651
Rodman, A. (2026). We need a new paradigm to think about generative AI. BMJ Quality & Safety.
Guo, J., Yan, P., Luo, H., et al. (2025). Predicting joint space changes in knee osteoarthritis over 6 years: a combined model of TransUNet and XGBoost. Quantitative Imaging in Medicine and Surgery, 15, 1396-1410. https://doi.org/10.21037/qims-24-1397
