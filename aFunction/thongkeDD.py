import arcpy, sys, os
from arcpy import env
env.workspace = "..\DHNT.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "DuongDayDien", df)[0]
#table = arcpy.mapping.ListTableViews(mxd, "DL_LoaiOngNuoc", df)[0]

output = sys.argv[1]

#arcpy.AddJoin_management(lyr, "maLoai", table, "maLoai")
arcpy.Statistics_analysis(lyr, output, [["chieudai", "SUM"],["chieudai", "MEAN"],["chieudai", "MAX"],["chieudai", "MIN"]])
#arcpy.RemoveJoin_management (lyr)
del mxd