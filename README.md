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

**Title**: In-Context Learning with Long-Context Models: An In-Depth Exploration [[paper link]](http://arxiv.org/abs/2405.00200) 2024-04-30  
**Authors**: Amanda Bertsch; Maor Ivgi; Uri Alon; Jonathan Berant; Matthew R. Gormley; Graham Neubig



**Title**: What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation [[paper link]](http://arxiv.org/abs/2404.07129) 2024-04-10  
**Authors**: Aaditya K. Singh; Ted Moskovitz; Felix Hill; Stephanie C. Y. Chan; Andrew M. Saxe



**Title**: Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability [[paper link]](http://arxiv.org/abs/2310.08049) 2024-04-01  
**Authors**: Ivan Lee; Nan Jiang; Taylor Berg-Kirkpatrick



**Title**: Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
**Authors**: Siyu Chen; Heejune Sheen; Tianhao Wang; Zhuoran Yang



**Title**: How Transformers Learn Causal Structure with Gradient Descent [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
**Authors**: Eshaan Nichani; Alex Damian; Jason D. Lee



**Title**: In-Context Learning of a Linear Transformer Block: Benefits of the MLP Component and One-Step GD Initialization [[paper link]](http://arxiv.org/abs/2402.14951) 2024-02-22  
**Authors**: Ruiqi Zhang; Jingfeng Wu; Peter L. Bartlett



**Title**: Identifying Semantic Induction Heads to Understand In-Context Learning [[paper link]](http://arxiv.org/abs/2402.13055) 2024-02-20  
**Authors**: Jie Ren; Qipeng Guo; Hang Yan; Dongrui Liu; Xipeng Qiu; Dahua Lin



**Title**: The Transient Nature of Emergent In-Context Learning in Transformers [[paper link]](http://arxiv.org/abs/2311.08360) 2023-12-11  
**Authors**: Aaditya K. Singh; Stephanie C. Y. Chan; Ted Moskovitz; Erin Grant; Andrew M. Saxe; Felix Hill



**Title**: In-Context Learning Functions with Varying Number of Minima [[paper link]](http://arxiv.org/abs/2311.12538) 2023-11-21  
**Authors**: David Oniani; Yanshan Wang



**Title**: Exploring the Relationship between In-Context Learning and Instruction Tuning [[paper link]](http://arxiv.org/abs/2311.10367) 2023-11-17  
**Authors**: Hanyu Duan; Yixuan Tang; Yi Yang; Ahmed Abbasi; Kar Yan Tam



**Title**: When does In-context Learning Fall Short and Why? A Study on Specification-Heavy Tasks [[paper link]](http://arxiv.org/abs/2311.08993) 2023-11-15  
**Authors**: Hao Peng; Xiaozhi Wang; Jianhui Chen; Weikai Li; Yunjia Qi; Zimu Wang; Zhili Wu; Kaisheng Zeng; Bin Xu; Lei Hou; Juanzi Li



**Title**: In-context Learning Generalizes, But Not Always Robustly: The Case of Syntax [[paper link]](http://arxiv.org/abs/2311.07811) 2023-11-13  
**Authors**: Aaron Mueller; Albert Webson; Jackson Petty; Tal Linzen



**Title**: Transformers learn to implement preconditioned gradient descent for in-context learning [[paper link]](http://arxiv.org/abs/2306.00297) 2023-11-09  
**Authors**: Kwangjun Ahn; Xiang Cheng; Hadi Daneshmand; Suvrit Sra



**Title**: Transformers Learn Higher-Order Optimization Methods for In-Context Learning: A Study with Linear Models [[paper link]](https://arxiv.org/abs/2310.17086v1) 2023-10-26  
**Authors**: Deqing Fu; Tian-Qi Chen; Robin Jia; Vatsal Sharan



**Title**: In-Context Learning Creates Task Vectors [[paper link]](http://arxiv.org/abs/2310.15916) 2023-10-24  
**Authors**: Roee Hendel; Mor Geva; Amir Globerson



**Title**: Function Vectors in Large Language Models [[paper link]](http://arxiv.org/abs/2310.15213) 2023-10-23  
**Authors**: Eric Todd; Millicent L. Li; Arnab Sen Sharma; Aaron Mueller; Byron C. Wallace; David Bau



**Title**: In-context Learning with Transformer Is Really Equivalent to a Contrastive Learning Pattern [[paper link]](http://arxiv.org/abs/2310.13220) 2023-10-19  
**Authors**: Ruifeng Ren; Yong Liu



**Title**: How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations [[paper link]](http://arxiv.org/abs/2310.10616) 2023-10-16  
**Authors**: Tianyu Guo; Wei Hu; Song Mei; Huan Wang; Caiming Xiong; Silvio Savarese; Yu Bai



**Title**: Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions [[paper link]](https://openreview.net/forum?id=ekeyCgeRfC) 2023-10-13  
**Authors**: Satwik Bhattamishra; Arkil Patel; Phil Blunsom; Varun Kanade



**Title**: How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression? [[paper link]](https://openreview.net/forum?id=vSh5ePa0ph) 2023-10-13  
**Authors**: Jingfeng Wu; Difan Zou; Zixiang Chen; Vladimir Braverman; Quanquan Gu; Peter Bartlett



**Title**: In-Context Learning Learns Label Relationships but Is Not Conventional Learning [[paper link]](https://openreview.net/forum?id=YPIA7bgd5y) 2023-10-13  
**Authors**: Jannik Kossen; Yarin Gal; Tom Rainforth



**Title**: In-context Convergence of Transformers [[paper link]](https://openreview.net/forum?id=kxpswbhr1r) 2023-10-13  
**Authors**: Yu Huang; Yuan Cheng; Yingbin Liang



**Title**: In-Context Learning through the Bayesian Prism [[paper link]](https://openreview.net/forum?id=HX5ujdsSon) 2023-10-13  
**Authors**: Madhur Panwar; Kabir Ahuja; Navin Goyal



**Title**: Do pretrained Transformers Really Learn In-context by Gradient Descent? [[paper link]](http://arxiv.org/abs/2310.08540) 2023-10-12  
**Authors**: Lingfeng Shen; Aayush Mishra; Daniel Khashabi



**Title**: What and How does In-Context Learning Learn? Bayesian Model Averaging, Parameterization, and Generalization [[paper link]](http://arxiv.org/abs/2305.19420) 2023-10-10  
**Authors**: Yufeng Zhang; Fengzhuo Zhang; Zhuoran Yang; Zhaoran Wang



**Title**: Explaining Emergent In-Context Learning as Kernel Regression [[paper link]](http://arxiv.org/abs/2305.12766) 2023-10-05  
**Authors**: Chi Han; Ziqi Wang; Han Zhao; Heng Ji



**Title**: CausalLM is not optimal for in-context learning [[paper link]](http://arxiv.org/abs/2308.06912) 2023-09-02  
**Authors**: Nan Ding; Tomer Levinboim; Jialin Wu; Sebastian Goodman; Radu Soricut



**Title**: One Step of Gradient Descent is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention [[paper link]](http://arxiv.org/abs/2307.03576) 2023-07-07  
**Authors**: Arvind Mahankali; Tatsunori B. Hashimoto; Tengyu Ma



**Title**: Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection [[paper link]](http://arxiv.org/abs/2306.04637) 2023-07-06  
**Authors**: Yu Bai; Fan Chen; Huan Wang; Caiming Xiong; Song Mei



**Title**: Transformers Learn In-Context by Gradient Descent [[paper link]](https://openreview.net/forum?id=tHvXrFQma5) 2023-06-15  
**Authors**: Johannes Von Oswald; Eyvind Niklasson; Ettore Randazzo; Joao Sacramento; Alexander Mordvintsev; Andrey Zhmoginov; Max Vladymyrov



**Title**: The Closeness of In-Context Learning and Weight Shifting for Softmax Regression [[paper link]](http://arxiv.org/abs/2304.13276) 2023-04-26  
**Authors**: Shuai Li; Zhao Song; Yu Xia; Tong Yu; Tianyi Zhou



**Title**: A Theory of Emergent In-Context Learning as Implicit Structure Induction [[paper link]](http://arxiv.org/abs/2303.07971) 2023-03-14  
**Authors**: Michael Hahn; Navin Goyal



**Title**: The Learnability of In-Context Learning [[paper link]](http://arxiv.org/abs/2303.07895) 2023-03-14  
**Authors**: Noam Wies; Yoav Levine; Amnon Shashua



**Title**: What Can Transformers Learn In-Context? A Case Study of Simple Function Classes [[paper link]](http://arxiv.org/abs/2208.01066) 2023-01-14  
**Authors**: Shivam Garg; Dimitris Tsipras; Percy Liang; Gregory Valiant



**Title**: Transformers generalize differently from information stored in context vs in weights [[paper link]](http://arxiv.org/abs/2210.05675) 2022-10-13  
**Authors**: Stephanie C. Y. Chan; Ishita Dasgupta; Junkyung Kim; Dharshan Kumaran; Andrew K. Lampinen; Felix Hill


</details>

### Chain-of-Thought

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Let's Think Dot by Dot: Hidden Computation in Transformer Language Models [[paper link]](http://arxiv.org/abs/2404.15758) 2024-04-24  
**Authors**: Jacob Pfau; William Merrill; Samuel R. Bowman



**Title**: Chain of Thought Empowers Transformers to Solve Inherently Serial Problems [[paper link]](http://arxiv.org/abs/2402.12875) 2024-02-20  
**Authors**: Zhiyuan Li; Hong Liu; Denny Zhou; Tengyu Ma



**Title**: Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective [[paper link]](http://arxiv.org/abs/2305.15408) 2023-12-22  
**Authors**: Guhao Feng; Bohang Zhang; Yuntian Gu; Haotian Ye; Di He; Liwei Wang



**Title**: Why Can Large Language Models Generate Correct Chain-of-Thoughts? [[paper link]](http://arxiv.org/abs/2310.13571) 2023-10-20  
**Authors**: Rasul Tutunov; Antoine Grosnit; Juliusz Ziomek; Jun Wang; Haitham Bou-Ammar



**Title**: How Large Language Models Implement Chain-of-Thought? [[paper link]](https://openreview.net/forum?id=b2XfOm3RJa) 2023-10-13  
**Authors**: Yiqun Wang; Sile Hu; Yonggang Zhang; Xiang Tian; Xuesong Liu; Yaowu Chen; Xu Shen; Jieping Ye



**Title**: The Expressive Power of Transformers with Chain of Thought [[paper link]](https://openreview.net/forum?id=NjNGlPh8Wh) 2023-10-13  
**Authors**: William Merrill; Ashish Sabharwal


</details>

### Hallucination

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations? [[paper link]](http://arxiv.org/abs/2405.05904) 2024-05-09  
**Authors**: Zorik Gekhman; Gal Yona; Roee Aharoni; Matan Eyal; Amir Feder; Roi Reichart; Jonathan Herzig



**Title**: Mechanisms of non-factual hallucinations in language models [[paper link]](http://arxiv.org/abs/2403.18167) 2024-03-26  
**Authors**: Lei Yu; Meng Cao; Jackie Chi Kit Cheung; Yue Dong



**Title**: Unfamiliar Finetuning Examples Control How Language Models Hallucinate [[paper link]](http://arxiv.org/abs/2403.05612) 2024-03-08  
**Authors**: Katie Kang; Eric Wallace; Claire Tomlin; Aviral Kumar; Sergey Levine



**Title**: In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation [[paper link]](http://arxiv.org/abs/2403.01548) 2024-03-05  
**Authors**: Shiqi Chen; Miao Xiong; Junteng Liu; Zhengxuan Wu; Teng Xiao; Siyang Gao; Junxian He



**Title**: Calibrated Language Models Must Hallucinate [[paper link]](http://arxiv.org/abs/2311.14648) 2023-11-24  
**Authors**: Adam Tauman Kalai; Santosh S. Vempala



**Title**: The Curious Case of Hallucinatory Unanswerablity: Finding Truths in the Hidden States of Over-Confident Large Language Models [[paper link]](http://arxiv.org/abs/2310.11877) 2023-10-18  
**Authors**: Aviv Slobodkin; Omer Goldman; Avi Caciularu; Ido Dagan; Shauli Ravfogel


</details>

### Reversal Curse

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics [[paper link]](http://arxiv.org/abs/2405.04669) 2024-05-07  
**Authors**: Hanlin Zhu; Baihe Huang; Shaolun Zhang; Michael Jordan; Jiantao Jiao; Yuandong Tian; Stuart Russell



**Title**: The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A" [[paper link]](http://arxiv.org/abs/2309.12288) 2024-04-04  
**Authors**: Lukas Berglund; Meg Tong; Max Kaufmann; Mikita Balesni; Asa Cooper Stickland; Tomasz Korbak; Owain Evans



**Title**: An Investigation of LLMs' Inefficacy in Understanding Converse Relations [[paper link]](https://aclanthology.org/2023.emnlp-main.429) 2023-12-01  
**Authors**: Chengwen Qi; Bowen Li; Binyuan Hui; Bailin Wang; Jinyang Li; Jinwang Wu; Yuanjun Laili



**Title**: Physics of Language Models: Part 3.2, Knowledge Manipulation [[paper link]](http://arxiv.org/abs/2309.14402) 2023-09-25  
**Authors**: Zeyuan Allen-Zhu; Yuanzhi Li


</details>

### Scaling Laws / Emergent Abilities / Grokking / etc.

This section includes papers that investigate how the performance of language models scales with model size, data size, or compute, and how emergent abilities arise in language models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Beyond Scaling Laws: Understanding Transformer Performance with Associative Memory [[paper link]](http://arxiv.org/abs/2405.08707) 2024-05-14  
**Authors**: Xueyan Niu; Bo Bai; Lei Deng; Wei Han



**Title**: More Compute Is What You Need [[paper link]](http://arxiv.org/abs/2404.19484) 2024-04-30  
**Authors**: Zhen Guo



**Title**: An exactly solvable model for emergence and scaling laws [[paper link]](http://arxiv.org/abs/2404.17563) 2024-04-26  
**Authors**: Yoonsoo Nam; Nayara Fonseca; Seok Hyeong Lee; Ard Louis



**Title**: Why do small language models underperform? Studying Language Model Saturation via the Softmax Bottleneck [[paper link]](http://arxiv.org/abs/2404.07647) 2024-04-11  
**Authors**: Nathan Godey; Éric de la Clergerie; Benoît Sagot



**Title**: A Large-Scale Exploration of $\mu$-Transfer [[paper link]](http://arxiv.org/abs/2404.05728) 2024-04-08  
**Authors**: Lucas Lingle



**Title**: Emergent Abilities in Reduced-Scale Generative Language Models [[paper link]](http://arxiv.org/abs/2404.02204) 2024-04-02  
**Authors**: Sherin Muckatira; Vijeta Deshpande; Vladislav Lialin; Anna Rumshisky



**Title**: Understanding Emergent Abilities of Language Models from the Loss Perspective [[paper link]](http://arxiv.org/abs/2403.15796) 2024-03-23  
**Authors**: Zhengxiao Du; Aohan Zeng; Yuxiao Dong; Jie Tang



**Title**: Unraveling the Mystery of Scaling Laws: Part I [[paper link]](http://arxiv.org/abs/2403.06563) 2024-03-21  
**Authors**: Hui Su; Zhi Tian; Xiaoyu Shen; Xunliang Cai



**Title**: Language models scale reliably with over-training and on downstream tasks [[paper link]](http://arxiv.org/abs/2403.08540) 2024-03-13  
**Authors**: Samir Yitzhak Gadre; Georgios Smyrnis; Vaishaal Shankar; Suchin Gururangan; Mitchell Wortsman; Rulin Shao; Jean Mercat; Alex Fang; Jeffrey Li; Sedrick Keh; Rui Xin; Marianna Nezhurina; Igor Vasiljevic; Jenia Jitsev; Alexandros G. Dimakis; Gabriel Ilharco; Shuran Song; Thomas Kollar; Yair Carmon; Achal Dave; Reinhard Heckel; Niklas Muennighoff; Ludwig Schmidt



**Title**: When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method [[paper link]](http://arxiv.org/abs/2402.17193) 2024-02-26  
**Authors**: Biao Zhang; Zhongtao Liu; Colin Cherry; Orhan Firat



**Title**: Interpreting Grokked Transformers in Complex Modular Arithmetic [[paper link]](https://arxiv.org/abs/2402.16726v2) 2024-02-26  
**Authors**: Hiroki Furuta; Gouki Minegishi; Yusuke Iwasawa; Yutaka Matsuo



**Title**: A Tale of Tails: Model Collapse as a Change of Scaling Laws [[paper link]](https://arxiv.org/abs/2402.07043) 2024-02-10  
**Authors**: Elvis Dohmatob; Yunzhen Feng; Pu Yang; Francois Charton; Julia Kempe



**Title**: Scaling Data-Constrained Language Models [[paper link]](http://arxiv.org/abs/2305.16264) 2023-10-25  
**Authors**: Niklas Muennighoff; Alexander M. Rush; Boaz Barak; Teven Le Scao; Aleksandra Piktus; Nouamane Tazi; Sampo Pyysalo; Thomas Wolf; Colin Raffel



**Title**: The Cost of Down-Scaling Language Models: Fact Recall Deteriorates before In-Context Learning [[paper link]](http://arxiv.org/abs/2310.04680) 2023-10-06  
**Authors**: Tian Jin; Nolan Clement; Xin Dong; Vaishnavh Nagarajan; Michael Carbin; Jonathan Ragan-Kelley; Gintare Karolina Dziugaite



**Title**: Are Emergent Abilities of Large Language Models a Mirage? [[paper link]](https://arxiv.org/abs/2304.15004v2) 2023-04-28  
**Authors**: Rylan Schaeffer; Brando Miranda; Sanmi Koyejo



**Title**: Training Compute-Optimal Large Language Models [[paper link]](http://arxiv.org/abs/2203.15556) 2022-03-29  
**Authors**: Jordan Hoffmann; Sebastian Borgeaud; Arthur Mensch; Elena Buchatskaya; Trevor Cai; Eliza Rutherford; Diego de Las Casas; Lisa Anne Hendricks; Johannes Welbl; Aidan Clark; Tom Hennigan; Eric Noland; Katie Millican; George van den Driessche; Bogdan Damoc; Aurelia Guy; Simon Osindero; Karen Simonyan; Erich Elsen; Jack W. Rae; Oriol Vinyals; Laurent Sifre



**Title**: Scaling Laws for Neural Language Models [[paper link]](http://arxiv.org/abs/2001.08361) 2020-01-22  
**Authors**: Jared Kaplan; Sam McCandlish; Tom Henighan; Tom B. Brown; Benjamin Chess; Rewon Child; Scott Gray; Alec Radford; Jeffrey Wu; Dario Amodei


</details>

### Knowledge / Memory mechanisms

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws [[paper link]](http://arxiv.org/abs/2404.05405) 2024-04-08  
**Authors**: Zeyuan Allen-Zhu; Yuanzhi Li



**Title**: Memorization Capacity of Multi-Head Attention in Transformers [[paper link]](http://arxiv.org/abs/2306.02010) 2024-03-02  
**Authors**: Sadegh Mahdavi; Renjie Liao; Christos Thrampoulidis



**Title**: Birth of a Transformer: A Memory Viewpoint [[paper link]](http://arxiv.org/abs/2306.00802) 2023-11-06  
**Authors**: Alberto Bietti; Vivien Cabannes; Diane Bouchacourt; Herve Jegou; Leon Bottou



**Title**: Physics of Language Models: Part 3.2, Knowledge Manipulation [[paper link]](http://arxiv.org/abs/2309.14402) 2023-09-25  
**Authors**: Zeyuan Allen-Zhu; Yuanzhi Li



**Title**: Can Neural Network Memorization Be Localized? [[paper link]](http://arxiv.org/abs/2307.09542) 2023-07-18  
**Authors**: Pratyush Maini; Michael C. Mozer; Hanie Sedghi; Zachary C. Lipton; J. Zico Kolter; Chiyuan Zhang


</details>

### Training Dynamics / Landscape / Optimization / Fine-tuning / etc.

This section focuses on the training dynamics of language models, including the optimization landscape, fine-tuning, and transfer learning.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics [[paper link]](http://arxiv.org/abs/2405.04669) 2024-05-07  
**Authors**: Hanlin Zhu; Baihe Huang; Shaolun Zhang; Michael Jordan; Jiantao Jiao; Yuandong Tian; Stuart Russell



**Title**: Control Theoretic Approach to Fine-Tuning and Transfer Learning [[paper link]](http://arxiv.org/abs/2404.11013) 2024-04-16  
**Authors**: Erkan Bayram; Shenyu Liu; Mohamed-Ali Belabbas; Tamer Başar



**Title**: Look at the Text: Instruction-Tuned Language Models are More Robust Multiple Choice Selectors than You Think [[paper link]](http://arxiv.org/abs/2404.08382) 2024-04-12  
**Authors**: Xinpeng Wang; Chengzhi Hu; Bolei Ma; Paul Röttger; Barbara Plank



**Title**: On Training Data Influence of GPT Models [[paper link]](http://arxiv.org/abs/2404.07840) 2024-04-11  
**Authors**: Qingyi Liu; Yekun Chai; Shuohuan Wang; Yu Sun; Keze Wang; Hua Wu



**Title**: Best Practices and Lessons Learned on Synthetic Data for Language Models [[paper link]](http://arxiv.org/abs/2404.07503) 2024-04-11  
**Authors**: Ruibo Liu; Jerry Wei; Fangyu Liu; Chenglei Si; Yanzhe Zhang; Jinmeng Rao; Steven Zheng; Daiyi Peng; Diyi Yang; Denny Zhou; Andrew M. Dai



**Title**: How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse [[paper link]](http://arxiv.org/abs/2404.05090) 2024-04-07  
**Authors**: Mohamed El Amine Seddik; Suei-Wen Chen; Soufiane Hayou; Pierre Youssef; Merouane Debbah



**Title**: Unveiling the Generalization Power of Fine-Tuned Large Language Models [[paper link]](http://arxiv.org/abs/2403.09162) 2024-03-14  
**Authors**: Haoran Yang; Yumeng Zhang; Jiaqi Xu; Hongyuan Lu; Pheng Ann Heng; Wai Lam



**Title**: Transformers Get Stable: An End-to-End Signal Propagation Theory for Language Models [[paper link]](http://arxiv.org/abs/2403.09635) 2024-03-14  
**Authors**: Akhil Kedia; Mohd Abbas Zaidi; Sushil Khyalia; Jungho Jung; Harshith Goka; Haejun Lee



**Title**: Linear Attention is (Maybe) All You Need (to Understand Transformer Optimization) [[paper link]](http://arxiv.org/abs/2310.01082) 2024-03-13  
**Authors**: Kwangjun Ahn; Xiang Cheng; Minhak Song; Chulhee Yun; Ali Jadbabaie; Suvrit Sra



**Title**: Hallmarks of Optimization Trajectories in Neural Networks and LLMs: The Lengths, Bends, and Dead Ends [[paper link]](http://arxiv.org/abs/2403.07379) 2024-03-12  
**Authors**: Sidak Pal Singh; Bobby He; Thomas Hofmann; Bernhard Schölkopf



**Title**: The Heuristic Core: Understanding Subnetwork Generalization in Pretrained Language Models [[paper link]](http://arxiv.org/abs/2403.03942) 2024-03-06  
**Authors**: Adithya Bhaskar; Dan Friedman; Danqi Chen



**Title**: Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
**Authors**: Siyu Chen; Heejune Sheen; Tianhao Wang; Zhuoran Yang



**Title**: How Transformers Learn Causal Structure with Gradient Descent [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
**Authors**: Eshaan Nichani; Alex Damian; Jason D. Lee



**Title**: Transformers learn through gradual rank increase [[paper link]](http://arxiv.org/abs/2306.07042) 2023-12-10  
**Authors**: Enric Boix-Adsera; Etai Littwin; Emmanuel Abbe; Samy Bengio; Joshua Susskind



**Title**: Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
**Authors**: Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



**Title**: Connecting Pre-trained Language Model and Downstream Task via Properties of Representation [[paper link]](https://openreview.net/forum?id=YLOJ4aKAka) 2023-11-02  
**Authors**: Chenwei Wu; Holden Lee; Rong Ge



**Title**: Scan and Snap: Understanding Training Dynamics and Token Composition in 1-layer Transformer [[paper link]](http://arxiv.org/abs/2305.16380) 2023-07-02  
**Authors**: Yuandong Tian; Yiping Wang; Beidi Chen; Simon Du



**Title**: A Kernel-Based View of Language Model Fine-Tuning [[paper link]](https://openreview.net/forum?id=49dTFIGdx8) 2023-06-15  
**Authors**: Sadhika Malladi; Alexander Wettig; Dingli Yu; Danqi Chen; Sanjeev Arora



**Title**: A Stability Analysis of Fine-Tuning a Pre-Trained Model [[paper link]](https://arxiv.org/abs/2301.09820v2) 2023-01-24  
**Authors**: Zihao Fu; Anthony Man-Cho So; Nigel Collier


</details>

### Learning / Generalization

This section includes papers that investigate the generalization ability of language models, and the general learning behavior of language models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Initialization is Critical to Whether Transformers Fit Composite Functions by Inference or Memorizing [[paper link]](http://arxiv.org/abs/2405.05409) 2024-05-08  
**Authors**: Zhongwang Zhang; Pengxiao Lin; Zhiwei Wang; Yaoyu Zhang; Zhi-Qin John Xu



**Title**: Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
**Authors**: Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



**Title**: The Impact of Depth and Width on Transformer Language Model Generalization [[paper link]](http://arxiv.org/abs/2310.19956) 2023-10-30  
**Authors**: Jackson Petty; Sjoerd van Steenkiste; Ishita Dasgupta; Fei Sha; Dan Garrette; Tal Linzen



**Title**: How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition [[paper link]](http://arxiv.org/abs/2310.05492) 2023-10-09  
**Authors**: Guanting Dong; Hongyi Yuan; Keming Lu; Chengpeng Li; Mingfeng Xue; Dayiheng Liu; Wei Wang; Zheng Yuan; Chang Zhou; Jingren Zhou



**Title**: A Theory for Emergence of Complex Skills in Language Models [[paper link]](http://arxiv.org/abs/2307.15936) 2023-07-29  
**Authors**: Sanjeev Arora; Anirudh Goyal



**Title**: On the Power of Foundation Models [[paper link]](https://proceedings.mlr.press/v202/yuan23b.html) 2023-07-03  
**Authors**: Yang Yuan



**Title**: Task-Specific Skill Localization in Fine-tuned Language Models [[paper link]](https://openreview.net/forum?id=Rgnaj43Pk0) 2023-06-15  
**Authors**: Abhishek Panigrahi; Nikunj Saunshi; Haoyu Zhao; Sanjeev Arora



**Title**: Towards Understanding Why Mask-Reconstruction Pretraining Helps in Downstream Tasks [[paper link]](http://arxiv.org/abs/2206.03826) 2023-02-11  
**Authors**: Jiachun Pan; Pan Zhou; Shuicheng Yan



**Title**: Same Pre-training Loss, Better Downstream: Implicit Bias Matters for Language Models [[paper link]](http://arxiv.org/abs/2210.14199) 2022-10-25  
**Authors**: Hong Liu; Sang Michael Xie; Zhiyuan Li; Tengyu Ma



**Title**: Why Do Pretrained Language Models Help in Downstream Tasks? An Analysis of Head and Prompt Tuning [[paper link]](http://arxiv.org/abs/2106.09226) 2022-04-20  
**Authors**: Colin Wei; Sang Michael Xie; Tengyu Ma



**Title**: A Mathematical Exploration of Why Language Models Help Solve Downstream Tasks [[paper link]](http://arxiv.org/abs/2010.03648) 2021-04-14  
**Authors**: Nikunj Saunshi; Sadhika Malladi; Sanjeev Arora



**Title**: Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning [[paper link]](http://arxiv.org/abs/2012.13255) 2020-12-22  
**Authors**: Armen Aghajanyan; Luke Zettlemoyer; Sonal Gupta



**Title**: How fine can fine-tuning be? Learning efficient language models [[paper link]](https://proceedings.mlr.press/v108/radiya-dixit20a.html) 2020-06-03  
**Authors**: Evani Radiya-Dixit; Xin Wang


</details>

### Other Phenomena

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: The Platonic Representation Hypothesis [[paper link]](https://arxiv.org/abs/2405.07987v1) 2024-05-13  
**Authors**: Minyoung Huh; Brian Cheung; Tongzhou Wang; Phillip Isola



**Title**: Algorithmic progress in language models [[paper link]](http://arxiv.org/abs/2403.05812) 2024-03-09  
**Authors**: Anson Ho; Tamay Besiroglu; Ege Erdil; David Owen; Robi Rahman; Zifan Carl Guo; David Atkinson; Neil Thompson; Jaime Sevilla



**Title**: Massive Activations in Large Language Models [[paper link]](http://arxiv.org/abs/2402.17762) 2024-02-27  
**Authors**: Mingjie Sun; Xinlei Chen; J. Zico Kolter; Zhuang Liu



**Title**: The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers [[paper link]](https://openreview.net/forum?id=TJ2nxciYCk-) 2023-02-01  
**Authors**: Zonglin Li; Chong You; Srinadh Bhojanapalli; Daliang Li; Ankit Singh Rawat; Sashank J. Reddi; Ke Ye; Felix Chern; Felix Yu; Ruiqi Guo; Sanjiv Kumar


</details>

## Representational Capacity

Investigate the expressiveness of transformer-based models about what they can do and what they can't do.

### What Can Transformer Do? / Properties of Transformer

This section includes positive results on the representational capacity and properties of transformer-based models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: ALPINE: Unveiling the Planning Capability of Autoregressive Learning in Language Models [[paper link]](http://arxiv.org/abs/2405.09220) 2024-05-15  
**Authors**:  Siwei Wang; Yifei Shen; Shi Feng; Haoran Sun; Shang-Hua Teng; Wei Chen



**Title**: What Formal Languages Can Transformers Express? A Survey [[paper link]](http://arxiv.org/abs/2311.00208) 2024-05-06  
**Authors**: Lena Strobl; William Merrill; Gail Weiss; David Chiang; Dana Angluin



**Title**: Transformers Can Represent $n$-gram Language Models [[paper link]](http://arxiv.org/abs/2404.14994) 2024-04-23  
**Authors**: Anej Svete; Ryan Cotterell



**Title**: Mechanics of Next Token Prediction with Self-Attention [[paper link]](https://proceedings.mlr.press/v238/li24f.html) 2024-04-18  
**Authors**: Yingcong Li; Yixiao Huang; Muhammed E. Ildiz; Ankit Singh Rawat; Samet Oymak



**Title**: When can transformers reason with abstract symbols? [[paper link]](http://arxiv.org/abs/2310.09753) 2024-04-16  
**Authors**: Enric Boix-Adsera; Omid Saremi; Emmanuel Abbe; Samy Bengio; Etai Littwin; Joshua Susskind



**Title**: The Illusion of State in State-Space Models [[paper link]](http://arxiv.org/abs/2404.08819) 2024-04-12  
**Authors**: William Merrill; Jackson Petty; Ashish Sabharwal



**Title**: Attention is Naturally Sparse with Gaussian Distributed Input [[paper link]](http://arxiv.org/abs/2404.02690) 2024-04-03  
**Authors**: Yichuan Deng; Zhao Song; Chiwun Yang



**Title**: What Can Transformer Learn with Varying Depth? Case Studies on Sequence Learning Tasks [[paper link]](http://arxiv.org/abs/2404.01601) 2024-04-01  
**Authors**: Xingwu Chen; Difan Zou



**Title**: The Topos of Transformer Networks [[paper link]](http://arxiv.org/abs/2403.18415) 2024-03-27  
**Authors**: Mattia Jacopo Villani; Peter McBurney



**Title**: Simulating Weighted Automata over Sequences and Trees with Transformers [[paper link]](http://arxiv.org/abs/2403.09728) 2024-03-12  
**Authors**: Michael Rizvi; Maude Lizaire; Clara Lacroce; Guillaume Rabusseau



**Title**: Simplicity Bias of Transformers to Learn Low Sensitivity Functions [[paper link]](http://arxiv.org/abs/2403.06925) 2024-03-11  
**Authors**: Bhavya Vasudeva; Deqing Fu; Tianyi Zhou; Elliott Kau; Youqi Huang; Vatsal Sharan



**Title**: On the Origins of Linear Representations in Large Language Models [[paper link]](http://arxiv.org/abs/2403.03867) 2024-03-06  
**Authors**: Yibo Jiang; Goutham Rajendran; Pradeep Ravikumar; Bryon Aragam; Victor Veitch



**Title**: How Well Can Transformers Emulate In-context Newton's Method? [[paper link]](http://arxiv.org/abs/2403.03183) 2024-03-05  
**Authors**: Angeliki Giannou; Liu Yang; Tianhao Wang; Dimitris Papailiopoulos; Jason D. Lee



**Title**: RNNs are not Transformers (Yet): The Key Bottleneck on In-context Retrieval [[paper link]](http://arxiv.org/abs/2402.18510) 2024-02-29  
**Authors**: Kaiyue Wen; Xingyu Dang; Kaifeng Lyu



**Title**: Implicit Bias of Next-Token Prediction [[paper link]](http://arxiv.org/abs/2402.18551) 2024-02-28  
**Authors**: Christos Thrampoulidis



**Title**: On the Expressive Power of a Variant of the Looped Transformer [[paper link]](http://arxiv.org/abs/2402.13572) 2024-02-21  
**Authors**: Yihang Gao; Chuanyang Zheng; Enze Xie; Han Shi; Tianyang Hu; Yu Li; Michael K. Ng; Zhenguo Li; Zhaoqiang Liu



**Title**: From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers [[paper link]](http://arxiv.org/abs/2402.13512) 2024-02-20  
**Authors**: M. Emrullah Ildiz; Yixiao Huang; Yingcong Li; Ankit Singh Rawat; Samet Oymak



**Title**: Transformers Implement Functional Gradient Descent to Learn Non-Linear Functions In Context [[paper link]](http://arxiv.org/abs/2312.06528) 2024-02-15  
**Authors**: Xiang Cheng; Yuxin Chen; Suvrit Sra



**Title**: Compositional Capabilities of Autoregressive Transformers: A Study on Synthetic, Interpretable Tasks [[paper link]](http://arxiv.org/abs/2311.12997) 2024-02-05  
**Authors**: Rahul Ramesh; Ekdeep Singh Lubana; Mikail Khona; Robert P. Dick; Hidenori Tanaka



**Title**: Are Transformers with One Layer Self-Attention Using Low-Rank Weight Matrices Universal Approximators? [[paper link]](http://arxiv.org/abs/2307.14023) 2024-01-29  
**Authors**: Tokio Kajitsuka; Issei Sato



**Title**: Transformers are Multi-State RNNs [[paper link]](http://arxiv.org/abs/2401.06104) 2024-01-11  
**Authors**: Matanel Oren; Michael Hassid; Yossi Adi; Roy Schwartz



**Title**: How Capable Can a Transformer Become? A Study on Synthetic, Interpretable Tasks [[paper link]](https://openreview.net/forum?id=KIhFggzePM) 2023-12-12  
**Authors**: Rahul Ramesh; Mikail Khona; Robert P. Dick; Hidenori Tanaka; Ekdeep Singh Lubana



**Title**: Transformers can optimally learn regression mixture models [[paper link]](http://arxiv.org/abs/2311.08362) 2023-11-14  
**Authors**: Reese Pathak; Rajat Sen; Weihao Kong; Abhimanyu Das



**Title**: The Expressive Power of Low-Rank Adaptation [[paper link]](http://arxiv.org/abs/2310.17513) 2023-10-26  
**Authors**: Yuchen Zeng; Kangwook Lee



**Title**: What Algorithms can Transformers Learn? A Study in Length Generalization [[paper link]](http://arxiv.org/abs/2310.16028) 2023-10-24  
**Authors**: Hattie Zhou; Arwen Bradley; Etai Littwin; Noam Razin; Omid Saremi; Josh Susskind; Samy Bengio; Preetum Nakkiran



**Title**: Transformers as Support Vector Machines [[paper link]](http://arxiv.org/abs/2308.16898) 2023-09-07  
**Authors**: Davoud Ataee Tarzanagh; Yingcong Li; Christos Thrampoulidis; Samet Oymak



**Title**: How Do Transformers Learn Topic Structure: Towards a Mechanistic Understanding [[paper link]](https://openreview.net/forum?id=LMXgU4zrq6) 2023-06-15  
**Authors**: Yuchen Li; Yuanzhi Li; Andrej Risteski



**Title**: Tighter Bounds on the Expressivity of Transformer Encoders [[paper link]](https://openreview.net/forum?id=XKcogevHj8) 2023-06-15  
**Authors**: David Chiang; Peter Cholak; Anand Pillay



**Title**: Fast Attention Requires Bounded Entries [[paper link]](https://arxiv.org/abs/2302.13214v2) 2023-02-26  
**Authors**: Josh Alman; Zhao Song



**Title**: Transformers Learn Shortcuts to Automata [[paper link]](https://openreview.net/forum?id=De4FYqjFueZ) 2023-02-01  
**Authors**: Bingbin Liu; Jordan T. Ash; Surbhi Goel; Akshay Krishnamurthy; Cyril Zhang



**Title**: Transformer Vs. MLP-Mixer: Exponential Expressive Gap For NLP Problems [[paper link]](http://arxiv.org/abs/2208.08191) 2022-11-17  
**Authors**: Dan Navon; Alex M. Bronstein



**Title**: Small Transformers Compute Universal Metric Embeddings [[paper link]](http://arxiv.org/abs/2209.06788) 2022-10-18  
**Authors**: Anastasis Kratsios; Valentin Debarnot; Ivan Dokmanić



**Title**: The Lipschitz Constant of Self-Attention [[paper link]](http://arxiv.org/abs/2006.04710) 2021-06-09  
**Authors**: Hyunjik Kim; George Papamakarios; Andriy Mnih



**Title**: On Identifiability in Transformers [[paper link]](http://arxiv.org/abs/1908.04211) 2020-02-07  
**Authors**: Gino Brunner; Yang Liu; Damián Pascual; Oliver Richter; Massimiliano Ciaramita; Roger Wattenhofer


</details>

### What Can Transformer Not Do? / Limitation of Transformer

The papers in this section investigate the limitations of transformer-based models, including the limitations of their expressiveness and learning abilities.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Collapse of Self-trained Language Models [[paper link]](http://arxiv.org/abs/2404.02305) 2024-04-02  
**Authors**: David Herel; Tomas Mikolov



**Title**: The pitfalls of next-token prediction [[paper link]](http://arxiv.org/abs/2403.06963) 2024-03-11  
**Authors**: Gregor Bachmann; Vaishnavh Nagarajan



**Title**: Why are Sensitive Functions Hard for Transformers? [[paper link]](http://arxiv.org/abs/2402.09963) 2024-03-03  
**Authors**: Michael Hahn; Mark Rofin



**Title**: Transformers are Expressive, But Are They Expressive Enough for Regression? [[paper link]](http://arxiv.org/abs/2402.15478) 2024-02-23  
**Authors**: Swaroop Nath; Harshad Khadilkar; Pushpak Bhattacharyya



**Title**: Limits of Transformer Language Models on Learning Algorithmic Compositions [[paper link]](http://arxiv.org/abs/2402.05785) 2024-02-13  
**Authors**: Jonathan Thomm; Aleksandar Terzic; Geethan Karunaratne; Giacomo Camposampiero; Bernhard Schölkopf; Abbas Rahimi



**Title**: Representational Strengths and Limitations of Transformers [[paper link]](http://arxiv.org/abs/2306.02896) 2023-11-16  
**Authors**: Clayton Sanford; Daniel Hsu; Matus Telgarsky



**Title**: Large Language Models Cannot Self-Correct Reasoning Yet [[paper link]](https://openreview.net/forum?id=IkmD3fKBPQ) 2023-10-13  
**Authors**: Jie Huang; Xinyun Chen; Swaroop Mishra; Huaixiu Steven Zheng; Adams Wei Yu; Xinying Song; Denny Zhou



**Title**: Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth [[paper link]](http://arxiv.org/abs/2103.03404) 2023-08-01  
**Authors**: Yihe Dong; Jean-Baptiste Cordonnier; Andreas Loukas



**Title**: Limits for Learning with Language Models [[paper link]](http://arxiv.org/abs/2306.12213) 2023-06-21  
**Authors**: Nicholas Asher; Swarnadeep Bhar; Akshay Chaturvedi; Julie Hunter; Soumya Paul



**Title**: Your Transformer May Not be as Powerful as You Expect [[paper link]](https://openreview.net/forum?id=NQFFNdsOGD) 2022-10-31  
**Authors**: Shengjie Luo; Shanda Li; Shuxin Zheng; Tie-Yan Liu; Liwei Wang; Di He



**Title**: The Devil in Linear Transformer [[paper link]](http://arxiv.org/abs/2210.10340) 2022-10-19  
**Authors**: Zhen Qin; XiaoDong Han; Weixuan Sun; Dongxu Li; Lingpeng Kong; Nick Barnes; Yiran Zhong


</details>

## Architectural Effectivity

discussion of the effectiveness of different architectures in terms of learning and generalization

### Layer-normalization

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: The Expressive Power of Tuning Only the Normalization Layers [[paper link]](https://proceedings.mlr.press/v195/giannou23a.html) 2023-07-12  
**Authors**: Angeliki Giannou; Shashank Rajput; Dimitris Papailiopoulos



**Title**: ResiDual: Transformer with Dual Residual Connections [[paper link]](http://arxiv.org/abs/2304.14802) 2023-04-28  
**Authors**: Shufang Xie; Huishuai Zhang; Junliang Guo; Xu Tan; Jiang Bian; Hany Hassan Awadalla; Arul Menezes; Tao Qin; Rui Yan



**Title**: DeepNet: Scaling Transformers to 1,000 Layers [[paper link]](http://arxiv.org/abs/2203.00555) 2022-03-01  
**Authors**: Hongyu Wang; Shuming Ma; Li Dong; Shaohan Huang; Dongdong Zhang; Furu Wei



**Title**: On Layer Normalization in the Transformer Architecture [[paper link]](http://arxiv.org/abs/2002.04745) 2020-06-29  
**Authors**: Ruibin Xiong; Yunchang Yang; Di He; Kai Zheng; Shuxin Zheng; Chen Xing; Huishuai Zhang; Yanyan Lan; Liwei Wang; Tie-Yan Liu


</details>

### Tokenization

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Toward a Theory of Tokenization in LLMs [[paper link]](http://arxiv.org/abs/2404.08335) 2024-04-12  
**Authors**: Nived Rajaraman; Jiantao Jiao; Kannan Ramchandran



**Title**: On the Effect of (Near) Duplicate Subwords in Language Modelling [[paper link]](http://arxiv.org/abs/2404.06508) 2024-04-09  
**Authors**: Anton Schäfer; Thomas Hofmann; Imanol Schlag; Tiago Pimentel



**Title**: Tokenization Is More Than Compression [[paper link]](http://arxiv.org/abs/2402.18376) 2024-02-28  
**Authors**: Craig W. Schmidt; Varshini Reddy; Haoran Zhang; Alec Alameddine; Omri Uzan; Yuval Pinter; Chris Tanner


</details>

## Training Paradigms

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Knowledge Distillation vs. Pretraining from Scratch under a Fixed (Computation) Budget [[paper link]](http://arxiv.org/abs/2404.19319) 2024-04-30  
**Authors**: Minh Duc Bui; Fabian David Schmidt; Goran Glavaš; Katharina von der Wense



**Title**: Why are Adaptive Methods Good for Attention Models? [[paper link]](http://arxiv.org/abs/1912.03194) 2020-10-23  
**Authors**: Jingzhao Zhang; Sai Praneeth Karimireddy; Andreas Veit; Seungyeon Kim; Sashank J. Reddi; Sanjiv Kumar; Suvrit Sra


</details>

## Mechanistic Engineering / Probing / Interpretability

This section includes papers that mainly investigate the mechanisms of language models through probing, mechanistic engineering, and other papers generally related to interpretability.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Anchored Answers: Unravelling Positional Bias in GPT-2's Multiple-Choice Questions [[paper link]](https://arxiv.org/abs/2405.03205) 2024-05-06  
**Authors**: Ruizhe Li; Yanjun Gao



**Title**: A Primer on the Inner Workings of Transformer-based Language Models [[paper link]](https://arxiv.org/abs/2405.00208) 2024-05-02  
**Authors**: Javier Ferrando; Gabriele Sarti; Arianna Bisazza; Marta R. Costa-jussà



**Title**: Talking Nonsense: Probing Large Language Models' Understanding of Adversarial Gibberish Inputs [[paper link]](http://arxiv.org/abs/2404.17120) 2024-04-25  
**Authors**: Valeriia Cherepanova; James Zou



**Title**: Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions [[paper link]](http://arxiv.org/abs/2402.15055) 2024-02-22  
**Authors**: Clement Neo; Shay B. Cohen; Fazl Barez



**Title**: Universal Neurons in GPT2 Language Models [[paper link]](http://arxiv.org/abs/2401.12181) 2024-01-22  
**Authors**: Wes Gurnee; Theo Horsley; Zifan Carl Guo; Tara Rezaei Kheirkhah; Qinyi Sun; Will Hathaway; Neel Nanda; Dimitris Bertsimas



**Title**: Interpretability Illusions in the Generalization of Simplified Models [[paper link]](http://arxiv.org/abs/2312.03656) 2023-12-06  
**Authors**: Dan Friedman; Andrew Lampinen; Lucas Dixon; Danqi Chen; Asma Ghandeharioun



**Title**: Transformers are uninterpretable with myopic methods: a case study with bounded Dyck grammars [[paper link]](http://arxiv.org/abs/2312.01429) 2023-12-03  
**Authors**: Kaiyue Wen; Yuchen Li; Bingbin Liu; Andrej Risteski



**Title**: White-Box Transformers via Sparse Rate Reduction: Compression Is All There Is? [[paper link]](https://arxiv.org/abs/2311.13110v2) 2023-11-22  
**Authors**: Yaodong Yu; Sam Buchanan; Druv Pai; Tianzhe Chu; Ziyang Wu; Shengbang Tong; Hao Bai; Yuexiang Zhai; Benjamin D. Haeffele; Yi Ma



**Title**: Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
**Authors**: Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



**Title**: Understanding the Mechanics and Dynamics of Memorisation in Large Language Models: A Case Study with Random Strings [[paper link]](https://openreview.net/forum?id=ILStlRb1Sp) 2023-10-13  
**Authors**: Till Speicher; Aflah Mohammad Khan; Qinyuan Wu; Vedant Nanda; Soumi Das; Bishwamittra Ghosh; Krishna P. Gummadi; Evimaria Terzi


</details>

## Miscellanea

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Dynamic Activation Pitfalls in LLaMA Models: An Empirical Study [[paper link]](http://arxiv.org/abs/2405.09274) 2024-05-15  
**Authors**: Chi Ma; Mincong Huang; Chao Wang; Yujie Wang; Lei Yu



**Title**: Challenges in Deploying Long-Context Transformers: A Theoretical Peak Performance Analysis [[paper link]](http://arxiv.org/abs/2405.08944) 2024-05-14  
**Authors**: Yao Fu



**Title**: Understand LLMs Requires More Than Statistical Generalization [[paper link]](http://arxiv.org/abs/2405.01964) 2024-05-03  
**Authors**: Patrik Reizinger; Szilvia Ujváry; Anna Mészáros; Anna Kerekes; Wieland Brendel; Ferenc Huszár



**Title**: Compression Represents Intelligence Linearly [[paper link]](http://arxiv.org/abs/2404.09937) 2024-04-15  
**Authors**: Yuzhen Huang; Jinghan Zhang; Zifei Shan; Junxian He



**Title**: Language Generation in the Limit [[paper link]](http://arxiv.org/abs/2404.06757) 2024-04-10  
**Authors**: Jon Kleinberg; Sendhil Mullainathan



**Title**: Do language models plan ahead for future tokens? [[paper link]](http://arxiv.org/abs/2404.00859) 2024-03-31  
**Authors**: Wilson Wu; John X. Morris; Lionel Levine



**Title**: What's In My Big Data? [[paper link]](http://arxiv.org/abs/2310.20707) 2024-03-05  
**Authors**: Yanai Elazar; Akshita Bhagia; Ian Magnusson; Abhilasha Ravichander; Dustin Schwenk; Alane Suhr; Pete Walsh; Dirk Groeneveld; Luca Soldaini; Sameer Singh; Hanna Hajishirzi; Noah A. Smith; Jesse Dodge



**Title**: Universality and Limitations of Prompt Tuning [[paper link]](http://arxiv.org/abs/2305.18787) 2023-11-16  
**Authors**: Yihan Wang; Jatin Chauhan; Wei Wang; Cho-Jui Hsieh



**Title**: Data Similarity is Not Enough to Explain Language Model Performance [[paper link]](http://arxiv.org/abs/2311.09006) 2023-11-15  
**Authors**: Gregory Yauney; Emily Reif; David Mimno



**Title**: Simplifying Transformer Blocks [[paper link]](http://arxiv.org/abs/2311.01906) 2023-11-03  
**Authors**: Bobby He; Thomas Hofmann



**Title**: Causal Interpretation of Self-Attention in Pre-Trained Transformers [[paper link]](http://arxiv.org/abs/2310.20307) 2023-10-31  
**Authors**: Raanan Y. Rohekar; Yaniv Gurwicz; Shami Nisimov



**Title**: How do Language Models Bind Entities in Context? [[paper link]](http://arxiv.org/abs/2310.17191) 2023-10-26  
**Authors**: Jiahai Feng; Jacob Steinhardt



**Title**: Understanding prompt engineering may not require rethinking generalization [[paper link]](https://openreview.net/forum?id=a745RnSFLT) 2023-10-13  
**Authors**: Victor Akinwande; Yiding Jiang; Dylan Sam; J. Zico Kolter



**Title**: Understanding Catastrophic Forgetting in Language Models via Implicit Inference [[paper link]](http://arxiv.org/abs/2309.10105) 2023-09-18  
**Authors**: Suhas Kotha; Jacob Mitchell Springer; Aditi Raghunathan



**Title**: Attention-Only Transformers and Implementing MLPs with Attention Heads [[paper link]](http://arxiv.org/abs/2309.08593) 2023-09-15  
**Authors**: Robert Huben; Valerie Morris



**Title**: On the Role of Attention in Prompt-tuning [[paper link]](https://openreview.net/forum?id=qorOnDor89) 2023-06-15  
**Authors**: Samet Oymak; Ankit Singh Rawat; Mahdi Soltanolkotabi; Christos Thrampoulidis


</details>

---

Contact:

- [Shiguang Wu](https://github.com/Furyton), furyton AT outlook.com / shiguang.wu AT mail.sdu.edu.cn