---
hide:
  - navigation
#   - toc

---

# QuAIR

Quantum AI Research (QuAIR) Lab, led by Prof. Xin Wang at HKUST (Guangzhou), is dedicated to pushing the fundamental boundaries of quantum information processing and driving technological advancements for quantum computing, guided by AI for Quantum and Quantum for AI.

# QuAIR-Platform (beta)

## Avocado
**Avocado** is a quantum research platform designed to empower researchers in the QuAIR team, by providing a robust and efficient suite of tools tailored for quantum computing and quantum information research.

## MPQQ
**MPQQ**: Matlab Package for Quantum Information Processing and Quantum Resource Theory is a MATLAB toolbox for exploring quantum resource theory.

### Features
- **Resource Measure**: Functions to calculate the amount of resource for the given state/channel within entanglement, coherence, and magic theories. 
- **Channel Simulation**: Capabilities to simulate quantum channels within different resource theories.
- **Error Mitigation**: Tools to compute the optimal probabilistic error cancellation protocols for a given noisy channel.

## QuICK
**QuICK**: Quantum Integrity and Correction Kit is a quantum error correction package in the QuAIR team (under construction). The tools are for code construction and decoding.

### Features
- **QuICK**: contain error correction codes include:
  - **code**: classical and quantum code construction
    - **ClassicalCode**: binary classical linear block code
    - **Stabilizer**: quantum stabilizer code
    - **CSSCode**: quantum Calderbank-Shor-Steane(CSS) code
    - **HGP**: quantum hypergraph product code
    - **LP**: quantum lifted product code
  - **utils**: binary linear algebra and code utilities