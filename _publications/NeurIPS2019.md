---
title: "SHE:A fast and accurate deep neural networks for encrypted data"
collection: publications
permalink: /publications/NeurIPS2019
venue: "Thirty-third Conference on Neural Information Processing Systems (NeurIPS 2019)"
date: 2019-12-8
citation: '<b>Qian Lou</b>, Lei Jiang<i>Thirty-third Conference on Neural Information Processing Systems</i> <b>NeurIPS 2019</b>.'
---
[[PDF]](http://qianlou.github.io/files/NeurIPS2019.pdf)

## Abstract
Homomorphic Encryption (HE) is one of the most promis-ing security solutions to emerging Machine Learning as aService (MLaaS). Several Leveled-HE (LHE)-enabled Con-volutional Neural Networks (LHECNNs) are proposed toimplement MLaaS to avoid the large bootstrapping over-head.  However, prior LHECNNs have to pay significantcomputational overhead but achieve only low inference ac-curacy, due to their polynomial approximation activationsand poolings. Stacking many polynomial approximation ac-tivation layers in a network greatly reduces the inferenceaccuracy, since the polynomial approximation activation er-rors lead to a low distortion of the output distribution of thenext batch normalization layer. So the polynomial approxi-mation activations and poolings have become the obstacleto a fast and accurate LHECNN model.In this paper,  we propose aShift-accumulation-basedLHE-enabled  deep  neural  network  (SHE)  for  fast  andaccurate  inferences  on  encrypted  data.We  use  thebinary-operation-friendly leveled-TFHE (LTFHE) encryp-tion scheme to implementReLUactivations and max pool-ings. We also adopt the logarithmic quantization to acceler-ate inferences by replacing expensive LTFHE multiplicationswith cheap LTFHE shifts. We propose a mixed bitwidth accu-mulator to expedite accumulations. Since the LTFHEReLUactivations, max poolings, shifts and accumulations havesmall multiplicative depth, SHE can implement much deepernetwork architectures with more convolutional and activa-tion layers.  Our experimental results show SHE achievesthe state-of-the-art inference accuracy and reduces the infer-ence latency by 76.21%∼94.23% over prior LHECNNs on MNIST and CIFAR-10.



