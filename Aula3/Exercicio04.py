import threading
import time
import os
from PIL import Image, ImageDraw


def mandelbrot(fractal_name, width, height):
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            c = complex(-2 + (x / width) * 3, -1.5 + (y / height) * 3)
            z = 0
            iteration = 0
            max_iteration = 100

            while abs(z) <= 2 and iteration < max_iteration:
                z = z * z + c
                iteration += 1

            color = 255 - int(iteration * 255 / max_iteration)
            draw.point([x, y], (color, color, color))

    image.save(f'{os.path.expanduser("~")}/Desktop/{fractal_name}.png')


def julia(fractal_name, width, height):
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    c = complex(-0.7, 0.27015)

    for x in range(width):
        for y in range(height):
            z = complex(-1.5 + (x / width) * 3, -1.5 + (y / height) * 3)
            iteration = 0
            max_iteration = 100

            while abs(z) <= 2 and iteration < max_iteration:
                z = z * z + c
                iteration += 1

            color = 255 - int(iteration * 255 / max_iteration)
            draw.point([x, y], (color, color, color))

    image.save(f'{os.path.expanduser("~")}/Desktop/{fractal_name}.png')


def burning_ship(fractal_name, width, height):
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            c = complex(-2 + (x / width) * 3, -1.5 + (y / height) * 2)
            z = 0
            iteration = 0
            max_iteration = 100

            while abs(z) <= 2 and iteration < max_iteration:
                z = complex(abs(z.real), abs(z.imag)) ** 2 + c
                iteration += 1

            color = 255 - int(iteration * 255 / max_iteration)
            draw.point([x, y], (color, color, color))

    image.save(f'{os.path.expanduser("~")}/Desktop/{fractal_name}.png')


def main():
    width, height = 800, 800
    start_time = time.time()

    threads = [
        threading.Thread(target=mandelbrot, args=("Mandelbrot", width, height)),
        threading.Thread(target=julia, args=("Julia", width, height)),
        threading.Thread(target=burning_ship, args=("Burning_Ship", width, height))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Tempo total com threads: {time.time() - start_time} segundos')


if __name__ == "__main__":
    main()
