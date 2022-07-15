import gdown

import os

# os.mkdir('/dataset')
# https://drive.google.com/file/d/1YM4w1FP0gWbe_sTd_A0j2njtZLtD0SUw/view?usp=sharing



id = '1YM4w1FP0gWbe_sTd_A0j2njtZLtD0SUw'
# https://drive.google.com/file/d/1UA3BBXQcKh0zAwJYwVTTX0i3wE_Fd43y/view?usp=sharing
# https://drive.google.com/file/d/17EAQ-L7BYZqIX5_APKHArcUvddkMIWzG/view?usp=sharing
url = 'https://drive.google.com/uc?id=17EAQ-L7BYZqIX5_APKHArcUvddkMIWzG'
output = 'train.zip'
gdown.download(url, output, quiet=False)
# https://drive.google.com/file/d/1PYf4vEWH74JMgkmJ3lEsFqHk6TtwiqNG/view?usp=sharing


# url = 'https://drive.google.com/uc?id=1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn'
# output = 'train.zip'
# gdown.download(url, output, quiet=False)


# url = 'https://drive.google.com/uc?id=1bxK5zgLn0_L8x276eKkuYA_FzwCIjb59'
# output = 'val.zip'
# gdown.download(url, output, quiet=False)

# url = 'https://drive.google.com/uc?id=1PFdW_VFSCfZ_sTSZAGjQdifF_Xd5mf0V'
# output = 'test.zip'
# gdown.download(url, output, quiet=False)