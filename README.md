# Simulated-Annealing-and-Greedy-TSP

Thanks to https://github.com/perrygeo/simanneal/tree/951e7d89a8b7f19aeb05b64e7cc8b844a734af89 for PyPi source code

The source code of the program can be found at: https://github.com/aaronfox/Simulated-Annealing-and-Greedy-TSP

To run the program, you must have Python 3 installed. You must also have all the prerequsuite Python modules using Python's pip installer:

pip install itertools
pip install matplotlib
pip install collections
pip install simanneal

After installing Python and each PyPi module in the command line, the user can then run

python salesman.py

on the file, which will then, by default, output:

> python salesman.py

 Temperature        Energy    Accept   Improve     Elapsed   Remaining
 
    17.00000       8434.32     2.70%     0.00%     0:00:06    -1:59:58
    
 Temperature        Energy    Accept   Improve     Elapsed   Remaining
 
    17.00000       8865.64     3.62%     0.12%     0:00:08     0:00:00
    
 Temperature        Energy    Accept   Improve     Elapsed   Remaining
 
     2.60000       8586.99     3.35%     0.00%     0:00:05     0:00:00
     
 Temperature        Energy    Accept   Improve     Elapsed   Remaining
 
     2.60000       8821.58     3.00%     0.00%     0:00:07     0:00:00
     
 Temperature        Energy    Accept   Improve     Elapsed   Remaining
 
     7.30000       8901.44     3.45%     0.00%     0:00:06    -1:59:58
     
 Temperature        Energy    Accept   Improve     Elapsed   Remaining
 
     7.30000       8860.23     3.50%     0.12%     0:00:05     0:00:00
     
     Parallel Simulated Annealing Results: 
     
Best Route: ['New York City', 'Boston', 'Detroit', 'MilWaukee', 'Chicago', 'Indianapolis', 'Columbus', 'Louisville', 'Nashville', 'Memphis', 'Fort Worth', 'Dallas', 'Oklahoma City', 'Albuquerque', 'Las Vegas', 'Portland', 'San Francisco', 'San Jose', 'Los Angeles', 'San Diego', 'Phoenix', 'El Paso', 'San Antonio', 'Austin', 'Houston', 'Jacksonville', 'Charlotte', 'Baltimore', 'Philadelphia']

Distance of route: 8434.319297998614

Local Greedy Results: 

Best Route: ['Memphis', 'Nashville', 'Louisville', 'Indianapolis', 'Chicago', 'MilWaukee', 'Detroit', 'Columbus', 'Baltimore', 'Philadelphia', 'New York City', 'Boston', 'Charlotte', 'Jacksonville', 'Houston', 'Austin', 'San Antonio', 'Fort Worth', 'Dallas', 'Oklahoma City', 'Albuquerque', 'El Paso', 'Phoenix', 'Las Vegas', 'Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Portland']

Distance of route: 8882.22315491822

Additionally, two matplotlib plots will appear and allow the user to visualize the results graphically.

The user can adjust the number of cities in line 332 of the code, adjusting the number of cities to analyze there.
