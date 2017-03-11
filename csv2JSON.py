originalFile = ""
geoJSONFile = ""

FeatureType = "LineString"

featName = "name"
XOri = "Xcoord_Ori"
YOri = "Ycoord_Ori"
XDes = "Xcoord_Des"
YDes = "Ycoord_Des"

#--------
import json

originalData = open(originalFile, "r")
newJSON = open(geoJSONFile, "w")
newJSON.write('{"type": "FeatureCollection",\n"features": [')

header = True

for i in originalData:
    i = (i.strip()).split(";")
    if header:
        header = False
        headValue = {}

        for j in i:
            headValue[j] = i.index(j)
    else:
        X1 = float(i[headValue[XOri]].replace(",","."))
        Y1 = float(i[headValue[YOri]].replace(",","."))
        X2 = float(i[headValue[XDes]].replace(",","."))
        Y2 = float(i[headValue[YDes]].replace(",","."))

        prop = {}
        newFeat = {}

        newFeat["type"] = "Feature"
        newFeat["geometry"] = {"type": FeatureType, "coordinates": [[X1, Y1], [X2,Y2]]}
        
        for j in headValue.keys():
            if j == featName:
                prop[j] = i[headValue[j]]
                
            elif j not in (XOri, YOri, XDes, YDes):
                try:
                    prop[j] = float(i[headValue[j]].replace(",","."))
                except:
                    prop[j] = 0.
        
        newFeat["properties"] = prop
        newFeat = json.dumps(newFeat)
        newJSON.write(newFeat + ",\n")
        
newJSON.write("]}")

originalData.close()
newJSON.close()
        
            


        



        
    


