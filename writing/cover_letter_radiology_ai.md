# Cover Letter – *Journal of the American Medical Informatics Association (JAMIA)*

---

[Date]

Dr. Suzanne Bakken, Editor-in-Chief
*Journal of the American Medical Informatics Association (JAMIA)*
Oxford University Press / American Medical Informatics Association

---

Dear Dr. Bakken and the Editorial Board,

We are pleased to submit our manuscript entitled **"Ground Truth Bias in AI-Assisted Medical Annotation: A Crossover Study Using an Independent Radiologist Reference Standard"** for exclusive consideration as a *Research and Applications* article in JAMIA.

**Why this work matters for JAMIA's readership**

The field of AI-assisted medical image annotation increasingly relies on crowdsourced or non-expert labellers guided by algorithmic predictions, yet the behavioural evaluations underpinning these pipelines typically treat public repository labels as an unexamined ground truth. Our study shows that this assumption can be structurally invalid—and that its consequences extend far beyond a minor calibration issue.

Using a crossover repeated-measures design in which 51 non-expert annotators labelled 50 knee radiographs from the Osteoarthritis Initiative (OAI) with and without a ResNet-18 AI assistant, we demonstrate a **measurement artifact** we term a *ground truth suppressor mechanism*. When human-AI decisions were scored against the original OAI labels, AI assistance appeared to produce a large and statistically robust accuracy improvement (OR = 1.23, p = 0.003). Scored against an independent expert radiologist reference standard—constructed by a board-certified radiologist and three radiology residents through a blinded, structured consensus process—the same data yielded a small, non-significant effect (OR = 1.16, p = 0.178). Beyond the aggregate accuracy shift, the corrected standard revealed that all residual over-reliance events were false-negative acceptances: participants agreeing with the AI's failure to detect genuine pathology. This clinically critical error category had been rendered statistically invisible by the shared false-negative bias of the model and its training labels. We believe this finding is of direct relevance to JAMIA's coverage of clinical AI evaluation, human-computer interaction, and diagnostic error informatics.

---

**Special considerations**

*Related papers by the same author(s):* This study is conceptually related to and explicitly cites the DANNY framework (Jeon Y et al., IUI 2025), which provided the methodological template our study extends and replicates in a new cohort. No text, figures, or data from that publication appear in the submitted manuscript. No other papers by the authors overlap in data or primary analyses with the present submission.

*Previous reviews of this article:* This manuscript has not been previously submitted to JAMIA or to any other journal. It has not undergone external peer review. No prior Editor or reviewer comments exist for this work.

*Sole submission:* This manuscript has not been published, is not under consideration elsewhere, and is being submitted solely to JAMIA.

*Artificial intelligence use disclosure:* Artificial intelligence tools (large language models) were used during the preparation of this study to assist with literature search and to aid in coding the custom annotation platform, particularly for debugging.

*Conflicts of interest:* The authors declare no competing interests. No industry funding was received. No author has a financial relationship with the Osteoarthritis Initiative, its data repository, or any company whose products are evaluated in this study. Conflict of interest information has been confirmed through the submission system.

*Funding:* No specific funding was received for this work. Authors are affiliated with Pázmány Péter Catholic University (Budapest, Hungary), the University of the West of Scotland (Lanarkshire, UK), and North Buda Saint John's Centre Hospital (Budapest, Hungary). None of the authors are NIH employees.

*Ethics:* The study was conducted in accordance with the Declaration of Helsinki. Under applicable Hungarian law (Act CLIV of 1997 on Health), this non-clinical annotation study conducted within established school partnerships did not require formal IRB review. Written parental or guardian consent was obtained for participants under 16 years of age; all participants provided digital informed assent. No personal health data were collected.

*Data availability:* Upon acceptance, a de-identified per-image outcome table (original OAI labels, independent consensus labels, AI predictions, AI confidence scores, aggregate participant agreement rates, and reliance-category counts under both reference standards) and all analysis code will be deposited in a public GitHub repository, subject to OAI data-use restrictions. A Data Availability Statement is included in the manuscript.

---

**Manuscript details**

- Article type: Research and Applications
- Running title: Ground truth bias and AI-assisted annotation
- Keywords: Artificial Intelligence; Automation; Osteoarthritis, Knee; Observer Variation; Diagnostic Errors
- Word count (main text, excluding title page, abstract, references, figures, and tables): approximately 4,800 words
- Figures: 6 | Tables: 3 | References: 48

---

We thank you for your time and consideration of our work. We would be happy to provide any additional materials or information the editorial office may require, including copies of related papers or reviewer communications from prior venues.

Yours sincerely,

**Márton Baltay** *(Corresponding author)*
Department of Sociology, Faculty of Humanities and Social Sciences
Pázmány Péter Catholic University, Budapest, Hungary
baltay.marton.mihaly@hallgato.ppke.hu | +36 20 397 1062
ORCID: 0009-0005-4484-2597

**Tamás Ilcsik**
School of Computing, Engineering and Physical Sciences
University of the West of Scotland, Lanarkshire, United Kingdom

**Márton Borbély, MD**
Department of Integrated Radiology
North Buda Saint John's Centre Hospital, Budapest, Hungary

---

## Draft Tweet (for JAMIA Social Media Submission)

> Does your AI assistant actually *help* — or does it just steer annotators toward the dataset's own mistakes? Our crossover study shows how false-negative bias in a public ground truth inflates apparent AI benefits and hides dangerous automation errors in medical imaging. #MedicalAI #HealthInformatics #JAMIA
