from PIL import Image

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
