# -*- coding: utf-8 -*-


import numpy as np 
import scipy.fftpack as ft


def ImportFile(file):
    """
    Imports k parameter or IRAS file for simulations in a comma delimited file with a header
    k parameter file form must be (wavenumber, k(x), k(y), k(z))
    IRAS spectra file form must be (wavenumber, s(y), p(xz), s(x), p(yz))
    The wavenumber column must be identical if importing both a k parameter and IRAS spectra file for simulations
    
    Inputs:
        file: location of import file from current directory (string)
        
    Returns:
        total: residual of absolute differences between the IRAS data and simulations (np.array)
    """
    data = np.genfromtxt(file,dtype=float, unpack=True, delimiter=",", skip_header=True)
    return(data)
    
def CalculateResidualAbsoluteDifference(data,sim, weightS, weightP,pPol=0, sPol=0):
    """
    Calculates the residual of absolute differences between the IRAS data and simulations
    Note: 3 spectra are needed to regress k parameters so only pPol or sPol can have non-default values otherwise only pPol value is accepted
    
    Inputs:
        data: a 2D (4 x n) matrix containing IRAS data (wavenumber,sy,pxy,sx,pyz) (np.array)
        sim: a 2D (4 x n) matrix containing simulated IRAS (wavenumber,sy,pxy,sx,pyz) (np.array)
        weightS: scale factor for s-polarized spectra residuals
        weightP: scale factor for p-polarized spectra residuals
        pPol: selects whether residuals for both s-polarized and only p(xz) (pPol="xz"), p(yz) (pPol="yz" or both (default) spectra are calculated
        sPol: selects whether residuals for both p-polarized and only s(y) (sPol="y"), s(x) (sPol="x" or both (default) spectra are calculated
        
    Returns:
        total: residual of absolute differences between the IRAS data and simulations (float)
    """
    stepX = np.absolute(data[0][0]-data[0][1]); numXsteps = len(data[0])
    if pPol == "xz" and sPol == 0:
        diffSy = np.absolute(data[1]-sim[1]); diffSx = np.absolute(data[3]-sim[3])
        diffPxz = np.absolute(data[2]-sim[2])
        total = (np.sum(diffSy)*weightS + np.sum(diffPxz)*weightP + np.sum(diffSx)*weightS)*stepX*(numXsteps-1)
    elif pPol == "yz" and sPol == 0:
        diffSy = np.absolute(data[1]-sim[1]); diffSx = np.absolute(data[3]-sim[3])
        diffPyz = np.absolute(data[4]-sim[4])
        total = (np.sum(diffSy)*weightS + np.sum(diffSx)*weightS + np.sum(diffPyz)*weightP)*stepX*(numXsteps-1)
    elif sPol == "y" and pPol == 0:
        diffSy = np.absolute(data[1]-sim[1])
        diffPxz = np.absolute(data[2]-sim[2]); diffPyz = np.absolute(data[4]-sim[4])
        total = (np.sum(diffSy)*weightS + np.sum(diffPxz)*weightP + np.sum(diffPyz)*weightP)*stepX*(numXsteps-1)
    elif sPol == "x" and pPol == 0:
        diffSx = np.absolute(data[3]-sim[3])
        diffPxz = np.absolute(data[2]-sim[2]); diffPyz = np.absolute(data[4]-sim[4])
        total = (np.sum(diffPxz)*weightP + np.sum(diffSx)*weightS + np.sum(diffPyz)*weightP)*stepX*(numXsteps-1)
    else:
        diffSy = np.absolute(data[1]-sim[1]); diffSx = np.absolute(data[3]-sim[3])
        diffPxz = np.absolute(data[2]-sim[2]); diffPyz = np.absolute(data[4]-sim[4])
        total = (np.sum(diffSy)*weightS + np.sum(diffPxz)*weightP + np.sum(diffSx)*weightS + np.sum(diffPyz)*weightP)*stepX*(numXsteps-1)
    return total

def CalcIndexRefractFromK(kParameters):
    """
    Calculates the complex index of refraction from the k parameters (imaginary index of refraction)
    using a Kramers-Kronig (or Hilbert for mathematicians) transformation
    
    Inputs:
        kParameters: a 2D (3 x n) matrix with k(w) parameters (np.array)
        
    Returns:
        complexIndexRefractAdsorbate: a 2D (3 x n) matrix with the complex index of refraction (np.array)
    """
    complexIndexRefractAdsorbateX = ft.hilbert(kParameters[0]) + 1.0j * kParameters[0]
    complexIndexRefractAdsorbateY = ft.hilbert(kParameters[1]) + 1.0j * kParameters[1]
    complexIndexRefractAdsorbateZ = ft.hilbert(kParameters[2]) + 1.0j * kParameters[2]
    complexIndexRefractAdsorbate = np.array([complexIndexRefractAdsorbateX,
                                  complexIndexRefractAdsorbateY,
                                  complexIndexRefractAdsorbateZ],
                                dtype=complex)
    return complexIndexRefractAdsorbate

