from __future__ import print_function

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # This will hide those Keras messages

"""
    InvceptionV3 has input (299, 299, 3) ((in case the environment is configured to have the channel at the end)
"""


from modules.helper import subfolder_names

res = subfolder_names("../local/data/dataset")

print(res)
