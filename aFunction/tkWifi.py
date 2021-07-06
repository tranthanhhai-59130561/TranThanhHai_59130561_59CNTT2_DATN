import arcpy, sys, os

arcpy.env.workspace = "..\DHNT.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "Wifi", df)[0]
lyr_kv = arcpy.mapping.ListLayers(mxd, "KhuVuc", df)[0]
table_lkv = arcpy.mapping.ListTableViews(mxd, "DL_LoaiKhuVuc", df)[0]

#td = sys.argv[1]
if sys.argv[1] == '#':
    twf = 0
else:
    twf = sys.argv[1]

if sys.argv[2] == '#':
    tkv = 0
else:
    tkv = sys.argv[2]

if sys.argv[3] == '#':
    tlkv = 0
else:
    tlkv = sys.argv[3]

arcpy.AddJoin_management(lyr_kv, "maLKV", table_lkv, "maLKV")
arcpy.AddJoin_management(lyr, "maKV", lyr_kv, "maKV")

query="Wifi.tenWifi LIKE '%{0}%' or KhuVuc.TenKV LIKE '%{1}%' or DL_LoaiKhuVuc.tenLKV LIKE '%{2}%'".format(twf, tkv, tlkv) # String formatting.

arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", query)

arcpy.RemoveJoin_management (lyr_kv)
arcpy.RemoveJoin_management (lyr)

del mxd