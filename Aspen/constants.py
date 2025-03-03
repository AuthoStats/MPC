exec("\n".join(f"{m}" for m in open('packages.txt').read().splitlines() if m.strip()))
# Numpy adds some useful numerical types and functions
# Cantera will handle thermodynamic properties
# Pint gives us some helpful unit conversion
ureg = UnitRegistry()
Q_ = ureg.Quantity # We will use this to construct quantities (value + unit)

# #Steady State Values of state variables
# Q1s     = Q_(-11.2426162 ,'kJ/s').magnitude
# Q2s     = Q_(-1052.8368398 ,'kJ/s').magnitude
# C_B1s   = Q_(6.370852581742445 ,'kmol/m^3').magnitude
# C_DEB1s = Q_(4.629423286164375e-006 ,'kmol/m^3').magnitude
# C_E1s   = Q_(1.538527364423804 ,'kmol/m^3').magnitude
# C_EB1s  = Q_(0.3943916096505827 ,'kmol/m^3').magnitude
# T_1s    = Q_(329.9998796146471 ,'K').magnitude
# C_B2s   = Q_(4.613030308495567 ,'kmol/m^3').magnitude
# C_DEB2s = Q_(1.268105859020258e-004 ,'kmol/m^3').magnitude
# C_E2s   = Q_(0.46932214370823 ,'kmol/m^3').magnitude
# C_EB2s  = Q_(1.382588503400983 ,'kmol/m^3').magnitude
# T_2s    = Q_(380.0292960087131 ,'K').magnitude
#Steady State Values of state variables
Q1s     = Q_(-56.46231268955555 ,'kJ/s').magnitude
Q2s     = Q_(-56.21205216238889 ,'kJ/s').magnitude
C_B1s   = Q_(6.957584736581086 ,'kmol/m^3').magnitude
C_DEB1s = Q_(3.102860753791362e-008 ,'kmol/m^3').magnitude
C_E1s   = Q_(1.957602633624548 ,'kmol/m^3').magnitude
C_EB1s  = Q_(0.04239013077460398 ,'kmol/m^3').magnitude
T_1s    = Q_(299.9999996223807 ,'K').magnitude
C_B2s   = Q_(6.435017815688568 ,'kmol/m^3').magnitude
C_DEB2s = Q_(2.818619157578272e-008 ,'kmol/m^3').magnitude
C_E2s   = Q_(1.961093837323424 ,'kmol/m^3').magnitude
C_EB2s  = Q_(0.03873219180531986 ,'kmol/m^3').magnitude
T_2s    = Q_(299.9999998195908 ,'K').magnitude
# Q1s     = Q_(-1074.63 ,'kJ/s').magnitude
# Q2s     = Q_(-6768.83 ,'kJ/s').magnitude
# C_B1s   = Q_(5.551990403223146 ,'kmol/m^3').magnitude
# C_DEB1s = Q_(8.75999437550174e-006 ,'kmol/m^3').magnitude
# C_E1s   = Q_(4.333830798637546 ,'kmol/m^3').magnitude
# C_EB1s  = Q_(0.539305 ,'kmol/m^3').magnitude
# T_1s    = Q_(321.154 ,'K').magnitude
# C_B2s   = Q_(1.309395934989596 ,'kmol/m^3').magnitude
# C_DEB2s = Q_(0.007767870421433004 ,'kmol/m^3').magnitude
# C_E2s   = Q_(0.1962010989664658 ,'kmol/m^3').magnitude
# C_EB2s  = Q_(4.211820652459363 ,'kmol/m^3').magnitude
# T_2s    = Q_(442.9880212435662 ,'K').magnitude

# #Steady State Values of state variables
# C_B10   = Q_(5.53823 ,'kmol/m^3').magnitude
# C_DEB10 = Q_(0.0 ,'kmol/m^3').magnitude
# C_E10   = Q_(4.43068 ,'kmol/m^3').magnitude
# C_EB10  = Q_(0.0 ,'kmol/m^3').magnitude
# T_10    = Q_(350 ,'K').magnitude
# C_B20   = Q_(5.01953 ,'kmol/m^3').magnitude
# C_DEB20 = Q_(0.0 ,'kmol/m^3').magnitude
# C_E20   = Q_(4.0162 ,'kmol/m^3').magnitude
# C_EB20  = Q_(0.0 ,'kmol/m^3').magnitude
# T_20    = Q_(350 ,'K').magnitude
#Steady State Values of state variables
C_B10   = Q_(6.999958587602 ,'kmol/m^3').magnitude
C_DEB10 = Q_(0.0 ,'kmol/m^3').magnitude
C_E10   = Q_(1.999988166233 ,'kmol/m^3').magnitude
C_EB10  = Q_(0.0 ,'kmol/m^3').magnitude
T_10    = Q_(300 ,'K').magnitude
C_B20   = Q_(5.999976193973 ,'kmol/m^3').magnitude
C_DEB20 = Q_(0.0 ,'kmol/m^3').magnitude
C_E20   = Q_(1.999992064658 ,'kmol/m^3').magnitude
C_EB20  = Q_(0.0 ,'kmol/m^3').magnitude
T_20    = Q_(300 ,'K').magnitude

