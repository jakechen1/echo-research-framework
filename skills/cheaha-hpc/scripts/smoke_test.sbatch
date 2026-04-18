#!/bin/bash
#SBATCH --job-name=smoke_test
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:05:00
#SBATCH --output=smoke_%j.out
#SBATCH --error=smoke_%j.err

echo "Hello from $(hostname) at $(date)"
echo "SLURM_JOB_ID=$SLURM_JOB_ID"
echo "SLURM_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK"
sleep 30
echo "Done at $(date)"
