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
* **Referee report**: At the end of each topic, students must select a research paper from the given list and write a referee report with critical analysis (min 2 pages, similar to a peer-review in a AI conference). During the course, four reports will be assigned.
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
|   1   |  9/2  | Introduction: Motivation & trends [[DOTs] CO w/ DRL](https://www.youtube.com/watch?v=bi16pVVW52U), [[DOTs] AI OPT modeling](https://www.youtube.com/watch?v=_vN3pwB-PKI)                                                                                                                                |                                |
|       |  9/4  | Deep Reinforcement Learning (DRL) – Graph Neural Networks (GNN) [[Stanford CS224W] Lecture 6.2](https://www.youtube.com/watch?v=tutlI9YzJ2g), [6.3](https://www.youtube.com/watch?v=MH4yvtgAR-4), [7.1](https://www.youtube.com/watch?v=RU9uTa_-ZOw)                                                    |                                |
|   2   |  9/9  | Deep Reinforcement Learning (DRL) – Graph Neural Networks (GNN) [[Stanford CS224W] Lecture 7.2](https://youtu.be/247Mkqj_wRM), [7.3](https://www.youtube.com/watch?v=ew1cnUjRgl4), [[PyTorch] Intro to GNN](https://www.youtube.com/watch?v=8owQBFAHw7E)                                                |
|       | 9/11  | Deep Reinforcement Learning (DRL) – Basic reinforcement learning [[MIT 6.S091] Intro to DRL](https://www.youtube.com/watch?v=zR11FLZ-O9M), [[Stanford CS231n] DRL](https://www.youtube.com/watch?v=lvoHnicueoE)                                                                                         | Team formation                 |
|   3   | 9/16  | Deep Reinforcement Learning (DRL) – Basic reinforcement learning [[Stanford CS234] Q-Learning, VFA](https://www.youtube.com/watch?v=b_wvosA70f8), [Policy Gradient](https://www.youtube.com/watch?v=L6OVEmV3NcE)                                                                                        |                                |
|       | 9/18  | Applications of DRL: Routing and scheduling problems [[Stanford CS234] PPO](https://www.youtube.com/watch?v=b_wvosA70f8), ♦[[Kwon et al.2020 NeurIPS]](#paper-kwon-2020-pomo) [(video)](https://www.youtube.com/watch?v=nGc1MVNRvjE)                                                                    |                                |
|   4   | 9/23  | <span style="color:green;">Simulation-based learning – Bandit models</span> [[Rutgers CS 550] v1](https://www.youtube.com/watch?v=dToYm34TIk4), [v2](https://www.youtube.com/watch?v=9ZwE078mbaU), [v3](https://www.youtube.com/watch?v=7hmzDzpbFsE), [v4](https://www.youtube.com/watch?v=ZIonygoiNVM) |                                |
|       | 9/25  | <span style="color:green;">Simulation-based learning – Bandit models and others</span> [[Google Talks] TS for Online Decision Making](https://www.youtube.com/watch?v=o6HBIGzQfJs) ♦[[Kool et al. 2018 ICLR]](#paper-kool-2018) [(video)](https://www.youtube.com/watch?v=nqAubq2K_Ug)                  |                                |
|       |       | [**Part II: Data-driven algorithm design**](/teaching/ai4do/2025/reading-list#part-2)                                                                                                                                                                                                                   |                                |
|   5   | 9/30  | Branch & cut in a MIP solver [[CO@Work 2020] MIP solving v1](https://youtu.be/gObYR3TEn4w), [v2](https://youtu.be/1Z4-FNUXj60), [v3](https://youtu.be/_Bdhd40U1Bc), [v4](https://youtu.be/1PzRiuYAvnk)                                                                                                                                                                                                                                                                           |                                |
|       | 10/2  | Learn-to-branch [[CO@Work 2024] ML augmented B&B](https://www.youtube.com/watch?v=SEZC03h6cIs), [[IPAM 2023] ML in MIP](https://www.youtube.com/watch?v=ifQg5SJD45c)                                                                                                                                                                                                                                                                           | Report 1                       |
|   6   | 10/7  | <span style="color:red;">Holiday</span>                                                                                                                                                                                                                                                                 |                                |
|       | 10/9  | <span style="color:red;">Holiday</span>                                                                                                                                                                                                                                                                 |  |
|   7   | 10/14 | Learn-to-branch ♦[[Gasse et al. NeurIPS 2019]](#paper-gasse-2019) [(video)](https://www.youtube.com/watch?v=Uo3OuPTQayg)                                                                                                                                                                                                                                                                        | Proposal for the final project                               |
|       | 10/16 | Learn-to-cut [[IPAM 2021] RL for IP: Learning to cut](https://www.youtube.com/watch?v=CiQ1blLbYzg)                                                                                                                                                                                                                                                                         |                                |
|   8   | 10/21 | Learn-to-cut / Other topics in MIP solving                                                                                                                                                                                                                                                                          |                                |
|       | 10/23 | Large Neighborhood Search (LNS) [[AI4OPT 2025] Synergy of ML and Comb. Solver](https://www.youtube.com/watch?v=a97HUka8oOM), [[IPAM 2021] Solving MIP using NN](https://www.youtube.com/watch?v=qf8TeiGTZys)
|   9   | 10/28 | <span style="color:rgb(0, 112, 192);"> INFORMS Annual Meeting  </span>                                                                                                                                                                                                                                  |                                |
|       | 10/30 | <span style="color:rgb(0, 112, 192);"> INFORMS Annual Meeting  </span>                                                                                                                                                                                                                                  |                                |
|  10   | 11/4  | Learning for branch & price / column generation [[CO@Work 2024] B&P Crash Course](https://www.youtube.com/watch?v=CFRbQoaBLIQ), [[Scheduling Seminar] ML inside Decomposition](https://www.youtube.com/watch?v=u3YIK32rMtI)                                                                                                                                                                                                                                                       |                        | 
|       | 11/6  | Learning for branch & price / column generation                                                                                                                                                                                                                                      |                                |
|  11   | 11/11 | Algorithm with prediction [[Simons Institute 2022] ML for Algorithm Design](https://www.youtube.com/watch?v=6PzfHUmFhyI), [[Uni Bonn 2021] Ski Rental](https://www.youtube.com/watch?v=wzOOZK-Jch4)                                                                                                                                                                                                                                                                               | Report 2                               |
|       | 11/13 | Neural algorithmic reasoning [[DS4DM] Melting Pot of NAR](https://www.youtube.com/watch?v=1HhTpH3ZXMY), [[LoG 2022] Tutorial: NAR](https://www.youtube.com/watch?v=SKQ96tDZhgw)                                                                                                                                                                                                                                                                                |                  |
|  12   | 11/18 | Highlight talk (Student presentation)                                                                                                                                                                                                        |                               Highlight talk |
|       |       | [**Part III: Data-driven optimization**](/teaching/ai4do/2025/reading-list#part-3)                                                                                                                                                                                                                      |                                |
|       | 11/20 | Automated algorithm configuration [[PPSN 2020] Tutorial on Alg Config](https://www.youtube.com/watch?v=O78Edc13BTg), [[UAI 2018] Bayesian Optimization](https://www.youtube.com/watch?v=C5nqEHpdyoE)  |                        |
|  13   | 11/25 | Optimization under uncertainty – Theory                                                                                                                                                                                                                                        |                                |
|       | 11/27 | Optimization under uncertainty – Theory                                                                                                                                                                                                                                       |                                |
|  14   | 12/2  |Optimization under uncertainty – Data-driven robust optimization                                                                                                                                                                                                                                                                               |                                |
|       | 12/4  | Decision-focused learning                                                                                                                                                                                                                                                                              |   Report 3                             |
|       |       | [**Part IV: Finale**](/teaching/ai4do/2025/reading-list#part-4)                                                                                                                                                                                                                                         |                                |
|  15   | 12/9  | Decision-focused learning  ♦                                                                                                                                                                                                                            |                                |
|       | 12/11 | <span style="color:rgb(0, 112, 192);">Recent topics – Optimization over a trained neural network, Large language models, Explainable AI</span>                                                                                                                                                                                                                                                                          |                        |
|  16   | 12/16 | Final project presentation                                                                                                                                                                                                                                                                              |                                |
|       | 12/18 | Final project presentation                                                                                                                                                                                                                                                                              | Report 4, Final report                   |

---

Note:

* The corresponding reading materials and videos can be found [here](/teaching/ai4do/2025/reading-list).
* Students must select papers from [the listed journals and conferences](/teaching/ai4do/2025/journal-list)
* The <span style="color:green;">classes in Week 4</span> will be delivered online due to the instructor's business trip.
* Potential <span style="color:rgb(0, 112, 192);">make-up classes</span> are colored in blue.
  * Video lectures for Part III may be provided instead.
* Another make-up class for term project presentation in Week 16 may be scheduled.

## Useful information

* [Resources](/teaching/ai4do/2025/resources) – A list of useful resources for this course.
* [Previous Academic Events](/teaching/ai4do/2025/previous-academic-events) – A list of previous academic events related to this course.

## Reference for in-class presentation

- Week 3, 9/18 (Presentation: Group 1; Discussion: Kyungduk Moon)
  - <a id="paper-kwon-2020-pomo"></a>Kwon, Y.-D., Choo, J., Kim, B., Yoon, I., Gwon, Y., & Min, S. (2020). *POMO: Policy Optimization with Multiple Optima for Reinforcement Learning*. In **NeurIPS**, 33, 21188–21198.
- Week 4, 9/25 (Presentation: Group 5; Discussion: Group 3)
  - <a id="paper-kool-2018"></a>Kool, W., van Hoof, H., & Welling, M. (2018). *Attention, Learn to Solve Routing Problems!* In **ICLR**.
- Week 7, 10/12 (Presentation: Group 4; Discussion: Group 2)
  - <a id="paper-gasse-2019"></a>Gasse, M., Chetelat, D., Ferroni, N., Charlin, L., & Lodi, A. (2019). Exact Combinatorial Optimization with Graph Convolutional Neural Networks. In **NeurIPS**, 32.
- Week 15, 12/9 (Presentation: Group ?; Discussion: Group ?)
  - To be determined.
- Week 15, 12/9 (Presentation: Group ?; Discussion: Group ?)
  - To be determined.
- Week 15, 12/9 (Presentation: Group ?; Discussion: Group ?)
  - To be determined.
