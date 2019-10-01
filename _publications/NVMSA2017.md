---
title: "Runtime and reconfiguration dual-aware placement for SRAM-NVM hybrid FPGAs."
collection: publications
permalink: /publications/NVMSA2017
venue: "IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA)"
date: 2017-6-12
citation: '<b>Qian Lou</b>, Mengying Zhao, Lei Ju, Chun Jason Xue, Jingtong Hu, Zhiping Jia. <i>IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA).</i> <b>NVMSA 2017</b>.'
---
[[PDF]](http://qianlou.github.io/files/NVMSA2017.pdf)

## Abstract
Field Programmable Gate Array (FPGA) has been widely adopted as modern reconfigurable computing platforms. Traditionally, the storage elements in FPGAs are static RAM (SRAM), which has large leakage power and limited scalability. Recently, non-volatile memory (NVM) is proposed to replace the SRAM in FPGA systems for static power and density considerations, at the cost of inducing larger dynamic power. Hybrid FPGAs combine the advantages of SRAM and NVM by employing both SRAM and NVM as logic storage elements. Although the feasibility of hybrid FPGA has been confirmed, the design flow has not fully explored the hybrid features yet, resulting in inferior system performance. Besides, traditional design flow does not consider the reconfiguration cost, which may prolong the reconfiguration procedures and thus degrade the system performance in dynamically reconfigurable FPGA systems. This work proposes a runtime and reconfiguration dual aware placement strategy for dynamically reconfigurable hybrid architecture. The proposed scheme considers the tradeoff between runtime and dynamic reconfiguration latency and optimizes the overall performance of the reconfigurable system. Evaluation shows that the proposed scheme improves the system performance by 14.6% for SRAM-MRAM hybrid FPGAs compared with the default placement strategy.
