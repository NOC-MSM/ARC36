conda activate pybdy

JVM="jre-17"
export JAVA_HOME=/usr/lib/jvm/$JVM/
cd /home/users/benbar/work/ARC36/pybdy/
 
pybdy -s ./namelist_arc36.bdy
pybdy -s ./namelist_arc36_tide.bdy # run with master
