---
title: "Glyph: Fast and Accurately Training Deep Neural Networks on Encrypted Data"
collection: publications
permalink: /publications/Arxiv2019
venue: "Arxiv preprint"
date: 2019-12-8
citation: '<b>Qian Lou</b>, Bo Feng, Geofrry Fox, Lei Jiang<i> </i> <b>Arxiv preprint</b>.'
---
[[PDF]](https://arxiv.org/abs/1911.07101)

## Abstract
Big data is one of the cornerstones to enabling and training deep neural networks (DNNs). Because of the lack of expertise, to gain benefits from their data, average users have to rely on and upload their private data to big data companies they may not trust. Due to the compliance, legal, or privacy constraints, most users are willing to contribute only their encrypted data, and lack interests or resources to join the training of DNNs in cloud. To train a DNN on encrypted data in a completely non-interactive way, a recent work proposes a fully homomorphic encryption (FHE)-based technique implementing all activations in the neural network by \textit{Brakerski-Gentry-Vaikuntanathan (BGV)}-based lookup tables. However, such inefficient lookup-table-based activations significantly prolong the training latency of privacy-preserving DNNs.
In this paper, we propose, Glyph, a FHE-based scheme to fast and accurately train DNNs on encrypted data by switching between TFHE (Fast Fully Homomorphic Encryption over the Torus) and BGV cryptosystems. Glyph uses logic-operation-friendly TFHE to implement nonlinear activations, while adopts vectorial-arithmetic-friendly BGV to perform multiply-accumulation (MAC) operations. Glyph further applies transfer learning on the training of DNNs to improve the test accuracy and reduce the number of MAC operations between ciphertext and ciphertext in convolutional layers. Our experimental results show Glyph obtains the state-of-the-art test accuracy, but reduces the training latency by 99% over the prior FHE-based technique on various encrypted datasets. 


