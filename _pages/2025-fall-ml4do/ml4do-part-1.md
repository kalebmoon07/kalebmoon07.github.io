---
layout: archive
title: "Machine Learning for Discrete Optimization (IMEN891N, Fall 2025)"
permalink: /teaching/2025-fall-ml4do/part-1
author_profile: false
---

(♦: In-class presentation by students)

## Part I: Basic machine learning techniques

### Week 1: Introduction

- **Motivation and trends**: [Stanford MS&E236] Lecture “Introduction” [(link)](https://vitercik.github.io/ml4do/schedule/), Survey ([Bengio et al. 2021](#paper-bengio-2021))
  - 2021 AAAI Tutorial: Recent Advances in Integrating Machine Learning and Combinatorial Optimization [(link)](https://www.youtube.com/watch?v=XVLd7hf6y6M)
  - 2024 AI4OPT Seminar: Using Machine Learning for Combinatorial Optimization (ML4CO) [(link)](https://youtu.be/ZBTLn5K9jQ0?si=kaEa4tGEIswiIzYZ)
  - 2021 FODSI Workshop: Learning in Graph Neural Networks for Algorithms [(link)](https://www.youtube.com/watch?v=P_1WPsoLLNw)

### Week 1–3: Deep reinforcement learning

- **Graph Neural Networks (GNN)**: [Stanford MS&E236] Lecture “GNNs” [(link)](https://vitercik.github.io/ml4do/schedule/)
  - Tutorials ([Cappart et al. 2023](#paper-cappart-2023), [Angioni et al. 2025](#paper-angioni-2025))
  - [Stanford CS224W] Lecture 3–4 [(link)](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn)

- **Reinforcement Learning (RL)**: [Stanford MS&E236] Lecture “Reinforcement learning (Q-learning)” [(link)](https://vitercik.github.io/ml4do/schedule/)
  - Textbook ([Sutton & Barto 2020](#paper-sutton-barto-2020)) Chapter 3–6
  - [Stanford CS234] Lecture 2–6 [(link)](https://www.youtube.com/playlist?list=PLoROMvodv4rN4wG6Nk6sNpTEbuOSosZdX)

- ♦ **End-to-end heuristics**:  
  &nbsp;&nbsp;&nbsp;&nbsp;Routing ([Dai et al. 2018](#paper-dai-2018), [Kool et al. 2018](#paper-kool-2018), [Deudon et al. 2018](#paper-deudon-2018))  
  &nbsp;&nbsp;&nbsp;&nbsp;Scheduling ([Kwon et al. 2020](#paper-kwon-2020-pomo), [Park et al. 2021](#paper-park-2021), [Kwon et al. 2021](#paper-kwon-2021-men))
  - 2023 DIMACS Workshop: Search Heuristics for Solving Routing Problems with Deep Reinforcement Learning [(link)](https://www.youtube.com/watch?v=nqAubq2K_Ug)
  - 2023 DIMACS Workshop: (Bad) Reinforcement Learning Approaches to Vehicle Routing Problems [(link)](https://www.youtube.com/watch?v=nGc1MVNRvjE)

### Week 4: Simulation-based learning

- **Bandit models**: Textbook ([Sutton & Barto 2020](#paper-sutton-barto-2020)) Chapter 2, Tutorial ([Agrawal 2019](#paper-agrawal-2019))
  - Monographs ([Lattimore & Szepesvári 2020](#paper-lattimore-szepesvari-2020), [Slivkins 2019](#paper-slivkins-2019))
  - 2019 INFORMS TutORial: Recent Advances in Multiarmed Bandits [(link)](https://www.youtube.com/watch?v=7F0jPUyb7m4)

- **Bayesian optimization** ([Frazier 2018](#paper-frazier-2018), [Theodoridis 2015](#paper-theodoridis-2015))
  - 2018 INFORMS TutORial: Bayesian Optimization [(link)](https://www.youtube.com/watch?v=c4KKvyWW_Xk)

---

## Part I — Reading list

- <a id="paper-bengio-2021"></a>Bengio, Y., Lodi, A., & Prouvost, A. (2021). *Machine learning for combinatorial optimization: A methodological tour d’horizon*. **European Journal of Operational Research**, 290(2), 405–421.

- <a id="paper-cappart-2023"></a>Cappart, Q., Chételat, D., Khalil, E. B., Lodi, A., Morris, C., & Veličković, P. (2023). *Combinatorial Optimization and Reasoning with Graph Neural Networks*. **Journal of Machine Learning Research**, 24(130), 1–61.

- <a id="paper-angioni-2025"></a>Angioni, D., Archetti, C., & Speranza, M. G. (2025). *Neural combinatorial optimization: A tutorial*. **Computers & Operations Research**, 182, 107102. [(link)](https://doi.org/10.1016/j.cor.2025.107102)

- <a id="paper-sutton-barto-2020"></a>Sutton, R. S., & Barto, A. G. (2020). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.

- <a id="paper-dai-2018"></a>Dai, H., Khalil, E. B., Zhang, Y., Dilkina, B., & Song, L. (2018). *Learning Combinatorial Optimization Algorithms over Graphs*.

- <a id="paper-kool-2018"></a>Kool, W., van Hoof, H., & Welling, M. (2018). *Attention, Learn to Solve Routing Problems!* In **ICLR**.

- <a id="paper-deudon-2018"></a>Deudon, M., Cournut, P., Lacoste, A., Adulyasak, Y., & Rousseau, L.-M. (2018). *Learning Heuristics for the TSP by Policy Gradient*. In **CPAIOR** (LNCS), 170–181. [(link)](https://doi.org/10.1007/978-3-319-93031-2_12)

- <a id="paper-kwon-2020-pomo"></a>Kwon, Y.-D., Choo, J., Kim, B., Yoon, I., Gwon, Y., & Min, S. (2020). *POMO: Policy Optimization with Multiple Optima for Reinforcement Learning*. In **NeurIPS**, 33, 21188–21198.

- <a id="paper-park-2021"></a>Park, J., Chun, J., Kim, S. H., Kim, Y., & Park, J. (2021). *Learning to schedule job-shop problems: Representation and policy learning using graph neural network and reinforcement learning*. **International Journal of Production Research**, 59(11), 3360–3377. [(link)](https://doi.org/10.1080/00207543.2020.1870013)

- <a id="paper-kwon-2021-men"></a>Kwon, Y.-D., Choo, J., Yoon, I., Park, M., Park, D., & Gwon, Y. (2021). *Matrix encoding networks for neural combinatorial optimization*. In **NeurIPS**, 34, 5138–5149.

- <a id="paper-agrawal-2019"></a>Agrawal, S. (2019). *Recent Advances in Multiarmed Bandits for Sequential Decision Making*. In **INFORMS TutORials in Operations Research**, 167–188. [(link)](https://doi.org/10.1287/educ.2019.0204)

- <a id="paper-lattimore-szepesvari-2020"></a>Lattimore, T., & Szepesvári, C. (2020). *Bandit Algorithms*. Cambridge University Press. [(link)](https://doi.org/10.1017/9781108571401)

- <a id="paper-slivkins-2019"></a>Slivkins, A. (2019). *Introduction to Multi-Armed Bandits*. **Foundations and Trends® in Machine Learning**, 12(1–2), 1–286. [(link)](https://doi.org/10.1561/2200000068)

- <a id="paper-frazier-2018"></a>Frazier, P. I. (2018). *Bayesian Optimization*. In **INFORMS TutORials in Operations Research**, 255–278. [(link)](https://doi.org/10.1287/educ.2018.0188)

- <a id="paper-theodoridis-2015"></a>Theodoridis, S. (2015). *Machine Learning: A Bayesian and Optimization Perspective*. Academic Press.
