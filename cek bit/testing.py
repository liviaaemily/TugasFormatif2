from PIL import Image

def check_rgb_data(image_path):
    img = Image.open(image_path)
    width, height = img.size

    if width != 4 or height != 4:
        print("Gambar harus memiliki ukuran 4x4 piksel.")
        return

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            r, g, b = pixel

            # Output data RGB untuk setiap piksel
            print(f"Pixel ({x}, {y}):")
            print(f"R: {r}")
            print(f"G: {g}")
            print(f"B: {b}")
            print("---")

# Contoh pemanggilan fungsi untuk gambar dengan path "contoh_gambar.png"
check_rgb_data("output.png")