"""QR Code Generator with user filename input"""
import qrcode


class MyQR:
    '''QR Code Class'''

    def __init__(self, size: int, padding: int) -> None:
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, fg: str, bg: str) -> None:
        '''Creates a custom QR Code'''
        user_input: str = input('Enter text for the QR Code: ')
        user_file_name_base: str = input('Enter a file name for the QR Code: ')
        user_file_name = user_file_name_base + '.png'

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(user_file_name)
            print(f"Successfully create QR Code for ({user_file_name})")
        except Exception as e:
            print(f'Error: {e}')


def main():
    '''Main program entry point'''
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr(fg="blue",
                   bg='white')


if __name__ == '__main__':
    main()
