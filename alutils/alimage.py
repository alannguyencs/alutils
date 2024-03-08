from PIL import Image
import numpy as np

def concatenate_image(pil_image_a, pil_image_b, direction='HORIZONTAL'):
    assert(direction=='HORIZONTAL' or direction=='VERTICAL')
    (wa, ha) = pil_image_a.size
    (wb, hb) = pil_image_b.size

    if direction == 'HORIZONTAL':
        assert(ha==hb)
        new_image = Image.new('RGB', (wa + wb, ha))
        new_image.paste(pil_image_a, (0, 0))
        new_image.paste(pil_image_b, (wa, 0))
    else:
        assert (wa == wb)
        new_image = Image.new('RGB', (wa, ha + hb))
        new_image.paste(pil_image_a, (0, 0))
        new_image.paste(pil_image_b, (0, ha))

    return new_image


def embed_image_mask(image, mask):
    np_image = np.array(image).astype('float64')
    np_mask = np.array(mask).astype('float64')
    np_mask = (np_mask * 3 + np_image) / 4.0
    np_mask[np_mask > 255] = 255
    out = Image.fromarray(np_mask.astype('uint8'), 'RGB')
    return out

def stack_images(pil_images, unit_w=256, unit_h=256, GAP=16, direction='VERTICAL'):
    assert (direction == 'HORIZONTAL' or direction == 'VERTICAL')
    if direction=='VERTICAL':
        new_image = Image.new('RGB', (unit_w, len(pil_images) * (unit_h + GAP) - GAP), (255, 255, 255))
        for i, image in enumerate(pil_images):
            image = image.resize((unit_w, unit_h), Image.ANTIALIAS)
            new_image.paste(image, (0, (unit_h + GAP) * i))

    elif direction=='HORIZONTAL':
        new_image = Image.new('RGB', (len(pil_images) * (unit_w + GAP) - GAP, unit_h), (255, 255, 255))
        for i, image in enumerate(pil_images):
            # print (image.size)
            image = image.resize((unit_w, unit_h), Image.ANTIALIAS)
            # if i > 0:
            #     image = image.crop((22, 3, 253, 241))
            #     image = image.resize((SIZE, SIZE), Image.ANTIALIAS)
            new_image.paste(image, ((unit_w + GAP) * i, 0))
    return new_image

def append_images(img_1, img_2, GAP=16):
    if img_1 == None: return img_2
    (w_1, h_1) = img_1.size
    (w_2, h_2) = img_2.size
    assert (h_1 == h_2)
    img_new = Image.new('RGB', (w_1 + GAP + w_2, h_1), (255, 255, 255))
    img_new.paste(img_1, (0, 0, w_1, h_1))
    img_new.paste(img_2, (w_1 + GAP, 0, w_1 + GAP + w_2, h_2))
    return img_new
    
def stack_in_row(images, GAP=16):
    new_image = None
    for image in images:
        new_image = append_images(new_image, image, GAP)
    return new_image

def make_square(image, square_size=256, fill_color=(255, 255, 255)):
    """
    Aligns a PIL Image to a square image with padding.

    Parameters:
    - image: PIL.Image object, the original image to be aligned.
    - min_size: int, the size of the sides of the square canvas. Default is 256.
    - fill_color: tuple, the color of the padding. Default is white (255, 255, 255).

    Returns:
    - square_image: PIL.Image object, the original image centered on a square canvas with padding.
    """
    x, y = image.size
    size = max(square_size, x, y)
    new_image = Image.new('RGB', (size, size), fill_color)
    new_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))
    new_image = new_image.resize((square_size, square_size), Image.LANCZOS)
    return new_image