# QRLab

**QRLab** is a MATLAB toolbox for exploring quantum information processing and quantum resource theory.


## Features
- **Entanglement Theory**: 

    - *Static Entanglement Measure*: Tempered Logarithmic Negativity $E_{
\mathrm{\tau}}$, Rains Bound $R$, MaxRainsEntropy $R_{
\mathrm{max}}$, Logarithmic Negativity $E_\text{N}$, $E_{
\mathrm{PPT}}$, $E_
\mathrm{eta}$

    - *Dynamic Entanglement Measure*: Max Logarithmic Negativity, Max Rains information. 

    - *Quantum Capacity*

- **Coherence Theory**: 

    - *Static Coherence Measure*: Robustness of Coherence 

    - *Channel Simulation*: Simulating non-free operations via resource states.

- **Magic Theory**: 

    - *Static Magic Measure*: Robustness of Magic (qubit), Magic Mana (qudit), max/min Thuama (qudit) 

    - *Representative Magic State Generation*


- **Quasi-Theory**: 

    - Probabilistic error cancelation 

    - Observable dependent probabilistic error cancellation 

    - Observable dependent deterministic error cancelation 

    - Circuit Knitting 

    - Virtual Recovery

- **Supermap**: 
    - Quantum Switch (both kraus and choi), Apply Quantum Switch
    - Link Product

- **Seesaw Algorithms**: Algorithms for providing sub-optimal solutions for non-linear optimization problems. 

    - CHSH game 

    - LOCC protocol

- **Extra Functions - Quantum Information Processing**: 

    - Conditional quantum mutual information 

    - Virtual Markovian State

## Requirements
1. QETLAB == 0.9
2. CVX == 2.1


## Installation
1. Clone QRLab to your local machine.
2. Download QETLAB 0.9. You could download it from https://qetlab.com/.
3. Add QRLab and QETLAB to MATLAB's path​, through command
```matlab
addpath(genpath('...\QETLAB-0.9'));
addpath(genpath('...\QRlab'));
```
4. Download and install CVX 2.1. You could download it from https://cvxr.com/cvx/.
Install CVX on Windows
```matlab
cd yourpath\cvx;​
cvx_setup;
```
Install CVX on Linux or a Mac
```matlab
cd ~/MATLAB/cvx;​
cvx_setup;
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
