# FJSSP and FJSSP-W Benchmarking Environment
This provided environment can be used to test and compare different algorithms for the flexible job shop scheduling problem (FJSSP) and the FJSSP with worker flexibility (FJSSP-W). The provided benchmark instance collection can be found in the "instances" subdirectory, including some example instances for the FJSSP-W. Also provided in the directory "InstanceData" are known best results and lower bounds for the different problems and their instances.
"util" contains the provided evaluation and comparison functionality of the benchmarking environment, including the algorithm used to create FJSSP-W problem instances from the well known FJSSP instances.

## FJSSP-W Benchmarking Instances

Note that while a translation algorithm between FJSSP and FJSSP-W instances is provided, the FJSSP-W instances are generated randomly (based on the respective FJSSP instance). The provided best known results for the FJSSP-W are specific to the FJSSP-W instances which are provided and can not not be used for comparison with newly generated instances.

## References for the included FJSSP problems
1. P. Brandimarte. Routing and Scheduling in a Flexible Job Shop by Tabu Search. Annals of Operations Research, 41(3):157–183, 1993.
2. J. Hurink, B. Jurisch, and M. Thole. Tabu search for the job-shop scheduling problem with multi-purpose machines. Operations-Research-Spektrum, vol. 15, no. 4, pp. 205–215, 1994.
3. S. Dauzère-Pérès and J. Paulli. Solving the General Multiprocessor Job-Shop Scheduling Problem. Technical report, Rotterdam School of Management, Erasmus Universiteit Rotterdam, 1994.
4. J. B. Chambers and J. W. Barnes. Flexible Job Shop Scheduling by Tabu Search. The University of Texas, Austin, TX, Technical Report Series ORP96-09, Graduate Program in Operations Research and Industrial Engineering, 1996.
5. I. Kacem, S. Hammadi, and P. Borne. Pareto-Optimality Approach for Flexible, Job-Shop Scheduling Problems: Hybridization of Evolutionary Algorithms and Fuzzy Logic. Mathematics and Computers in Simulation, 60(3-5):245–276, 2002.
6. P. Fattahi, M. S. Mehrabad, and F. Jolai. Mathematical Modeling and Heuristic Approaches to Flexible Job Shop Scheduling Problems. Journal of Intelligent Manufacturing, 18(3):331–342, 2007.
7. Behnke, D., & Geiger, M. J. (2012). Test instances for the flexible job shop scheduling problem with work centers. Arbeitspapier/Research Paper/Helmut-Schmidt-Universität, Lehrstuhl für Betriebswirtschaftslehre, insbes. Logistik-Management.