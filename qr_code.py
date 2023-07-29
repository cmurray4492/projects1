"""QR Code Generator"""
import qrcode


class MyQR:
    '''QR Code Class'''

    def __init__(self, size: int, padding: int) -> None:
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str) -> None:
        '''Creates a custom QR Code'''
        user_input: str = input('Enter text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            print(f"Successfully create QR Code for ({file_name})")
        except Exception as e:
            print(f'Error: {e}')


def main():
    '''Main program entry point'''
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr('sample.png',
                   fg="black",
                   bg='white')


if __name__ == '__main__':
    main()
