---
layout: archive
title: "AI for Discrete Optimization (IMEN891N, Fall 2025)"
permalink: /teaching/ai4do/2025/part-2
author_profile: false
---

(♦: In-class presentation by students)

## Part II: Data-driven algorithm design

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