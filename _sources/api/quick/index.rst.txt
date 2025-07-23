QuICK
=====

Quantum Integrity and Correction Kit (QuICK) is a quantum error correction package in the QuAIR team (under construction). The tools are for code construction and decoding.

.. image:: logo.png
   :alt: QuICK Logo
   :align: center

Features
--------

**QuICK** contains error correction codes including:

- **code**: classical and quantum code construction

  - **ClassicalCode**: binary classical linear block code
  - **Stabilizer**: quantum stabilizer code
  - **CSSCode**: quantum Calderbank-Shor-Steane(CSS) code
  - **HGP**: quantum hypergraph product code
  - **LP**: quantum lifted product code

- **utils**: binary linear algebra and code utilities
- **dataset**: commonly used classical and quantum codes
- **error**: simple Pauli error
- **decoder**: code decoder

  - **bp_decoder**: belief propagation sum-product decoder

- **tutorial**: tutorials for quantum error correction

Installation
------------

Set up Anaconda environment::

    conda create -n quair python=3.10
    conda activate quair
    conda install jupyter notebook

Install QuICK locally::

    cd ./< your place for QuICK >
    pip install -e .

Tutorials
---------

Error Correction Codes
~~~~~~~~~~~~~~~~~~~~~~~

- `CSS Code <./tutorials/code/CSS%20code%20tutorial.ipynb>`_
- `Hypergraph Product Code <./tutorials/code/Hypergraph%20Product%20Code%20tutorial.ipynb>`_
- `Lifted Product Code <./tutorials/code/Lifted%20Product%20Code%20tutorial.ipynb>`_
- `Stabilizer Code <./tutorials/code/Stabilizer%20Code%20tutorial.ipynb>`_

Error Correction Decoders
~~~~~~~~~~~~~~~~~~~~~~~~~

- `Belief Propagation Decoder <./tutorials/decoder/belief_propagation_demo.ipynb>`_
- `PyMatching Decoder <./tutorials/decoder/pymatching_decoder_demo.ipynb>`_
