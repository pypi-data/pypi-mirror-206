import cv2
from material_zui.image.data import MAX_MP
from material_zui.image.index import get_images
from material_zui.image.upscale import get_image_ratio_to_max_mp


def save_upscale_toJpg(directory_path:  str, new_directory_path: str = '', max_mp: int = MAX_MP) -> None:
    new_directory_path = new_directory_path if new_directory_path else directory_path
    images = get_images(directory_path)
    for index, image in enumerate(images):
        ratio = get_image_ratio_to_max_mp(image, max_mp)
        jpg_dir = f'{new_directory_path}/{index}.jpg'
        upscale_image = cv2.resize(
            image, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_CUBIC)  # type: ignore
        cv2.imwrite(jpg_dir, upscale_image)
        print(index+1, jpg_dir, ratio)

# def save_upscale_toJpg(directory_path:  str, new_directory_path: str = '', max_mp: int = MAX_MP) -> None:
#     new_directory_path = new_directory_path if new_directory_path else directory_path
#     images = get_images(directory_path)
#     image_paths = get_image_paths(directory_path)
#     for index, image in enumerate(images):
#         ratio = get_image_ratio_to_max_mp(image, max_mp)
#         image_url = upscale(image_paths[index], ratio)
#         png_dir = f'{new_directory_path}/{index}.png'
#         jpg_dir = f'{new_directory_path}/{index}.jpg'
#         download(image_url, png_dir)
#         to_jpg(png_dir, jpg_dir)
#         print(index+1, jpg_dir, ratio)
