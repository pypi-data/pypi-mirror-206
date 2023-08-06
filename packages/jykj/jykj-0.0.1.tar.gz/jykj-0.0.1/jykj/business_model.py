import numpy as np


def rela_to_abs(arr, size):
    '''
    相对坐标转换为绝对, arr为[center_x, center_y, width, height]
    '''
    w, h = size[0], size[1]
    if (np.array(arr) <= 1).all():
        b = np.array([w, h, w, h])
        return arr * b
    else:
        return arr


def pnpoly(verts: list, testx: int, testy: int) -> bool:
    '''
    判断点在多边形内, PNPoly算法
    参数:
        verts (list): 由多边形顶点组成的列表, 例如[[129,89],[342,68],[397,206],[340,373],[87,268]]
        testx (int): 点的x坐标, 例如123
        testy (int): 点的y坐标, 例如234
    '''

    vertx = [xyvert[0] for xyvert in verts]
    verty = [xyvert[1] for xyvert in verts]
    nvert = len(verts)
    c = False
    j = nvert - 1
    for i in range(nvert):
        if ((verty[i] > testy) !=
            (verty[j] > testy)) and (testx < (vertx[j] - vertx[i]) *
                                     (testy - verty[i]) /
                                     (verty[j] - verty[i]) + vertx[i]):
            c = not c
        j = i
    return c


def persons_in_areas(persons_coords: list,
                     areas: list,
                     resolution: list,
                     w_thresh: float = 1,
                     h_thresh: float = 1,
                     h_offset: float = 0) -> bool:
    '''
    判断人是否在区域内, 支持单人坐标和多人坐标, 支持单区域和多区域, 支持过滤人检测框的宽度和高度, 支持人的位置偏移。

    参数：
        persons_coords (list): 单人[cx, cy, w, h], 多人[[cx1, cy1, w1, h1],[cx2, cy2, w2, h2],...]
        area (list): 单区域[[x1, y1], [x2, y2], [x3, y3]], 多区域[[[x1, y1], [x2, y2], [x3, y3]], [[x4, y4], [x5, y5], [x6, y6], [x7, 7]], ...]
        resolution: 视频分辨率, [width, height] 
        w_thresh (float): 检测框宽度过滤阈值, 0 <= w_thresh <= 1
        h_thresh (flost): 检测框高度过滤阈值, 0 <= h_thresh <= 1
        h_offset (float): 人的位置纵向偏移量, -0.5 <= h_thresh <= 0.5
    '''

    assert np.array(persons_coords).ndim in [1, 2]
    assert np.array(areas).ndim in [2, 3]
    assert 0 < w_thresh <= 1
    assert 0 < h_thresh <= 1
    assert -0.5 <= h_offset <= 0.5

    if np.array(persons_coords).ndim == 1:
        persons_coords = [persons_coords]
    if np.array(areas).ndim == 2:
        areas = [areas]

    persons_coords = rela_to_abs(persons_coords, resolution)
    w_thresh = int(w_thresh * resolution[0])
    h_thresh = int(h_thresh * resolution[1])

    persons_coords = [
        p for p in persons_coords if p[2] <= w_thresh and p[3] <= h_thresh
    ]

    for p in persons_coords:
        cx = p[0]
        cy = p[1] + int(h_offset * p[3])
        for area in areas:
            if pnpoly(area, cx, cy):
                return True
    return False


if __name__ == '__main__':
    persons_coords = [[1, 2, 3, 4]]
    areas = [[1111, 0], [1920, 0], [1920, 1080], [1111, 1080]]
    resolution = [1920, 1080]
    print(
        person_in_area(persons_coords=persons_coords,
                       areas=areas,
                       resolution=resolution,
                       w_thresh=0.25,
                       h_offset=0.4))
