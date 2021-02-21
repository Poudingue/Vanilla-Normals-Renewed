from time import time

from PIL import Image
import numpy as np
import os


def normalize(path, depth):
    local_nb = 0
    if os.path.isdir(path):
        if os.path.islink(path):
            print(" " * depth + path + " is a symbolic link", end='\r')
            return

        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                if item not in ["colormap", "effect", "gui", "font", ".git"]:
                    local_nb += normalize(full_path, depth + 1)
                continue

            elif os.path.isfile(full_path):
                filename = item.split(".")[0]
                extension = '.'.join(item.split('.')[1:])
                if extension != "png":
                    print(" " * depth + "Not a png : " + item, end='\r')
                    continue
                if filename.endswith("_n"):
                    img = Image.open(full_path).convert("RGBA")
                    arr = np.asarray(img, dtype=np.float) / 255

                    # Convert to -1;+1 range (normals)
                    width, height, depth = arr.shape
                    # Only edit R and G channels
                    arr[:, :, 0:2] = 2 * arr[:, :, 0:2] - 1
                    arr_norm = np.linalg.norm(arr[:, :, 0:2], axis=2)
                    arr_norm = np.expand_dims(arr_norm, axis=2)
                    if (arr_norm > 1).any():
                        print(" " * depth + "Normalizing %s pixels (%s%% of image)" %
                              (np.sum(arr_norm > 1),
                               100 * np.sum(arr_norm > 1) / (width * height))
                              )
                        arr_norm[arr_norm <= 1] = 1
                        # Don’t touch the blue channel, it’s for ao
                        arr[:, :, 0:1] /= arr_norm
                        arr[:, :, 0:2] += 1
                        arr[:, :, 0:2] /= 2
                        arr = np.ndarray.astype(255 * arr + 0.4999999, dtype=np.uint8)

                        print(" " * depth + "Saving : %s" % item)
                        Image.fromarray(arr).save(full_path, optimize=True)
                        local_nb += 1
                else:
                    pass

    return local_nb


curr_path = os.path.abspath(".")
total_nb = normalize(curr_path, depth=0)
print("Finished, total of %s files repainted" % total_nb)
