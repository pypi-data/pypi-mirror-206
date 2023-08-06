# pICNIK 

pICNIK is a module with implemented isoconversional computations for non-isothermal kinetcis.\
The package has an object oriented interface with two classes: DataExtraction and ActivationEnergy, with the purpose of managing the experimental data and computing activation energies  with the next isoconversional methods: 

- Ozawa-Flynn-Wall (OFW)\
- Kissinger-Akahira-Sunose (KAS)\ 
- Friedman (Fr)\
- Vyazovkin (Vy)\
- Advanced method of Vyazovkin (aVy)\


The repository consist in the following directories:
- picnik.py. Contains the package
- examples. Contains a script (example.py) which executes some commmands of picnik in order to ilustrate the suggested procedure. And three more directories which contain data to use with example.py:
    - Constant_E. Simulated TGA data for a process with constant activation energy.
    - Two_Steps. Simulated TGA data for a process with two steps, each with constant activation energy.
    - Variable_E. Simulated TGA data for a process with variable activation energy.


### Installation

`picnik` can be installed from PyPi with `pip`:
`$ pip install picnik`


### DataExtractioin class

It has methods to open the .csv files containing the thermogravimetric data as pandas DataFrames for the experimental data, computing and adding the conversion for the process and the conversion rate as columns in the DataFrame.\
The class also has methods for creating isoconversional DataFrames of time, temperature, conversion rates (for the OFW, KAS, Fr and Vy methods) and also "advanced" DataFrames of time and temperature (for the aVy method).\
Example:

    import picnik as pnk
 
    files = ["HR_1.csv","HR_2.csv",...,"HR_n.csv"]
    xtr = pnk.DataExtraction()
    Beta, T0 = xtr.read_files(files,encoding)
    xtr.Conversion(T0,Tf)
    TDF,tDF,dDF,TaDF,taDF = xtr.Isoconversion(advanced=(bool))
    
    
The DataFrames are also stored as attributes of the `xtr` object 


### ActivationEnergy class

This class has methods to compute the activation energies with the DataFrames created with the `xtr` object along with its associated error. The `Fr()`,`OFW()`,`KAS()` methods return a tuple of three, two and two elements respectively. The first element of the tuples is a numpy array containing the isoconversional activation energies. The second element contains the associated error within a 95\% confidence interval. The third element in the case of the `Fr()` method is a numpy array containing the intercept of the Friedman method. The `Vy()` and `aVy()` only return a numpy array of isoconversional activation energies, the error associated to this methods are obtained with the `Vy_error()` and `aVy_error()` methods
Example:

    ace = pnk.ActivationEnergy(Beta,
                               T0,
                               TDF,
                               dDF,
                               TaDF,
                               taDF)
    E_Fr, E_OFW, E_KAS, E_Vy, E_aVy = ace.Fr(), ace.OFW(), ace.KAS(), ace.Vy(), ace.aVy()
    
The constructor of this class needs six arguments, a list/array/tuple of Temperature rates, a list/array of initial temperatures and four DataFrames: one of temperature, one of convertsion rates and two "advanced" one of temperature and the other of time.

### Exporting results

The DataExtractionclass also has a method to export the results as .csv or .xlsx files:

    xtr.export_Ea(E_Fr = (Bool), 
                  E_OFW = (Bool), 
                  E_KAS = (Bool), 
                  E_Vy = (Bool), 
                  E_aVy = (Bool),
                  file_t="xlsx" )

Set to True the method which values want to be exported. Set `file_t` to `xlsx` to export results as as an Excel spreadsheet or to `csv` to export results as a CSV file.



