import arcpy, sys, os

arcpy.env.workspace = "..\DHNT.gdb"
arcpy.env.workspace = True

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
table = arcpy.mapping.ListTableViews(mxd, "DL_PhongHoc", df)[0]
table_t = arcpy.mapping.ListTableViews(mxd, "DL_TangHoc", df)[0]
lyr_kv = arcpy.mapping.ListLayers(mxd, "KhuVuc", df)[0]

#td = sys.argv[1]
if sys.argv[1] == '#':
    tp = 0
else:
    tp = sys.argv[1]


arcpy.AddJoin_management(table, "maTang", table_t, "maTang")
arcpy.AddJoin_management(table, "maKV", lyr_kv, "maKV")

query="DL_PhongHoc.tenPhong LIKE '%{0}%'".format(tp) # String formatting.
arcpy.SelectLayerByAttribute_management(table, "NEW_SELECTION", query)

arcpy.RemoveJoin_management (table)

del mxd