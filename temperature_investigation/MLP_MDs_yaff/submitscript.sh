#!/bin/sh

#PBS -o output_gpu_Til1d.txt
#PBS -e error_gpu_Til1d.txt
#PBS -l nodes=1:ppn=12:gpus=1
#PBS -A 2023_096
#PBS -l walltime=71:59:00

cd ${PBS_O_WORKDIR}

ml psiflow/3.0.0

python -u shortMD.py il1d
