Because I will never stop being lacking when it comes to math.
# Differential equations
## Basic concepts
### Definitions
Differential equation
> Any equation which contains any kind of derivatives. As a familiar example newtons second law of motion F=ma, since a = dv/dt = d2s/dt2. A good thing to know about since they can describe incredibly many physical phenomena.

Order of a differential equation
> The highest derivative present in the equation

Ordinary differential equation (ODE)
> A differential equation without partial derivatives, there is only one independent variable.

Partial differential equation (PDE)
> A differential equation with partial derivatives, there are more than one independent variable.

Linear differential equation
> The sum of derivatives of a function. No term is multiplied with any other term (it is a linear sum), no term occurs to any power other than one (all the terms are linear). The coefficients for each term are allowed to be both non-linear and arbritrary values, the import thing is that the differentiated function remains linear.

> It is all differential equations that can be written on the form: **g(x) = f(x)a0 + f'(x)a1 + f''(x)a2 +... f''...'an**

Initial condition(s)
> A set of conditions that will decide what form the final solution takes. is written on the form of what values we want the function to take at certain points of differentatiation. For example, at t = 0 f(y) = a0, at t = n f'''n(y) = (a1)

Initial value problem
> A differentiation problem where the initial conditions are provided.

Interval of validity
> The largest interval on which the solution is valid and contains the initial conditions(??)

General solution
> The most general form a solution to a differential equation can take, not imposing any initial conditions

Actual solution
> A solution that adheres to the imposed initial conditions

Explicit solution
> A solution where y appears only once on the left side, raised to the first power

Implicit solution
> A solution that is not explicit. Fantastic

Modeling
> To describe a physical phenomena via differential equations

## First order differential equations
### Linear equations


## Integrate

### Setup
A neural membrane is a good insultor

Injecting current (I) into a neuron will thuse charge the membrane rather than go anywhere else - the membrane acts like a capacitor with capacity (C).

Since the membrane isn't a perfect insulator, the charge will slowly leak out. The membrane has a finite resistance (R).

Due to biology the cell also has a baseline membrane potential (u*rest*)

We can thus look at a neuronal membrane as a electric circuit consisting of one capacitor (the ability to store charge) and one resistor (determining how much is let through, with one battery (the rest membrane potential) providing the baseline potential.

### Injecting current
* I = Ir + Ic
 The injected current will pass either through the resistor or the capacitor.
* Ir = ur/R
* ur = u - urest
 Per ohms law the current across the resistor is the voltage over the resistance of the resistor. The voltage across it (ur) is simply the difference in potential.
* Ic = dq/dt
* C = q/u
* Ic = Cdu/dt
 The current across the capacitor = charge over time. The charge = the capacitance/the voltage.

Given that we now have that
* I = (u-urest)/R + Cdu/dt
Multiplying with R yields the standard form, AKA the equation of the passive membrane. The RC product is said to be 𝜏 AKA the time constant

