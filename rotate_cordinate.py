import math
import numpy as np


def calculate_180(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=w-xmin
    nw_ymax=h-ymin
    nw_xmin=nw_xmax-x
    nw_ymin=nw_ymax-y
    #print("xmin",nw_xmin,"ymin",nw_ymin,"xmax",nw_xmax,"ymax",nw_ymax)
    return nw_xmin,nw_ymin,nw_xmax,nw_ymax



def calculate_270(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=w-ymin
    nw_ymax=xmin+x
    nw_xmin=nw_xmax-y
    nw_ymin=xmin

    return nw_xmin,nw_ymin,nw_xmax,nw_ymax
    #print("xmin",nw_xmin,"ymin",nw_ymin,"xmax",nw_xmax,"ymax",nw_ymax)

def calculate_90(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=ymin+y
    nw_ymax=h-xmin
    nw_xmin=ymin
    nw_ymin=nw_ymax-x
    print("xmin",nw_xmin,"ymin",nw_ymin,"xmax",nw_xmax,"ymax",nw_ymax)
    return nw_xmin,nw_ymin,nw_xmax,nw_ymax

rotate_180=calculate_180(248.07339449541286,106.86238532110093,445.35779816513764,266.56880733944956,512,512)
#print(type(rotate_180))
print("orginial 248.07339449541286,106.86238532110093,445.35779816513764,266.56880733944956")
#calculate_180(248.07339449541286,106.86238532110093,445.35779816513764,266.56880733944956,512,512)
calculate_90(248.07339449541286,106.86238532110093,445.35779816513764,266.56880733944956,512,512)

#calculate_180(243.9633027522936,247.7798165137615,403.66972477064223,443.88990825688074,512,512)