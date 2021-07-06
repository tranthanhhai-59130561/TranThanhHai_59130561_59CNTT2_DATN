import arcpy, sys, os
from arcpy import env
env.workspace = "..\DHNT.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "KhuVuc", df)[0]
table = arcpy.mapping.ListTableViews(mxd, "DL_LoaiKhuVuc", df)[0]

output = sys.argv[1]

arcpy.AddJoin_management(lyr, "maLKV", table, "maLKV")
arcpy.Statistics_analysis(lyr, output, [["dientich", "SUM"],["dientich", "MEAN"],["dientich", "MAX"],["dientich", "MIN"]], "DL_LoaiKhuVuc.tenLKV")
arcpy.RemoveJoin_management (lyr)
del mxd