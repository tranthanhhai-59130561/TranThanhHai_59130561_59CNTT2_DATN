import arcpy, sys, os

arcpy.env.workspace = "..\DHNT.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "DiaVat", df)[0]
table = arcpy.mapping.ListTableViews(mxd, "DL_LoaiDiaVat", df)[0]
lyr_duong = arcpy.mapping.ListLayers(mxd, "DuongDi", df)[0]

#tdv = sys.argv[1]
if sys.argv[1] == '#':
    tdv = 0
else:
    tdv = sys.argv[1]

#ldv = sys.argv[2]
if sys.argv[2] == '#':
    ldv = 0
else:
    ldv = sys.argv[2]

if sys.argv[3] == '#':
    td = 0
else:
    td = sys.argv[3]

arcpy.AddJoin_management(lyr, "maLDV", table, "maLDV")
arcpy.AddJoin_management(lyr, "maDuong", lyr_duong, "maDuong")
query = "DiaVat.tenDV LIKE '%{0}%' or DL_LoaiDiaVat.tenLDV LIKE '%{1}%' or DuongDi.tenDuong LIKE '%{2}%'".format(tdv, ldv, td)
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)
arcpy.RemoveJoin_management (lyr)

del mxd