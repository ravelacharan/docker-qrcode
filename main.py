"""This is the driver file of the project"""
from qrcode_generator import generate_qr_code
from file_operations import get_current_working_directory, join_path, make_dir
from pil import save_image, watermark
from config import Config


def main():
    """Driver function"""

    qrcode = generate_qr_code(Config.QR_CODE_DATA)
    destination_path = join_path([get_current_working_directory(), Config.QR_CODE_FILE_PATH, Config.QR_CODE_FILE_NAME])

    for i in range(0, 1):
        while True:
            try:
                qrcode = watermark(qrcode)
                save_image(qrcode, destination_path)

                print("QR Code Generated Successfully!!!\n")
                print("File saved to the path ", destination_path)
            except FileNotFoundError:

                directory_path = join_path([get_current_working_directory(), Config.QR_CODE_FILE_PATH])
                make_dir(directory_path)
                continue

            break


if __name__ == '__main__':
    main()
