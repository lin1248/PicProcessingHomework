# 合并长方形

""" 
功能：合并两个相交的长方形
参数：
    rect为Rect类
    
"""

def mergedRect(minx1,miny1,maxx1,maxy1,minx2,miny2,maxx2,maxy2):

    min_x=max(minx1,minx2)
    min_y=max(miny1,miny2)
    max_x=min(maxx1,maxx2)
    max_y=min(maxy1,maxy2)

    # 如果两个长方形相交，则返回两个长方形构成的长方形
    if (max_y >= min_y and max_x >= min_x):
    # if (max_y >= min_y and max_x >= min_x) or abs(max_x - min_x)<=1 or abs(max_y - min_y) <= 1:
    # if (max_x == maxx1 and max_y == maxy1 and min_x == minx1 and min_y == miny1) or (max_x == maxx2 and max_y == maxy2 and min_x == minx2 and min_y == miny2):
        min_x=min(minx1,minx2)
        min_y=min(miny1,miny2)
        max_x=max(maxx1,maxx2)
        max_y=max(maxy1,maxy2)
        return min_x,min_y,max_x,max_y
    return -1,-1,-1,-1



