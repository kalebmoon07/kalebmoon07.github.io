---
layout: archive
title: "AI for Discrete Optimization (IMEN891N, Fall 2025)"
permalink: /teaching/ai4do/2025/
author_profile: false
---
## Introduction

Recent progress in Artificial Intelligence (AI) has demonstrated its power to tackle NP-hard discrete optimization problems and improve the decision-making process. Numerous research articles have been published in both traditional Operations Research (OR) journals and top AI conferences, reflecting increasing interest in this emerging field.

This course is designed to prepare students to conduct their own research at the intersection of AI and discrete optimization. We will focus primarily on scheduling and routing problems, graph optimization problems, and general mixed-integer programming (MIP). The course will cover two core topics:

* (i) **Data-driven algorithm design**: Using AI to improve the performance of optimization algorithms
* (ii) **Data-driven optimization**: Leveraging learned data to make better decisions under uncertainty.

## Prerequisites

### Strongly recommended

* **IMEN662 Discrete Optimization**
* IMEN260 Operations Research I (or IMEN661 Advanced Linear Programming)
* IMEN272 Probability and Statistics for Engineers (or equivalent)

### Not required, but useful

* IMEN764 Dynamic Programming & Reinforcement Learning Applications (or CSED627 Reinforcement Learning)
* Basic concepts in various machine learning models
  * Only deep reinforcement learning and bandit models will be quickly reviewed

## Course Logistics

The course is designed to be comprehensive and interactive with the components below. For each topic, a list of reading materials will be provided. Students may propose additional papers to instructor for discussion.

* **Lecture**: The instructor will present the main concepts and techniques.
* **In-class presentation**: Some classes will be reserved for student presentations. An assigned team must select a research paper among the given list and explain it to the class (25 minutes). Each student must be involved in at least one presentation.
* **Referee report**: At the end of each topic, students must select a research paper from the given list and write a referee report with critical analysis (min 2 pages, similar to a peer-review in an AI conference). During the course, three reports will be assigned.
  <!-- * See the [writing guidelines](/teaching/ai4do/2025/writing-guideline) -->
* **Final project**: Students in a team will develop a new method that applies AI to discrete optimization.
  * A proposal must be submitted at the end of week 6 (max 2 pages).
  * In week 11, a highlight talk will be given by each team (5 minutes).
  * The final results will be presented at the end of the course (30 minutes), which will be peer-reviewed by other students.
  * A final report must be submitted (max 16 pages).
  * The results should **include an evaluation of the proposed method** unless it is theoretical.

### Grade policy

* In-class presentation: 15%
* Referee reports: 25%
* Final project: 50%
* Participation and attendance: 10%

## Course Schedule {#schedule}

(♦: Potential slots for in-class presentation by students)

