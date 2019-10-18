---
title: "SHE:A fast and accurate deep neural networks for encrypted data"
collection: publications
permalink: /publications/NeurIPS2019
venue: "Thirty-third Conference on Neural Information Processing Systems (NeurIPS 2019)"
date: 2019-12-8
citation: '<b>Qian Lou</b>, Lei Jiang<i> Thirty-third Conference on Neural Information Processing Systems</i> <b>NeurIPS 2019</b>.'
---
[[PDF]](http://qianlou.github.io/files/NeurIPS2019.pdf)

## Abstract
Homomorphic Encryption (HE) is one of the most promising security solutions to emerging Machine Learning as a Service (MLaaS). Several Leveled-HE (LHE)-enabled Convolutional Neural Networks (LHECNNs) are proposed to implement MLaaS to avoid the large bootstrapping overhead. However, prior LHECNNs have to pay significant computational overhead but achieve only low inference accuracy, due to their polynomial approximation activationsand poolings. Stacking many polynomial approximation activation layers in a network greatly reduces the inference accuracy, since the polynomial approximation activation errors lead to a low distortion of the output distribution of the next batch normalization layer. So the polynomial approximation activations and poolings have become the obstacle to a fast and accurate LHECNN model. In this paper, we propose a Shift-accumulation-basedLHE-enabled  deep  neural  network (SHE) for fast  andaccurate  inferences  on  encrypted  data. We use the binary operation-friendly leveled-TFHE (LTFHE) encryption scheme to implement ReLU activations and max poolings. We also adopt the logarithmic quantization to accelerate inferences by replacing expensive LTFHE multiplicationswith cheap LTFHE shifts. We propose a mixed bitwidth accumulator to expedite accumulations. Since the LTFHE ReLU activations, max poolings, shifts and accumulations have small multiplicative depth, SHE can implement much deeper network architectures with more convolutional and activation layers. Our experimental results show SHE achievesthe state-of-the-art inference accuracy and reduces the inference latency by 76.21%∼94.23% over prior LHECNNs on MNIST and CIFAR-10.



