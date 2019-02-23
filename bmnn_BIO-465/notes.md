# TODO
Vid 1, 2, 3, 4, 5
Ch1
Ch5
Exercises
Python
# Lecture 1 Overview
## Differential Equations
## 1.1 Neurons and Synapses:
### Structures and terminology
* Dendrite: The input channel for the soma, a set of threads connected via synapses to other neurons axons. Carries signals to the soma.
* Synapses: The contact points between neurons  
* Soma: The cell body. Signals from the dendrides are integrated here, and if their sum surpass a certain threshold, the neuron "fires"
* Axon: The output channel for the soma, along which signals are sent along to other neurons dendrites.
* Signal: AKA action potential AKA spike. In essence an electric pulse lasting a few milliseconds with an amplitude around 100mV
* Presynaptic neuron: A neuron that sends a pulse
* Postsynaptic neuron: A neuron that receives a pulse
* Postsynaptic potential: the potential of the receiving neuron when integrating the effects of all the pulses it receives.
* Threshold: the value the postsynaptic potential must reach in order for the postsynaptic neuron to fire.
* Receptive field: The area of stimulus that a neuron can react to. This can be both an inhibition and excitation. 
* On size: There are around 10 000 neurons with a total length of 3000 m per mm^3
### Genreation of the action potential
The neuron, much like any other cell, has a cell membrane.

The cell membrane has pores which can open and close.

When the pores are open ions - which carry an electrical charge - can flow in and out.

The models for this process are known as Hodgkin-Huxley type models, and will be described in mored detail next week.

### Integrate-and-Fire model
A simple model for describing how a neuron functions, abstracting away the underlying biophysical principles that control function.
* Spikes are events
* Events are triggered at the threshold 
* After the event, the neuron enters a period of absolute refraction when no events can happen.

## 1.2 The Passive Membrane
Haha, my god. I lack so much prerequisites for this course. 
Better now than ever I suppose!

### One-dimensional linear differential equation primer

### Electricity primer
* Linear circuit: A circuit in which all parameters such as resistance and capacitance are constant - they don't change when voltage or current change.
* Voltage (V): The difference in electric potential between two points. Much like how water moves from an area of high pressure to an area of lower pressure, electricty moves from areas with high electrical potential to areas with low electric potential. The bigger the difference the bigger the flow.
* Current(I): How much electricty is flowing through the circuit. Higher voltage => higher current.
* Resistors: Anything that resists the flow/current. Anything that stops the electrons from moving along the circuit.
* Capacitors: Anything that stores charge in a circuit. Can thus be used as a temporary battery. Can deliver energy faster than batteries
#### RC-circuit primer
A circuit consisting of a Resistor and a Capacitor.

In this case the capacitor C will discharge its stored energe through the resistor. The voltage across the capacitor can be found using Kirchofs current law, since the current leaving the capacitor must equal the current entering the resistor.
> Kirchhoff's current law (KCL): The sum of current out from a node = the sum of current in to a node

This yields the equation

C * dV / dt + V / R = 0

Solving for V yields the formula for exponential decay

V(t) = V0e^(-t/RC)

where V0 = capacitor voltage at t = 0

The time for the voltage to fall to V0/e is called the RC time constant and is equal to 

tau = RC


### Signal primer
* Impulse-response function: The output of a system when presented with a brief signal/pulse. Or more generally, the response of a dynamic system to any external change.       
* Dirac delta-function
### 1.3 Leaky Integrate-and-Fire Model
### 1.4 Generalized Integrate-and-Fire Model
### 1.5. Quality of Integrate-and-Fire Models
### RC-circuit
A circuit with a resistor and a capacitor

# Lecture 2
# Lecture 3
# Lecture 4
# Lecture 5
# Lecture 6
# Lecture 7
# Lecture 8