| Week  | Date  | Topic(s)                                                                                                                                                                                                                                                                                                | Assignment due dates           |
| :---: | :---: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
|       |       | [**Part I: Basic AI techniques**](/teaching/ai4do/2025/reading-list#part-1)                                                                                                                                                                                                                             |                                |
|   1   |  9/2  | Introduction: Motivation & trends [[DOTs 23] CO w/ DRL](https://www.youtube.com/watch?v=bi16pVVW52U), [[DOTs 24] AI OPT modeling](https://www.youtube.com/watch?v=_vN3pwB-PKI)                                                                                                                                |                                |
|       |  9/4  | Deep Reinforcement Learning (DRL) – Graph Neural Networks (GNN) [[Stanford CS224W] Lecture 6.2](https://www.youtube.com/watch?v=tutlI9YzJ2g), [6.3](https://www.youtube.com/watch?v=MH4yvtgAR-4), [7.1](https://www.youtube.com/watch?v=RU9uTa_-ZOw)                                                    |                                |
|   2   |  9/9  | Deep Reinforcement Learning (DRL) – Graph Neural Networks (GNN) [[Stanford CS224W] Lecture 7.2](https://youtu.be/247Mkqj_wRM), [7.3](https://www.youtube.com/watch?v=ew1cnUjRgl4), [[Google Talks 21] Intro to GNN](https://www.youtube.com/watch?v=8owQBFAHw7E)                                                |
|       | 9/11  | Deep Reinforcement Learning (DRL) – Basic reinforcement learning [[MIT 6.S091] Intro to DRL](https://www.youtube.com/watch?v=zR11FLZ-O9M), [[Stanford CS231n] DRL](https://www.youtube.com/watch?v=lvoHnicueoE)                                                                                         | Team formation                 |
|   3   | 9/16  | Deep Reinforcement Learning (DRL) – Basic reinforcement learning [[Stanford CS234] Q-Learning, VFA](https://www.youtube.com/watch?v=b_wvosA70f8), [Policy Gradient](https://www.youtube.com/watch?v=L6OVEmV3NcE)                                                                                        |                                |
|       | 9/18  | Applications of DRL: Routing and scheduling problems [[Stanford CS234] PPO](https://www.youtube.com/watch?v=b_wvosA70f8), ♦[[Kwon et al. NeurIPS 20]](#paper-kwon-2020-pomo) [(video)](https://www.youtube.com/watch?v=nGc1MVNRvjE)                                                                    |                                |
|   4   | 9/23  | <span style="color:green;">Simulation-based learning – Bandit models</span> [[Rutgers CS 550] v1](https://www.youtube.com/watch?v=dToYm34TIk4), [v2](https://www.youtube.com/watch?v=9ZwE078mbaU), [v3](https://www.youtube.com/watch?v=7hmzDzpbFsE), [v4](https://www.youtube.com/watch?v=ZIonygoiNVM) |                                |
|       | 9/25  | <span style="color:green;">Simulation-based learning – Thompson sampling</span> [[Google Talks] TS for Online Decision Making](https://www.youtube.com/watch?v=o6HBIGzQfJs) ♦[[Kool et al. ICLR 18]](#paper-kool-2018) [(video)](https://www.youtube.com/watch?v=nqAubq2K_Ug)                  |                                |
|       |       | [**Part II-1: Data-driven algorithm design: MIP solving**](/teaching/ai4do/2025/reading-list#part-2)                                                                                                                                                                                                                   |                                |
|   5   | 9/30  | Branch & cut in a MIP solver [[CO@Work 20] MIP solving v1](https://youtu.be/gObYR3TEn4w), [v2](https://youtu.be/1Z4-FNUXj60), [v3](https://youtu.be/_Bdhd40U1Bc), [v4](https://youtu.be/1PzRiuYAvnk)                                                                                                                                                                                                                                                                           |                                |
|       | 10/2  | Learn-to-branch [[CO@Work 24] ML augmented B&B](https://www.youtube.com/watch?v=SEZC03h6cIs), [[IPAM 23] ML in MIP](https://www.youtube.com/watch?v=ifQg5SJD45c)                                                                                                                                                                                                                                                                           | Report 1                       |
|   6   | 10/7  | <span style="color:red;">Holiday</span>                                                                                                                                                                                                                                                                 |                                |
|       | 10/9  | <span style="color:red;">Holiday</span>                                                                                                                                                                                                                                                                 |  |
|   7   | 10/14 | Learn-to-branch ♦[[Gasse et al. NeurIPS 19]](#paper-gasse-2019) [(video)](https://www.youtube.com/watch?v=Uo3OuPTQayg)                                                                                                                                                                                                                                                                        | Proposal for the final project                               |
|       | 10/16 | Learn-to-cut [[IPAM 21] RL for IP: Learning to cut](https://www.youtube.com/watch?v=CiQ1blLbYzg)                                                                                                                                                                                                                                                                         |                                |
|   8   | 10/21 | Learn-to-cut / Other topics in MIP solving                                                                                                                                                                                                                                                                          |                                |
|       | 10/23 | Large Neighborhood Search (LNS) [[AI4OPT 25] Synergy of ML and Comb. Solver](https://www.youtube.com/watch?v=a97HUka8oOM), [[IPAM 21] Solving MIP using NN](https://www.youtube.com/watch?v=qf8TeiGTZys)
|   9   | 10/28 | <span style="color:rgb(0, 112, 192);"> INFORMS Annual Meeting  </span>                                                                                                                                                                                                                                  |                                |
|       | 10/30 | <span style="color:rgb(0, 112, 192);"> INFORMS Annual Meeting  </span>                                                                                                                                                                                                                                  |                                |
|  10   | 11/4  | Learning for branch & price / column generation [[CO@Work 24] B&P Crash Course](https://www.youtube.com/watch?v=CFRbQoaBLIQ), [[Scheduling Seminar 25] ML inside Decomposition](https://www.youtube.com/watch?v=u3YIK32rMtI)                                                                                                                                                                                                                                                       |                        | 
|       | 11/6  | Learning for branch & price / column generation                                                                                                                                                                                                                                      |                                |
|       |       | [**Part II-2: Data-driven algorithm design: Combinatorial algorithms**](/teaching/ai4do/2025/reading-list#part-2)                                                                                                                                                                                                                   |                                |
|  11   | 11/11 | Algorithm with prediction [[Simons Inst. 22] ML for Algorithm Design](https://www.youtube.com/watch?v=6PzfHUmFhyI), [[UniBonn MA-INF1218] Ski Rental](https://www.youtube.com/watch?v=wzOOZK-Jch4)                                                                                                                                                                                                                                                                               | Report 2                               |
|       | 11/13 | Neural algorithmic reasoning [[DS4DM 23] Melting Pot of NAR](https://www.youtube.com/watch?v=1HhTpH3ZXMY), [[LoG 2022] Tutorial: NAR](https://www.youtube.com/watch?v=SKQ96tDZhgw)                                                                                                                                                                                                                                                                                |                  |
|  12   | 11/18 | Highlight talk (Student presentation)                                                                                                                                                                                                        |                               Highlight talk |
|       | 11/20 | Automated algorithm configuration [[PPSN 20] Tutorial on Alg Config](https://www.youtube.com/watch?v=O78Edc13BTg), [[UAI 18] Bayesian Optimization](https://www.youtube.com/watch?v=C5nqEHpdyoE)  |                        |
|  13   | 11/25 | Automated algorithm configuration - Runtime analysis [[AutoML 23] Survey for AAC](https://www.youtube.com/watch?v=av2KIgjS90o)                                                                                                                                                                                                                                        |                                |
|       | 11/27 | Automated algorithm configuration - Generalization bounds [[IPAM 21] How much data is sufficient ...?](https://www.youtube.com/watch?v=3_6A_Qof9MI)                                                                                                                                                                                                                                      |                                |
|       |       | [**Part III: Data-driven optimization**](/teaching/ai4do/2025/reading-list#part-3)                                                                                                                                                                                                                      |                                |
|  14   | 12/2  | Optimization under uncertainty – Theory [[Purdue CHE597] Stoc. Prog. and Benders](https://www.youtube.com/watch?v=ZuBIWN8AR1s)                                                                                                                                                                                                                                                                               |                                |
|       | 12/4  | Decision-focused learning [[CPAIOR 24] DFL Tutorial](https://www.youtube.com/watch?v=cNEL9QcHzBE), [[RPI Seminar] Predict-then-optimize](https://www.youtube.com/watch?v=Cu0EN92ESZo)                                                                                                                                                                                                                                                                              |   Report 3                             |
|  15   | 12/9  |  In-class presentations ♦                                                                                                                                                                                                                            |                                |
|       | 12/11 | <span style="color:rgb(0, 112, 192);"> Data-driven robust optimization, Optimization over a trained neural network (in three video lectures)</span> [[CO@Work 24] DL in RO](https://www.youtube.com/watch?v=nX7RLEDGDEY), [[Gurobi Webinar 25] Opt. over NN](https://www.youtube.com/watch?v=wixZHD37dkg)                                                                                                                                                                                                                                                                         |                        |
|       |       | [**Part IV: Finale**](/teaching/ai4do/2025/reading-list#part-4)                                                                                                                                                                                                                                         |                                |
|  16   | 12/16 | Final project presentation                                                                                                                                                                                                                                                                              |                                |
|       | 12/18 | Final project presentation; Recent topics – Large language models, Explainable AI [[DOTs 24] AI OPT modeling](https://www.youtube.com/watch?v=_vN3pwB-PKI), [[AAAI 22] Explainable AI Tutorial](https://www.youtube.com/watch?v=07hifxAsXjc), [[IMUS 21] Counterfactual explanations](https://www.youtube.com/watch?v=havqyKnsg-A)                                                                                                                                                                                                                                                                              | Final report                   |

---

Note:

* The corresponding reading materials and videos can be found [here](/teaching/ai4do/2025/reading-list).
* Students must select papers from [the listed journals and conferences](/teaching/ai4do/2025/journal-list)
* The <span style="color:green;">classes in Week 4</span> will be delivered online due to the instructor's business trip.
* Potential <span style="color:rgb(0, 112, 192);">make-up classes</span> are colored in blue.
  * Video lectures for Part III will be provided instead.
* Another make-up class for term project presentation in Week 16 may be scheduled.

## Useful information

* [Resources](/teaching/ai4do/2025/resources) – A list of useful resources for this course.
* [Previous Academic Events](/teaching/ai4do/2025/previous-academic-events) – A list of previous academic events related to this course.

## Reference for in-class presentation

- Week 3, 9/18 (Presentation: Group 1; Discussion: Kyungduk Moon)
  - <a id="paper-kwon-2020-pomo"></a>Kwon, Y.-D., Choo, J., Kim, B., Yoon, I., Gwon, Y., & Min, S. (2020). POMO: Policy Optimization with Multiple Optima for Reinforcement Learning. Advances in Neural Information Processing Systems, 33, 21188–21198.
- Week 4, 9/25 (Presentation: Group 5; Discussion: Group 3)
  - <a id="paper-kool-2018"></a>Kool, W., Hoof, H. van, & Welling, M. (2018, September 27). Attention, Learn to Solve Routing Problems! International Conference on Learning Representations.
- Week 7, 10/14 (Presentation: Group 4; Discussion: Group 2)
  - <a id="paper-gasse-2019"></a>Gasse, M., Chetelat, D., Ferroni, N., Charlin, L., & Lodi, A. (2019). Exact Combinatorial Optimization with Graph Convolutional Neural Networks. Advances in Neural Information Processing Systems, 32.
- Week 15, 12/9 (Presentation: Group 3; Discussion: Group 1)
  - Zhang, X., Chen, L., Gendreau, M., & Langevin, A. (2022). Learning-Based Branch-and-Price Algorithms for the Vehicle Routing Problem with Time Windows and Two-Dimensional Loading Constraints. _INFORMS Journal on Computing_, _34_(3), 1419–1436.
- Week 15, 12/9 (Presentation: Group 2; Discussion: Group 4)
  - Ferber, A., Wilder, B., Dilkina, B., & Tambe, M. (2020). MIPaaL: Mixed Integer Program as a Layer. _Proceedings of the AAAI Conference on Artificial Intelligence_, _34_(02), Article 02.
- Week 15, 12/9 (Presentation: Kyungduk Moon; Discussion: Group 5)
  - Fischetti, M., & Jo, J. (2018). Deep neural networks and mixed integer linear optimization. _Constraints_, _23_(3), 296–309.

## Final project topics

* **Group 1**: Online Scheduling Problem:
A Combinatorial Semi-Bandit Perspective
* **Group 2**: Deep Multi-Agent Reinforcement Learning with Graph Attention Network for Large-Scale Traffic Signal Control
* **Group 3**: Scalable Estimation of TSP Tour Lengths via a Unified GNN-based Approach
* **Group 4**: Preference-Based Black-box Optimization: Mathematical Optimization from Human Feedback
* **Group 5**: ORMINI: Improving the Accuracy of Automated Optimization Modeling from Natural Language via RAG-based Domain Knowledge Injection