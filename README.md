# GlueViz--Fortran-Data-Loader
Data loader for [Glueviz](https://github.com/glue-viz). Enables Glue viz to load unformatted Fortran data files

Currently allows 4D and 3D data cubes to be read in.

Only 'format' loader can currently read in is unfomatted fortran files written out in this form:

   open(62, file = file_name, access = 'direct', status = 'REPLACE', form = 'unformatted', recl = iolength)
   
   write(62,rec=1) array_to_be_written

##ToDo

Generalise code to allow more formats.
