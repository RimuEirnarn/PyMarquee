"""Python Marquee"""
from os import get_terminal_size
from time import sleep
from argh import ArghParser, arg


class Marquee:
    '''Marquee'''

    def __init__(self, text: str):
        self._data = text

    def mainloop(self):
        """Main loop"""
        # Only works on linux?
        textln = len(self._data)
        pos = 0
        if textln >= get_terminal_size()[0]:
            raise Exception("Cannot do marquee, text is too big")
        while True:
            try:
                width = get_terminal_size()[0]
                if pos >= width:
                    pos = 0
                paddln = pos
                padd = " "*paddln
                out = padd+self._data
                overflow = self._data[-(len(out)-width) -
                                      1:] if len(out) >= width else ""
                out = overflow + \
                    out[len(overflow)*1:width] if len(out) >= width else out
                pos += 1
                print(f'{out}', end="\r", flush=True)
                sleep(0.09)
                print("\033[2K", end='\r', flush=True)
            except (ValueError, EOFError, KeyboardInterrupt, TypeError):
                print("\033[2K", end='\n', flush=True)
                # print(f"{type(exc).__name__}: {str(exc)}")
                break


@arg("text", help="Text to marquee")
def main(text: str):
    """Python Marquee"""
    Marquee(text).mainloop()


if __name__ == "__main__":
    parser = ArghParser()
    parser.set_default_command(main)
    parser.dispatch()
