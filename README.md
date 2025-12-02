*******************
# ARCtic 1/36 degree NEMO configuration
*******************

This model configuration has been developed for the Arctic Ocean for the CANARI project.

<img width="541" alt="ARC36 Mesh Grid" src="https://github.com/NOC-MSM/ARC36/blob/master/images/ARC36grid.png" />

## Quick Start
On ARCHER2
```
git clone git@github.com:NOC-MSM/ARC36.git
./ARC36/SCRIPTS/setup/ARC36_setup -p $PWD/ARC36_RUNS -r $PWD/ARC36 -n 5.0 -x 2 -m archer2 -a mpich -c cray
cd ARC36_RUNS/nemo/cfgs/ARC36/
cp -rP EXPREF EXP_MYRUN
cd EXP_MYRUN
ln -s ../INPUTS/domain_cfg.nc domain_cfg.nc
```
Edit the project code and options in  `runscript.slurm` then:
```
sbatch runscript.slurm
```

*****************************************
## NEMO regional configuration of the Arctic Ocean
*****************************************

### Model Summary

The model grid:
- has *1/36*&deg; lat-lon resolution
- *Z* hybrid sigma / z-partial-step vertical levels
- covering  *55*&deg;N to *90*&deg;N, *-180*&deg;E to *180*&deg;E.
For more details on the model parameters, bathymetry and external forcing, see *Ref*

