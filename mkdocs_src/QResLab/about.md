# QResLab

Quantum Resource Theory Matlab Package (QResLab) is a MATLAB toolbox for exploring quantum resource theory.


## Features
- **Resource Measure**: Functions to calculate the amount of resource for the given state/channel within entanglement, coherence and magic theories.
 -- *Entanglement Measure*: Tempered Logarithmic Negativity $E_{\tau}$, Rains Bound $R$, MaxRainsEntropy $R_{\max}$, Logarithmic Negativity $E_{N}$, $E_{\mathrm{PPT}}$, $E_\eta$\
 -- *Coherence Measure*: Robustness of Coherence\
 -- *Magic Measure*: Robustness of Magic (qubit), Magic Mana (qudit), max/min Thuama (qudit)

- **Channel Simulation**:  Simulating non-free operations via resource states.

- **Error Mitigation**:  Tools to compute the protocol to mitigate quantum errors with minimal sampling overhead. \
 -- Probabilistic error cancelation \
 -- Observable dependent probabilistic error cancellation \
 -- Observable dependent deterministic error cancelation

- **Indefinite Causal Order**: 
 -- Quantum Switch (both kraus and choi), Apply Quantum Switch
 -- Link Product

- **Seesaw Algorithms**: Algorithms for providing sub-optimal solutions for non-linear optimization problems. \
 -- CHSH game \
 -- LOCC protocol \
 -- Circuit Knitting

- **Extra Functions - Quantum Information Processing**: \
 -- Conditional quantum mutual information \
 -- Virtual Markovian State \
 -- Quantum Capacity (degradable)

## Requirements
1. QETLAB == 0.9
2. CVX == 2.1


## Installation
1. Clone this repository to your local machine.
2. Add the package to your MATLAB path:
```matlab
addpath('path_to_package');
```


## Getting Started: Use Cases

To use the package, simply call the function you need with appropriate parameters. For example:

```matlab
% To calculate the robustness of entanglement
rho = [0.5, 0.5; 0.5, 0.5]; % Define a quantum state
robustness = EntanglementRobustness(rho);
disp('Robustness of Entanglement:');
disp(robustness);
```


## More functions are coming.


## Contributing

Contributions to expand and improve this package are welcome.