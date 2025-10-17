# Lotka-Volterra Predator-Prey Model: Foxes and Rabbits

This repository contains an implementation of the Lotka-Volterra equations, a classic model describing predator-prey dynamics, featuring foxes (predators) and rabbits (prey).

## Model Description

The Lotka-Volterra model represents the populations as follows:

- \( x(t) \): Rabbit population (prey)
- \( y(t) \): Fox population (predator)

The dynamics are governed by the following system of differential equations:

\[
\frac{dx}{dt} = \alpha x - \beta x y
\]
\[
\frac{dy}{dt} = \delta x y - \gamma y
\]

where:
- \( \alpha \): Natural growth rate of rabbits (without predation)
- \( \beta \): Rate of predation upon the rabbits
- \( \gamma \): Natural death rate of foxes (in absence of food)
- \( \delta \): Efficiency of turning predated rabbits into new foxes

Key assumptions of the model include unlimited prey food, predator food dependence solely on the prey, constant rate parameters, and no evolution or changes in the environment.

## Biological Interpretation

- The rabbit population increases naturally but decreases due to predation by the foxes.
- The fox population decreases naturally in the absence of prey but increases as they hunt rabbits.
- The interaction between the two species leads to cyclic fluctuations in both populations over time.

## How To Use

1. Configure the initial population sizes and parameter values for rabbits, foxes, and model parameters (\( \alpha, \beta, \gamma, \delta \)).
2. Run the simulation code to observe population changes over time.
3. Visualize results using the provided plotting functions or insert your own analysis.

---

## Plots

<!-- Place your first plot or conceptual diagram here -->
  
![Rabbit and Fox Population vs Time](https://github.com/Ujjalkakati/Lotka_Volterra_Predator_Prey_Model_Simulation/blob/main/Screenshot%202025-10-17%20202209.png?raw=true)

<!-- Place your second plot, for example, a phase plot of Foxes vs Rabbits -->
  
![Phase Plot: Foxes vs Rabbits](https://github.com/Ujjalkakati/Lotka_Volterra_Predator_Prey_Model_Simulation/blob/main/Screenshot%202025-10-17%20202318.png?raw=true)

---

## References

- Lotka–Volterra model overview
- Example applications and simulation resources

