import arcpy, sys, os


arcpy.env.workspace = "..\DHNT.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "DuongDi", df)[0]

#fc = "E:\DATN\TranThanhHai_59130561_DATN\DHNT.gdb\DuongDi"
#fields = ['maDuong', 'tenDuong', 'chieudai']
#td = sys.argv[1]
if sys.argv[1] == '#':
    td = 0
else:
    td = sys.argv[1]

#cd = sys.argv[2]
if sys.argv[2] == '#':
    cd = 0
else:
    cd = sys.argv[2]

query="tenDuong LIKE N'%{0}%' or chieudai = {1}".format(td, cd) # String formatting.

#makelyr = arcpy.MakeFeatureLayer_management(fc, "duongdi_lyr")
#arcpy.SelectLayerByLocation_management("duongdi_lyr", "intersect", "chihuahua", 0, "new_selection")
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)
#arcpy.SelectLayerByAttribute_management(lyr, "CLEAR_SELECTION")
#with arcpy.da.SearchCursor(fc, fields, query) as cursor:
    #for row in cursor:
        #print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        #reportSTargs.printArc(u'KQ: {0}, {1}, {2}'.format(row[0], row[1], row[2]))
del mxd        