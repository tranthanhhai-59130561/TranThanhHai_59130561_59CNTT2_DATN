import arcpy, sys, os

arcpy.env.workspace = "..\DHNT.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "KhuVuc", df)[0]
table = arcpy.mapping.ListTableViews(mxd, "DL_LoaiKhuVuc", df)[0]
lyr_duong = arcpy.mapping.ListLayers(mxd, "DuongDi", df)[0]


#tkv = sys.argv[1]
if sys.argv[1] == '#':
    tkv = 0
else:
    tkv = sys.argv[1]

#dt = sys.argv[2]
if sys.argv[2] == '#':
    dt = 0
else:
    dt = sys.argv[2]

if sys.argv[3] == '#':
    td = 0
else:
    td = sys.argv[3]

if sys.argv[4] == '#':
    tlkv = 0
else:
    tlkv = sys.argv[4]


arcpy.AddJoin_management(lyr, "maLKV", table, "maLKV")
arcpy.AddJoin_management(lyr, "maDuong", lyr_duong, "maDuong")
query = "KhuVuc.tenKV LIKE '%{0}%' or KhuVuc.dientich <= {1} or DuongDi.tenDuong LIKE '%{2}%' or DL_LoaiKhuVuc.tenLKV LIKE '%{3}%'".format(tkv,dt, td, tlkv)
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)
arcpy.RemoveJoin_management (lyr)

del mxd
