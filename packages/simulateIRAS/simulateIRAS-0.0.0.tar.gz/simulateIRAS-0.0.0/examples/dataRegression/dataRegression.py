# -*- coding: utf-8 -*-


import numpy as np 
from matplotlib import pyplot as plt
import scipy.fftpack as ft
import random
import simulateIRAS as iras


# IRAS physical parameters (Change these values for different model systems)
nVacuumComplexExpression = 1.0 + 0.0j
nSubstrateComplexExpression = 2.3 + 0.0j
nAdsorbateInf = 1.37

filmThickness = 1.6*10**-8
angle = 86*np.pi/180

dataFile = "IRASTest2ML.csv"

# IRAS simulation parameters (Change these values for different regression conditions)
fittingXmin = 1900; fittingXmax = 3000; simulationBuffer = 10; simulationXspacing = 0.05
kPosition = 2100; kFWHM = 1; kAmplitude = 0.01; scaleStoP = 5

numSimulationXY = 30000; kAmplitudeXY = 0.05; cutoffXY = 0.05
numSimulationZ = 50000; cutoffZ = 1
numSimulationXYZ = 50000; cutoffXYZ = 0; 

# Imports IRAS data
dataIRAS = iras.ImportFile(dataFile)
simulationWavenumber = dataIRAS[0]

# Generates the complex index of refraction for the vacuum and substrate layers
nVacuum = \
    iras.GenerateIsotropicMatrix(simulationWavenumber,constantComplex = nVacuumComplexExpression)
    
nSubstrate= \
    iras.GenerateIsotropicMatrix(simulationWavenumber,constantComplex = nSubstrateComplexExpression)

# Generates initial k parameters for the adsorbate layer (imaginary index of refraction)
kAdsorbateX = iras.LorentzianFunction(simulationWavenumber,kPosition,0,kFWHM)
kAdsorbateY = iras.LorentzianFunction(simulationWavenumber,kPosition,0,kFWHM)
kAdsorbateZ = iras.LorentzianFunction(simulationWavenumber,kPosition,0,kFWHM)
kAdsorbate = np.array([kAdsorbateX, kAdsorbateY, kAdsorbateZ])
simulatedKSpectra = np.array([simulationWavenumber,kAdsorbateX, kAdsorbateY, kAdsorbateZ])

# Calculates the complex index of refraction for the adsorbate layer
nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(kAdsorbate)

# Simulates and plots polarization- and azimuth-resolved spectra
simulatedSpectra = iras.SimulatePolarizationAzimuthSpectra_3Layer(simulationWavenumber,
                        nVacuum, nSubstrate, nAdsorbate,
                        filmThickness, angle)

