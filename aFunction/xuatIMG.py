import arcpy ,sys

mapName = sys.argv[1]
imgName = sys.argv[2]
#E:\DATN\TranThanhHai_59130561_DATN\TranThanhHai.mxd E:\DATN\thunghiem.png
mxd = arcpy.mapping.MapDocument(mapName)

arcpy.mapping.ExportToPNG(mxd, imgName)
print '{0} created.'.format(imgName)
del mxd

