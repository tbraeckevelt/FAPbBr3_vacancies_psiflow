# FAPbBr3_vacancies_psiflow
A repository for the paper about the effect of vacancies on the structural properties of FAPbBr3 

This repository consists of three folder:

- psiflow_files: contains the input files for the active learning via psiflow.
*hortense.yaml: contains the configuration settings for parsl, this selects the requested resources for the three different type of simulations (AI reference, MLP training, and MLP MD)
*run_sequential_learning.py: the main python script, which performs the psiflow active learning workflow.
*submitscript.sh: submits the python job to our local HPC, and loads the psiflow module (version 3.0.0)
*data: contains the input settings for CP2K, and the initial structures dataset

-MLP_MDs_yaff: contains the input files for the MDs performed with the final MLP constructed with psiflow. From these MDs the Pb-Br-Pb bond angles distribution is extracted, the post-analysis python script to construct these figures is also present in this folder.
*each folder contains the input files for a separate MD simulation. The name indicates how many vacancies are present in the initial structure
*themodel.tar.gz: the MACE model is tarred (to reduce the size of the file)
*shortMD.py: python script to perform the MLP MDs via yaff and ASE.
*create_snapshot_cifs: post-analysis script which extracts random snapshots and an average snapshot for all MDs.
*get_angle_dist: post-analysis script which constucts the Br-Pb-Br bond angle plots (also present in this folder).
*submitscript.sh: submits the python job to our local HPC,, and loads the psiflow module (version 3.0.0).

-temperature_investigation: also contains the psiflow_files and MLP_MDs_yaff folder. The same calculations were also performed to investigate the effect of temperature (instead of vacancies), the input files for these calculations can be found in this folder.
