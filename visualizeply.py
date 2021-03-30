import numpy as np
import open3d as o3d
   
   
print("Load a ply point cloud, print it, and render it")
pcd = o3d.read_point_cloud("1.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.draw_geometries([pcd])