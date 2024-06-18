# QRLab

QRLab is a MATLAB toolbox for exploring quantum information processing and quantum resource theory.


## Features
- **Entanglement Theory**: 

 -- *Static Entanglement Measure*: Tempered Logarithmic Negativity $E_{
tau}$, Rains Bound $R$, MaxRainsEntropy $R_{
max}$, Logarithmic Negativity $E_{N}$, $E_{
mathrm{PPT}}$, $E_
eta$

 -- *Dynamic Entanglement Measure*: Max Logarithmic Negativity, Max Rains information. 

 -- *Quantum Capacity*

- **Coherence Theory**: 

 -- *Static Coherence Measure*: Robustness of Coherence 

 -- *Channel Simulation*: Simulating non-free operations via resource states.

- **Magic Theory**: 

 -- *Static Magic Measure*: Robustness of Magic (qubit), Magic Mana (qudit), max/min Thuama (qudit) 

 -- *Representative Magic State Generation*


- **Quasi-Theory**: 

 -- Probabilistic error cancelation 

 -- Observable dependent probabilistic error cancellation 

 -- Observable dependent deterministic error cancelation 

 -- Circuit Knitting 

 -- Virtual Recovery

- **Supermap**: 
 -- Quantum Switch (both kraus and choi), Apply Quantum Switch
 -- Link Product

- **Seesaw Algorithms**: Algorithms for providing sub-optimal solutions for non-linear optimization problems. 

 -- CHSH game 

 -- LOCC protocol

- **Extra Functions - Quantum Information Processing**: 

 -- Conditional quantum mutual information 

 -- Virtual Markovian State

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