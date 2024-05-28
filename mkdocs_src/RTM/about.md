# MPQQ

MPQQ: Matlab Package for Quantum Information Processing and Quantum Resource Theory is a MATLAB toolbox for exploring quantum resource theory.


## Features
- **Resource Measure**: Functions to calculate the amount of resource for the given state/channel within entanglement, coherence and magic theories.
 -- Tempered Logarithmic Negativity (Ent)\
 -- Rains Bound (Ent)\
 -- MaxRainsEntropy (Ent)\
 -- Logarithmic Negativity (Ent)\
 -- EPPT (Ent)\
 -- Eeta (Ent)\
 -- Robustness Coherence (Coh)\
 -- Magic Mana (Magic)

- **Channel Simulation**: Capabilities to simulate quantum channels within different resource theories.
 -- 

- **Error Mitigation**: Tools to compute the optimal probablistic error cancellation protocols for a given noisy channel.
 -- Without Observable\
 -- Given Observable\
 -- Observable Shift

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



## Contributing

Contributions to expand and improve this package are welcome. Please fork the repository, make your changes, and submit a pull request.