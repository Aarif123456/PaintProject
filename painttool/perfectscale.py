from pygame import*
def perfectscale(img):#allows images os cale perfectly if they were not already the same size  
    ix,iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_ratio = bx/float(ix)#test to see if loat is better or int 
        sy = scaleRatio * iy        
        scale_ratio = by/float(iy)
        sx = scaleRatio * ix
        sy = by        
    else:
        # fit to height
        scaleRactor = by/float(iy)
        sx = scaleRatio * ix
        #sx > bx:
        scaleRatio = bx/float(ix)
        sx = bx
        sy = scaleRatio * iy       

    img=transform.scale(img, (sx,sy))
