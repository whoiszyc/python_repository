# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:58:35 2018

@author: yichen.zhang

The data format discreption is copied from the matpwoer manual chapter "Appendix Data File Format".
Refer to the manual for more details.

Table B-1: Bus Data (mpc.bus)

BUS I       1 bus number (positive integer)
BUS TYPE    2 bus type (1 = PQ, 2 = PV, 3 = ref, 4 = isolated)
PD          3 real power demand (MW)
QD          4 reactive power demand (MVAr)
GS          5 shunt conductance (MW demanded at V = 1.0 p.u.)
BS          6 shunt susceptance (MVAr injected at V = 1.0 p.u.)
BUS AREA    7 area number (positive integer)
VM          8 voltage magnitude (p.u.)
VA          9 voltage angle (degrees)
BASE KV     10 base voltage (kV)
ZONE        11 loss zone (positive integer)
VMAX        12 maximum voltage magnitude (p.u.)
VMIN        13 minimum voltage magnitude (p.u.)
LAM P†      14 Lagrange multiplier on real power mismatch (u/MW)
LAM Q†      15 Lagrange multiplier on reactive power mismatch (u/MVAr)
MU VMAX†    16 Kuhn-Tucker multiplier on upper voltage limit (u/p.u.)
MU VMIN†    17 Kuhn-Tucker multiplier on lower voltage limit (u/p.u.)




Table B-2: Generator Data (mpc.gen)

GEN BUS     1 bus number
PG          2 real power output (MW)
QG          3 reactive power output (MVAr)
QMAX        4 maximum reactive power output (MVAr)
QMIN        5 minimum reactive power output (MVAr)
VG‡         6 voltage magnitude setpoint (p.u.)
MBASE       7 total MVA base of machine, defaults to baseMVA
GEN STATUS  8 machine status, > 0 = machine in-service ≤ 0 = machine out-of-service
PMAX        9 maximum real power output (MW)
PMIN        10 minimum real power output (MW)
PC1*        11 lower real power output of PQ capability curve (MW)
PC2*        12 upper real power output of PQ capability curve (MW)
QC1MIN*     13 minimum reactive power output at PC1 (MVAr)
QC1MAX*     14 maximum reactive power output at PC1 (MVAr)
QC2MIN*     15 minimum reactive power output at PC2 (MVAr)
QC2MAX*     16 maximum reactive power output at PC2 (MVAr)
RAMP AGC*   17 ramp rate for load following/AGC (MW/min)
RAMP 10*    18 ramp rate for 10 minute reserves (MW)
RAMP 30*    19 ramp rate for 30 minute reserves (MW)
RAMP Q*     20 ramp rate for reactive power (2 sec timescale) (MVAr/min)
APF*        21 area participation factor
MU PMAX†    22 Kuhn-Tucker multiplier on upper Pg limit (u/MW)
MU PMIN†    23 Kuhn-Tucker multiplier on lower Pg limit (u/MW)
MU QMAX†    24 Kuhn-Tucker multiplier on upper Qg limit (u/MVAr)
MU QMIN†    25 Kuhn-Tucker multiplier on lower Qg limit (u/MVAr)


Table B-3: Branch Data (mpc.branch)

F BUS       1 \from" bus number
T BUS       2 \to" bus number
BR R        3 resistance (p.u.)
BR X        4 reactance (p.u.)
BR B        5 total line charging susceptance (p.u.)
RATE A      6 MVA rating A (long term rating), set to 0 for unlimited
RATE B      7 MVA rating B (short term rating), set to 0 for unlimited
RATE C      8 MVA rating C (emergency rating), set to 0 for unlimited
TAP         9 transformer off nominal turns ratio, (taps at \from" bus, impedance at \to" bus, i.e. if r = x = b = 0, tap = jjVVftjj)
SHIFT       10 transformer phase shift angle (degrees), positive ) delay
BR STATUS   11 initial branch status, 1 = in-service, 0 = out-of-service
ANGMIN*     12 minimum angle difference, θf − θt (degrees)
ANGMAX*     13 maximum angle difference, θf − θt (degrees)
PF†         14 real power injected at \from" bus end (MW)
QF†         15 reactive power injected at \from" bus end (MVAr)
PT†         16 real power injected at \to" bus end (MW)
QT†         17 reactive power injected at \to" bus end (MVAr)
MU SF‡      18 Kuhn-Tucker multiplier on MVA limit at \from" bus (u/MVA)
MU ST‡      19 Kuhn-Tucker multiplier on MVA limit at \to" bus (u/MVA)
MU ANGMIN‡  20 Kuhn-Tucker multiplier lower angle difference limit (u/degree)
MU ANGMAX‡  21 Kuhn-Tucker multiplier upper angle difference limit (u/degree)