def SimulatePolarizationAzimuthSpectra_3Layer(wavenumber,nVacuum,nSubstrate,nAdsorbate, filmThickness,angle):
    """Simulates 4 polarization- and azimuth-resolved spectra
    
    Inputs: 
           wavenumber: a 2D (1 x n) matrix with the simulation wavenumbers (np.array)
           nVacuum: a 2D (3 x n) matrix with the vacuum complex index of refraction (x,y,z) (np.array)
           nSubstrate: a 2D (3 x n) matrix with the substrate complex index of refraction (x,y,z) (np.array)
           nAdsorbate: a 2D (3 x n) matrix with the adsorbate complex index of refraction (x,y,z) (np.array)
           filmThickness: adsorbate layer thickness or approximate coverage as partial layer thickness (np.array)
           angle: light incident to surface normal angle
        
    Returns:
        spectra4: a 2D matrix (5xn) consisting of wavenumber, S(y), P(xz), S(x) and P(yz) simulated spectra
    """
    
    spectraSy = CalculateSPolarSpectra_3Layer(wavenumber,
                            nVacuum, nSubstrate, nAdsorbate,
                            filmThickness, angle)
    spectraPxz = CalculatePPolarSpectra_3Layer(wavenumber,
                            nVacuum, nSubstrate, nAdsorbate,
                            filmThickness, angle)
    spectraSx = CalculateSPolarSpectra_3Layer(wavenumber,
                            RotateMatrix(nVacuum), RotateMatrix(nSubstrate), RotateMatrix(nAdsorbate),
                            filmThickness, angle)
    spectraPyz = CalculatePPolarSpectra_3Layer(wavenumber,
                            RotateMatrix(nVacuum), RotateMatrix(nSubstrate), RotateMatrix(nAdsorbate),
                            filmThickness, angle)
    spectra4 = np.array([wavenumber,spectraSy,spectraPxz,spectraSx,spectraPyz])
    return spectra4

# s-polarization from Chabal_1987_(SemiconInterfaces_workshop_full_book), for the k-vector projected into the x-direction on the surface (i.e. electric field in the y-direction on the surface)
def CalculateSPolarSpectra_3Layer(wavenumber,refractionVacuum,refractionSubstrate,refractionAdsorbate,filmThickness,angle):
    """Calculates p-polarized IRAS spectra according to Eqn: 2.19 of Chabal YJ (1987) Vibrational Properties at Semiconductor Surfaces and Interfaces. In: Le Lay G, Derrien J, Boccara N (eds) Semiconductor Interfaces: Formation and Properties. Springer Berlin Heidelberg, Berlin, Heidelberg
    Inputs:
           wavenumber: a 2D (1 x n) matrix with the simulation wavenumbers (np.array)
           refractionVacuum: a 2D (3 x n) matrix with the vacuum complex index of refraction (x,y,z) (np.array)
           refractionSubstrate: a 2D (3 x n) matrix with the substrate complex index of refraction (x,y,z) (np.array)
           refractionAdsorbate: a 2D (3 x n) matrix with the adsorbate complex index of refraction (x,y,z) (np.array)
           filmThickness: adsorbate layer thickness or approximate coverage as partial layer thickness (np.array)
           angle: light incident to surface normal angle
        
    Retuns:
        deltaRR: deltaR/R spectra ~ absorbance spectra for p(xz) light
    """
    eVacuum = refractionVacuum**2; eSubstrate = refractionSubstrate**2; eAdsorbate = refractionAdsorbate**2
    Imag = (eSubstrate[1] - eAdsorbate[1]) / (eSubstrate[1]-eVacuum[1])
    deltaRR = 8 * np.pi  * wavenumber * refractionVacuum[1] * filmThickness * np.cos(angle) * np.imag(Imag)
    return deltaRR

