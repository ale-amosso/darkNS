import math
from dictionaries.dict_neutron_star import neutron_star
import quantities as pq

import scipy.constants as const

pi = math.pi
R_star = neutron_star["neutron_star"]["R_star"]  #km
M_star = neutron_star["neutron_star"]["M_star"]  #kg
E_k = 1.0525 * 10 ** 25 * pq.GeV / pq.s  # Joglekar article [A]


def calc_Temp():
    sigma = const.Stefan_Boltzmann * pq.W / pq.m ** 2 / pq.K ** 4
    sigma_rescaled = sigma.rescale(pq.W / pq.km ** 2 / pq.K ** 4)
    watt_to_GeV_o_s = 6241509647.1204 / pq.W / pq.s * pq.GeV
    sigma_GeV = sigma_rescaled * watt_to_GeV_o_s
    print(f"We have{sigma_GeV =}")

    denom = 4 * pi * sigma_GeV * R_star ** 2
    T_4 = E_k / denom
    T = T_4 ** (1 / 4)
    G = (const.G * pq.m ** 3 / pq.kg / pq.s ** 2).rescale(pq.km ** 3 / pq.kg / pq.s ** 2)  # km^3/(kg s^2)
    c = (const.c * pq.m / pq.s).rescale(pq.km / pq.s)  # km/s

    B = 1 - ((2 * G * M_star) / (c ** 2 * R_star))
    T_B = (B ** (1 / 2) * T)

    return T_B
