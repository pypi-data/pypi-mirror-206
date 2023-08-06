# -*- coding: utf-8 -*-


import numpy as np 
from matplotlib import pyplot as plt
import simulateIRAS as iras


# IRAS Simulation parameters (Change these values for different simulations)
nSubstrateComplexExpression = 2.3 + 0.0j # Complex index of refraction constant of an isotropic substrate
nAdsorbateInf = 1.37 # Real index of refraction constant of absorbate film for high wavenumber limit

filmThickness = 1.6474*10**-8
angle = 84*np.pi/180

kFile = "IRASTestK.txt" # comma delimited file with header of 2D matrix with columns as wavenumber, kx (in-plane), ky (in-plane), kz (out-of-plane)

# Imports adsorbate k parameters for simulated IRAS
dataK = iras.ImportFile(kFile)
simulationWavenumber = dataK[0]; dataK = dataK[1:] 

# Generates the complex index of refraction for the vacuum and substrate layers
nVacuumComplexExpression = 1.0 + 0.0j
nVacuum = \
    iras.GenerateIsotropicMatrix(simulationWavenumber,constantComplex = nVacuumComplexExpression)
    
nSubstrate= \
    iras.GenerateIsotropicMatrix(simulationWavenumber,constantComplex = nSubstrateComplexExpression)

# Calculates the complex index of refraction for the adsorbate layer
nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(dataK)

# Simulates the 4 polarization- and azimuth-resolved IRAS spectra
simulatedSpectra = iras.SimulatePolarizationAzimuthSpectra_3Layer(simulationWavenumber,
                        nVacuum, nSubstrate, nAdsorbate,
                        filmThickness, angle)
simulatedSpectra = simulatedSpectra.real

# Plots the k parameters and 4 polarization- and azimuth-resolved IRAS spectra
plt.figure(0); plt.clf()
plt.xlabel("$\mathregular{Wavenumber\ (cm^{-1})}$")
plt.ylabel("$\mathregular{k(\omega)}$")
plt.plot(simulationWavenumber, dataK[0], label="k(x)")
plt.plot(simulationWavenumber, dataK[1], label="k(y)")
plt.plot(simulationWavenumber, dataK[2], label="k(z)")
plt.xlim(1900, 3000)
plt.legend()
plt.tight_layout()
plt.ion()
plt.show()
plt.savefig("Figure0.png", dpi=300, format='png')


plt.figure(1); plt.clf()
plt.xlabel("$\mathregular{Wavenumber\ (cm^{-1})}$")
plt.ylabel("$\mathregular{\Delta R / R}$")
plt.plot(simulatedSpectra[0], simulatedSpectra[1],label="s(y)")
plt.plot(simulatedSpectra[0], simulatedSpectra[2],label="p(xz)")
plt.plot(simulatedSpectra[0], simulatedSpectra[3],label="s(x)")
plt.plot(simulatedSpectra[0], simulatedSpectra[4],label="p(yz)")
plt.xlim(1900, 3000)
plt.legend()
plt.tight_layout()
plt.ion()
plt.show()
plt.savefig("Figure1.png", dpi=300, format='png')

# Exports the 4 polarization- and azimuth-resolved IRAS spectra
np.savetxt("SimulatedIRAS.txt", np.transpose(simulatedSpectra.real), 
           delimiter = ",", 
           header="wavenumber(cm^-1),spol(y),ppol(zx),spol(x),ppol(zy)",comments=''
           )
