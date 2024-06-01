---
hide:
  - navigation
#   - toc

---

# QuAIR

<div style="display: flex; align-items: flex-start;">
  <div style="flex: 1; padding: 10px;">
    <h1>Quantum AI</h1>
    <p>Quantum AI Research (QuAIR) Lab, led by Prof. <a href="https://www.quair.group">Xin Wang</a> at HKUST (Guangzhou), is dedicated to pushing the fundamental boundaries of quantum information processing and driving technological advancements for quantum computing, guided by AI for Quantum and Quantum for AI.</p>
  </div>
  <div style="flex: 1; padding: 10px;">
    <img src="https://www.quair.group/media/welcome_hu01b1aaffad28f84349178a25160d6ab1_1045841_1200x0_resize_q75_lanczos.jpg" alt="Quantum AI Image" style="width: 100%;">
  </div>
</div>


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