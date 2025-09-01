---
layout: archive
title: "AI for Discrete Optimization (IMEN891N, Fall 2025)"
permalink: /teaching/ai4do/2025/reading-list
author_profile: false
---

(♦: In-class presentation by students)

## Part I: Basic AI techniques {#part-1}

### Week 1: Introduction

- **Motivation and trends**: [Stanford MS&E236] Lecture “Introduction” [(link)](https://vitercik.github.io/ml4do/schedule/), Survey ([Bengio et al. 2021](#paper-bengio-2021))
  - 2021 AAAI Tutorial: Recent Advances in Integrating Machine Learning and Combinatorial Optimization [(link)](https://www.youtube.com/watch?v=XVLd7hf6y6M)
  - 2024 AI4OPT Seminar: Using Machine Learning for Combinatorial Optimization (ML4CO) [(link)](https://youtu.be/ZBTLn5K9jQ0?si=kaEa4tGEIswiIzYZ)
  - 2021 FODSI Workshop: Learning in Graph Neural Networks for Algorithms [(link)](https://www.youtube.com/watch?v=P_1WPsoLLNw)

### Week 1–3: Deep reinforcement learning

- **Graph Neural Networks (GNN)**: [Stanford MS&E236] Lecture “GNNs” [(link)](https://vitercik.github.io/ml4do/schedule/)
  - Tutorials ([Cappart et al. 2023](#paper-cappart-2023), [Angioni et al. 2025](#paper-angioni-2025))
  - [Stanford CS224W] Lecture 6--8 [(link)](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn)

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

## Part II: Data-driven algorithm design {#part-2}

### Week 5–7: Branch & cut in a MIP solver

- Theory class ([Achterberg 2009](#paper-achterberg-2009))
  - CO@Work 2024 Lecture: Section “The Fundamentals of MIP” [(link)](https://co-at-work.zib.de/#schedule)
- ♦ Learn-to-branch ([Khalil et al. 2016](#paper-khalil-2016), [Lodi & Zarpellon 2017](#paper-lodi-2017), [Balcan et al. 2018](#paper-balcan-2018)), Learn-to-cut ([Deza & Khalil 2023](#paper-deza-2023), [Scavuzzo et al. 2024](#paper-scavuzzo-2024))
  - 2023 Gurobi Days Digital: On The Interplay Between Learning And Optimization And Its Effect On MIP Solving (by Andrea Lodi @ Cornell Tech) [(link)](https://www.youtube.com/watch?v=ntoH-r6Ijsw)
  - 2023 IPAM Workshop: Machine Learning for MIP Solving (by Bistra Dilkina @ University of Southern California) [(link)](https://youtu.be/hdad1if4MqU?si=hAz_G0MFDWbygJbq)
- Proposal of the final project

### Week 7-8: Large Neighborhood Search (LNS) heuristics

- Theory class ([Pisinger & Ropke 2019](#paper-pisinger-2019), [Windras Mara et al. 2022](#paper-windras-mara-2022), [Voigt 2025](#paper-voigt-2025))
- ♦ Learning applications: MIP ([Song et al. 2020](#paper-song-2020), [Wu et al. 2021](#paper-wu-2021), [Hendel 2022](#paper-hendel-2022)), Routing ([Hottung & Tierney 2020](#paper-hottung-2020), [Ma et al. 2022](#paper-ma-2022), [Qin et al. 2022](#paper-qin-2022)), Scheduling ([Zhang et al. 2023](#paper-zhang-2023), [Li et al. 2025](#paper-li-2025))
  - 2022 CPAIOR Keynote: Deep Learning and Neural Network Accelerators for Combinatorial Optimization (by Vinod Nair @ Google) [(link)](https://www.youtube.com/watch?v=uiGJH2cZR9I)
  - LNS [(link)](https://www.youtube.com/watch?v=y9HSuu1pS28) and Adaptive LNS for MIP (by Krunal Patel @ Polytechnique Montréal) [(link)](https://www.youtube.com/watch?v=KQJ2NgxbI1c)

### Week 8-10: Branch & price algorithms

- Theory class ([Desrosiers et al. 2025](#paper-desrosiers-2025), [Uchoa et al. 2024](#paper-uchoa-2024))
  - CO@Work 2024 Lecture: “Branch-and-Price Crash Course” [(link)](https://www.youtube.com/watch?v=CFRbQoaBLIQ)
  - CO@Work 2020 Lecture: “Column Generation, Dantzig-Wolfe, Branch-Price-and-Cut” [(link)](https://www.youtube.com/watch?v=vx2LNKx48vY)
- ♦ Learning for column generation: Scheduling ([Koutecká et al. 2025](#paper-kouteck-a-2025), [Václavík et al. 2018](#paper-v-aclav-ik-2018)), Routing ([Morabit et al. 2021](#paper-morabit-2021)), Graph problems ([Shen et al. 2022](#paper-shen-2022), [Sun et al. 2023](#paper-sun-2023))
  - 2025 Scheduling Seminar: Machine Learning Inside Decomposition of Scheduling Problems (by Přemysl Šůcha @ CTU in Prague) [(link)](https://www.youtube.com/watch?v=u3YIK32rMtI)

### Week 11-12: Algorithms without a solver

- Data-driven algorithm design: [Stanford MS&E236] Lecture “Algorithms with predictions” [(link)](https://vitercik.github.io/ml4do/schedule/), Survey ([Balcan 2021](#paper-balcan-2021), [Gupta & Roughgarden 2020](#paper-gupta-2020), [Mitzenmacher & Vassilvitskii 2022](#paper-mitzenmacher-2022))
  - 2022 Simons Institute Boot Camp: Machine Learning for Algorithm Design (by Ellen Vitercik @ Stanford University) [(link)](https://www.youtube.com/watch?v=6PzfHUmFhyI)
- ♦ Automated algorithm configuration: Survey ([Schede et al. 2022](#paper-schede-2022)), `irace` package ([López-Ibáñez et al. 2016](#paper-l-opez-ib-a-nez-2016))
  - 2023 AutoML Conference Tutorial: A Survey for Automated Algorithm Configuration (Viktor Bengs @ LMU Munich et al.) [(link)](https://www.youtube.com/watch?v=av2KIgjS90o)
- ♦ (Optional) Neural algorithmic reasoning: [Stanford MS&E236] Lecture “Neural algorithmic reasoning” [(link)](https://vitercik.github.io/ml4do/schedule/), Seminal works ([Veličković & Blundell 2021](#paper-veli-ckovi-c-2021), [Cappart et al. 2023](#paper-cappart-2023))
  - 2022 Learning on Graphs Conference Tutorial: Neural Algorithmic Reasoning (by Petar Veličković @ DeepMind et al.) [(link)](https://www.youtube.com/watch?v=SKQ96tDZhgw)

---

## Part II — Reading list

- <a id="paper-achterberg-2009"></a>Achterberg, Tobias (2009). *SCIP: Solving Constraint Integer Programs*. **Mathematical Programming Computation**, 1(1), 1–41. [(link)](https://doi.org/10.1007/s12532-008-0001-1)
- <a id="paper-khalil-2016"></a>Khalil, Elias, Bodic, Pierre Le, Song, Le, Nemhauser, George, Dilkina, Bistra (2016). *Learning to Branch in Mixed Integer Programming*. **Proceedings of the AAAI Conference on Artificial Intelligence**, 30(1). [(link)](https://ojs.aaai.org/index.php/AAAI/article/view/10080)
- <a id="paper-lodi-2017"></a>Lodi, Andrea, Zarpellon, Giulia (2017). *On learning and branching: a survey*. **TOP**, 25(2), 207–236. [(link)](https://doi.org/10.1007/s11750-017-0451-6)
- <a id="paper-balcan-2018"></a>Balcan, Maria-Florina, Dick, Travis, Sandholm, Tuomas, Vitercik, Ellen (2018). *Learning to Branch*. **Proceedings of the 35th International Conference on Machine Learning**, 344–353. [(link)](https://proceedings.mlr.press/v80/balcan18a.html)
- <a id="paper-deza-2023"></a>Deza, Arnaud, Khalil, Elias B. (2023). *Machine Learning for Cutting Planes in Integer Programming: A Survey*. **Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence**, 6592–6600. [(link)](https://doi.org/10.24963/ijcai.2023/739)
- <a id="paper-scavuzzo-2024"></a>Scavuzzo, Lara, Aardal, Karen, Lodi, Andrea, Yorke-Smith, Neil (2024). *Machine Learning Augmented Branch and Bound for Mixed Integer Linear Programming*. **Mathematical Programming**. [(link)](https://doi.org/10.1007/s10107-024-02130-y)
- <a id="paper-pisinger-2019"></a>Pisinger, David, Ropke, Stefan (2019). *Large Neighborhood Search*. **Handbook of Metaheuristics**, 99–127. [(link)](https://doi.org/10.1007/978-3-319-91086-4_4)
- <a id="paper-windras-mara-2022"></a>Windras Mara, Setyo Tri, Norcahyo, Rachmadi, Jodiawan, Panca, Lusiantoro, Luluk, Rifai, Achmad Pratama (2022). *A Survey of Adaptive Large Neighborhood Search Algorithms and Applications*. **Computers & Operations Research**, 146, 105903. [(link)](https://doi.org/10.1016/j.cor.2022.105903)
- <a id="paper-voigt-2025"></a>Voigt, Stefan (2025). *A Review and Ranking of Operators in Adaptive Large Neighborhood Search for Vehicle Routing Problems*. **European Journal of Operational Research**, 322(2), 357–375. [(link)](https://doi.org/10.1016/j.ejor.2024.05.033)
- <a id="paper-song-2020"></a>Song, Jialin, Lanka, Ravi, Yue, Yisong, Dilkina, Bistra (2020). *A General Large Neighborhood Search Framework for Solving Integer Linear Programs*. **Advances in Neural Information Processing Systems**, 33, 20012–20023.
- <a id="paper-wu-2021"></a>Wu, Yaoxin, Song, Wen, Cao, Zhiguang, Zhang, Jie (2021). *Learning Large Neighborhood Search Policy for Integer Programming*. **Advances in Neural Information Processing Systems**, 34, 30075–30087.
- <a id="paper-hendel-2022"></a>Hendel, Gregor (2022). *Adaptive Large Neighborhood Search for Mixed Integer Programming*. **Mathematical Programming Computation**, 14(2), 185–221. [(link)](https://doi.org/10.1007/s12532-021-00209-7)
- <a id="paper-hottung-2020"></a>Hottung, André, Tierney, Kevin (2020). *Neural Large Neighborhood Search for the Capacitated Vehicle Routing Problem*. **ECAI 2020**, 443–450. [(link)](https://doi.org/10.3233/FAIA200124)
- <a id="paper-ma-2022"></a>Ma, Yining, Li, Jingwen, Cao, Zhiguang, Song, Wen, Guo, Hongliang, Gong, Yuejiao, Chee, Yeow Meng (2022). *Efficient Neural Neighborhood Search for Pickup and Delivery Problems*. **Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence**, 4776–4784. [(link)](https://doi.org/10.24963/ijcai.2022/662)
- <a id="paper-qin-2022"></a>Qin, Zhiwei (Tony), Zhu, Hongtu, Ye, Jieping (2022). *Reinforcement Learning for Ridesharing: An Extended Survey*. **Transportation Research Part C: Emerging Technologies**, 144, 103852. [(link)](https://doi.org/10.1016/j.trc.2022.103852)
- <a id="paper-zhang-2023"></a>Zhang, Cong, Cao, Zhiguang, Song, Wen, Wu, Yaoxin, Zhang, Jie (2023). *Deep Reinforcement Learning Guided Improvement Heuristic for Job Shop Scheduling*. **The Twelfth International Conference on Learning Representations**.
- <a id="paper-li-2025"></a>Li, Sirui, Ouyang, Wenbin, Ma, Yining, Wu, Cathy (2025). *Learning-Guided Rolling Horizon Optimization for Long-Horizon Flexible Job-Shop Scheduling*. **The Thirteenth International Conference on Learning Representations**.
- <a id="paper-desrosiers-2025"></a>Desrosiers, Jacques, Lübbecke, Marco, Desaulniers, Guy, Gauthier, Jean Bertrand (2025). *Branch-and-Price*. **Springer**.
- <a id="paper-uchoa-2024"></a>Uchoa, Eduardo, Pessoa, Artur, Moreno, Lorenza (2024). *Optimizing with Column Generation: Advanced Branch-Cut-and-Price Algorithms (Part I)*.
- <a id="paper-kouteck-a-2025"></a>Koutecká, Pavlína, Šůcha, Přemysl, Hůla, Jan, Maenhout, Broos (2025). *A Machine Learning Approach to Rank Pricing Problems in Branch-and-Price*. **European Journal of Operational Research**, 320(2), 328–342. [(link)](https://doi.org/10.1016/j.ejor.2024.07.029)
- <a id="paper-v-aclav-ik-2018"></a>Václavík, Roman, Novák, Antonín, Šůcha, Přemysl, Hanzálek, Zdeněk (2018). *Accelerating the Branch-and-Price Algorithm Using Machine Learning*. **European Journal of Operational Research**, 271(3), 1055–1069. [(link)](https://doi.org/10.1016/j.ejor.2018.05.046)
- <a id="paper-morabit-2021"></a>Morabit, Mouad, Desaulniers, Guy, Lodi, Andrea (2021). *Machine-Learning--Based Column Selection for Column Generation*. **Transportation Science**, 55(4), 815–831. [(link)](https://doi.org/10.1287/trsc.2021.1045)
- <a id="paper-shen-2022"></a>Shen, Yunzhuang, Sun, Yuan, Li, Xiaodong, Eberhard, Andrew, Ernst, Andreas (2022). *Enhancing Column Generation by a Machine-Learning-Based Pricing Heuristic for Graph Coloring*. **Proceedings of the AAAI Conference on Artificial Intelligence**, 36(9), 9926–9934. [(link)](https://doi.org/10.1609/aaai.v36i9.21230)
- <a id="paper-sun-2023"></a>Sun, Yuan, Ernst, Andreas T., Li, Xiaodong, Weiner, Jake (2023). *Learning to Generate Columns with Application to Vertex Coloring*. **The Eleventh International Conference on Learning Representations**.
- <a id="paper-balcan-2021"></a>Maria-Florina Balcan (2021). *Data-Driven Algorithm Design*. In Tim Roughgarden (ed.), **Beyond the Worst-Case Analysis of Algorithms**, 626–645. Cambridge University Press, Cambridge. [(link)](https://doi.org/10.1017/9781108637435.036)
- <a id="paper-gupta-2020"></a>Rishi Gupta, & Tim Roughgarden (2020). *Data-driven algorithm design*. **Commun. ACM**, 63(6), 87–94. [(link)](https://doi.org/10.1145/3394625)
- <a id="paper-mitzenmacher-2022"></a>Michael Mitzenmacher, & Sergei Vassilvitskii (2022). *Algorithms with predictions*. **Commun. ACM**, 65(7), 33–35. [(link)](https://doi.org/10.1145/3528087)
- <a id="paper-schede-2022"></a>Elias Schede, Jasmin Brandt, Alexander Tornede, Marcel Wever, Viktor Bengs, Eyke Hüllermeier, & Kevin Tierney (2022). *A Survey of Methods for Automated Algorithm Configuration*. **Journal of Artificial Intelligence Research**, 75, 425–487. [(link)](https://doi.org/10.1613/jair.1.13676)
- <a id="paper-l-opez-ib-a-nez-2016"></a>Manuel López‑Ibáñez, Jérémie Dubois‑Lacoste, Leslie Pérez Cáceres, Mauro Birattari, & Thomas Stützle (2016). *The irace package: Iterated racing for automatic algorithm configuration*. **Operations Research Perspectives**, 3, 43–58. [(link)](https://doi.org/10.1016/j.orp.2016.09.002)
- <a id="paper-veli-ckovi-c-2021"></a>Petar Veličković, & Charles Blundell (2021). *Neural algorithmic reasoning*. **Patterns**, 2(7), 100273. [(link)](https://doi.org/10.1016/j.patter.2021.100273)
- <a id="paper-cappart-2023"></a>Quentin Cappart, Didier Chételat, Elias B. Khalil, Andrea Lodi, Christopher Morris, & Petar Veličković (2023). *Combinatorial Optimization and Reasoning with Graph Neural Networks*. **Journal of Machine Learning Research**, 24(130), 1–61.

---

## Part III: Data-driven optimization {#part-3}

### Week 12-13: Optimization under uncertainty

- Theory in robust optimization ([Bertsimas et al. 2011](#paper-bertsimas-2011), [Gorissen et al. 2015](#paper-gorissen-2015), [Bertsimas & den Hertog 2022](#paper-bertsimas-2022))
  - 2005 Robust and Adaptive Optimization: A Tractable Approach to Optimization Under Uncertainty (by Dimitris Bertsimas @ MIT) [(link)](https://www.youtube.com/watch?v=RBbgKMpgrDg)
  - 2019 DTU Seminar: Adaptive Robust Optimization and its Applications to Power Systems (by Antonio J. Conejo @ Ohio State University) [(link)](https://www.youtube.com/watch?v=Zk6y8joQLNQ)
- ♦ Data-driven robust optimization ([Bertsimas et al. 2018](#paper-bertsimas-2018), [Goerigk & Kurtz 2023](#paper-goerigk-2023), [Ning & You 2018](#paper-ning-2018))
  - 2017 AIChE Webinar: Machine Learning and Robust Optimization (by Fengqi You @ Cornell University) [(link)](https://www.youtube.com/watch?v=7eQpuBVeCiQ)
  - 2024 Robust Optimization Webinar: Learning for Decision-Making under Uncertainty (by Bartolomeo Stellato @ Princeton University) [(link)](https://www.youtube.com/watch?v=f3nGgODXjmg)

### Week 14: Decision-focused learning

- ♦ Decision-focused learning ([Wilder et al. 2019](#paper-wilder-2019), [Mandi et al. 2024](#paper-mandi-2024))
  - 2024 CPAIOR Keynote: Decision-Focused Learning: Foundations, State of Art, Benchmarking & Opportunities (by Tias Guns @ KU Leuven) [(link)](https://www.youtube.com/watch?v=cNEL9QcHzBE)
- ♦ Predict-then-optimize ([Elmachtoub & Grigas 2022](#paper-elmachtoub-2022), [Mandi et al. 2020](#paper-mandi-2020), [Tang & Khalil 2024](#paper-tang-2024))
  - 2022 CPAIOR Master Class: Learning, Optimization, and Generalization in the Predict-then-Optimize Setting (by Tias Guns @ KU Leuven) [(link)](https://www.youtube.com/watch?v=kj5HM-af8YU)
  - 2023 ACP Summer School: Predict-then-Optimize (by Elias B. Khalil @ University of Toronto) [(link)](https://www.youtube.com/watch?v=pZqm-i57gxk)

---

## Part III — Reading list

- <a id="paper-bertsimas-2011"></a>Bertsimas, Dimitris, Brown, David B., Caramanis, Constantine (2011). *Theory and Applications of Robust Optimization*. **SIAM Review**, 53(3), 464–501. [(link)](https://doi.org/10.1137/080734510)
- <a id="paper-gorissen-2015"></a>Gorissen, Bram L., Yanıkoğlu, İhsan, den Hertog, Dick (2015). *A Practical Guide to Robust Optimization*. **Omega**, 53, 124–137. [(link)](https://doi.org/10.1016/j.omega.2014.12.006)
- <a id="paper-bertsimas-2022"></a>Bertsimas, Dimitris, den Hertog, D. (2022). *Robust and Adaptive Optimization*. **Dynamic Ideas LLC**.
- <a id="paper-bertsimas-2018"></a>Bertsimas, Dimitris, Gupta, Vishal, Kallus, Nathan (2018). *Data-Driven Robust Optimization*. **Mathematical Programming**, 167(2), 235–292. [(link)](https://doi.org/10.1007/s10107-017-1125-8)
- <a id="paper-goerigk-2023"></a>Goerigk, Marc, Kurtz, Jannis (2023). *Data-Driven Robust Optimization Using Deep Neural Networks*. **Computers & Operations Research**, 151, 106087. [(link)](https://doi.org/10.1016/j.cor.2022.106087)
- <a id="paper-ning-2018"></a>Ning, Chao, You, Fengqi (2018). *Data-Driven Stochastic Robust Optimization: General Computational Framework and Algorithm Leveraging Machine Learning for Optimization under Uncertainty in the Big Data Era*. **Computers & Chemical Engineering**, 111, 115–133. [(link)](https://doi.org/10.1016/j.compchemeng.2017.12.015)
- <a id="paper-wilder-2019"></a>Wilder, Bryan, Dilkina, Bistra, Tambe, Milind (2019). *Melding the Data-Decisions Pipeline: Decision-Focused Learning for Combinatorial Optimization*. **Proceedings of the AAAI Conference on Artificial Intelligence**, 33(01), 1658–1665. [(link)](https://doi.org/10.1609/aaai.v33i01.33011658)
- <a id="paper-mandi-2024"></a>Mandi, Jayanta, Kotary, James, Berden, Senne, Mulamba, Maxime, Bucarey, Victor, Guns, Tias, Fioretto, Ferdinando (2024). *Decision-Focused Learning: Foundations, State of the Art, Benchmark and Future Opportunities*. **Journal of Artificial Intelligence Research**, 80, 1623–1701. [(link)](https://doi.org/10.1613/jair.1.15320)
- <a id="paper-elmachtoub-2022"></a>Elmachtoub, Adam N., Grigas, Paul (2022). *Smart “Predict, Then Optimize”*. **Management Science**, 68(1), 9–26. [(link)](https://doi.org/10.1287/mnsc.2020.3922)
- <a id="paper-mandi-2020"></a>Mandi, Jayanta, Demirović, Emir, Stuckey, Peter J., Guns, Tias (2020). *Smart Predict-and-Optimize for Hard Combinatorial Optimization Problems*. **Proceedings of the AAAI Conference on Artificial Intelligence**, 34, 1603–1610. [(link)](https://doi.org/10.1609/aaai.v34i02.5521)
- <a id="paper-tang-2024"></a>Tang, Bo, Khalil, Elias B. (2024). *PyEPO: A PyTorch-based End-to-End Predict-Then-Optimize Library for Linear and Integer Programming*. **Mathematical Programming Computation**, 16(3), 297–335. [(link)](https://doi.org/10.1007/s12532-024-00255-x)

---

## Part IV: Finale {#part-4}

### Week 15: Recent topics

- Optimization over a trained neural network ([Anderson et al. 2020](#paper-anderson-2020), [Bunel et al. 2020](#paper-bunel-2020))
    - 2021 IPAM Workshop: Neural network verification as piecewise linear optimization (by Joseph Huchette @ Rice University) [(link)](https://www.youtube.com/watch?v=7w_KeAklyTc)
- ♦ Generative AI: Large language models ([Wasserkrug et al. 2025](#paper-wasserkrug-2025), [Ahmaditeshnizi et al. 2024](#paper-ahmaditeshnizi-2024), [Huang et al. 2025](#paper-huang-2025)), Foundation models ([Li et al. 2024](#paper-li-2024), [Berto et al. 2024](#paper-berto-2024)), Diffusion models, etc
    - 2024 Women in Data Science and Maths Seminar: AI and the Future of Optimization (by Madeleine Udell @ Stanford University) [(link)](https://www.youtube.com/watch?v=hI5bhPPRGmU)
    - 2025 AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms (by AlphaEvolve team @ Google DeepMind) [(link)](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
    - Combining Large Language Models and OR/MS to Make Smarter Decisions (by Boussioux @ University of Washington, and Wei Sun @ IBM Research) [(link)](https://www.youtube.com/watch?v=08em5Urkl8s)
- (Optional) Explainable AI: Survey ([De Bock et al. 2024](#paper-de-bock-2024), [Bertsimas 2019](#paper-bertsimas-2019)), Counterfactual explanations ([Guidotti 2022](#paper-guidotti-2022), [Carrizosa et al. 2024](#paper-carrizosa-2024), [Maragno et al. 2024](#paper-maragno-2024)), Tree-based explanations, Neurosymbolic AI, ...
    - 2022 NeEDS Seminar: The Counterfactual Explanation—Yet More Algorithms as a Solution to Explain Complex Models? (by David Martens @ University of Antwerp) [(link)](https://www.youtube.com/watch?v=zw7KfHFMrzM)
    - 2021 GdR RO Seminar: Combinatorial optimization and interpretable machine learning (by Thibaut Vidal @ Ecole Polytechnique Montréal) [(link)](https://www.youtube.com/watch?v=1Ix-vukTkPc)

---

## Part IV — Reading list

- <a id="paper-anderson-2020"></a>Anderson, Ross, Huchette, Joey, Ma, Will, Tjandraatmadja, Christian, Vielma, Juan Pablo (2020). *Strong Mixed-Integer Programming Formulations for Trained Neural Networks*. **Mathematical Programming**, 183(1), 3–39. [(link)](https://doi.org/10.1007/s10107-020-01474-5)
- <a id="paper-bunel-2020"></a>Bunel, Rudy, Lu, Jingyue, Turkaslan, Ilker, Torr, Philip H. S., Kohli, Pushmeet, Kumar, M. Pawan (2020). *Branch and Bound for Piecewise Linear Neural Network Verification*. **Journal of Machine Learning Research**, 21(42), 1–39.
- <a id="paper-wasserkrug-2025"></a>Wasserkrug, Segev, Boussioux, Leonard, den Hertog, Dick, Mirzazadeh, Farzaneh, Birbil, Ş. İlker, Kurtz, Jannis, Maragno, Donato (2025). *Enhancing Decision Making Through the Integration of Large Language Models and Operations Research Optimization*. **Proceedings of the AAAI Conference on Artificial Intelligence**, 39(27), 28643–28650. [(link)](https://doi.org/10.1609/aaai.v39i27.35090)
- <a id="paper-ahmaditeshnizi-2024"></a>Ahmaditeshnizi, Ali, Gao, Wenzhi, Udell, Madeleine (2024). *OptiMUS: Scalable Optimization Modeling with (MI)LP Solvers and Large Language Models*. **Proceedings of the 41st International Conference on Machine Learning**, 577–596.
- <a id="paper-huang-2025"></a>Huang, Chenyu, Tang, Zhengyang, Hu, Shixi, Jiang, Ruoqing, Zheng, Xin, Ge, Dongdong, Wang, Benyou, Wang, Zizhuo (2025). *ORLM: A Customizable Framework in Training Large Models for Automated Optimization Modeling*. **Operations Research**. [(link)](https://doi.org/10.1287/opre.2024.1233)
- <a id="paper-li-2024"></a>Li, Sirui, Kulkarni, Janardhan, Menache, Ishai, Wu, Cathy, Li, Beibin (2024). *Towards Foundation Models for Mixed Integer Linear Programming*. **The Thirteenth International Conference on Learning Representations**.
- <a id="paper-berto-2024"></a>Berto, Federico, Hua, Chuanbo, Zepeda, Nayeli Gast, Hottung, Andre, Wouda, Niels, Lan, Leon, Tierney, Kevin, Park, Jinkyoo (2024). *RouteFinder: Towards Foundation Models for Vehicle Routing Problems*. **ICML 2024 Workshop on Foundation Models in the Wild**.
- <a id="paper-de-bock-2024"></a>De Bock, Koen W., Coussement, Kristof, Caigny, Arno De, Słowinski, Roman, Baesens, Bart, Boute, Robert N., Choi, Tsan-Ming, Delen, Dursun, Kraus, Mathias, Lessmann, Stefan, Maldonado, Sebastian, Martens, David, Oskarsdottir, Maria, Vairetti, Carla, Verbeke, Wouter, Weber, Richard (2024). *Explainable AI for Operational Research: A Defining Framework, Methods, Applications, and a Research Agenda*. **European Journal of Operational Research**, 317(2), 249–272. [(link)](https://doi.org/10.1016/j.ejor.2023.09.026)
- <a id="paper-bertsimas-2019"></a>Bertsimas, Dimitris (2019). *Machine Learning Under a Modern Optimization Lens*. **Dynamic Ideas LLC**.
- <a id="paper-guidotti-2022"></a>Guidotti, Riccardo (2022). *Counterfactual Explanations and How to Find Them: Literature Review and Benchmarking*. **Data Mining and Knowledge Discovery**. [(link)](https://doi.org/10.1007/s10618-022-00831-6)
- <a id="paper-carrizosa-2024"></a>Carrizosa, Emilio, Ramirez-Ayerbe, Jasone, Romero Morales, Dolores (2024). *Mathematical Optimization Modelling for Group Counterfactual Explanations*. **European Journal of Operational Research**, 319(2), 399–412. [(link)](https://doi.org/10.1016/j.ejor.2024.01.002)
- <a id="paper-maragno-2024"></a>Maragno, Donato, Kurtz, Jannis, Rober, Tabea E., Goedhart, Rob, Birbil, Ş. İlker, den Hertog, Dick (2024). *Finding Regions of Counterfactual Explanations via Robust Optimization*. **INFORMS Journal on Computing**, 36(5), 1316–1334. [(link)](https://doi.org/10.1287/ijoc.2023.0153)

