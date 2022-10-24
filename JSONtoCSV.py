def jtc(savedir):
  
  import re
  import os
  import glob

  savedir = savedir

  path_w = os.path.join("./",savedir,"data.csv")

  for p in glob.glob(os.path.join("./",savedir,"*.json")) :

    str = open(p).read()
    str = re.sub('{".*pose_keypoints_2d":\[', '', str)
    str = re.sub('\],"face_keypoint.*', '', str)
    #print(str)

    with open(path_w, mode='a') as file :
      file.write(p)
      file.write(", ")
      file.write(str)
      file.write('\n')