# p-polarization from Chabal_1987_(SemiconInterfaces_workshop_full_book), for the k-vector projected into the x-direction on the surface (i.e. electric field in the xz-direction on the surface)
def CalculatePPolarSpectra_3Layer(wavenumber,refractionVacuum,refractionSubstrate,refractionAdsorbate,filmThickness,angle):
    """Calculates p-polarized IRAS spectra according to Eqn: 2.27 of Chabal YJ (1987) Vibrational Properties at Semiconductor Surfaces and Interfaces. In: Le Lay G, Derrien J, Boccara N (eds) Semiconductor Interfaces: Formation and Properties. Springer Berlin Heidelberg, Berlin, Heidelberg
    Inputs:
           wavenumber: a 2D (1 x n) matrix with the simulation wavenumbers (np.array)
           refractionVacuum: a 2D (3 x n) matrix with the vacuum complex index of refraction (x,y,z) (np.array)
           refractionSubstrate: a 2D (3 x n) matrix with the substrate complex index of refraction (x,y,z) (np.array)
           refractionAdsorbate: a 2D (3 x n) matrix with the adsorbate complex index of refraction (x,y,z) (np.array)
           filmThickness: adsorbate layer thickness or approximate coverage as partial layer thickness (np.array)
           angle: light incident to surface normal angle
        
    Retuns:
        deltaRR: deltaR/R spectra ~ absorbance spectra for s(y) light
    """
    eVacuum = refractionVacuum**2; eSubstrate = refractionSubstrate**2; eAdsorbate = refractionAdsorbate**2
    ImagTop = (eSubstrate[0]-eAdsorbate[0])-(((eSubstrate[0]/eAdsorbate[2])-(eAdsorbate[0]/eSubstrate[2]))*eVacuum[0]*(np.sin(angle))**2)
    ImagBottom = (eSubstrate[0]-eVacuum[0])-(((eSubstrate[0]/eVacuum[2])-(eVacuum[0]/eSubstrate[2]))*eVacuum[0]*(np.sin(angle))**2)
    deltaRR = 8 * np.pi  * wavenumber * refractionVacuum[1] * filmThickness * np.cos(angle) * np.imag(ImagTop / ImagBottom)
    return deltaRR

def GaussianFunction(xData,xShift,yAmplitude,FWHM):
    """
    Gaussian FWHM Functional Form
    
    Inputs:
        xData: a 2D (1 x n) matrix with the simulation wavenumbers  (np.array)
        xShift: wavenumber of the peak maximum
        yAmplitude: peak area
        FWHM: peak full-width at half maximum
        
    Returns:
        a 2D (1 x n) matrix with the desired Gaussian Function (np.array)
    """
    return (yAmplitude * np.exp(-(xData-xShift)**2 / (2*(FWHM/(2*np.sqrt(2*np.log(2))))**2)))

def LorentzianFunction(xData,xShift,yAmplitude,FWHM):
    """
    Lorentzian FWHM Functional Form
    
    Inputs:
        xData: a 2D (1 x n) matrix with the simulation wavenumbers  (np.array)
        xShift: wavenumber of the peak maximum
        yAmplitude: peak area
        FWHM: peak full-width at half maximum
        
    Returns:
        a 2D (1 x n) matrix with the desired Lorentzian Function (np.array)
    """
    return (yAmplitude / np.pi) * FWHM / ((xData-xShift)**2 + FWHM**2)
    
def GenerateConstantComplexMatrix(wavenumberX,yComplex):
    """
    Generates an appropriately sized 1D complex matrix
    
    Inputs:
        spectraWavenumber: a 2D (1 x n) matrix with the simulation wavenumbers (np.array)
        constantComplex: a complex expression of the form X + Yj 
        
    Returns:
        a 2D (1 x n) matrix with the complex numbers (np.array)
    """
    return np.full(wavenumberX.shape,yComplex)
       
def GenerateIsotropicMatrix(spectraWavenumber,constantComplex,dimensions = 3):
    """
    Generates an appropriately sized 3D isotrophic matrix (same dependence based on direction)
    
    Inputs:
        spectraWavenumber: a 2D (1 x n) matrix with the simulation wavenumbers (np.array)
        constantComplex: a complex expression of the form X + Yj 
        dimensions: the number of dimensions to generate for the isotropic matrix (integer)
        
    Returns:
        complexMatrix: a mD (m x n) matrix with the complex numbers (np.array)
    """
    complexMatrixX = GenerateConstantComplexMatrix(spectraWavenumber,constantComplex) # Complex Index of Refraction (w) for the vacuum layer in the x-direction
    for n in range (0,dimensions):
        if n == 0: complexMatrix = complexMatrixX
        else:    complexMatrix = np.vstack((complexMatrix,complexMatrixX))
    return complexMatrix

def RotateMatrix(matrix,initial="xyz",final="yxz"):
    """
    Reorders matrix directional component elements according to crystal azimuth rotation
    
    Inputs:
        matrix: a 2D (3 x n) matrix to be rotated (np.array)
        initial: order of matrix indices in current matrix (string)
        final: order of matrix indices in desired matrix (string)
        
    Returns:
        rotate: a 2D (3 x n) matrix that has been rotated (np.array)  
    """
    for n in range(0,len(initial)):
        if n == 0: rotate = matrix[initial.find(final[n])]
        else: rotate = np.vstack((rotate,matrix[initial.find(final[n])]))
    return rotate