Table B-4: Generator Cost Data† (mpc.gencost)

MODEL       1 cost model, 1 = piecewise linear, 2 = polynomial
STARTUP     2 startup cost in US dollars*
SHUTDOWN    3 shutdown cost in US dollars*
NCOST       4 number of cost coefficients for polynomial cost function, or number of data points for piecewise linear
COST        5 parameters defining total cost function f(p) begin in this column, units of f and p are $/hr and MW (or MVAr), respectively
(MODEL = 1) ) p0; f0; p1; f1; : : : ; pn; fn where p0 < p1 < · · · < pn and the cost f(p) is defined by
the coordinates (p0; f0), (p1; f1), . . . , (pn; fn)
of the end/break-points of the piecewise linear cost
(MODEL = 2) ) cn; : : : ; c1; c0
n + 1 coefficients of n-th order polynomial cost, starting with
highest order, where cost is f(p) = cnpn + · · · + c1p + c0


Table B-5: DC Line Data* (mpc.dcline)

F BUS       1 \from" bus number
T BUS       2 \to" bus number
BR STATUS   3 initial branch status, 1 = in-service, 0 = out-of-service
PF†         4 real power flow at \from" bus end (MW), \from" ! \to"
PT†         5 real power flow at \to" bus end (MW), \from" ! \to"
QF†         6 reactive power injected into \from" bus (MVAr)
QT†         7 reactive power injected into \to" bus (MVAr)
VF          8 voltage magnitude setpoint at \from" bus (p.u.)
VT          9 voltage magnitude setpoint at \to" bus (p.u.)
PMIN        10 if positive (negative), lower limit on PF (PT)
PMAX        11 if positive (negative), upper limit on PF (PT)
QMINF       12 lower limit on reactive power injection into \from" bus (MVAr)
QMAXF       13 upper limit on reactive power injection into \from" bus (MVAr)
QMINT       14 lower limit on reactive power injection into \to" bus (MVAr)
QMAXT       15 upper limit on reactive power injection into \to" bus (MVAr)
LOSS0       16 coefficient l0 of constant term of linear loss function (MW)
LOSS1       17 coefficient l1 of linear term of linear loss function (MW/MW)
(ploss = l0 + l1pf, where pf is the flow at the \from" end)
MU PMIN‡    18 Kuhn-Tucker multiplier on lower flow limit at \from" bus (u/MW)
MU PMAX‡    19 Kuhn-Tucker multiplier on upper flow limit at \from" bus (u/MW)
MU QMINF‡   20 Kuhn-Tucker multiplier on lower VAr limit at \from" bus (u/MVAr)
MU QMAXF‡   21 Kuhn-Tucker multiplier on upper VAr limit at \from" bus (u/MVAr)
MU QMINT‡   22 Kuhn-Tucker multiplier on lower VAr limit at \to" bus (u/MVAr)
MU QMAXT‡   23 Kuhn-Tucker multiplier on upper VAr limit at \to" bus (u/MVAr)

"""

# Copyright (c) 1996-2015 PSERC. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Power flow data for 39 bus New England system.
"""

from numpy import array

def case39():
    """Power flow data for 39 bus New England system.
    Please see L{caseformat} for details on the case file format.

    Data taken from [1] with the following modifications/additions:

        - renumbered gen buses consecutively (as in [2] and [4])
        - added C{Pmin = 0} for all gens
        - added C{Qmin}, C{Qmax} for gens at 31 & 39 (copied from gen at 35)
        - added C{Vg} based on C{V} in bus data (missing for bus 39)
        - added C{Vg, Pg, Pd, Qd} at bus 39 from [2] (same in [4])
        - added C{Pmax} at bus 39: C{Pmax = Pg + 100}
        - added line flow limits and area data from [4]
        - added voltage limits, C{Vmax = 1.06, Vmin = 0.94}
        - added identical quadratic generator costs
        - increased C{Pmax} for gen at bus 34 from 308 to 508
          (assumed typo in [1], makes initial solved case feasible)
        - re-solved power flow

    Notes:
        - Bus 39, its generator and 2 connecting lines were added
          (by authors of [1]) to represent the interconnection with
          the rest of the eastern interconnect, and did not include
          C{Vg, Pg, Qg, Pd, Qd, Pmin, Pmax, Qmin} or C{Qmax}.
        - As the swing bus, bus 31 did not include and Q limits.
        - The voltages, etc in [1] appear to be quite close to the
          power flow solution of the case before adding bus 39 with
          it's generator and connecting branches, though the solution
          is not exact.
        - Explicit voltage setpoints for gen buses are not given, so
          they are taken from the bus data, however this results in two
          binding Q limits at buses 34 & 37, so the corresponding
          voltages have probably deviated from their original setpoints.
        - The generator locations and types are as follows:
            - 1   30      hydro
            - 2   31      nuke01
            - 3   32      nuke02
            - 4   33      fossil02
            - 5   34      fossil01
            - 6   35      nuke03
            - 7   36      fossil04
            - 8   37      nuke04
            - 9   38      nuke05
            - 10  39      interconnection to rest of US/Canada

    This is a solved power flow case, but it includes the following
    violations:
        - C{Pmax} violated at bus 31: C{Pg = 677.87, Pmax = 646}
        - C{Qmin} violated at bus 37: C{Qg = -1.37,  Qmin = 0}

    References:

    [1] G. W. Bills, et.al., I{"On-Line Stability Analysis Study"}
    RP90-1 Report for the Edison Electric Institute, October 12, 1970,
    pp. 1-20 - 1-35.
    prepared by
      - E. M. Gulachenski - New England Electric System
      - J. M. Undrill     - General Electric Co.
    "...generally representative of the New England 345 KV system, but is
    not an exact or complete model of any past, present or projected
    configuration of the actual New England 345 KV system."

    [2] M. A. Pai, I{Energy Function Analysis for Power System Stability},
    Kluwer Academic Publishers, Boston, 1989.
    (references [3] as source of data)

    [3] Athay, T.; Podmore, R.; Virmani, S., I{"A Practical Method for the
    Direct Analysis of Transient Stability,"} IEEE Transactions on Power
    Apparatus and Systems , vol.PAS-98, no.2, pp.573-584, March 1979.
    U{http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4113518&isnumber=4113486}
    (references [1] as source of data)

    [4] Data included with TC Calculator at
    U{http://www.pserc.cornell.edu/tcc/} for 39-bus system.

    @return: Power flow data for 39 bus New England system.
    """
    ppc = {"version": '2'}

    ##-----  Power Flow Data  -----##
    ## system MVA base
    ppc["baseMVA"] = 100.0
    
    # (ZYC@09-30-2018) system base
    ppc["baseKV"]=345

    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([
        [1, 1, 97.6, 44.2, 0, 0, 2, 1.0393836, -13.536602, 345, 1, 1.06, 0.94],
        [2, 1, 0, 0, 0, 0, 2, 1.0484941, -9.7852666, 345, 1, 1.06, 0.94],
        [3, 1, 322, 2.4, 0, 0, 2, 1.0307077, -12.276384, 345, 1, 1.06, 0.94],
        [4, 1, 500, 184, 0, 0, 1, 1.00446, -12.626734, 345, 1, 1.06, 0.94],
        [5, 1, 0, 0, 0, 0, 1, 1.0060063, -11.192339, 345, 1, 1.06, 0.94],
        [6, 1, 0, 0, 0, 0, 1, 1.0082256, -10.40833, 345, 1, 1.06, 0.94],
        [7, 1, 233.8, 84, 0, 0, 1, 0.99839728, -12.755626, 345, 1, 1.06, 0.94],
        [8, 1, 522, 176.6, 0, 0, 1, 0.99787232, -13.335844, 345, 1, 1.06, 0.94],
        [9, 1, 6.5, -66.6, 0, 0, 1, 1.038332, -14.178442, 345, 1, 1.06, 0.94],
        [10, 1, 0, 0, 0, 0, 1, 1.0178431, -8.170875, 345, 1, 1.06, 0.94],
        [11, 1, 0, 0, 0, 0, 1, 1.0133858, -8.9369663, 345, 1, 1.06, 0.94],
        [12, 1, 8.53, 88, 0, 0, 1, 1.000815, -8.9988236, 345, 1, 1.06, 0.94],
        [13, 1, 0, 0, 0, 0, 1, 1.014923, -8.9299272, 345, 1, 1.06, 0.94],
        [14, 1, 0, 0, 0, 0, 1, 1.012319, -10.715295, 345, 1, 1.06, 0.94],
        [15, 1, 320, 153, 0, 0, 3, 1.0161854, -11.345399, 345, 1, 1.06, 0.94],
        [16, 1, 329, 32.3, 0, 0, 3, 1.0325203, -10.033348, 345, 1, 1.06, 0.94],
        [17, 1, 0, 0, 0, 0, 2, 1.0342365, -11.116436, 345, 1, 1.06, 0.94],
        [18, 1, 158, 30, 0, 0, 2, 1.0315726, -11.986168, 345, 1, 1.06, 0.94],
        [19, 1, 0, 0, 0, 0, 3, 1.0501068, -5.4100729, 345, 1, 1.06, 0.94],
        [20, 1, 680, 103, 0, 0, 3, 0.99101054, -6.8211783, 345, 1, 1.06, 0.94],
        [21, 1, 274, 115, 0, 0, 3, 1.0323192, -7.6287461, 345, 1, 1.06, 0.94],
        [22, 1, 0, 0, 0, 0, 3, 1.0501427, -3.1831199, 345, 1, 1.06, 0.94],
        [23, 1, 247.5, 84.6, 0, 0, 3, 1.0451451, -3.3812763, 345, 1, 1.06, 0.94],
        [24, 1, 308.6, -92.2, 0, 0, 3, 1.038001, -9.9137585, 345, 1, 1.06, 0.94],
        [25, 1, 224, 47.2, 0, 0, 2, 1.0576827, -8.3692354, 345, 1, 1.06, 0.94],
        [26, 1, 139, 17, 0, 0, 2, 1.0525613, -9.4387696, 345, 1, 1.06, 0.94],
        [27, 1, 281, 75.5, 0, 0, 2, 1.0383449, -11.362152, 345, 1, 1.06, 0.94],
        [28, 1, 206, 27.6, 0, 0, 3, 1.0503737, -5.9283592, 345, 1, 1.06, 0.94],
        [29, 1, 283.5, 26.9, 0, 0, 3, 1.0501149, -3.1698741, 345, 1, 1.06, 0.94],
        [30, 2, 0, 0, 0, 0, 2, 1.0499, -7.3704746, 345, 1, 1.06, 0.94],
        [31, 3, 9.2, 4.6, 0, 0, 1, 0.982, 0, 345, 1, 1.06, 0.94],
        [32, 2, 0, 0, 0, 0, 1, 0.9841, -0.1884374, 345, 1, 1.06, 0.94],
        [33, 2, 0, 0, 0, 0, 3, 0.9972, -0.19317445, 345, 1, 1.06, 0.94],
        [34, 2, 0, 0, 0, 0, 3, 1.0123, -1.631119, 345, 1, 1.06, 0.94],
        [35, 2, 0, 0, 0, 0, 3, 1.0494, 1.7765069, 345, 1, 1.06, 0.94],
        [36, 2, 0, 0, 0, 0, 3, 1.0636, 4.4684374, 345, 1, 1.06, 0.94],
        [37, 2, 0, 0, 0, 0, 2, 1.0275, -1.5828988, 345, 1, 1.06, 0.94],
        [38, 2, 0, 0, 0, 0, 3, 1.0265, 3.8928177, 345, 1, 1.06, 0.94],
        [39, 2, 1104, 250, 0, 0, 1, 1.03, -14.535256, 345, 1, 1.06, 0.94]
    ])

    
    """
    (ZYC@09-30-2018) Generator maximum output is modified
    """
    ## generator data 
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    # ppc["gen"] = array([
    #     #                                                                   Pmax    Pmin
    #     [30, 250,       161.762,    400,    140,    1.0499,     100,    1,  1540,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [31, 678,       221.574,    300,    -100,   0.982,      100,    1,  1700,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [32, 650,       206.965,    300,    150,    0.9841,     100,    1,  1750,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [33, 632,       108.293,    250,    0,      0.9972,     100,    1,  1900,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [34, 508,       166.688,    167,    0,      1.0123,     100,    1,  1850,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [35, 650,       210.661,    300,    -100,   1.0494,     100,    1,  1950,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [36, 560,       100.165,    240,    0,      1.0636,     100,    1,  1880,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [37, 540,       -1.36945,   250,    0,      1.0275,     100,    1,  1800,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [38, 830,       21.7327,    300,    -150,   1.0265,     100,    1,  2100,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [39, 1000,      78.4674,    300,    -100,   1.03,       100,    1,  2300,   500,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ])

    """
    Customized generator data by ZYC@10-29-2018
    """
    ppc["gen"] = array([
    #  index    Pmin        Pmax        Rmax        RU      RD      cost_reserve        cost_startup        minimum up      minimum down
    [30,        500,        1540,       1000,       300,    400,        5,              1000,                   1,              1],
    [31,        500,        1700,       1000,       300,    400,        5,              1000,                   5,              1],
    [32,        500,        1750,       1000,       300,    400,        5,              1000,                   1,              1],
    [33,        500,        1900,       1000,       300,    400,        5,              1000,                   1,              1],
    [34,        500,        1850,       1000,       300,    400,        5,              1000,                   1,              1],
    [35,        500,        1950,       1000,       300,    400,        5,              1000,                   1,              1],
    [36,        500,        1880,       1000,       300,    400,        5,              1000,                   1,              1],
    [37,        500,        1800,       1000,       300,    400,        5,              1000,                   1,              1],
    [38,        500,        2100,       1000,       300,    400,        5,              1000,                   1,              1],
    [39,        500,        2300,       1000,       300,    400,        5,              1000,                   1,              1],
    ])

    ## branch data
    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    ppc["branch"] = array([
        [1, 2, 0.0035, 0.0411, 0.6987, 600, 600, 600, 0, 0, 1, -360, 360],
        [1, 39, 0.001, 0.025, 0.75, 1000, 1000, 1000, 0, 0, 1, -360, 360],
        [2, 3, 0.0013, 0.0151, 0.2572, 500, 500, 500, 0, 0, 1, -360, 360],
        [2, 25, 0.007, 0.0086, 0.146, 500, 500, 500, 0, 0, 1, -360, 360],
        [2, 30, 0, 0.0181, 0, 900, 900, 2500, 1.025, 0, 1, -360, 360],
        [3, 4, 0.0013, 0.0213, 0.2214, 500, 500, 500, 0, 0, 1, -360, 360],
        [3, 18, 0.0011, 0.0133, 0.2138, 500, 500, 500, 0, 0, 1, -360, 360],
        [4, 5, 0.0008, 0.0128, 0.1342, 600, 600, 600, 0, 0, 1, -360, 360],
        [4, 14, 0.0008, 0.0129, 0.1382, 500, 500, 500, 0, 0, 1, -360, 360],
        [5, 6, 0.0002, 0.0026, 0.0434, 1200, 1200, 1200, 0, 0, 1, -360, 360],
        [5, 8, 0.0008, 0.0112, 0.1476, 900, 900, 900, 0, 0, 1, -360, 360],
        [6, 7, 0.0006, 0.0092, 0.113, 900, 900, 900, 0, 0, 1, -360, 360],
        [6, 11, 0.0007, 0.0082, 0.1389, 480, 480, 480, 0, 0, 1, -360, 360],
        [6, 31, 0, 0.025, 0, 1800, 1800, 1800, 1.07, 0, 1, -360, 360],
        [7, 8, 0.0004, 0.0046, 0.078, 900, 900, 900, 0, 0, 1, -360, 360],
        [8, 9, 0.0023, 0.0363, 0.3804, 900, 900, 900, 0, 0, 1, -360, 360],
        [9, 39, 0.001, 0.025, 1.2, 900, 900, 900, 0, 0, 1, -360, 360],
        [10, 11, 0.0004, 0.0043, 0.0729, 600, 600, 600, 0, 0, 1, -360, 360],
        [10, 13, 0.0004, 0.0043, 0.0729, 600, 600, 600, 0, 0, 1, -360, 360],
        [10, 32, 0, 0.02, 0, 900, 900, 2500, 1.07, 0, 1, -360, 360],
        [12, 11, 0.0016, 0.0435, 0, 500, 500, 500, 1.006, 0, 1, -360, 360],
        [12, 13, 0.0016, 0.0435, 0, 500, 500, 500, 1.006, 0, 1, -360, 360],
        [13, 14, 0.0009, 0.0101, 0.1723, 600, 600, 600, 0, 0, 1, -360, 360],
        [14, 15, 0.0018, 0.0217, 0.366, 600, 600, 600, 0, 0, 1, -360, 360],
        [15, 16, 0.0009, 0.0094, 0.171, 600, 600, 600, 0, 0, 1, -360, 360],
        [16, 17, 0.0007, 0.0089, 0.1342, 600, 600, 600, 0, 0, 1, -360, 360],
        [16, 19, 0.0016, 0.0195, 0.304, 600, 600, 2500, 0, 0, 1, -360, 360],
        [16, 21, 0.0008, 0.0135, 0.2548, 600, 600, 600, 0, 0, 1, -360, 360],
        [16, 24, 0.0003, 0.0059, 0.068, 600, 600, 600, 0, 0, 1, -360, 360],
        [17, 18, 0.0007, 0.0082, 0.1319, 600, 600, 600, 0, 0, 1, -360, 360],
        [17, 27, 0.0013, 0.0173, 0.3216, 600, 600, 600, 0, 0, 1, -360, 360],
        [19, 20, 0.0007, 0.0138, 0, 900, 900, 2500, 1.06, 0, 1, -360, 360],
        [19, 33, 0.0007, 0.0142, 0, 900, 900, 2500, 1.07, 0, 1, -360, 360],
        [20, 34, 0.0009, 0.018, 0, 900, 900, 2500, 1.009, 0, 1, -360, 360],
        [21, 22, 0.0008, 0.014, 0.2565, 900, 900, 900, 0, 0, 1, -360, 360],
        [22, 23, 0.0006, 0.0096, 0.1846, 600, 600, 600, 0, 0, 1, -360, 360],
        [22, 35, 0, 0.0143, 0, 900, 900, 2500, 1.025, 0, 1, -360, 360],
        [23, 24, 0.0022, 0.035, 0.361, 600, 600, 600, 0, 0, 1, -360, 360],
        [23, 36, 0.0005, 0.0272, 0, 900, 900, 2500, 1, 0, 1, -360, 360],
        [25, 26, 0.0032, 0.0323, 0.531, 600, 600, 600, 0, 0, 1, -360, 360],
        [25, 37, 0.0006, 0.0232, 0, 900, 900, 2500, 1.025, 0, 1, -360, 360],
        [26, 27, 0.0014, 0.0147, 0.2396, 600, 600, 600, 0, 0, 1, -360, 360],
        [26, 28, 0.0043, 0.0474, 0.7802, 600, 600, 600, 0, 0, 1, -360, 360],
        [26, 29, 0.0057, 0.0625, 1.029, 600, 600, 600, 0, 0, 1, -360, 360],
        [28, 29, 0.0014, 0.0151, 0.249, 600, 600, 600, 0, 0, 1, -360, 360],
        [29, 38, 0.0008, 0.0156, 0, 1200, 1200, 2500, 1.025, 0, 1, -360, 360]
    ])

    ##-----  OPF Data  -----##
    # Polynomial generator cost
    # bus, a, b, c
    ppc["gencost"] = array([
        [30,    0.02533,    25.5472,    24.3891],  # A
        [31,    0.02649,    25.6753,    24.4100],  # A
        [32,    0.01199,    37.5510,    117.7551], # B
        [33,    0.00876,    13.3272,    81.1364],  # C
        [34,    0.00623,    18.1000,    217.8952], # D
        [35,    0.00463,    10.6940,    142.7348], # E
        [36,    0.00259,    23.0000,    259.1310], # F
        [37,    0.00153,    10.8616,    177.0575], # G
        [38,    0.00158,    11.1874,    182.3692], # G
        [39,    0.00194,    7.4921,     310.0021]  # H
    ])

    return ppc
