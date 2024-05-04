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

Table of Content
====================
- [Awesome Transformers LM Analytics ](#awesome-transformers-lm-analytics-)
- [Table of Content](#table-of-content)
  - [Phenomena of Interest](#phenomena-of-interest)
    - [In-Context Learning](#in-context-learning)
    - [Chain-of-Thought](#chain-of-thought)
    - [Hallucination](#hallucination)
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

**Title**: What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation [[paper link]](http://arxiv.org/abs/2404.07129) 2024-04-10  
**Authors**: Singh, Aaditya K.; Moskovitz, Ted; Hill, Felix; Chan, Stephanie C. Y.; Saxe, Andrew M.



**Title**: Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability [[paper link]](http://arxiv.org/abs/2310.08049) 2024-04-01  
**Authors**: Lee, Ivan; Jiang, Nan; Berg-Kirkpatrick, Taylor



**Title**: Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
**Authors**: Chen, Siyu; Sheen, Heejune; Wang, Tianhao; Yang, Zhuoran



**Title**: How Transformers Learn Causal Structure with Gradient Descent [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
**Authors**: Nichani, Eshaan; Damian, Alex; Lee, Jason D.



**Title**: In-Context Learning of a Linear Transformer Block: Benefits of the MLP Component and One-Step GD Initialization [[paper link]](http://arxiv.org/abs/2402.14951) 2024-02-22  
**Authors**: Zhang, Ruiqi; Wu, Jingfeng; Bartlett, Peter L.



**Title**: Identifying Semantic Induction Heads to Understand In-Context Learning [[paper link]](http://arxiv.org/abs/2402.13055) 2024-02-20  
**Authors**: Ren, Jie; Guo, Qipeng; Yan, Hang; Liu, Dongrui; Qiu, Xipeng; Lin, Dahua



**Title**: The Transient Nature of Emergent In-Context Learning in Transformers [[paper link]](http://arxiv.org/abs/2311.08360) 2023-12-11  
**Authors**: Singh, Aaditya K.; Chan, Stephanie C. Y.; Moskovitz, Ted; Grant, Erin; Saxe, Andrew M.; Hill, Felix



**Title**: In-Context Learning Functions with Varying Number of Minima [[paper link]](http://arxiv.org/abs/2311.12538) 2023-11-21  
**Authors**: Oniani, David; Wang, Yanshan



**Title**: Exploring the Relationship between In-Context Learning and Instruction Tuning [[paper link]](http://arxiv.org/abs/2311.10367) 2023-11-17  
**Authors**: Duan, Hanyu; Tang, Yixuan; Yang, Yi; Abbasi, Ahmed; Tam, Kar Yan



**Title**: When does In-context Learning Fall Short and Why? A Study on Specification-Heavy Tasks [[paper link]](http://arxiv.org/abs/2311.08993) 2023-11-15  
**Authors**: Peng, Hao; Wang, Xiaozhi; Chen, Jianhui; Li, Weikai; Qi, Yunjia; Wang, Zimu; Wu, Zhili; Zeng, Kaisheng; Xu, Bin; Hou, Lei; Li, Juanzi



**Title**: In-context Learning Generalizes, But Not Always Robustly: The Case of Syntax [[paper link]](http://arxiv.org/abs/2311.07811) 2023-11-13  
**Authors**: Mueller, Aaron; Webson, Albert; Petty, Jackson; Linzen, Tal



**Title**: Transformers learn to implement preconditioned gradient descent for in-context learning [[paper link]](http://arxiv.org/abs/2306.00297) 2023-11-09  
**Authors**: Ahn, Kwangjun; Cheng, Xiang; Daneshmand, Hadi; Sra, Suvrit



**Title**: In-Context Learning Creates Task Vectors [[paper link]](http://arxiv.org/abs/2310.15916) 2023-10-24  
**Authors**: Hendel, Roee; Geva, Mor; Globerson, Amir



**Title**: Function Vectors in Large Language Models [[paper link]](http://arxiv.org/abs/2310.15213) 2023-10-23  
**Authors**: Todd, Eric; Li, Millicent L.; Sharma, Arnab Sen; Mueller, Aaron; Wallace, Byron C.; Bau, David



**Title**: In-context Learning with Transformer Is Really Equivalent to a Contrastive Learning Pattern [[paper link]](http://arxiv.org/abs/2310.13220) 2023-10-19  
**Authors**: Ren, Ruifeng; Liu, Yong



**Title**: How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations [[paper link]](http://arxiv.org/abs/2310.10616) 2023-10-16  
**Authors**: Guo, Tianyu; Hu, Wei; Mei, Song; Wang, Huan; Xiong, Caiming; Savarese, Silvio; Bai, Yu



**Title**: Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions [[paper link]](https://openreview.net/forum?id=ekeyCgeRfC) 2023-10-13  
**Authors**: Bhattamishra, Satwik; Patel, Arkil; Blunsom, Phil; Kanade, Varun



**Title**: How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression? [[paper link]](https://openreview.net/forum?id=vSh5ePa0ph) 2023-10-13  
**Authors**: Wu, Jingfeng; Zou, Difan; Chen, Zixiang; Braverman, Vladimir; Gu, Quanquan; Bartlett, Peter



**Title**: In-Context Learning Learns Label Relationships but Is Not Conventional Learning [[paper link]](https://openreview.net/forum?id=YPIA7bgd5y) 2023-10-13  
**Authors**: Kossen, Jannik; Gal, Yarin; Rainforth, Tom



**Title**: In-context Convergence of Transformers [[paper link]](https://openreview.net/forum?id=kxpswbhr1r) 2023-10-13  
**Authors**: Huang, Yu; Cheng, Yuan; Liang, Yingbin



**Title**: In-Context Learning through the Bayesian Prism [[paper link]](https://openreview.net/forum?id=HX5ujdsSon) 2023-10-13  
**Authors**: Panwar, Madhur; Ahuja, Kabir; Goyal, Navin



**Title**: Do pretrained Transformers Really Learn In-context by Gradient Descent? [[paper link]](http://arxiv.org/abs/2310.08540) 2023-10-12  
**Authors**: Shen, Lingfeng; Mishra, Aayush; Khashabi, Daniel



**Title**: What and How does In-Context Learning Learn? Bayesian Model Averaging, Parameterization, and Generalization [[paper link]](http://arxiv.org/abs/2305.19420) 2023-10-10  
**Authors**: Zhang, Yufeng; Zhang, Fengzhuo; Yang, Zhuoran; Wang, Zhaoran



**Title**: Explaining Emergent In-Context Learning as Kernel Regression [[paper link]](http://arxiv.org/abs/2305.12766) 2023-10-05  
**Authors**: Han, Chi; Wang, Ziqi; Zhao, Han; Ji, Heng



**Title**: CausalLM is not optimal for in-context learning [[paper link]](http://arxiv.org/abs/2308.06912) 2023-09-02  
**Authors**: Ding, Nan; Levinboim, Tomer; Wu, Jialin; Goodman, Sebastian; Soricut, Radu



**Title**: One Step of Gradient Descent is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention [[paper link]](http://arxiv.org/abs/2307.03576) 2023-07-07  
**Authors**: Mahankali, Arvind; Hashimoto, Tatsunori B.; Ma, Tengyu



**Title**: Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection [[paper link]](http://arxiv.org/abs/2306.04637) 2023-07-06  
**Authors**: Bai, Yu; Chen, Fan; Wang, Huan; Xiong, Caiming; Mei, Song



**Title**: Transformers Learn In-Context by Gradient Descent [[paper link]](https://openreview.net/forum?id=tHvXrFQma5) 2023-06-15  
**Authors**: Oswald, Johannes Von; Niklasson, Eyvind; Randazzo, Ettore; Sacramento, Joao; Mordvintsev, Alexander; Zhmoginov, Andrey; Vladymyrov, Max



**Title**: The Closeness of In-Context Learning and Weight Shifting for Softmax Regression [[paper link]](http://arxiv.org/abs/2304.13276) 2023-04-26  
**Authors**: Li, Shuai; Song, Zhao; Xia, Yu; Yu, Tong; Zhou, Tianyi



**Title**: A Theory of Emergent In-Context Learning as Implicit Structure Induction [[paper link]](http://arxiv.org/abs/2303.07971) 2023-03-14  
**Authors**: Hahn, Michael; Goyal, Navin



**Title**: The Learnability of In-Context Learning [[paper link]](http://arxiv.org/abs/2303.07895) 2023-03-14  
**Authors**: Wies, Noam; Levine, Yoav; Shashua, Amnon



**Title**: What Can Transformers Learn In-Context? A Case Study of Simple Function Classes [[paper link]](http://arxiv.org/abs/2208.01066) 2023-01-14  
**Authors**: Garg, Shivam; Tsipras, Dimitris; Liang, Percy; Valiant, Gregory



**Title**: Transformers generalize differently from information stored in context vs in weights [[paper link]](http://arxiv.org/abs/2210.05675) 2022-10-13  
**Authors**: Chan, Stephanie C. Y.; Dasgupta, Ishita; Kim, Junkyung; Kumaran, Dharshan; Lampinen, Andrew K.; Hill, Felix


</details>

### Chain-of-Thought

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Let's Think Dot by Dot: Hidden Computation in Transformer Language Models [[paper link]](http://arxiv.org/abs/2404.15758) 2024-04-24  
**Authors**: Pfau, Jacob; Merrill, William; Bowman, Samuel R.



**Title**: Chain of Thought Empowers Transformers to Solve Inherently Serial Problems [[paper link]](http://arxiv.org/abs/2402.12875) 2024-02-20  
**Authors**: Li, Zhiyuan; Liu, Hong; Zhou, Denny; Ma, Tengyu



**Title**: Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective [[paper link]](http://arxiv.org/abs/2305.15408) 2023-12-22  
**Authors**: Feng, Guhao; Zhang, Bohang; Gu, Yuntian; Ye, Haotian; He, Di; Wang, Liwei



**Title**: Transformers Learn Higher-Order Optimization Methods for In-Context Learning: A Study with Linear Models [[paper link]](https://arxiv.org/abs/2310.17086v1) 2023-10-26  
**Authors**: Fu, Deqing; Chen, Tian-Qi; Jia, Robin; Sharan, Vatsal



**Title**: Why Can Large Language Models Generate Correct Chain-of-Thoughts? [[paper link]](http://arxiv.org/abs/2310.13571) 2023-10-20  
**Authors**: Tutunov, Rasul; Grosnit, Antoine; Ziomek, Juliusz; Wang, Jun; Bou-Ammar, Haitham



**Title**: How Large Language Models Implement Chain-of-Thought? [[paper link]](https://openreview.net/forum?id=b2XfOm3RJa) 2023-10-13  
**Authors**: Wang, Yiqun; Hu, Sile; Zhang, Yonggang; Tian, Xiang; Liu, Xuesong; Chen, Yaowu; Shen, Xu; Ye, Jieping



**Title**: The Expressive Power of Transformers with Chain of Thought [[paper link]](https://openreview.net/forum?id=NjNGlPh8Wh) 2023-10-13  
**Authors**: Merrill, William; Sabharwal, Ashish


</details>

### Hallucination

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Mechanisms of non-factual hallucinations in language models [[paper link]](http://arxiv.org/abs/2403.18167) 2024-03-26  
**Authors**: Yu, Lei; Cao, Meng; Cheung, Jackie Chi Kit; Dong, Yue



**Title**: Unfamiliar Finetuning Examples Control How Language Models Hallucinate [[paper link]](http://arxiv.org/abs/2403.05612) 2024-03-08  
**Authors**: Kang, Katie; Wallace, Eric; Tomlin, Claire; Kumar, Aviral; Levine, Sergey



**Title**: In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation [[paper link]](http://arxiv.org/abs/2403.01548) 2024-03-05  
**Authors**: Chen, Shiqi; Xiong, Miao; Liu, Junteng; Wu, Zhengxuan; Xiao, Teng; Gao, Siyang; He, Junxian



**Title**: Calibrated Language Models Must Hallucinate [[paper link]](http://arxiv.org/abs/2311.14648) 2023-11-24  
**Authors**: Kalai, Adam Tauman; Vempala, Santosh S.



**Title**: The Curious Case of Hallucinatory Unanswerablity: Finding Truths in the Hidden States of Over-Confident Large Language Models [[paper link]](http://arxiv.org/abs/2310.11877) 2023-10-18  
**Authors**: Slobodkin, Aviv; Goldman, Omer; Caciularu, Avi; Dagan, Ido; Ravfogel, Shauli


</details>

### Scaling Laws / Emergent Abilities / Grokking / etc.

This section includes papers that investigate how the performance of language models scales with model size, data size, or compute, and how emergent abilities arise in language models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: More Compute Is What You Need [[paper link]](http://arxiv.org/abs/2404.19484) 2024-04-30  
**Authors**: Guo, Zhen



**Title**: An exactly solvable model for emergence and scaling laws [[paper link]](http://arxiv.org/abs/2404.17563) 2024-04-26  
**Authors**: Nam, Yoonsoo; Fonseca, Nayara; Lee, Seok Hyeong; Louis, Ard



**Title**: Why do small language models underperform? Studying Language Model Saturation via the Softmax Bottleneck [[paper link]](http://arxiv.org/abs/2404.07647) 2024-04-11  
**Authors**: Godey, Nathan; de la Clergerie, Éric; Sagot, Benoît



**Title**: A Large-Scale Exploration of $\mu$-Transfer [[paper link]](http://arxiv.org/abs/2404.05728) 2024-04-08  
**Authors**: Lingle, Lucas



**Title**: Emergent Abilities in Reduced-Scale Generative Language Models [[paper link]](http://arxiv.org/abs/2404.02204) 2024-04-02  
**Authors**: Muckatira, Sherin; Deshpande, Vijeta; Lialin, Vladislav; Rumshisky, Anna



**Title**: Understanding Emergent Abilities of Language Models from the Loss Perspective [[paper link]](http://arxiv.org/abs/2403.15796) 2024-03-23  
**Authors**: Du, Zhengxiao; Zeng, Aohan; Dong, Yuxiao; Tang, Jie



**Title**: Unraveling the Mystery of Scaling Laws: Part I [[paper link]](http://arxiv.org/abs/2403.06563) 2024-03-21  
**Authors**: Su, Hui; Tian, Zhi; Shen, Xiaoyu; Cai, Xunliang



**Title**: Language models scale reliably with over-training and on downstream tasks [[paper link]](http://arxiv.org/abs/2403.08540) 2024-03-13  
**Authors**: Gadre, Samir Yitzhak; Smyrnis, Georgios; Shankar, Vaishaal; Gururangan, Suchin; Wortsman, Mitchell; Shao, Rulin; Mercat, Jean; Fang, Alex; Li, Jeffrey; Keh, Sedrick; Xin, Rui; Nezhurina, Marianna; Vasiljevic, Igor; Jitsev, Jenia; Dimakis, Alexandros G.; Ilharco, Gabriel; Song, Shuran; Kollar, Thomas; Carmon, Yair; Dave, Achal; Heckel, Reinhard; Muennighoff, Niklas; Schmidt, Ludwig



**Title**: When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method [[paper link]](http://arxiv.org/abs/2402.17193) 2024-02-26  
**Authors**: Zhang, Biao; Liu, Zhongtao; Cherry, Colin; Firat, Orhan



**Title**: Interpreting Grokked Transformers in Complex Modular Arithmetic [[paper link]](https://arxiv.org/abs/2402.16726v2) 2024-02-26  
**Authors**: Furuta, Hiroki; Minegishi, Gouki; Iwasawa, Yusuke; Matsuo, Yutaka



**Title**: Scaling Data-Constrained Language Models [[paper link]](http://arxiv.org/abs/2305.16264) 2023-10-25  
**Authors**: Muennighoff, Niklas; Rush, Alexander M.; Barak, Boaz; Scao, Teven Le; Piktus, Aleksandra; Tazi, Nouamane; Pyysalo, Sampo; Wolf, Thomas; Raffel, Colin



**Title**: The Cost of Down-Scaling Language Models: Fact Recall Deteriorates before In-Context Learning [[paper link]](http://arxiv.org/abs/2310.04680) 2023-10-06  
**Authors**: Jin, Tian; Clement, Nolan; Dong, Xin; Nagarajan, Vaishnavh; Carbin, Michael; Ragan-Kelley, Jonathan; Dziugaite, Gintare Karolina



**Title**: Are Emergent Abilities of Large Language Models a Mirage? [[paper link]](https://arxiv.org/abs/2304.15004v2) 2023-04-28  
**Authors**: Schaeffer, Rylan; Miranda, Brando; Koyejo, Sanmi



**Title**: Training Compute-Optimal Large Language Models [[paper link]](http://arxiv.org/abs/2203.15556) 2022-03-29  
**Authors**: Hoffmann, Jordan; Borgeaud, Sebastian; Mensch, Arthur; Buchatskaya, Elena; Cai, Trevor; Rutherford, Eliza; Casas, Diego de Las; Hendricks, Lisa Anne; Welbl, Johannes; Clark, Aidan; Hennigan, Tom; Noland, Eric; Millican, Katie; Driessche, George van den; Damoc, Bogdan; Guy, Aurelia; Osindero, Simon; Simonyan, Karen; Elsen, Erich; Rae, Jack W.; Vinyals, Oriol; Sifre, Laurent



**Title**: Scaling Laws for Neural Language Models [[paper link]](http://arxiv.org/abs/2001.08361) 2020-01-22  
**Authors**: Kaplan, Jared; McCandlish, Sam; Henighan, Tom; Brown, Tom B.; Chess, Benjamin; Child, Rewon; Gray, Scott; Radford, Alec; Wu, Jeffrey; Amodei, Dario


</details>

### Knowledge / Memory mechanisms

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws [[paper link]](http://arxiv.org/abs/2404.05405) 2024-04-08  
**Authors**: Allen-Zhu, Zeyuan; Li, Yuanzhi



**Title**: Memorization Capacity of Multi-Head Attention in Transformers [[paper link]](http://arxiv.org/abs/2306.02010) 2024-03-02  
**Authors**: Mahdavi, Sadegh; Liao, Renjie; Thrampoulidis, Christos



**Title**: Birth of a Transformer: A Memory Viewpoint [[paper link]](http://arxiv.org/abs/2306.00802) 2023-11-06  
**Authors**: Bietti, Alberto; Cabannes, Vivien; Bouchacourt, Diane; Jegou, Herve; Bottou, Leon



**Title**: Physics of Language Models: Part 3.2, Knowledge Manipulation [[paper link]](http://arxiv.org/abs/2309.14402) 2023-09-25  
**Authors**: Allen-Zhu, Zeyuan; Li, Yuanzhi



**Title**: Can Neural Network Memorization Be Localized? [[paper link]](http://arxiv.org/abs/2307.09542) 2023-07-18  
**Authors**: Maini, Pratyush; Mozer, Michael C.; Sedghi, Hanie; Lipton, Zachary C.; Kolter, J. Zico; Zhang, Chiyuan


</details>

### Training Dynamics / Landscape / Optimization / Fine-tuning / etc.

This section focuses on the training dynamics of language models, including the optimization landscape, fine-tuning, and transfer learning.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Control Theoretic Approach to Fine-Tuning and Transfer Learning [[paper link]](http://arxiv.org/abs/2404.11013) 2024-04-16  
**Authors**: Bayram, Erkan; Liu, Shenyu; Belabbas, Mohamed-Ali; Başar, Tamer



**Title**: Look at the Text: Instruction-Tuned Language Models are More Robust Multiple Choice Selectors than You Think [[paper link]](http://arxiv.org/abs/2404.08382) 2024-04-12  
**Authors**: Wang, Xinpeng; Hu, Chengzhi; Ma, Bolei; Röttger, Paul; Plank, Barbara



**Title**: On Training Data Influence of GPT Models [[paper link]](http://arxiv.org/abs/2404.07840) 2024-04-11  
**Authors**: Liu, Qingyi; Chai, Yekun; Wang, Shuohuan; Sun, Yu; Wang, Keze; Wu, Hua



**Title**: Best Practices and Lessons Learned on Synthetic Data for Language Models [[paper link]](http://arxiv.org/abs/2404.07503) 2024-04-11  
**Authors**: Liu, Ruibo; Wei, Jerry; Liu, Fangyu; Si, Chenglei; Zhang, Yanzhe; Rao, Jinmeng; Zheng, Steven; Peng, Daiyi; Yang, Diyi; Zhou, Denny; Dai, Andrew M.



**Title**: How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse [[paper link]](http://arxiv.org/abs/2404.05090) 2024-04-07  
**Authors**: Seddik, Mohamed El Amine; Chen, Suei-Wen; Hayou, Soufiane; Youssef, Pierre; Debbah, Merouane



**Title**: Unveiling the Generalization Power of Fine-Tuned Large Language Models [[paper link]](http://arxiv.org/abs/2403.09162) 2024-03-14  
**Authors**: Yang, Haoran; Zhang, Yumeng; Xu, Jiaqi; Lu, Hongyuan; Heng, Pheng Ann; Lam, Wai



**Title**: Transformers Get Stable: An End-to-End Signal Propagation Theory for Language Models [[paper link]](http://arxiv.org/abs/2403.09635) 2024-03-14  
**Authors**: Kedia, Akhil; Zaidi, Mohd Abbas; Khyalia, Sushil; Jung, Jungho; Goka, Harshith; Lee, Haejun



**Title**: Hallmarks of Optimization Trajectories in Neural Networks and LLMs: The Lengths, Bends, and Dead Ends [[paper link]](http://arxiv.org/abs/2403.07379) 2024-03-12  
**Authors**: Singh, Sidak Pal; He, Bobby; Hofmann, Thomas; Schölkopf, Bernhard



**Title**: The Heuristic Core: Understanding Subnetwork Generalization in Pretrained Language Models [[paper link]](http://arxiv.org/abs/2403.03942) 2024-03-06  
**Authors**: Bhaskar, Adithya; Friedman, Dan; Chen, Danqi



**Title**: Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
**Authors**: Chen, Siyu; Sheen, Heejune; Wang, Tianhao; Yang, Zhuoran



**Title**: How Transformers Learn Causal Structure with Gradient Descent [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
**Authors**: Nichani, Eshaan; Damian, Alex; Lee, Jason D.



**Title**: Transformers learn through gradual rank increase [[paper link]](http://arxiv.org/abs/2306.07042) 2023-12-10  
**Authors**: Boix-Adsera, Enric; Littwin, Etai; Abbe, Emmanuel; Bengio, Samy; Susskind, Joshua



**Title**: Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
**Authors**: Jain, Samyak; Kirk, Robert; Lubana, Ekdeep Singh; Dick, Robert P.; Tanaka, Hidenori; Grefenstette, Edward; Rocktäschel, Tim; Krueger, David Scott



**Title**: Connecting Pre-trained Language Model and Downstream Task via Properties of Representation [[paper link]](https://openreview.net/forum?id=YLOJ4aKAka) 2023-11-02  
**Authors**: Wu, Chenwei; Lee, Holden; Ge, Rong



**Title**: Scan and Snap: Understanding Training Dynamics and Token Composition in 1-layer Transformer [[paper link]](http://arxiv.org/abs/2305.16380) 2023-07-02  
**Authors**: Tian, Yuandong; Wang, Yiping; Chen, Beidi; Du, Simon



**Title**: A Kernel-Based View of Language Model Fine-Tuning [[paper link]](https://openreview.net/forum?id=49dTFIGdx8) 2023-06-15  
**Authors**: Malladi, Sadhika; Wettig, Alexander; Yu, Dingli; Chen, Danqi; Arora, Sanjeev



**Title**: A Stability Analysis of Fine-Tuning a Pre-Trained Model [[paper link]](https://arxiv.org/abs/2301.09820v2) 2023-01-24  
**Authors**: Fu, Zihao; So, Anthony Man-Cho; Collier, Nigel


</details>

### Learning / Generalization

This section includes papers that investigate the generalization ability of language models, and the general learning behavior of language models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
**Authors**: Jain, Samyak; Kirk, Robert; Lubana, Ekdeep Singh; Dick, Robert P.; Tanaka, Hidenori; Grefenstette, Edward; Rocktäschel, Tim; Krueger, David Scott



**Title**: The Impact of Depth and Width on Transformer Language Model Generalization [[paper link]](http://arxiv.org/abs/2310.19956) 2023-10-30  
**Authors**: Petty, Jackson; van Steenkiste, Sjoerd; Dasgupta, Ishita; Sha, Fei; Garrette, Dan; Linzen, Tal



**Title**: How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition [[paper link]](http://arxiv.org/abs/2310.05492) 2023-10-09  
**Authors**: Dong, Guanting; Yuan, Hongyi; Lu, Keming; Li, Chengpeng; Xue, Mingfeng; Liu, Dayiheng; Wang, Wei; Yuan, Zheng; Zhou, Chang; Zhou, Jingren



**Title**: A Theory for Emergence of Complex Skills in Language Models [[paper link]](http://arxiv.org/abs/2307.15936) 2023-07-29  
**Authors**: Arora, Sanjeev; Goyal, Anirudh



**Title**: On the Power of Foundation Models [[paper link]](https://proceedings.mlr.press/v202/yuan23b.html) 2023-07-03  
**Authors**: Yuan, Yang



**Title**: Task-Specific Skill Localization in Fine-tuned Language Models [[paper link]](https://openreview.net/forum?id=Rgnaj43Pk0) 2023-06-15  
**Authors**: Panigrahi, Abhishek; Saunshi, Nikunj; Zhao, Haoyu; Arora, Sanjeev



**Title**: Towards Understanding Why Mask-Reconstruction Pretraining Helps in Downstream Tasks [[paper link]](http://arxiv.org/abs/2206.03826) 2023-02-11  
**Authors**: Pan, Jiachun; Zhou, Pan; Yan, Shuicheng



**Title**: Same Pre-training Loss, Better Downstream: Implicit Bias Matters for Language Models [[paper link]](http://arxiv.org/abs/2210.14199) 2022-10-25  
**Authors**: Liu, Hong; Xie, Sang Michael; Li, Zhiyuan; Ma, Tengyu



**Title**: Why Do Pretrained Language Models Help in Downstream Tasks? An Analysis of Head and Prompt Tuning [[paper link]](http://arxiv.org/abs/2106.09226) 2022-04-20  
**Authors**: Wei, Colin; Xie, Sang Michael; Ma, Tengyu



**Title**: A Mathematical Exploration of Why Language Models Help Solve Downstream Tasks [[paper link]](http://arxiv.org/abs/2010.03648) 2021-04-14  
**Authors**: Saunshi, Nikunj; Malladi, Sadhika; Arora, Sanjeev



**Title**: Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning [[paper link]](http://arxiv.org/abs/2012.13255) 2020-12-22  
**Authors**: Aghajanyan, Armen; Zettlemoyer, Luke; Gupta, Sonal



**Title**: How fine can fine-tuning be? Learning efficient language models [[paper link]](https://proceedings.mlr.press/v108/radiya-dixit20a.html) 2020-06-03  
**Authors**: Radiya-Dixit, Evani; Wang, Xin


</details>

### Other Phenomena

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Algorithmic progress in language models [[paper link]](http://arxiv.org/abs/2403.05812) 2024-03-09  
**Authors**: Ho, Anson; Besiroglu, Tamay; Erdil, Ege; Owen, David; Rahman, Robi; Guo, Zifan Carl; Atkinson, David; Thompson, Neil; Sevilla, Jaime



**Title**: Massive Activations in Large Language Models [[paper link]](http://arxiv.org/abs/2402.17762) 2024-02-27  
**Authors**: Sun, Mingjie; Chen, Xinlei; Kolter, J. Zico; Liu, Zhuang



**Title**: The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers [[paper link]](https://openreview.net/forum?id=TJ2nxciYCk-) 2023-02-01  
**Authors**: Li, Zonglin; You, Chong; Bhojanapalli, Srinadh; Li, Daliang; Rawat, Ankit Singh; Reddi, Sashank J.; Ye, Ke; Chern, Felix; Yu, Felix; Guo, Ruiqi; Kumar, Sanjiv


</details>

## Representational Capacity

Investigate the expressiveness of transformer-based models about what they can do and what they can't do.

### What Can Transformer Do? / Properties of Transformer

This section includes positive results on the representational capacity and properties of transformer-based models.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Transformers Can Represent $n$-gram Language Models [[paper link]](http://arxiv.org/abs/2404.14994) 2024-04-23  
**Authors**: Svete, Anej; Cotterell, Ryan



**Title**: Mechanics of Next Token Prediction with Self-Attention [[paper link]](https://proceedings.mlr.press/v238/li24f.html) 2024-04-18  
**Authors**: Li, Yingcong; Huang, Yixiao; Ildiz, Muhammed E.; Rawat, Ankit Singh; Oymak, Samet



**Title**: When can transformers reason with abstract symbols? [[paper link]](http://arxiv.org/abs/2310.09753) 2024-04-16  
**Authors**: Boix-Adsera, Enric; Saremi, Omid; Abbe, Emmanuel; Bengio, Samy; Littwin, Etai; Susskind, Joshua



**Title**: The Illusion of State in State-Space Models [[paper link]](http://arxiv.org/abs/2404.08819) 2024-04-12  
**Authors**: Merrill, William; Petty, Jackson; Sabharwal, Ashish



**Title**: Attention is Naturally Sparse with Gaussian Distributed Input [[paper link]](http://arxiv.org/abs/2404.02690) 2024-04-03  
**Authors**: Deng, Yichuan; Song, Zhao; Yang, Chiwun



**Title**: What Can Transformer Learn with Varying Depth? Case Studies on Sequence Learning Tasks [[paper link]](http://arxiv.org/abs/2404.01601) 2024-04-01  
**Authors**: Chen, Xingwu; Zou, Difan



**Title**: The Topos of Transformer Networks [[paper link]](http://arxiv.org/abs/2403.18415) 2024-03-27  
**Authors**: Villani, Mattia Jacopo; McBurney, Peter



**Title**: Simulating Weighted Automata over Sequences and Trees with Transformers [[paper link]](http://arxiv.org/abs/2403.09728) 2024-03-12  
**Authors**: Rizvi, Michael; Lizaire, Maude; Lacroce, Clara; Rabusseau, Guillaume



**Title**: Simplicity Bias of Transformers to Learn Low Sensitivity Functions [[paper link]](http://arxiv.org/abs/2403.06925) 2024-03-11  
**Authors**: Vasudeva, Bhavya; Fu, Deqing; Zhou, Tianyi; Kau, Elliott; Huang, Youqi; Sharan, Vatsal



**Title**: On the Origins of Linear Representations in Large Language Models [[paper link]](http://arxiv.org/abs/2403.03867) 2024-03-06  
**Authors**: Jiang, Yibo; Rajendran, Goutham; Ravikumar, Pradeep; Aragam, Bryon; Veitch, Victor



**Title**: How Well Can Transformers Emulate In-context Newton's Method? [[paper link]](http://arxiv.org/abs/2403.03183) 2024-03-05  
**Authors**: Giannou, Angeliki; Yang, Liu; Wang, Tianhao; Papailiopoulos, Dimitris; Lee, Jason D.



**Title**: RNNs are not Transformers (Yet): The Key Bottleneck on In-context Retrieval [[paper link]](http://arxiv.org/abs/2402.18510) 2024-02-29  
**Authors**: Wen, Kaiyue; Dang, Xingyu; Lyu, Kaifeng



**Title**: Implicit Bias of Next-Token Prediction [[paper link]](http://arxiv.org/abs/2402.18551) 2024-02-28  
**Authors**: Thrampoulidis, Christos



**Title**: On the Expressive Power of a Variant of the Looped Transformer [[paper link]](http://arxiv.org/abs/2402.13572) 2024-02-21  
**Authors**: Gao, Yihang; Zheng, Chuanyang; Xie, Enze; Shi, Han; Hu, Tianyang; Li, Yu; Ng, Michael K.; Li, Zhenguo; Liu, Zhaoqiang



**Title**: From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers [[paper link]](http://arxiv.org/abs/2402.13512) 2024-02-20  
**Authors**: Ildiz, M. Emrullah; Huang, Yixiao; Li, Yingcong; Rawat, Ankit Singh; Oymak, Samet



**Title**: Transformers Implement Functional Gradient Descent to Learn Non-Linear Functions In Context [[paper link]](http://arxiv.org/abs/2312.06528) 2024-02-15  
**Authors**: Cheng, Xiang; Chen, Yuxin; Sra, Suvrit



**Title**: Compositional Capabilities of Autoregressive Transformers: A Study on Synthetic, Interpretable Tasks [[paper link]](http://arxiv.org/abs/2311.12997) 2024-02-05  
**Authors**: Ramesh, Rahul; Lubana, Ekdeep Singh; Khona, Mikail; Dick, Robert P.; Tanaka, Hidenori



**Title**: Are Transformers with One Layer Self-Attention Using Low-Rank Weight Matrices Universal Approximators? [[paper link]](http://arxiv.org/abs/2307.14023) 2024-01-29  
**Authors**: Kajitsuka, Tokio; Sato, Issei



**Title**: Transformers are Multi-State RNNs [[paper link]](http://arxiv.org/abs/2401.06104) 2024-01-11  
**Authors**: Oren, Matanel; Hassid, Michael; Adi, Yossi; Schwartz, Roy



**Title**: How Capable Can a Transformer Become? A Study on Synthetic, Interpretable Tasks [[paper link]](https://openreview.net/forum?id=KIhFggzePM) 2023-12-12  
**Authors**: Ramesh, Rahul; Khona, Mikail; Dick, Robert P.; Tanaka, Hidenori; Lubana, Ekdeep Singh



**Title**: Transformers can optimally learn regression mixture models [[paper link]](http://arxiv.org/abs/2311.08362) 2023-11-14  
**Authors**: Pathak, Reese; Sen, Rajat; Kong, Weihao; Das, Abhimanyu



**Title**: The Expressive Power of Low-Rank Adaptation [[paper link]](http://arxiv.org/abs/2310.17513) 2023-10-26  
**Authors**: Zeng, Yuchen; Lee, Kangwook



**Title**: What Algorithms can Transformers Learn? A Study in Length Generalization [[paper link]](http://arxiv.org/abs/2310.16028) 2023-10-24  
**Authors**: Zhou, Hattie; Bradley, Arwen; Littwin, Etai; Razin, Noam; Saremi, Omid; Susskind, Josh; Bengio, Samy; Nakkiran, Preetum



**Title**: Transformers as Support Vector Machines [[paper link]](http://arxiv.org/abs/2308.16898) 2023-09-07  
**Authors**: Tarzanagh, Davoud Ataee; Li, Yingcong; Thrampoulidis, Christos; Oymak, Samet



**Title**: How Do Transformers Learn Topic Structure: Towards a Mechanistic Understanding [[paper link]](https://openreview.net/forum?id=LMXgU4zrq6) 2023-06-15  
**Authors**: Li, Yuchen; Li, Yuanzhi; Risteski, Andrej



**Title**: Tighter Bounds on the Expressivity of Transformer Encoders [[paper link]](https://openreview.net/forum?id=XKcogevHj8) 2023-06-15  
**Authors**: Chiang, David; Cholak, Peter; Pillay, Anand



**Title**: Fast Attention Requires Bounded Entries [[paper link]](https://arxiv.org/abs/2302.13214v2) 2023-02-26  
**Authors**: Alman, Josh; Song, Zhao



**Title**: Transformers Learn Shortcuts to Automata [[paper link]](https://openreview.net/forum?id=De4FYqjFueZ) 2023-02-01  
**Authors**: Liu, Bingbin; Ash, Jordan T.; Goel, Surbhi; Krishnamurthy, Akshay; Zhang, Cyril



**Title**: Transformer Vs. MLP-Mixer: Exponential Expressive Gap For NLP Problems [[paper link]](http://arxiv.org/abs/2208.08191) 2022-11-17  
**Authors**: Navon, Dan; Bronstein, Alex M.



**Title**: Small Transformers Compute Universal Metric Embeddings [[paper link]](http://arxiv.org/abs/2209.06788) 2022-10-18  
**Authors**: Kratsios, Anastasis; Debarnot, Valentin; Dokmanić, Ivan



**Title**: The Lipschitz Constant of Self-Attention [[paper link]](http://arxiv.org/abs/2006.04710) 2021-06-09  
**Authors**: Kim, Hyunjik; Papamakarios, George; Mnih, Andriy



**Title**: On Identifiability in Transformers [[paper link]](http://arxiv.org/abs/1908.04211) 2020-02-07  
**Authors**: Brunner, Gino; Liu, Yang; Pascual, Damián; Richter, Oliver; Ciaramita, Massimiliano; Wattenhofer, Roger


</details>

### What Can Transformer Not Do? / Limitation of Transformer

The papers in this section investigate the limitations of transformer-based models, including the limitations of their expressiveness and learning abilities.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Collapse of Self-trained Language Models [[paper link]](http://arxiv.org/abs/2404.02305) 2024-04-02  
**Authors**: Herel, David; Mikolov, Tomas



**Title**: The pitfalls of next-token prediction [[paper link]](http://arxiv.org/abs/2403.06963) 2024-03-11  
**Authors**: Bachmann, Gregor; Nagarajan, Vaishnavh



**Title**: Why are Sensitive Functions Hard for Transformers? [[paper link]](http://arxiv.org/abs/2402.09963) 2024-03-03  
**Authors**: Hahn, Michael; Rofin, Mark



**Title**: Transformers are Expressive, But Are They Expressive Enough for Regression? [[paper link]](http://arxiv.org/abs/2402.15478) 2024-02-23  
**Authors**: Nath, Swaroop; Khadilkar, Harshad; Bhattacharyya, Pushpak



**Title**: Limits of Transformer Language Models on Learning Algorithmic Compositions [[paper link]](http://arxiv.org/abs/2402.05785) 2024-02-13  
**Authors**: Thomm, Jonathan; Terzic, Aleksandar; Karunaratne, Geethan; Camposampiero, Giacomo; Schölkopf, Bernhard; Rahimi, Abbas



**Title**: Representational Strengths and Limitations of Transformers [[paper link]](http://arxiv.org/abs/2306.02896) 2023-11-16  
**Authors**: Sanford, Clayton; Hsu, Daniel; Telgarsky, Matus



**Title**: Large Language Models Cannot Self-Correct Reasoning Yet [[paper link]](https://openreview.net/forum?id=IkmD3fKBPQ) 2023-10-13  
**Authors**: Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny



**Title**: Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth [[paper link]](http://arxiv.org/abs/2103.03404) 2023-08-01  
**Authors**: Dong, Yihe; Cordonnier, Jean-Baptiste; Loukas, Andreas



**Title**: Limits for Learning with Language Models [[paper link]](http://arxiv.org/abs/2306.12213) 2023-06-21  
**Authors**: Asher, Nicholas; Bhar, Swarnadeep; Chaturvedi, Akshay; Hunter, Julie; Paul, Soumya



**Title**: Your Transformer May Not be as Powerful as You Expect [[paper link]](https://openreview.net/forum?id=NQFFNdsOGD) 2022-10-31  
**Authors**: Luo, Shengjie; Li, Shanda; Zheng, Shuxin; Liu, Tie-Yan; Wang, Liwei; He, Di



**Title**: The Devil in Linear Transformer [[paper link]](http://arxiv.org/abs/2210.10340) 2022-10-19  
**Authors**: Qin, Zhen; Han, XiaoDong; Sun, Weixuan; Li, Dongxu; Kong, Lingpeng; Barnes, Nick; Zhong, Yiran


</details>

## Architectural Effectivity

discussion of the effectiveness of different architectures in terms of learning and generalization

### Layer-normalization

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: The Expressive Power of Tuning Only the Normalization Layers [[paper link]](https://proceedings.mlr.press/v195/giannou23a.html) 2023-07-12  
**Authors**: Giannou, Angeliki; Rajput, Shashank; Papailiopoulos, Dimitris



**Title**: ResiDual: Transformer with Dual Residual Connections [[paper link]](http://arxiv.org/abs/2304.14802) 2023-04-28  
**Authors**: Xie, Shufang; Zhang, Huishuai; Guo, Junliang; Tan, Xu; Bian, Jiang; Awadalla, Hany Hassan; Menezes, Arul; Qin, Tao; Yan, Rui



**Title**: DeepNet: Scaling Transformers to 1,000 Layers [[paper link]](http://arxiv.org/abs/2203.00555) 2022-03-01  
**Authors**: Wang, Hongyu; Ma, Shuming; Dong, Li; Huang, Shaohan; Zhang, Dongdong; Wei, Furu



**Title**: On Layer Normalization in the Transformer Architecture [[paper link]](http://arxiv.org/abs/2002.04745) 2020-06-29  
**Authors**: Xiong, Ruibin; Yang, Yunchang; He, Di; Zheng, Kai; Zheng, Shuxin; Xing, Chen; Zhang, Huishuai; Lan, Yanyan; Wang, Liwei; Liu, Tie-Yan


</details>

### Tokenization

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Toward a Theory of Tokenization in LLMs [[paper link]](http://arxiv.org/abs/2404.08335) 2024-04-12  
**Authors**: Rajaraman, Nived; Jiao, Jiantao; Ramchandran, Kannan



**Title**: On the Effect of (Near) Duplicate Subwords in Language Modelling [[paper link]](http://arxiv.org/abs/2404.06508) 2024-04-09  
**Authors**: Schäfer, Anton; Hofmann, Thomas; Schlag, Imanol; Pimentel, Tiago



**Title**: Tokenization Is More Than Compression [[paper link]](http://arxiv.org/abs/2402.18376) 2024-02-28  
**Authors**: Schmidt, Craig W.; Reddy, Varshini; Zhang, Haoran; Alameddine, Alec; Uzan, Omri; Pinter, Yuval; Tanner, Chris


</details>

## Training Paradigms

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Knowledge Distillation vs. Pretraining from Scratch under a Fixed (Computation) Budget [[paper link]](http://arxiv.org/abs/2404.19319) 2024-04-30  
**Authors**: Bui, Minh Duc; Schmidt, Fabian David; Glavaš, Goran; von der Wense, Katharina



**Title**: Why are Adaptive Methods Good for Attention Models? [[paper link]](http://arxiv.org/abs/1912.03194) 2020-10-23  
**Authors**: Zhang, Jingzhao; Karimireddy, Sai Praneeth; Veit, Andreas; Kim, Seungyeon; Reddi, Sashank J.; Kumar, Sanjiv; Sra, Suvrit


</details>

## Mechanistic Engineering / Probing / Interpretability

This section includes papers that mainly investigate the mechanisms of language models through probing, mechanistic engineering, and other papers generally related to interpretability.

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Talking Nonsense: Probing Large Language Models' Understanding of Adversarial Gibberish Inputs [[paper link]](http://arxiv.org/abs/2404.17120) 2024-04-25  
**Authors**: Cherepanova, Valeriia; Zou, James



**Title**: Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions [[paper link]](http://arxiv.org/abs/2402.15055) 2024-02-22  
**Authors**: Neo, Clement; Cohen, Shay B.; Barez, Fazl



**Title**: Universal Neurons in GPT2 Language Models [[paper link]](http://arxiv.org/abs/2401.12181) 2024-01-22  
**Authors**: Gurnee, Wes; Horsley, Theo; Guo, Zifan Carl; Kheirkhah, Tara Rezaei; Sun, Qinyi; Hathaway, Will; Nanda, Neel; Bertsimas, Dimitris



**Title**: Interpretability Illusions in the Generalization of Simplified Models [[paper link]](http://arxiv.org/abs/2312.03656) 2023-12-06  
**Authors**: Friedman, Dan; Lampinen, Andrew; Dixon, Lucas; Chen, Danqi; Ghandeharioun, Asma



**Title**: Transformers are uninterpretable with myopic methods: a case study with bounded Dyck grammars [[paper link]](http://arxiv.org/abs/2312.01429) 2023-12-03  
**Authors**: Wen, Kaiyue; Li, Yuchen; Liu, Bingbin; Risteski, Andrej



**Title**: White-Box Transformers via Sparse Rate Reduction: Compression Is All There Is? [[paper link]](https://arxiv.org/abs/2311.13110v2) 2023-11-22  
**Authors**: Yu, Yaodong; Buchanan, Sam; Pai, Druv; Chu, Tianzhe; Wu, Ziyang; Tong, Shengbang; Bai, Hao; Zhai, Yuexiang; Haeffele, Benjamin D.; Ma, Yi



**Title**: Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
**Authors**: Jain, Samyak; Kirk, Robert; Lubana, Ekdeep Singh; Dick, Robert P.; Tanaka, Hidenori; Grefenstette, Edward; Rocktäschel, Tim; Krueger, David Scott



**Title**: Understanding the Mechanics and Dynamics of Memorisation in Large Language Models: A Case Study with Random Strings [[paper link]](https://openreview.net/forum?id=ILStlRb1Sp) 2023-10-13  
**Authors**: Speicher, Till; Khan, Aflah Mohammad; Wu, Qinyuan; Nanda, Vedant; Das, Soumi; Ghosh, Bishwamittra; Gummadi, Krishna P.; Terzi, Evimaria


</details>

## Miscellanea

<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

**Title**: Compression Represents Intelligence Linearly [[paper link]](http://arxiv.org/abs/2404.09937) 2024-04-15  
**Authors**: Huang, Yuzhen; Zhang, Jinghan; Shan, Zifei; He, Junxian



**Title**: Language Generation in the Limit [[paper link]](http://arxiv.org/abs/2404.06757) 2024-04-10  
**Authors**: Kleinberg, Jon; Mullainathan, Sendhil



**Title**: Do language models plan ahead for future tokens? [[paper link]](http://arxiv.org/abs/2404.00859) 2024-03-31  
**Authors**: Wu, Wilson; Morris, John X.; Levine, Lionel



**Title**: Universality and Limitations of Prompt Tuning [[paper link]](http://arxiv.org/abs/2305.18787) 2023-11-16  
**Authors**: Wang, Yihan; Chauhan, Jatin; Wang, Wei; Hsieh, Cho-Jui



**Title**: Data Similarity is Not Enough to Explain Language Model Performance [[paper link]](http://arxiv.org/abs/2311.09006) 2023-11-15  
**Authors**: Yauney, Gregory; Reif, Emily; Mimno, David



**Title**: Simplifying Transformer Blocks [[paper link]](http://arxiv.org/abs/2311.01906) 2023-11-03  
**Authors**: He, Bobby; Hofmann, Thomas



**Title**: Causal Interpretation of Self-Attention in Pre-Trained Transformers [[paper link]](http://arxiv.org/abs/2310.20307) 2023-10-31  
**Authors**: Rohekar, Raanan Y.; Gurwicz, Yaniv; Nisimov, Shami



**Title**: How do Language Models Bind Entities in Context? [[paper link]](http://arxiv.org/abs/2310.17191) 2023-10-26  
**Authors**: Feng, Jiahai; Steinhardt, Jacob



**Title**: Understanding prompt engineering may not require rethinking generalization [[paper link]](https://openreview.net/forum?id=a745RnSFLT) 2023-10-13  
**Authors**: Akinwande, Victor; Jiang, Yiding; Sam, Dylan; Kolter, J. Zico



**Title**: Understanding Catastrophic Forgetting in Language Models via Implicit Inference [[paper link]](http://arxiv.org/abs/2309.10105) 2023-09-18  
**Authors**: Kotha, Suhas; Springer, Jacob Mitchell; Raghunathan, Aditi



**Title**: Attention-Only Transformers and Implementing MLPs with Attention Heads [[paper link]](http://arxiv.org/abs/2309.08593) 2023-09-15  
**Authors**: Huben, Robert; Morris, Valerie



**Title**: On the Role of Attention in Prompt-tuning [[paper link]](https://openreview.net/forum?id=qorOnDor89) 2023-06-15  
**Authors**: Oymak, Samet; Rawat, Ankit Singh; Soltanolkotabi, Mahdi; Thrampoulidis, Christos


</details>

---

Contact:

- [Shiguang Wu](https://github.com/Furyton), furyton AT outlook.com / shiguang.wu AT mail.sdu.edu.cn