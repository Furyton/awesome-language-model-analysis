# Awesome Transformers LM Analytics [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

This paper list focuses on the **theoretical and empirical analysis** of language models, especially **large language models** (LLMs).
The papers in this list investigate the learning behavior, generalization ability, and other properties of language models through theoretical analysis, empirical analysis, or a combination of both.

Scope of this list:
- Currently, this list focuses on **transformer-based** models.
- We hope to collect papers that only focus on the theoretical and empirical analysis of language models, instead of papers that aim to improve the performance of language models.

Limitations of this list:
- This list is not exhaustive, and we may miss some very important papers.
- This list is not well-organized yet, and we may need to reorganize the list in the future.
- Some popular topics are not well-covered yet, such as mechanistic engineering, probing, and interpretability.

If you have any suggestions or want to contribute, please feel free to open an issue or a pull request.

For details on how to contribute, please refer to the [contribution guidelines](CONTRIBUTING.md).

You can also share your thoughts and discuss with others in the [Discussions](https://github.com/Furyton/awesome-transformers-LM-analytics/discussions).

Table of Content
====================
- [Awesome Transformers LM Analytics ](#awesome-transformers-lm-analytics-)
- [Table of Content](#table-of-content)
  - [Phenomena of Interest](#phenomena-of-interest)
    - [In-Context Learning](#in-context-learning)
    - [Chain-of-Thought](#chain-of-thought)
    - [Hallucination](#hallucination)
    - [Reversal Curse](#reversal-curse)
    - [Scaling Laws / Emergent Abilities / Grokking / etc.](#scaling-laws--emergent-abilities--grokking--etc)
    - [Knowledge / Memory mechanisms](#knowledge--memory-mechanisms)
    - [Training Dynamics / Landscape / Optimization / Fine-tuning / etc.](#training-dynamics--landscape--optimization--fine-tuning--etc)
    - [Learning / Generalization](#learning--generalization)
    - [Other Phenomena](#other-phenomena)
  - [Representational Capacity](#representational-capacity)
    - [What Can Transformer Do? / Properties of Transformer](#what-can-transformer-do--properties-of-transformer)
    - [What Can Transformer Not Do? / Limitation of Transformer](#what-can-transformer-not-do--limitation-of-transformer)
  - [Architectural Effectivity](#architectural-effectivity)
    - [Layer-normalization](#layer-normalization)
    - [Tokenization](#tokenization)
  - [Training Paradigms](#training-paradigms)
  - [Mechanistic Engineering / Probing / Interpretability](#mechanistic-engineering--probing--interpretability)
  - [Miscellanea](#miscellanea)

## Phenomena of Interest

Here are some phenomena that are interesting to investigate in language models.

### In-Context Learning

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **In-Context Learning with Long-Context Models: An In-Depth Exploration** [[paper link]](http://arxiv.org/abs/2405.00200) 2024-04-30  
Amanda Bertsch; Maor Ivgi; Uri Alon; Jonathan Berant; Matthew R. Gormley; Graham Neubig



- **What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation** [[paper link]](http://arxiv.org/abs/2404.07129) 2024-04-10  
Aaditya K. Singh; Ted Moskovitz; Felix Hill; Stephanie C. Y. Chan; Andrew M. Saxe



- **Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability** [[paper link]](http://arxiv.org/abs/2310.08049) 2024-04-01  
Ivan Lee; Nan Jiang; Taylor Berg-Kirkpatrick



- **Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality** [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
Siyu Chen; Heejune Sheen; Tianhao Wang; Zhuoran Yang



- **How Transformers Learn Causal Structure with Gradient Descent** [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
Eshaan Nichani; Alex Damian; Jason D. Lee



- **In-Context Learning of a Linear Transformer Block: Benefits of the MLP Component and One-Step GD Initialization** [[paper link]](http://arxiv.org/abs/2402.14951) 2024-02-22  
Ruiqi Zhang; Jingfeng Wu; Peter L. Bartlett



- **Identifying Semantic Induction Heads to Understand In-Context Learning** [[paper link]](http://arxiv.org/abs/2402.13055) 2024-02-20  
Jie Ren; Qipeng Guo; Hang Yan; Dongrui Liu; Xipeng Qiu; Dahua Lin



- **The Transient Nature of Emergent In-Context Learning in Transformers** [[paper link]](http://arxiv.org/abs/2311.08360) 2023-12-11  
Aaditya K. Singh; Stephanie C. Y. Chan; Ted Moskovitz; Erin Grant; Andrew M. Saxe; Felix Hill



- **In-Context Learning Functions with Varying Number of Minima** [[paper link]](http://arxiv.org/abs/2311.12538) 2023-11-21  
David Oniani; Yanshan Wang



- **Exploring the Relationship between In-Context Learning and Instruction Tuning** [[paper link]](http://arxiv.org/abs/2311.10367) 2023-11-17  
Hanyu Duan; Yixuan Tang; Yi Yang; Ahmed Abbasi; Kar Yan Tam



- **When does In-context Learning Fall Short and Why? A Study on Specification-Heavy Tasks** [[paper link]](http://arxiv.org/abs/2311.08993) 2023-11-15  
Hao Peng; Xiaozhi Wang; Jianhui Chen; Weikai Li; Yunjia Qi; Zimu Wang; Zhili Wu; Kaisheng Zeng; Bin Xu; Lei Hou; Juanzi Li



- **In-context Learning Generalizes, But Not Always Robustly: The Case of Syntax** [[paper link]](http://arxiv.org/abs/2311.07811) 2023-11-13  
Aaron Mueller; Albert Webson; Jackson Petty; Tal Linzen



- **Transformers learn to implement preconditioned gradient descent for in-context learning** [[paper link]](http://arxiv.org/abs/2306.00297) 2023-11-09  
Kwangjun Ahn; Xiang Cheng; Hadi Daneshmand; Suvrit Sra



- **Transformers Learn Higher-Order Optimization Methods for In-Context Learning: A Study with Linear Models** [[paper link]](https://arxiv.org/abs/2310.17086v1) 2023-10-26  
Deqing Fu; Tian-Qi Chen; Robin Jia; Vatsal Sharan



- **In-Context Learning Creates Task Vectors** [[paper link]](http://arxiv.org/abs/2310.15916) 2023-10-24  
Roee Hendel; Mor Geva; Amir Globerson



- **Function Vectors in Large Language Models** [[paper link]](http://arxiv.org/abs/2310.15213) 2023-10-23  
Eric Todd; Millicent L. Li; Arnab Sen Sharma; Aaron Mueller; Byron C. Wallace; David Bau



- **In-context Learning with Transformer Is Really Equivalent to a Contrastive Learning Pattern** [[paper link]](http://arxiv.org/abs/2310.13220) 2023-10-19  
Ruifeng Ren; Yong Liu



- **How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations** [[paper link]](http://arxiv.org/abs/2310.10616) 2023-10-16  
Tianyu Guo; Wei Hu; Song Mei; Huan Wang; Caiming Xiong; Silvio Savarese; Yu Bai



- **Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions** [[paper link]](https://openreview.net/forum?id=ekeyCgeRfC) 2023-10-13  
Satwik Bhattamishra; Arkil Patel; Phil Blunsom; Varun Kanade



- **How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression?** [[paper link]](https://openreview.net/forum?id=vSh5ePa0ph) 2023-10-13  
Jingfeng Wu; Difan Zou; Zixiang Chen; Vladimir Braverman; Quanquan Gu; Peter Bartlett



- **In-Context Learning Learns Label Relationships but Is Not Conventional Learning** [[paper link]](https://openreview.net/forum?id=YPIA7bgd5y) 2023-10-13  
Jannik Kossen; Yarin Gal; Tom Rainforth



- **In-context Convergence of Transformers** [[paper link]](https://openreview.net/forum?id=kxpswbhr1r) 2023-10-13  
Yu Huang; Yuan Cheng; Yingbin Liang



- **In-Context Learning through the Bayesian Prism** [[paper link]](https://openreview.net/forum?id=HX5ujdsSon) 2023-10-13  
Madhur Panwar; Kabir Ahuja; Navin Goyal



- **Do pretrained Transformers Really Learn In-context by Gradient Descent?** [[paper link]](http://arxiv.org/abs/2310.08540) 2023-10-12  
Lingfeng Shen; Aayush Mishra; Daniel Khashabi



- **What and How does In-Context Learning Learn? Bayesian Model Averaging, Parameterization, and Generalization** [[paper link]](http://arxiv.org/abs/2305.19420) 2023-10-10  
Yufeng Zhang; Fengzhuo Zhang; Zhuoran Yang; Zhaoran Wang



- **Explaining Emergent In-Context Learning as Kernel Regression** [[paper link]](http://arxiv.org/abs/2305.12766) 2023-10-05  
Chi Han; Ziqi Wang; Han Zhao; Heng Ji



- **CausalLM is not optimal for in-context learning** [[paper link]](http://arxiv.org/abs/2308.06912) 2023-09-02  
Nan Ding; Tomer Levinboim; Jialin Wu; Sebastian Goodman; Radu Soricut



- **One Step of Gradient Descent is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention** [[paper link]](http://arxiv.org/abs/2307.03576) 2023-07-07  
Arvind Mahankali; Tatsunori B. Hashimoto; Tengyu Ma



- **Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection** [[paper link]](http://arxiv.org/abs/2306.04637) 2023-07-06  
Yu Bai; Fan Chen; Huan Wang; Caiming Xiong; Song Mei



- **Transformers Learn In-Context by Gradient Descent** [[paper link]](https://openreview.net/forum?id=tHvXrFQma5) 2023-06-15  
Johannes Von Oswald; Eyvind Niklasson; Ettore Randazzo; Joao Sacramento; Alexander Mordvintsev; Andrey Zhmoginov; Max Vladymyrov



- **The Closeness of In-Context Learning and Weight Shifting for Softmax Regression** [[paper link]](http://arxiv.org/abs/2304.13276) 2023-04-26  
Shuai Li; Zhao Song; Yu Xia; Tong Yu; Tianyi Zhou



- **A Theory of Emergent In-Context Learning as Implicit Structure Induction** [[paper link]](http://arxiv.org/abs/2303.07971) 2023-03-14  
Michael Hahn; Navin Goyal



- **The Learnability of In-Context Learning** [[paper link]](http://arxiv.org/abs/2303.07895) 2023-03-14  
Noam Wies; Yoav Levine; Amnon Shashua



- **What Can Transformers Learn In-Context? A Case Study of Simple Function Classes** [[paper link]](http://arxiv.org/abs/2208.01066) 2023-01-14  
Shivam Garg; Dimitris Tsipras; Percy Liang; Gregory Valiant



- **Transformers generalize differently from information stored in context vs in weights** [[paper link]](http://arxiv.org/abs/2210.05675) 2022-10-13  
Stephanie C. Y. Chan; Ishita Dasgupta; Junkyung Kim; Dharshan Kumaran; Andrew K. Lampinen; Felix Hill


</details>

### Chain-of-Thought

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Let's Think Dot by Dot: Hidden Computation in Transformer Language Models** [[paper link]](http://arxiv.org/abs/2404.15758) 2024-04-24  
Jacob Pfau; William Merrill; Samuel R. Bowman



- **Chain of Thought Empowers Transformers to Solve Inherently Serial Problems** [[paper link]](http://arxiv.org/abs/2402.12875) 2024-02-20  
Zhiyuan Li; Hong Liu; Denny Zhou; Tengyu Ma



- **Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective** [[paper link]](http://arxiv.org/abs/2305.15408) 2023-12-22  
Guhao Feng; Bohang Zhang; Yuntian Gu; Haotian Ye; Di He; Liwei Wang



- **Why Can Large Language Models Generate Correct Chain-of-Thoughts?** [[paper link]](http://arxiv.org/abs/2310.13571) 2023-10-20  
Rasul Tutunov; Antoine Grosnit; Juliusz Ziomek; Jun Wang; Haitham Bou-Ammar



- **How Large Language Models Implement Chain-of-Thought?** [[paper link]](https://openreview.net/forum?id=b2XfOm3RJa) 2023-10-13  
Yiqun Wang; Sile Hu; Yonggang Zhang; Xiang Tian; Xuesong Liu; Yaowu Chen; Xu Shen; Jieping Ye



- **The Expressive Power of Transformers with Chain of Thought** [[paper link]](https://openreview.net/forum?id=NjNGlPh8Wh) 2023-10-13  
William Merrill; Ashish Sabharwal


</details>

### Hallucination

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?** [[paper link]](http://arxiv.org/abs/2405.05904) 2024-05-09  
Zorik Gekhman; Gal Yona; Roee Aharoni; Matan Eyal; Amir Feder; Roi Reichart; Jonathan Herzig



- **Mechanisms of non-factual hallucinations in language models** [[paper link]](http://arxiv.org/abs/2403.18167) 2024-03-26  
Lei Yu; Meng Cao; Jackie Chi Kit Cheung; Yue Dong



- **Unfamiliar Finetuning Examples Control How Language Models Hallucinate** [[paper link]](http://arxiv.org/abs/2403.05612) 2024-03-08  
Katie Kang; Eric Wallace; Claire Tomlin; Aviral Kumar; Sergey Levine



- **In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation** [[paper link]](http://arxiv.org/abs/2403.01548) 2024-03-05  
Shiqi Chen; Miao Xiong; Junteng Liu; Zhengxuan Wu; Teng Xiao; Siyang Gao; Junxian He



- **Calibrated Language Models Must Hallucinate** [[paper link]](http://arxiv.org/abs/2311.14648) 2023-11-24  
Adam Tauman Kalai; Santosh S. Vempala



- **The Curious Case of Hallucinatory Unanswerablity: Finding Truths in the Hidden States of Over-Confident Large Language Models** [[paper link]](http://arxiv.org/abs/2310.11877) 2023-10-18  
Aviv Slobodkin; Omer Goldman; Avi Caciularu; Ido Dagan; Shauli Ravfogel


</details>

### Reversal Curse

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics** [[paper link]](http://arxiv.org/abs/2405.04669) 2024-05-07  
Hanlin Zhu; Baihe Huang; Shaolun Zhang; Michael Jordan; Jiantao Jiao; Yuandong Tian; Stuart Russell



- **The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"** [[paper link]](http://arxiv.org/abs/2309.12288) 2024-04-04  
Lukas Berglund; Meg Tong; Max Kaufmann; Mikita Balesni; Asa Cooper Stickland; Tomasz Korbak; Owain Evans



- **An Investigation of LLMs' Inefficacy in Understanding Converse Relations** [[paper link]](https://aclanthology.org/2023.emnlp-main.429) 2023-12-01  
Chengwen Qi; Bowen Li; Binyuan Hui; Bailin Wang; Jinyang Li; Jinwang Wu; Yuanjun Laili



- **Physics of Language Models: Part 3.2, Knowledge Manipulation** [[paper link]](http://arxiv.org/abs/2309.14402) 2023-09-25  
Zeyuan Allen-Zhu; Yuanzhi Li


</details>

### Scaling Laws / Emergent Abilities / Grokking / etc.

This section includes papers that investigate how the performance of language models scales with model size, data size, or compute, and how emergent abilities arise in language models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Beyond Scaling Laws: Understanding Transformer Performance with Associative Memory** [[paper link]](http://arxiv.org/abs/2405.08707) 2024-05-14  
Xueyan Niu; Bo Bai; Lei Deng; Wei Han



- **More Compute Is What You Need** [[paper link]](http://arxiv.org/abs/2404.19484) 2024-04-30  
Zhen Guo



- **An exactly solvable model for emergence and scaling laws** [[paper link]](http://arxiv.org/abs/2404.17563) 2024-04-26  
Yoonsoo Nam; Nayara Fonseca; Seok Hyeong Lee; Ard Louis



- **Why do small language models underperform? Studying Language Model Saturation via the Softmax Bottleneck** [[paper link]](http://arxiv.org/abs/2404.07647) 2024-04-11  
Nathan Godey; Éric de la Clergerie; Benoît Sagot



- **A Large-Scale Exploration of $\mu$-Transfer** [[paper link]](http://arxiv.org/abs/2404.05728) 2024-04-08  
Lucas Lingle



- **Emergent Abilities in Reduced-Scale Generative Language Models** [[paper link]](http://arxiv.org/abs/2404.02204) 2024-04-02  
Sherin Muckatira; Vijeta Deshpande; Vladislav Lialin; Anna Rumshisky



- **Understanding Emergent Abilities of Language Models from the Loss Perspective** [[paper link]](http://arxiv.org/abs/2403.15796) 2024-03-23  
Zhengxiao Du; Aohan Zeng; Yuxiao Dong; Jie Tang



- **Unraveling the Mystery of Scaling Laws: Part I** [[paper link]](http://arxiv.org/abs/2403.06563) 2024-03-21  
Hui Su; Zhi Tian; Xiaoyu Shen; Xunliang Cai



- **Language models scale reliably with over-training and on downstream tasks** [[paper link]](http://arxiv.org/abs/2403.08540) 2024-03-13  
Samir Yitzhak Gadre; Georgios Smyrnis; Vaishaal Shankar; Suchin Gururangan; Mitchell Wortsman; Rulin Shao; Jean Mercat; Alex Fang; Jeffrey Li; Sedrick Keh; Rui Xin; Marianna Nezhurina; Igor Vasiljevic; Jenia Jitsev; Alexandros G. Dimakis; Gabriel Ilharco; Shuran Song; Thomas Kollar; Yair Carmon; Achal Dave; Reinhard Heckel; Niklas Muennighoff; Ludwig Schmidt



- **When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method** [[paper link]](http://arxiv.org/abs/2402.17193) 2024-02-26  
Biao Zhang; Zhongtao Liu; Colin Cherry; Orhan Firat



- **Interpreting Grokked Transformers in Complex Modular Arithmetic** [[paper link]](https://arxiv.org/abs/2402.16726v2) 2024-02-26  
Hiroki Furuta; Gouki Minegishi; Yusuke Iwasawa; Yutaka Matsuo



- **A Tale of Tails: Model Collapse as a Change of Scaling Laws** [[paper link]](https://arxiv.org/abs/2402.07043) 2024-02-10  
Elvis Dohmatob; Yunzhen Feng; Pu Yang; Francois Charton; Julia Kempe



- **Scaling Data-Constrained Language Models** [[paper link]](http://arxiv.org/abs/2305.16264) 2023-10-25  
Niklas Muennighoff; Alexander M. Rush; Boaz Barak; Teven Le Scao; Aleksandra Piktus; Nouamane Tazi; Sampo Pyysalo; Thomas Wolf; Colin Raffel



- **The Cost of Down-Scaling Language Models: Fact Recall Deteriorates before In-Context Learning** [[paper link]](http://arxiv.org/abs/2310.04680) 2023-10-06  
Tian Jin; Nolan Clement; Xin Dong; Vaishnavh Nagarajan; Michael Carbin; Jonathan Ragan-Kelley; Gintare Karolina Dziugaite



- **Are Emergent Abilities of Large Language Models a Mirage?** [[paper link]](https://arxiv.org/abs/2304.15004v2) 2023-04-28  
Rylan Schaeffer; Brando Miranda; Sanmi Koyejo



- **Training Compute-Optimal Large Language Models** [[paper link]](http://arxiv.org/abs/2203.15556) 2022-03-29  
Jordan Hoffmann; Sebastian Borgeaud; Arthur Mensch; Elena Buchatskaya; Trevor Cai; Eliza Rutherford; Diego de Las Casas; Lisa Anne Hendricks; Johannes Welbl; Aidan Clark; Tom Hennigan; Eric Noland; Katie Millican; George van den Driessche; Bogdan Damoc; Aurelia Guy; Simon Osindero; Karen Simonyan; Erich Elsen; Jack W. Rae; Oriol Vinyals; Laurent Sifre



- **Scaling Laws for Neural Language Models** [[paper link]](http://arxiv.org/abs/2001.08361) 2020-01-22  
Jared Kaplan; Sam McCandlish; Tom Henighan; Tom B. Brown; Benjamin Chess; Rewon Child; Scott Gray; Alec Radford; Jeffrey Wu; Dario Amodei


</details>

### Knowledge / Memory mechanisms

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws** [[paper link]](http://arxiv.org/abs/2404.05405) 2024-04-08  
Zeyuan Allen-Zhu; Yuanzhi Li



- **Memorization Capacity of Multi-Head Attention in Transformers** [[paper link]](http://arxiv.org/abs/2306.02010) 2024-03-02  
Sadegh Mahdavi; Renjie Liao; Christos Thrampoulidis



- **Birth of a Transformer: A Memory Viewpoint** [[paper link]](http://arxiv.org/abs/2306.00802) 2023-11-06  
Alberto Bietti; Vivien Cabannes; Diane Bouchacourt; Herve Jegou; Leon Bottou



- **Physics of Language Models: Part 3.2, Knowledge Manipulation** [[paper link]](http://arxiv.org/abs/2309.14402) 2023-09-25  
Zeyuan Allen-Zhu; Yuanzhi Li



- **Can Neural Network Memorization Be Localized?** [[paper link]](http://arxiv.org/abs/2307.09542) 2023-07-18  
Pratyush Maini; Michael C. Mozer; Hanie Sedghi; Zachary C. Lipton; J. Zico Kolter; Chiyuan Zhang


</details>

### Training Dynamics / Landscape / Optimization / Fine-tuning / etc.

This section focuses on the training dynamics of language models, including the optimization landscape, fine-tuning, and transfer learning.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics** [[paper link]](http://arxiv.org/abs/2405.04669) 2024-05-07  
Hanlin Zhu; Baihe Huang; Shaolun Zhang; Michael Jordan; Jiantao Jiao; Yuandong Tian; Stuart Russell



- **Control Theoretic Approach to Fine-Tuning and Transfer Learning** [[paper link]](http://arxiv.org/abs/2404.11013) 2024-04-16  
Erkan Bayram; Shenyu Liu; Mohamed-Ali Belabbas; Tamer Başar



- **Look at the Text: Instruction-Tuned Language Models are More Robust Multiple Choice Selectors than You Think** [[paper link]](http://arxiv.org/abs/2404.08382) 2024-04-12  
Xinpeng Wang; Chengzhi Hu; Bolei Ma; Paul Röttger; Barbara Plank



- **On Training Data Influence of GPT Models** [[paper link]](http://arxiv.org/abs/2404.07840) 2024-04-11  
Qingyi Liu; Yekun Chai; Shuohuan Wang; Yu Sun; Keze Wang; Hua Wu



- **Best Practices and Lessons Learned on Synthetic Data for Language Models** [[paper link]](http://arxiv.org/abs/2404.07503) 2024-04-11  
Ruibo Liu; Jerry Wei; Fangyu Liu; Chenglei Si; Yanzhe Zhang; Jinmeng Rao; Steven Zheng; Daiyi Peng; Diyi Yang; Denny Zhou; Andrew M. Dai



- **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** [[paper link]](http://arxiv.org/abs/2404.05090) 2024-04-07  
Mohamed El Amine Seddik; Suei-Wen Chen; Soufiane Hayou; Pierre Youssef; Merouane Debbah



- **Unveiling the Generalization Power of Fine-Tuned Large Language Models** [[paper link]](http://arxiv.org/abs/2403.09162) 2024-03-14  
Haoran Yang; Yumeng Zhang; Jiaqi Xu; Hongyuan Lu; Pheng Ann Heng; Wai Lam



- **Transformers Get Stable: An End-to-End Signal Propagation Theory for Language Models** [[paper link]](http://arxiv.org/abs/2403.09635) 2024-03-14  
Akhil Kedia; Mohd Abbas Zaidi; Sushil Khyalia; Jungho Jung; Harshith Goka; Haejun Lee



- **Linear Attention is (Maybe) All You Need (to Understand Transformer Optimization)** [[paper link]](http://arxiv.org/abs/2310.01082) 2024-03-13  
Kwangjun Ahn; Xiang Cheng; Minhak Song; Chulhee Yun; Ali Jadbabaie; Suvrit Sra



- **Hallmarks of Optimization Trajectories in Neural Networks and LLMs: The Lengths, Bends, and Dead Ends** [[paper link]](http://arxiv.org/abs/2403.07379) 2024-03-12  
Sidak Pal Singh; Bobby He; Thomas Hofmann; Bernhard Schölkopf



- **The Heuristic Core: Understanding Subnetwork Generalization in Pretrained Language Models** [[paper link]](http://arxiv.org/abs/2403.03942) 2024-03-06  
Adithya Bhaskar; Dan Friedman; Danqi Chen



- **Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality** [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
Siyu Chen; Heejune Sheen; Tianhao Wang; Zhuoran Yang



- **How Transformers Learn Causal Structure with Gradient Descent** [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
Eshaan Nichani; Alex Damian; Jason D. Lee



- **Transformers learn through gradual rank increase** [[paper link]](http://arxiv.org/abs/2306.07042) 2023-12-10  
Enric Boix-Adsera; Etai Littwin; Emmanuel Abbe; Samy Bengio; Joshua Susskind



- **Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks** [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



- **Connecting Pre-trained Language Model and Downstream Task via Properties of Representation** [[paper link]](https://openreview.net/forum?id=YLOJ4aKAka) 2023-11-02  
Chenwei Wu; Holden Lee; Rong Ge



- **Scan and Snap: Understanding Training Dynamics and Token Composition in 1-layer Transformer** [[paper link]](http://arxiv.org/abs/2305.16380) 2023-07-02  
Yuandong Tian; Yiping Wang; Beidi Chen; Simon Du



- **A Kernel-Based View of Language Model Fine-Tuning** [[paper link]](https://openreview.net/forum?id=49dTFIGdx8) 2023-06-15  
Sadhika Malladi; Alexander Wettig; Dingli Yu; Danqi Chen; Sanjeev Arora



- **A Stability Analysis of Fine-Tuning a Pre-Trained Model** [[paper link]](https://arxiv.org/abs/2301.09820v2) 2023-01-24  
Zihao Fu; Anthony Man-Cho So; Nigel Collier


</details>

### Learning / Generalization

This section includes papers that investigate the generalization ability of language models, and the general learning behavior of language models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Initialization is Critical to Whether Transformers Fit Composite Functions by Inference or Memorizing** [[paper link]](http://arxiv.org/abs/2405.05409) 2024-05-08  
Zhongwang Zhang; Pengxiao Lin; Zhiwei Wang; Yaoyu Zhang; Zhi-Qin John Xu



- **Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks** [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



- **The Impact of Depth and Width on Transformer Language Model Generalization** [[paper link]](http://arxiv.org/abs/2310.19956) 2023-10-30  
Jackson Petty; Sjoerd van Steenkiste; Ishita Dasgupta; Fei Sha; Dan Garrette; Tal Linzen



- **How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition** [[paper link]](http://arxiv.org/abs/2310.05492) 2023-10-09  
Guanting Dong; Hongyi Yuan; Keming Lu; Chengpeng Li; Mingfeng Xue; Dayiheng Liu; Wei Wang; Zheng Yuan; Chang Zhou; Jingren Zhou



- **A Theory for Emergence of Complex Skills in Language Models** [[paper link]](http://arxiv.org/abs/2307.15936) 2023-07-29  
Sanjeev Arora; Anirudh Goyal



- **On the Power of Foundation Models** [[paper link]](https://proceedings.mlr.press/v202/yuan23b.html) 2023-07-03  
Yang Yuan



- **Task-Specific Skill Localization in Fine-tuned Language Models** [[paper link]](https://openreview.net/forum?id=Rgnaj43Pk0) 2023-06-15  
Abhishek Panigrahi; Nikunj Saunshi; Haoyu Zhao; Sanjeev Arora



- **Towards Understanding Why Mask-Reconstruction Pretraining Helps in Downstream Tasks** [[paper link]](http://arxiv.org/abs/2206.03826) 2023-02-11  
Jiachun Pan; Pan Zhou; Shuicheng Yan



- **Same Pre-training Loss, Better Downstream: Implicit Bias Matters for Language Models** [[paper link]](http://arxiv.org/abs/2210.14199) 2022-10-25  
Hong Liu; Sang Michael Xie; Zhiyuan Li; Tengyu Ma



- **Why Do Pretrained Language Models Help in Downstream Tasks? An Analysis of Head and Prompt Tuning** [[paper link]](http://arxiv.org/abs/2106.09226) 2022-04-20  
Colin Wei; Sang Michael Xie; Tengyu Ma



- **A Mathematical Exploration of Why Language Models Help Solve Downstream Tasks** [[paper link]](http://arxiv.org/abs/2010.03648) 2021-04-14  
Nikunj Saunshi; Sadhika Malladi; Sanjeev Arora



- **Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning** [[paper link]](http://arxiv.org/abs/2012.13255) 2020-12-22  
Armen Aghajanyan; Luke Zettlemoyer; Sonal Gupta



- **How fine can fine-tuning be? Learning efficient language models** [[paper link]](https://proceedings.mlr.press/v108/radiya-dixit20a.html) 2020-06-03  
Evani Radiya-Dixit; Xin Wang


</details>

### Other Phenomena

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **The Platonic Representation Hypothesis** [[paper link]](https://arxiv.org/abs/2405.07987v1) 2024-05-13  
Minyoung Huh; Brian Cheung; Tongzhou Wang; Phillip Isola



- **Algorithmic progress in language models** [[paper link]](http://arxiv.org/abs/2403.05812) 2024-03-09  
Anson Ho; Tamay Besiroglu; Ege Erdil; David Owen; Robi Rahman; Zifan Carl Guo; David Atkinson; Neil Thompson; Jaime Sevilla



- **Massive Activations in Large Language Models** [[paper link]](http://arxiv.org/abs/2402.17762) 2024-02-27  
Mingjie Sun; Xinlei Chen; J. Zico Kolter; Zhuang Liu



- **The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers** [[paper link]](https://openreview.net/forum?id=TJ2nxciYCk-) 2023-02-01  
Zonglin Li; Chong You; Srinadh Bhojanapalli; Daliang Li; Ankit Singh Rawat; Sashank J. Reddi; Ke Ye; Felix Chern; Felix Yu; Ruiqi Guo; Sanjiv Kumar


</details>

## Representational Capacity

Investigate the expressiveness of transformer-based models about what they can do and what they can't do.

### What Can Transformer Do? / Properties of Transformer

This section includes positive results on the representational capacity and properties of transformer-based models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **ALPINE: Unveiling the Planning Capability of Autoregressive Learning in Language Models** [[paper link]](http://arxiv.org/abs/2405.09220) 2024-05-15  
 Siwei Wang; Yifei Shen; Shi Feng; Haoran Sun; Shang-Hua Teng; Wei Chen



- **What Formal Languages Can Transformers Express? A Survey** [[paper link]](http://arxiv.org/abs/2311.00208) 2024-05-06  
Lena Strobl; William Merrill; Gail Weiss; David Chiang; Dana Angluin



- **Transformers Can Represent $n$-gram Language Models** [[paper link]](http://arxiv.org/abs/2404.14994) 2024-04-23  
Anej Svete; Ryan Cotterell



- **Mechanics of Next Token Prediction with Self-Attention** [[paper link]](https://proceedings.mlr.press/v238/li24f.html) 2024-04-18  
Yingcong Li; Yixiao Huang; Muhammed E. Ildiz; Ankit Singh Rawat; Samet Oymak



- **When can transformers reason with abstract symbols?** [[paper link]](http://arxiv.org/abs/2310.09753) 2024-04-16  
Enric Boix-Adsera; Omid Saremi; Emmanuel Abbe; Samy Bengio; Etai Littwin; Joshua Susskind



- **The Illusion of State in State-Space Models** [[paper link]](http://arxiv.org/abs/2404.08819) 2024-04-12  
William Merrill; Jackson Petty; Ashish Sabharwal



- **Attention is Naturally Sparse with Gaussian Distributed Input** [[paper link]](http://arxiv.org/abs/2404.02690) 2024-04-03  
Yichuan Deng; Zhao Song; Chiwun Yang



- **What Can Transformer Learn with Varying Depth? Case Studies on Sequence Learning Tasks** [[paper link]](http://arxiv.org/abs/2404.01601) 2024-04-01  
Xingwu Chen; Difan Zou



- **The Topos of Transformer Networks** [[paper link]](http://arxiv.org/abs/2403.18415) 2024-03-27  
Mattia Jacopo Villani; Peter McBurney



- **Simulating Weighted Automata over Sequences and Trees with Transformers** [[paper link]](http://arxiv.org/abs/2403.09728) 2024-03-12  
Michael Rizvi; Maude Lizaire; Clara Lacroce; Guillaume Rabusseau



- **Simplicity Bias of Transformers to Learn Low Sensitivity Functions** [[paper link]](http://arxiv.org/abs/2403.06925) 2024-03-11  
Bhavya Vasudeva; Deqing Fu; Tianyi Zhou; Elliott Kau; Youqi Huang; Vatsal Sharan



- **On the Origins of Linear Representations in Large Language Models** [[paper link]](http://arxiv.org/abs/2403.03867) 2024-03-06  
Yibo Jiang; Goutham Rajendran; Pradeep Ravikumar; Bryon Aragam; Victor Veitch



- **How Well Can Transformers Emulate In-context Newton's Method?** [[paper link]](http://arxiv.org/abs/2403.03183) 2024-03-05  
Angeliki Giannou; Liu Yang; Tianhao Wang; Dimitris Papailiopoulos; Jason D. Lee



- **RNNs are not Transformers (Yet): The Key Bottleneck on In-context Retrieval** [[paper link]](http://arxiv.org/abs/2402.18510) 2024-02-29  
Kaiyue Wen; Xingyu Dang; Kaifeng Lyu



- **Implicit Bias of Next-Token Prediction** [[paper link]](http://arxiv.org/abs/2402.18551) 2024-02-28  
Christos Thrampoulidis



- **On the Expressive Power of a Variant of the Looped Transformer** [[paper link]](http://arxiv.org/abs/2402.13572) 2024-02-21  
Yihang Gao; Chuanyang Zheng; Enze Xie; Han Shi; Tianyang Hu; Yu Li; Michael K. Ng; Zhenguo Li; Zhaoqiang Liu



- **From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers** [[paper link]](http://arxiv.org/abs/2402.13512) 2024-02-20  
M. Emrullah Ildiz; Yixiao Huang; Yingcong Li; Ankit Singh Rawat; Samet Oymak



- **Transformers Implement Functional Gradient Descent to Learn Non-Linear Functions In Context** [[paper link]](http://arxiv.org/abs/2312.06528) 2024-02-15  
Xiang Cheng; Yuxin Chen; Suvrit Sra



- **Compositional Capabilities of Autoregressive Transformers: A Study on Synthetic, Interpretable Tasks** [[paper link]](http://arxiv.org/abs/2311.12997) 2024-02-05  
Rahul Ramesh; Ekdeep Singh Lubana; Mikail Khona; Robert P. Dick; Hidenori Tanaka



- **Are Transformers with One Layer Self-Attention Using Low-Rank Weight Matrices Universal Approximators?** [[paper link]](http://arxiv.org/abs/2307.14023) 2024-01-29  
Tokio Kajitsuka; Issei Sato



- **Transformers are Multi-State RNNs** [[paper link]](http://arxiv.org/abs/2401.06104) 2024-01-11  
Matanel Oren; Michael Hassid; Yossi Adi; Roy Schwartz



- **How Capable Can a Transformer Become? A Study on Synthetic, Interpretable Tasks** [[paper link]](https://openreview.net/forum?id=KIhFggzePM) 2023-12-12  
Rahul Ramesh; Mikail Khona; Robert P. Dick; Hidenori Tanaka; Ekdeep Singh Lubana



- **Transformers can optimally learn regression mixture models** [[paper link]](http://arxiv.org/abs/2311.08362) 2023-11-14  
Reese Pathak; Rajat Sen; Weihao Kong; Abhimanyu Das



- **The Expressive Power of Low-Rank Adaptation** [[paper link]](http://arxiv.org/abs/2310.17513) 2023-10-26  
Yuchen Zeng; Kangwook Lee



- **What Algorithms can Transformers Learn? A Study in Length Generalization** [[paper link]](http://arxiv.org/abs/2310.16028) 2023-10-24  
Hattie Zhou; Arwen Bradley; Etai Littwin; Noam Razin; Omid Saremi; Josh Susskind; Samy Bengio; Preetum Nakkiran



- **Transformers as Support Vector Machines** [[paper link]](http://arxiv.org/abs/2308.16898) 2023-09-07  
Davoud Ataee Tarzanagh; Yingcong Li; Christos Thrampoulidis; Samet Oymak



- **How Do Transformers Learn Topic Structure: Towards a Mechanistic Understanding** [[paper link]](https://openreview.net/forum?id=LMXgU4zrq6) 2023-06-15  
Yuchen Li; Yuanzhi Li; Andrej Risteski



- **Tighter Bounds on the Expressivity of Transformer Encoders** [[paper link]](https://openreview.net/forum?id=XKcogevHj8) 2023-06-15  
David Chiang; Peter Cholak; Anand Pillay



- **Fast Attention Requires Bounded Entries** [[paper link]](https://arxiv.org/abs/2302.13214v2) 2023-02-26  
Josh Alman; Zhao Song



- **Transformers Learn Shortcuts to Automata** [[paper link]](https://openreview.net/forum?id=De4FYqjFueZ) 2023-02-01  
Bingbin Liu; Jordan T. Ash; Surbhi Goel; Akshay Krishnamurthy; Cyril Zhang



- **Transformer Vs. MLP-Mixer: Exponential Expressive Gap For NLP Problems** [[paper link]](http://arxiv.org/abs/2208.08191) 2022-11-17  
Dan Navon; Alex M. Bronstein



- **Small Transformers Compute Universal Metric Embeddings** [[paper link]](http://arxiv.org/abs/2209.06788) 2022-10-18  
Anastasis Kratsios; Valentin Debarnot; Ivan Dokmanić



- **The Lipschitz Constant of Self-Attention** [[paper link]](http://arxiv.org/abs/2006.04710) 2021-06-09  
Hyunjik Kim; George Papamakarios; Andriy Mnih



- **On Identifiability in Transformers** [[paper link]](http://arxiv.org/abs/1908.04211) 2020-02-07  
Gino Brunner; Yang Liu; Damián Pascual; Oliver Richter; Massimiliano Ciaramita; Roger Wattenhofer


</details>

### What Can Transformer Not Do? / Limitation of Transformer

The papers in this section investigate the limitations of transformer-based models, including the limitations of their expressiveness and learning abilities.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Collapse of Self-trained Language Models** [[paper link]](http://arxiv.org/abs/2404.02305) 2024-04-02  
David Herel; Tomas Mikolov



- **The pitfalls of next-token prediction** [[paper link]](http://arxiv.org/abs/2403.06963) 2024-03-11  
Gregor Bachmann; Vaishnavh Nagarajan



- **Why are Sensitive Functions Hard for Transformers?** [[paper link]](http://arxiv.org/abs/2402.09963) 2024-03-03  
Michael Hahn; Mark Rofin



- **Transformers are Expressive, But Are They Expressive Enough for Regression?** [[paper link]](http://arxiv.org/abs/2402.15478) 2024-02-23  
Swaroop Nath; Harshad Khadilkar; Pushpak Bhattacharyya



- **Limits of Transformer Language Models on Learning Algorithmic Compositions** [[paper link]](http://arxiv.org/abs/2402.05785) 2024-02-13  
Jonathan Thomm; Aleksandar Terzic; Geethan Karunaratne; Giacomo Camposampiero; Bernhard Schölkopf; Abbas Rahimi



- **Representational Strengths and Limitations of Transformers** [[paper link]](http://arxiv.org/abs/2306.02896) 2023-11-16  
Clayton Sanford; Daniel Hsu; Matus Telgarsky



- **Large Language Models Cannot Self-Correct Reasoning Yet** [[paper link]](https://openreview.net/forum?id=IkmD3fKBPQ) 2023-10-13  
Jie Huang; Xinyun Chen; Swaroop Mishra; Huaixiu Steven Zheng; Adams Wei Yu; Xinying Song; Denny Zhou



- **Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth** [[paper link]](http://arxiv.org/abs/2103.03404) 2023-08-01  
Yihe Dong; Jean-Baptiste Cordonnier; Andreas Loukas



- **Limits for Learning with Language Models** [[paper link]](http://arxiv.org/abs/2306.12213) 2023-06-21  
Nicholas Asher; Swarnadeep Bhar; Akshay Chaturvedi; Julie Hunter; Soumya Paul



- **Your Transformer May Not be as Powerful as You Expect** [[paper link]](https://openreview.net/forum?id=NQFFNdsOGD) 2022-10-31  
Shengjie Luo; Shanda Li; Shuxin Zheng; Tie-Yan Liu; Liwei Wang; Di He



- **The Devil in Linear Transformer** [[paper link]](http://arxiv.org/abs/2210.10340) 2022-10-19  
Zhen Qin; XiaoDong Han; Weixuan Sun; Dongxu Li; Lingpeng Kong; Nick Barnes; Yiran Zhong


</details>

## Architectural Effectivity

discussion of the effectiveness of different architectures in terms of learning and generalization

### Layer-normalization

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **The Expressive Power of Tuning Only the Normalization Layers** [[paper link]](https://proceedings.mlr.press/v195/giannou23a.html) 2023-07-12  
Angeliki Giannou; Shashank Rajput; Dimitris Papailiopoulos



- **ResiDual: Transformer with Dual Residual Connections** [[paper link]](http://arxiv.org/abs/2304.14802) 2023-04-28  
Shufang Xie; Huishuai Zhang; Junliang Guo; Xu Tan; Jiang Bian; Hany Hassan Awadalla; Arul Menezes; Tao Qin; Rui Yan



- **DeepNet: Scaling Transformers to 1,000 Layers** [[paper link]](http://arxiv.org/abs/2203.00555) 2022-03-01  
Hongyu Wang; Shuming Ma; Li Dong; Shaohan Huang; Dongdong Zhang; Furu Wei



- **On Layer Normalization in the Transformer Architecture** [[paper link]](http://arxiv.org/abs/2002.04745) 2020-06-29  
Ruibin Xiong; Yunchang Yang; Di He; Kai Zheng; Shuxin Zheng; Chen Xing; Huishuai Zhang; Yanyan Lan; Liwei Wang; Tie-Yan Liu


</details>

### Tokenization

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Toward a Theory of Tokenization in LLMs** [[paper link]](http://arxiv.org/abs/2404.08335) 2024-04-12  
Nived Rajaraman; Jiantao Jiao; Kannan Ramchandran



- **On the Effect of (Near) Duplicate Subwords in Language Modelling** [[paper link]](http://arxiv.org/abs/2404.06508) 2024-04-09  
Anton Schäfer; Thomas Hofmann; Imanol Schlag; Tiago Pimentel



- **Tokenization Is More Than Compression** [[paper link]](http://arxiv.org/abs/2402.18376) 2024-02-28  
Craig W. Schmidt; Varshini Reddy; Haoran Zhang; Alec Alameddine; Omri Uzan; Yuval Pinter; Chris Tanner


</details>

## Training Paradigms

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Knowledge Distillation vs. Pretraining from Scratch under a Fixed (Computation) Budget** [[paper link]](http://arxiv.org/abs/2404.19319) 2024-04-30  
Minh Duc Bui; Fabian David Schmidt; Goran Glavaš; Katharina von der Wense



- **Why are Adaptive Methods Good for Attention Models?** [[paper link]](http://arxiv.org/abs/1912.03194) 2020-10-23  
Jingzhao Zhang; Sai Praneeth Karimireddy; Andreas Veit; Seungyeon Kim; Sashank J. Reddi; Sanjiv Kumar; Suvrit Sra


</details>

## Mechanistic Engineering / Probing / Interpretability

This section includes papers that mainly investigate the mechanisms of language models through probing, mechanistic engineering, and other papers generally related to interpretability.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Anchored Answers: Unravelling Positional Bias in GPT-2's Multiple-Choice Questions** [[paper link]](https://arxiv.org/abs/2405.03205) 2024-05-06  
Ruizhe Li; Yanjun Gao



- **A Primer on the Inner Workings of Transformer-based Language Models** [[paper link]](https://arxiv.org/abs/2405.00208) 2024-05-02  
Javier Ferrando; Gabriele Sarti; Arianna Bisazza; Marta R. Costa-jussà



- **Talking Nonsense: Probing Large Language Models' Understanding of Adversarial Gibberish Inputs** [[paper link]](http://arxiv.org/abs/2404.17120) 2024-04-25  
Valeriia Cherepanova; James Zou



- **Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions** [[paper link]](http://arxiv.org/abs/2402.15055) 2024-02-22  
Clement Neo; Shay B. Cohen; Fazl Barez



- **Universal Neurons in GPT2 Language Models** [[paper link]](http://arxiv.org/abs/2401.12181) 2024-01-22  
Wes Gurnee; Theo Horsley; Zifan Carl Guo; Tara Rezaei Kheirkhah; Qinyi Sun; Will Hathaway; Neel Nanda; Dimitris Bertsimas



- **Interpretability Illusions in the Generalization of Simplified Models** [[paper link]](http://arxiv.org/abs/2312.03656) 2023-12-06  
Dan Friedman; Andrew Lampinen; Lucas Dixon; Danqi Chen; Asma Ghandeharioun



- **Transformers are uninterpretable with myopic methods: a case study with bounded Dyck grammars** [[paper link]](http://arxiv.org/abs/2312.01429) 2023-12-03  
Kaiyue Wen; Yuchen Li; Bingbin Liu; Andrej Risteski



- **White-Box Transformers via Sparse Rate Reduction: Compression Is All There Is?** [[paper link]](https://arxiv.org/abs/2311.13110v2) 2023-11-22  
Yaodong Yu; Sam Buchanan; Druv Pai; Tianzhe Chu; Ziyang Wu; Shengbang Tong; Hao Bai; Yuexiang Zhai; Benjamin D. Haeffele; Yi Ma



- **Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks** [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



- **Understanding the Mechanics and Dynamics of Memorisation in Large Language Models: A Case Study with Random Strings** [[paper link]](https://openreview.net/forum?id=ILStlRb1Sp) 2023-10-13  
Till Speicher; Aflah Mohammad Khan; Qinyuan Wu; Vedant Nanda; Soumi Das; Bishwamittra Ghosh; Krishna P. Gummadi; Evimaria Terzi


</details>

## Miscellanea

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Dynamic Activation Pitfalls in LLaMA Models: An Empirical Study** [[paper link]](http://arxiv.org/abs/2405.09274) 2024-05-15  
Chi Ma; Mincong Huang; Chao Wang; Yujie Wang; Lei Yu



- **Challenges in Deploying Long-Context Transformers: A Theoretical Peak Performance Analysis** [[paper link]](http://arxiv.org/abs/2405.08944) 2024-05-14  
Yao Fu



- **Understand LLMs Requires More Than Statistical Generalization** [[paper link]](http://arxiv.org/abs/2405.01964) 2024-05-03  
Patrik Reizinger; Szilvia Ujváry; Anna Mészáros; Anna Kerekes; Wieland Brendel; Ferenc Huszár



- **Compression Represents Intelligence Linearly** [[paper link]](http://arxiv.org/abs/2404.09937) 2024-04-15  
Yuzhen Huang; Jinghan Zhang; Zifei Shan; Junxian He



- **Language Generation in the Limit** [[paper link]](http://arxiv.org/abs/2404.06757) 2024-04-10  
Jon Kleinberg; Sendhil Mullainathan



- **Do language models plan ahead for future tokens?** [[paper link]](http://arxiv.org/abs/2404.00859) 2024-03-31  
Wilson Wu; John X. Morris; Lionel Levine



- **What's In My Big Data?** [[paper link]](http://arxiv.org/abs/2310.20707) 2024-03-05  
Yanai Elazar; Akshita Bhagia; Ian Magnusson; Abhilasha Ravichander; Dustin Schwenk; Alane Suhr; Pete Walsh; Dirk Groeneveld; Luca Soldaini; Sameer Singh; Hanna Hajishirzi; Noah A. Smith; Jesse Dodge



- **Universality and Limitations of Prompt Tuning** [[paper link]](http://arxiv.org/abs/2305.18787) 2023-11-16  
Yihan Wang; Jatin Chauhan; Wei Wang; Cho-Jui Hsieh



- **Data Similarity is Not Enough to Explain Language Model Performance** [[paper link]](http://arxiv.org/abs/2311.09006) 2023-11-15  
Gregory Yauney; Emily Reif; David Mimno



- **Simplifying Transformer Blocks** [[paper link]](http://arxiv.org/abs/2311.01906) 2023-11-03  
Bobby He; Thomas Hofmann



- **Causal Interpretation of Self-Attention in Pre-Trained Transformers** [[paper link]](http://arxiv.org/abs/2310.20307) 2023-10-31  
Raanan Y. Rohekar; Yaniv Gurwicz; Shami Nisimov



- **How do Language Models Bind Entities in Context?** [[paper link]](http://arxiv.org/abs/2310.17191) 2023-10-26  
Jiahai Feng; Jacob Steinhardt



- **Understanding prompt engineering may not require rethinking generalization** [[paper link]](https://openreview.net/forum?id=a745RnSFLT) 2023-10-13  
Victor Akinwande; Yiding Jiang; Dylan Sam; J. Zico Kolter



- **Understanding Catastrophic Forgetting in Language Models via Implicit Inference** [[paper link]](http://arxiv.org/abs/2309.10105) 2023-09-18  
Suhas Kotha; Jacob Mitchell Springer; Aditi Raghunathan



- **Attention-Only Transformers and Implementing MLPs with Attention Heads** [[paper link]](http://arxiv.org/abs/2309.08593) 2023-09-15  
Robert Huben; Valerie Morris



- **On the Role of Attention in Prompt-tuning** [[paper link]](https://openreview.net/forum?id=qorOnDor89) 2023-06-15  
Samet Oymak; Ankit Singh Rawat; Mahdi Soltanolkotabi; Christos Thrampoulidis


</details>

---

Contact:

- [Shiguang Wu](https://github.com/Furyton), furyton AT outlook.com / shiguang.wu AT mail.sdu.edu.cn