# Initial Fitting kx and ky
for i in range(0,numSimulationXY):
        # Randomizer for new peak fitting
        randomXY = random.randint(0, 1)
        randomWavenumber = random.randint(fittingXmin, fittingXmax)
        randomKAmplitude = random.randint(-25,25) / 100
        kNew = iras.LorentzianFunction(simulationWavenumber,randomWavenumber,(1+randomKAmplitude)*kAmplitude*scaleStoP,kFWHM)
        
        # Evaluate initial fit quality
        fitQualityInitial = iras.CalculateResidualAbsoluteDifference(dataIRAS, simulatedSpectra, 1,0)
        # print(np.sum(np.absolute(dataIRAS[1]-simulatedSpectra[1])))
        # print(np.sum(np.absolute(dataIRAS[3]-simulatedSpectra[3])))
            
        if randomXY == 0:
                kAdsorbateX = kAdsorbateX + kNew
        if randomXY == 1:
            kAdsorbateY = kAdsorbateY + kNew

        kAdsorbate = np.array([kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            
        # Generates the k parameters for the adsorbate layer (imaginary index of refraction)
        simulatedKSpectra = np.array([simulationWavenumber,kAdsorbateX, kAdsorbateY, kAdsorbateZ])
        
        # Calculates the complex index of refraction for the adsorbate layer
        nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(kAdsorbate)
        
        # Simulates and plots polarization- and azimuth-resolved spectra
        simulatedSpectra = iras.SimulatePolarizationAzimuthSpectra_3Layer(simulationWavenumber,
                                nVacuum, nSubstrate, nAdsorbate,
                                filmThickness, angle)
        
        # Evaulate new fit quality
        fitQualityFinal = iras.CalculateResidualAbsoluteDifference(dataIRAS, simulatedSpectra, 1,0)
        
        if fitQualityInitial < fitQualityFinal+(kAmplitudeXY*cutoffXY):
            if randomXY == 0:
                kAdsorbateX = kAdsorbateX - kNew
            if randomXY == 1:
                kAdsorbateY = kAdsorbateY - kNew
            kAdsorbate = np.array([kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            simulatedKSpectra = np.array([simulationWavenumber,kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(kAdsorbate)
                
# Initial fitting routine kz
for i in range(0,numSimulationZ):
        # Randomizer for new peak fitting
        randomWavenumber = random.randint(fittingXmin, fittingXmax)
        randomKAmplitude = random.randint(-25,25) / 100
        kNew = iras.LorentzianFunction(simulationWavenumber,randomWavenumber,(1+randomKAmplitude)*kAmplitude,kFWHM)
        
        # Evaluate initial fit quality
        fitQualityInitial = iras.CalculateResidualAbsoluteDifference(dataIRAS, simulatedSpectra, 0,1)

        kAdsorbateZ = kAdsorbateZ + kNew
        kAdsorbate = np.array([kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            
        # Generates the k parameters for the adsorbate layer (imaginary index of refraction)
        simulatedKSpectra = np.array([simulationWavenumber,kAdsorbateX, kAdsorbateY, kAdsorbateZ])
        
        # Calculates the complex index of refraction for the adsorbate layer
        nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(kAdsorbate)
        
        # Simulates and plots polarization- and azimuth-resolved spectra
        simulatedSpectra = iras.SimulatePolarizationAzimuthSpectra_3Layer(simulationWavenumber,
                                nVacuum, nSubstrate, nAdsorbate,
                                filmThickness, angle)
        
        # Evaulate new fit quality
        fitQualityFinal = iras.CalculateResidualAbsoluteDifference(dataIRAS, simulatedSpectra, 0,1)
        
        if fitQualityInitial < fitQualityFinal+(kAmplitude*cutoffZ):
            kAdsorbateZ = kAdsorbateZ - kNew
            kAdsorbate = np.array([kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            simulatedKSpectra = np.array([simulationWavenumber,kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(kAdsorbate)

# Combined kx, ky, kz fitting routine
for i in range(0,numSimulationXYZ):
        # Randomizer for new peak fitting
        randomWavenumber = random.randint(fittingXmin, fittingXmax)
        randomKAmplitude = random.randint(-25,25) / 100
        randomKXYSign = random.choice([-1,1])
        kNew = iras.LorentzianFunction(simulationWavenumber,randomWavenumber,(randomKXYSign+randomKAmplitude)*kAmplitude,kFWHM)
        
        # Evaluate initial fit quality
        fitQualityInitial = iras.CalculateResidualAbsoluteDifference(dataIRAS, simulatedSpectra, scaleStoP,1)
            
        kAdsorbateX = kAdsorbateX + kNew*scaleStoP
        kAdsorbateY = kAdsorbateY + kNew*scaleStoP
        kAdsorbateZ = kAdsorbateZ - kNew
        kAdsorbate = np.array([kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            
        # Generates the k parameters for the adsorbate layer (imaginary index of refraction)
        simulatedKSpectra = np.array([simulationWavenumber,kAdsorbateX, kAdsorbateY, kAdsorbateZ])
        
        # Calculates the complex index of refraction for the adsorbate layer
        nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(kAdsorbate)
        
        # Simulates and plots polarization- and azimuth-resolved spectra
        simulatedSpectra = iras.SimulatePolarizationAzimuthSpectra_3Layer(simulationWavenumber,
                                nVacuum, nSubstrate, nAdsorbate,
                                filmThickness, angle)
        
        # Evaulate new fit quality
        fitQualityFinal = iras.CalculateResidualAbsoluteDifference(dataIRAS, simulatedSpectra, scaleStoP,1)
        
        if fitQualityInitial < fitQualityFinal+(kAmplitude*cutoffXYZ):
            kAdsorbateX = kAdsorbateX - kNew*scaleStoP
            kAdsorbateY = kAdsorbateY - kNew*scaleStoP
            kAdsorbateZ = kAdsorbateZ + kNew
            kAdsorbate = np.array([kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            simulatedKSpectra = np.array([simulationWavenumber,kAdsorbateX, kAdsorbateY, kAdsorbateZ])
            nAdsorbate = nAdsorbateInf + iras.CalcIndexRefractFromK(kAdsorbate)
    
# Plots the adsorbate k(w) parameters
plt.figure(0); plt.clf()
plt.xlabel("$\mathregular{Wavenumber\ (cm^{-1})}$")
plt.ylabel("$\mathregular{k(\omega)}$")
plt.plot(simulatedKSpectra[0], simulatedKSpectra[1], label="k(x)")
plt.plot(simulatedKSpectra[0], simulatedKSpectra[2], label="k(y)")
plt.plot(simulatedKSpectra[0], simulatedKSpectra[3], label="k(z)")
plt.xlim(1900, 3000)
plt.legend()
plt.tight_layout()
plt.ion()
plt.show()
plt.savefig("Figure0.png", dpi=300, format='png')

plt.figure(1); plt.clf() 
plt.xlabel("$\mathregular{Wavenumber\ (cm^{-1})}$")
plt.ylabel("$\mathregular{\Delta R / R}$")
plt.scatter(dataIRAS[0], dataIRAS[1]*scaleStoP, s=1)
plt.scatter(dataIRAS[0], dataIRAS[2], s=1)
plt.scatter(dataIRAS[0], dataIRAS[3]*scaleStoP, s=1)
plt.scatter(dataIRAS[0], dataIRAS[4], s=1)

simulatedSpectra = simulatedSpectra.real
plt.plot(simulatedSpectra[0], simulatedSpectra[1]*scaleStoP, label="s(y) x "+str(scaleStoP))
plt.plot(simulatedSpectra[0], simulatedSpectra[2], label="p(xz)")
plt.plot(simulatedSpectra[0], simulatedSpectra[3]*scaleStoP, label="s(x) x "+str(scaleStoP))
plt.plot(simulatedSpectra[0], simulatedSpectra[4], label="p(yz))")
plt.xlim(1900, 3000)
plt.legend()
plt.tight_layout() 
plt.ion()
plt.show()
plt.savefig("Figure1.png", dpi=300, format='png')

#Exports the 4 polarization- and azimuth-resolved IRAS spectra
np.savetxt("SimulatedIRAS.txt", np.transpose(simulatedSpectra.real), 
            delimiter = ",", 
            header="wavenumber(cm^-1),spol(y),ppol(zx),spol(x),ppol(zy)",comments=''
            )

#Exports the 4 polarization- and azimuth-resolved IRAS spectra
np.savetxt("SimulatedK.txt", np.transpose(simulatedKSpectra), 
            delimiter = ",", 
            header="wavenumber(cm^-1),k(x),k(y),k(z)",comments=''
            )
