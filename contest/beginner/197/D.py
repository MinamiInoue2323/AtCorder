import numpy as np

def rotation_o(u, t, deg=False):

    if deg == True:
        t = np.deg2rad(t)

    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])

    return  np.dot(R, u)

N = int(input())
x0,y0 = map(int,input().split())
x5,y5 = map(int,input().split())
center = [(x5 + x0) / 2, (y5 + y0) / 2]
start = np.array([x0 - center[0],y0 - center[1]])
ans = rotation_o(start,np.pi / (N / 2))+np.array(center)
print("{:.12f} {:.12f}".format(ans[0],ans[1]))