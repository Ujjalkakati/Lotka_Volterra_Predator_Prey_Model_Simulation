# Lotka-Volterra Predator-Prey Model: Foxes and Rabbits

This repository contains an implementation of the Lotka-Volterra equations, a classic model also known as the predator-prey model are a set of first order non-linear differential equations. The set of equations are useed in studying the dynamics of biological system. There are generally two species, one is the predator and the other is a prey. The equation evolve with time with definite conditions. Consider a system of Foxes and Rabbits in a Jungle and assume that there are no other species in the jungle. 

## Model Description

The Lotka-Volterra model represents the populations as follows:

-x: Rabbit population (prey)
-y: Fox population (predator)

The dynamics are governed by the following system of differential equations:
dx/dt = αx -βxy
dy/dt = -γy + δxy
where:
- α: Natural growth rate of rabbits (without predation)
- β: Rate of predation upon the rabbits
- γ: Natural death rate of foxes (in absence of food)
- δ: Rate at which predator (fox) increase by consuming prey ( rabbit)

Key assumptions of the model include α = 1.5, β = 1, γ = 3, δ = 1. And there are 10 rabbits and 4 foxes initially.

## Biological Interpretation

- The rabbit population increases naturally but decreases due to predation by the foxes.
- The fox population decreases naturally in the absence of prey but increases as they hunt rabbits.
- The interaction between the two species leads to cyclic fluctuations in both populations over time.


---

## Plots
 
![Rabbit and Fox Population vs Time](https://github.com/Ujjalkakati/Lotka_Volterra_Predator_Prey_Model_Simulation/blob/main/Screenshot%202025-10-17%20202209.png?raw=true)

  
![Phase Plot: Foxes vs Rabbits](https://github.com/Ujjalkakati/Lotka_Volterra_Predator_Prey_Model_Simulation/blob/main/Screenshot%202025-10-17%20202318.png?raw=true)

---

## References

- Lotka–Volterra model overview
- Example applications and simulation resources

