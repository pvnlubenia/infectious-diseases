# Agent-based models of spread of infectious diseases using Python

The models presented are based on the SIR (susceptible-infectious-recovered) and the SEIR (susceptible-exposed--infectious-recovered) frameworks. In the models, behavior of the agents are not governed by any set of ordinary differential equations. The purpose of these models is to demonstrate that simply describing the behavior of individuals naturally creates the trends governed by equations for the SIR and the SEIR frameworks.

The models use basic Python libraries, and the codes can be run on their own.

## SIR Model

In the SIR model, agents belong to one of three states: susceptible, infectious, or recovered. Infectious agents spend a length of time (recovery period) in the state before becoming recovered. Furthermore, they can infect people within a defined neighborhood. Two scenarios are presented for the behavior of individual agents: 1) everyone moves randomly regardless of their state; 2) infectious agents do not move. The modeling activity shows that it is easy to modify the parameters of the model, e.g, by changing the description of how agents behave.

## SEIR Model

The SEIR model is similar to the SIR model but with the additional exposed state where an agent is already infected but not yet infectious. Exposed agents spend a length of time (incubation period) in the state before becoming infectious. The modeling activity shows that it is easy to incorporate modifications to the model, and this can be done even by logic. It may be a little bit more involved in terms of programming, but the process is more "natural" compared to modeling frameworks working with equations.
