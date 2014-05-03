#This script produces the numerical integration for the EoMs
#generated by three_link_pendulum.py

from three_link_pendulum import l, m, M, Ixx, Iyy, Izz, g, kane
from scipy.integrate import odeint
from code_gen import numeric_right_hand_side
from numpy import radians, linspace, hstack, zeros, ones

params = list(l) + list(m) + list(M) + list(Ixx) + list(Iyy) + list(Izz) + [g]

link_length = 10.0  # meters
link_mass = 10.0  # kg
link_radius = 0.5  # meters
link_ixx = 1.0 / 12.0 * link_mass * \
    (3 * link_radius ** 2 + link_length ** 2)
link_iyy = link_mass * link_radius ** 2
link_izz = link_ixx

particle_mass = 5.0  # kg
particle_radius = 1.0  # meters

param_vals = [link_length for x in l] + \
             [particle_mass for x in m] + \
             [link_mass for x in M] + \
             [link_ixx for x in list(Ixx)] + \
             [link_iyy for x in list(Iyy)] + \
             [link_izz for x in list(Izz)] + \
             [9.8]

print("Generating numeric right hand side.")
right_hand_side = numeric_right_hand_side(kane, params)

t = linspace(0.0, 60.0, num=6000)
x0 = hstack((ones(6) * radians(10.0), zeros(6)))

print("Integrating equations of motion.")
states = odeint(right_hand_side, x0, t, args=(param_vals,))
print("Integration done.")