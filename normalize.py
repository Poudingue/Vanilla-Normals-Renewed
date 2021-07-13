import os
from time import time

import numpy as np
from PIL import Image


def normalize(path, depth):
    local_nb = 0
    if os.path.isdir(path):
        if os.path.islink(path):
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
                    continue
                if filename.endswith("_n"):
                    img = Image.open(full_path)

                    arr = np.asarray(img)
                    width, height, depth = arr.shape
                    # Keep alpha intact
                    removed_alpha = False
                    alpha8bit = None
                    if depth == 4:
                        # Get alpha channel
                        alpha8bit = arr[:, :, 3]
                        if (alpha8bit == 255).all():
                            # No need for alpha channel
                            print("No need for alpha channel, everything at 255")
                            arr = arr[:, :, :-1]
                            removed_alpha = True
                            alpha8bit = None

                    # Keep original array for comparison
                    original_arr = arr

                    arr = arr.astype(dtype=np.float) / 255

                    arr *= 2
                    arr -= 1

                    arr_norm = np.linalg.norm(arr[:, :, 0:3], axis=2)
                    arr_norm = np.expand_dims(arr_norm, axis=2)
                    if (arr_norm > 1).any() or removed_alpha:
                        proportion_incorrect = 100 * np.count_nonzero(arr_norm > 1) / (width * height)
                        arr_norm[arr_norm < 1] = 1
                        arr /= arr_norm

                        arr += 1
                        arr /= 2

                        # To avoid drift to negative values because of clamping (on red and green)
                        arr[0:2] = 0.999 + arr[0:2] * (254 / 255)

                        arr = np.ndarray.astype(255 * arr, dtype=np.uint8)
                        if alpha8bit is not None:
                            arr[:, :, 3] = alpha8bit
                        if (arr == original_arr).all():
                            print("Unchanged : %s" % item)
                        else:
                            proportion_changed = 100 * np.count_nonzero(arr != original_arr) / (width * height * depth)
                            print("Changed and saved %s" % item)
                            print("Proportion incorrect : %.2f%%" % proportion_incorrect)
                            print("Proportion changed : %.2f%%" % proportion_changed)
                            print("(%d values changed)" % np.count_nonzero(arr != original_arr))
                            Image.fromarray(arr).save(full_path, optimize=True)
                            local_nb += 1
                else:
                    pass

    return local_nb


t0 = time()
curr_path = os.path.abspath(".")
total_nb = normalize(curr_path, depth=0)
print("Finished, total of %s files repainted in %s seconds" % (total_nb, int(time() - t0)))
