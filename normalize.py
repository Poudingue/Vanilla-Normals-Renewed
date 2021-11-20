import os
from time import time, sleep

import numpy as np
from PIL import Image


def correct_resourcepack(path, depth):
    local_nb = 0
    if os.path.isdir(path):
        if os.path.islink(path):
            return

        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                #if item not in ["colormap", "effect", "gui", "font", ".git"]:
                local_nb += correct_resourcepack(full_path, depth + 1)
                continue

            elif os.path.isfile(full_path):
                filename = item.split(".")[0]
                extension = '.'.join(item.split('.')[1:])
                if extension != "png":
                    continue
                # Normals
                if remove_useless_alpha(full_path):
                    local_nb += 1
                if filename.endswith("_n"):
                    if correct_normals(full_path):
                        local_nb += 1
                else:
                    pass

    return local_nb


def remove_useless_alpha(file_path):
    img = Image.open(file_path)
    if img.mode == "P":
        img = img.convert("RGBA")
    if img.mode != "RGBA":
        return False
    arr = np.asarray(img)
    if len(arr.shape) < 3:
        print(f"Is {file_path} that a b&w image ?")
        sleep(1)
        return False
    width, height, depth = arr.shape
    if depth < 4:
        return False
    # Get alpha channel
    alpha8bit = arr[:, :, 3]
    if (alpha8bit == 255).all():
        # No need for alpha channel
        print("No need for alpha channel, everything is at 255")
        arr = arr[:, :, :3]
        print(f"Changed and saved {file_path}")
        # Image.fromarray(arr_normal).save(full_path, optimize=True)
        return True
    return False


def correct_normals(file_path):
    img = Image.open(file_path)
    arr = np.asarray(img)
    width, height, depth = arr.shape
    # Keep alpha intact
    removed_alpha = False
    alpha8bit = None
    if depth == 4:
        # Get alpha channel
        alpha8bit = arr[:, :, 3]
    # Keep original array for comparison
    original_arr = arr
    # Remove alpha channel if there is one
    arr_normal = arr[:, :, :3].astype(float) / 255
    arr_normal *= 2
    arr_normal -= 1
    arr_norm = np.linalg.norm(arr_normal, axis=2)
    arr_norm = np.expand_dims(arr_norm, axis=2)
    if (arr_norm > 1).any():
        proportion_incorrect = 100 * np.count_nonzero(arr_norm > 1) / (width * height)
        arr_norm[arr_norm < 1] = 1
        arr_normal /= arr_norm

        arr_normal += 1
        arr_normal /= 2

        # If dx or dy values deviate, it should be toward the center, not toward the extremes
        arr_normal[:, :, 0:2] += np.random.rand(width, height, 2) / 255

        arr = np.ndarray.astype(255 * arr_normal, dtype=np.uint8)
        if alpha8bit is not None:
            arr = np.stack((arr_normal, alpha8bit), axis=2)
        if (arr == original_arr).all():
            print(f"Unchanged : {file_path}")
        else:
            print(f"Changed and saved {file_path}")
            print("Proportion incorrect normals : %.2f%%" % proportion_incorrect)
            print(f"{np.count_nonzero(arr_normal != original_arr)} values changed")
            #Image.fromarray(arr_normal).save(full_path, optimize=True)
        return True
    return False


t0 = time()
curr_path = os.path.abspath(".")
for ii in range(256):
    print(f"Iteration {ii}")
    total_nb = correct_resourcepack(curr_path, depth=0)
print(f"Finished, total of {total_nb} files repainted in {int(time() - t0)} seconds")
