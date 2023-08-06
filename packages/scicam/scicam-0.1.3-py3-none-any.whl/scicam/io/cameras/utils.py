import cv2
import time
import warnings

def mark_image(camera, img):    
    # signal it's the first frame afer a pause
    try:
        print(img.shape)
        # img[0, [0, 2, 4, 6]] = 255 
        # img[0, [1, 3, 5, 7]] = 0 
        # img[1, [0, 2, 4, 8]] = 0
        # img[1, [1, 3, 5, 7]] = 255
        # img[2, [0, 2, 4, 6]] = 255 
        # img[2, [1, 3, 5, 7]] = 0 
        # img[3, [0, 2, 4, 8]] = 0
        # img[3, [1, 3, 5, 7]] = 255
        img = cv2.putText(img, "error", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 5, 127, 5)


    except Exception as error:
        print(error)
        print(f"{camera} cannot mark frame")

    return img


def validate_img(img, target_shape=None):
    """
    Return 0 if the img is fine, 1 if it's None
    and 2 if it's not None but it has a shape different from the expected 
    """

    img_is_None = img is None or img.shape[0] is None
    image_is_corrupt=False
    if not img_is_None and target_shape is not None:
        image_is_corrupt = target_shape[0] != img.shape[0] or target_shape[1] != img.shape[1]


    if not img_is_None and not image_is_corrupt:
        return 0
    elif img_is_None:
        return 1
    elif image_is_corrupt:
        try:
            cv2.imwrite(f"/home/vibflysleep/{time.time()}-corrupt_image.png", img)
        except:
            print("Could not save corrupt image")

        return 2

def ensure_img(camera):
    print("Alert: img is None")
    before = time.time()
    camera.close()

    camera.open(idx=camera._idx)
    warnings.warn("Recursive call to next_image_default_timeit")
    (code, img), msec =camera._next_image_default_timeit()
    if img.shape[0] is None:

        print("img is still None, look below")
        print(img.shape)
        print(img)
        print("----- ------")

    after = time.time()
    lost_time = after - before
    print(f"Done in {lost_time} seconds")
    # img = mark_image(camera, img.copy())
    # cv2.imwrite(f"/home/vibflysleep/{camera.friendly_name}.png", img)
    return (code, img)