#Non-linear System Parameters
rhoe_L1  = Q_(639.153,'kg/m^3').magnitude
rhoe_L2  = Q_(607.504,'kg/m^3').magnitude

#Volume and flow rates
F1     = Q_(43.2,'m^3/hr').to('m^3/s').magnitude
F2_new = Q_(47.879,'m^3/hr').to('m^3/s').magnitude
F2_net = F2_new + F1
V1 = Q_(60.0,'m^3').magnitude
V2 = Q_(60.0,'m^3').magnitude


#Thermodynamic Parameters
E_1 = Q_(71160,'kJ/kmol').magnitude
E_2 = Q_(83680,'kJ/kmol').magnitude
E_3 = Q_(62760,'kJ/kmol').magnitude
H_1 = Q_(-1.04e5,'kJ/kmol').magnitude
H_2 = Q_(-1.02e5,'kJ/kmol').magnitude
H_3 = Q_(-5.5e2,'kJ/kmol').magnitude
R   = Q_(8.31446261815324,'kJ/kmol/K').magnitude
# https://www.sciencedirect.com/science/article/pii/S1876619615000868
# B + E -> EB -114.13 kJ/mole
# EB + E -> DEB -112.56 kJ/mole
# DEB + B -> 2EB -1.57 kJ/mole

# Initial Guesses
Cp1 = Q_(2.411,'kJ/kg/K').magnitude
Cp2 = Q_(2.411,'kJ/kg/K').magnitude
k_1 = Q_(1.528e6,'m^3/kmol/s').magnitude
k_2 = Q_(27780,'m^3/kmol/s').magnitude
k_3 = Q_(0.4167,'m^3/kmol/s').magnitude
k=np.array([k_1,k_2,k_3])
E=np.array([E_1,E_2,E_3])
rxnCoeffs=np.array([[1,0,1,0],[0,0,1,1],[1,1,0,0]])
dH=np.array([H_1,H_2,H_3])

###################################### MPC simulation constants ##############################################
hcPI   = 0.03  # s Numerical Integration Step Size for PI 
hcMPC  = 0.3  # s Numerical Integration Step Size for MPC
tFinal = 60*60*6     # s Total Simulation Time(including multiple runs)
# Based on hcMPC
controlStepSize = 100  # Integration Steps per Sampling Period

# Based on hcPI
setpointStepSize  = 4000  # Integration Steps per Set-Point
PIcontrolStepSize = 100  # Integration Steps per PI Sampling Period

# Based on delta
HORIZON_LENGTH  = 10  # Number of MPC sampling periods per Horizon
delta = hcMPC*controlStepSize       # Sampling period is 30 seconds

# Model in this context is the First Principle Model, not IPOPT.
NUM_OUTPUTS = 10  # Model Outputs: x1 x2
NUM_INPUTS = 12  # Model  Inputs: u1 u2 x1 x2
NUM_U = int(NUM_INPUTS - NUM_OUTPUTS)  # Number of control inputs

###################################### MPC simulation constants ##############################################

timeModulus     = round(hcMPC / hcPI)
netTimeStepsPI  = round(tFinal / hcPI)   # Number of calculated steps for PI
netTimeStepsMPC = round(tFinal / hcMPC)  # Number of calculated steps for MPC


# Based on hcPI
controlStepSizePI = controlStepSize * timeModulus

# Based on hcMPC
NUM_MPC_ITERATION = round(netTimeStepsMPC/controlStepSize)  # Number of times simulation is run

# Based on hcMPC
netControlTimeSteps = round(netTimeStepsMPC / controlStepSize)

# Based on hcPI
netSetPointTimeSteps  = round(netTimeStepsPI / setpointStepSize)
netPIControlTimeSteps = round(netTimeStepsPI / PIcontrolStepSize)

controlTimeStepsPerMPC   = round(HORIZON_LENGTH * netControlTimeSteps / NUM_MPC_ITERATION)    # Horizon Length
setpointTimeStepsPerMPC  = round(HORIZON_LENGTH * netSetPointTimeSteps / NUM_MPC_ITERATION)   # Unused
PIControlTimeStepsPerMPC = round(HORIZON_LENGTH * netPIControlTimeSteps / NUM_MPC_ITERATION)  # Unused
timeStepsPerMPC          = round(HORIZON_LENGTH * netTimeStepsMPC / NUM_MPC_ITERATION)

controlTimeStepsPerControlAction   = round(netControlTimeSteps / NUM_MPC_ITERATION)
setpointTimeStepsPerControlAction  = round(netSetPointTimeSteps / NUM_MPC_ITERATION)
PIControlTimeStepsPerControlAction = round(netPIControlTimeSteps / NUM_MPC_ITERATION)
timeStepsPerControlAction          = round(netTimeStepsPI / NUM_MPC_ITERATION)

NUM_MPC_INPUTS = int(NUM_U * controlTimeStepsPerMPC)  # 1 set of control inputs per Horizon
NUM_MPC_CONSTRAINTS = controlTimeStepsPerMPC  # Constraints must be satisfied at all points