import pyrealsense2 as rs
import numpy as np    
import matplotlib.pyplot as plt
print("Environment is Ready")


# pipe = rs.pipeline()
# #cfg = rs.config()
# pipe.start()
# while True:
#     frames = pipe.wait_for_frames()
#     depth = frames.get_depth_frame()
#     width = depth.get_width()
#     height = depth.get_height()
#     dist = depth.get_distance(width/2,height/2)
#     print("Facing an object{0:.3} meters away".format(dist))

# pipe.stop()



# Setup:
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_device_from_file("stream4.bag")
profile = pipe.start(cfg)

# Skip 5 first frames to give the Auto-Exposure time to adjust
for x in range(5):
  pipe.wait_for_frames()
  
# Store next frameset for later processing:
frameset = pipe.wait_for_frames()

color_frame = frameset.get_color_frame()
depth_frame = frameset.get_depth_frame()

# Cleanup:
pipe.stop()
print("Frames Captured")

color = np.asanyarray(color_frame.get_data())
plt.rcParams["axes.grid"] = False
plt.rcParams['figure.figsize'] = [12, 6]
plt.imshow(color)
plt.show()




# # Setup:
# pipe = rs.pipeline()
# cfg = rs.config()
# cfg.enable_device_from_file("/home/tgiencov/Registration Codes/RealsensePython/stream1.bag")
# profile = pipe.start(cfg)

# # Skip 5 first frames to give the Auto-Exposure time to adjust
# for x in range(5):
#   pipe.wait_for_frames()
  
# # Store next frameset for later processing:
# frameset = pipe.wait_for_frames()
# depth_frame = frameset.get_depth_frame()

# # Cleanup:
# pipe.stop()
# print("Frames Captured")



# colorizer = rs.colorizer()
# # print(colorizer)
# colorized_depth = np.asanyarray(colorizer.colorize(depth_frame).get_data())
# print(colorized_depth)
# plt.rcParams["axes.grid"] = False
# plt.rcParams['figure.figsize'] = [8, 4]
# plt.imshow(colorized_depth)
# plt.show()
