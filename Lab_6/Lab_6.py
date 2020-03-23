#import arcpy module
import arcpy

#define buffer input feature class
fc = "mc_major_roads"
out = "C:\\temp\\"

#define distance to buffer the roads
distance_list = ["100 meters","200 meters","300 meters"]

#loop through each distance and buffer
for dist in distance_list:
    #append feature class with first three characters of dist value
    out = fc + "_" + dist[0:3]
    print("Now Buffering:" + out)
    #Using ALL parameter which performs dissolve
    arcpy.Buffer_analysis(fc,out,dist,"","","ALL")

print("Finished Buffering")