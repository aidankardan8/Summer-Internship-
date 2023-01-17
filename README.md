This page consists of a summary of the work in this repository.

Within the phyto-voc folder, the file 'function.py' defines the function and parameters used in this project.

**function.py**- is able to extract Aqua-Modis Satellite data from Sable Island, Canada for the date range: April 12th to May 2nd, 2016, in the form of 200 netCDF files from NASA's oceandata website and store them into a folder called "data".

**SI Chlorophyll Graph.ipynb**- Uses the files stored in the "data" folder to find the proportion of non-null chlorophyll pixels from NASA's Aqua-Modis Satellite for Sable Island from April 12th to May 2nd, 2016 and graph it with the date and time on the x-axis, and the proportion of non-null chlorophyll pixels on the y-axis.

From this graph, it is evident that the most clear satellite images(highest proportion of non-null chlorophyll pixels) occur daily in the evening and the most unclear satellite images(lowest proportion of non-null chlorophyll pixels) occur daily in the early morning.

**SI Cloud Graph.ipynb**- Uses the files stores in the "data" folder to find the proportion of cloud-covered pixels from NASA's Aqua-Modis Satellite for Sable Island from April 12th to May 2nd, 2016 and graph it with the date and time on the x-axis, and the proportion of cloud-covered pixels on the y-axis.

From this graph, it is evident that the most clear satellite images(lowest proportion of cloud-covered pixels) occur daily in the early morning and the most unclear satellite images(highest proportion of cloud-covered pixels) occur daily in the evening.

**Small Sample.ipynb**- Uses the files stored in the "Aqua-Modis" folder(contains netcdf files for the date range: April 22nd, 2016 +/- 3 days) for the purpose of learning how to read and extract information from netCDF files to be able to create 'SI Chlorophyll Graph and Cloud Graph'. The sample size for this graph was too small(7) to have results considered statistically meaningful.

Thank you for visiting my page! If you have any questions or comments, please feel free to reach me at a.a.ashrafi@wustl.edu!
