import cv2
from pathlib import Path

def main():
    image_path = Path(r"C:\Users\USER\Desktop\image\Happy.jpg")

    if not image_path.exists():
        print("Image file does not exist.")
        return

    color_image = cv2.imread(str(image_path))

    if color_image is None:
        print("Failed to load image. Check the file path or file format.")
        return

    cartoon_style_selection = "1"

    if cartoon_style_selection == "1":
        # Enhance clarity with stronger edge preservation and contrast boost
        cartoon_image = cv2.stylization(color_image, sigma_s=100, sigma_r=0.1)
        output_path = image_path.parent / "cartoon_style_1.jpg"
        cv2.imwrite(str(output_path), cartoon_image)
        print(f"Cartoon style 1 image saved at: {output_path}")

    elif cartoon_style_selection == "2":
        cartoon_image = cv2.stylization(color_image, sigma_s=60, sigma_r=0.5)
        output_path = image_path.parent / "cartoon_style_2.jpg"
        cv2.imwrite(str(output_path), cartoon_image)
        print(f"Cartoon style 2 image saved at: {output_path}")

    else:
        print("Invalid style selection.")

if __name__ == "main":
    main()