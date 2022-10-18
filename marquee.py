from argh import ArghParser, arg
from os import get_terminal_size
from time import sleep

class Marquee:
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
                width, height = get_terminal_size()
                if pos >= width:
                    pos =  0
                paddln = pos
                padd = " "*paddln
                out = padd+self._data
                overflow = self._data[-(len(out)-width)-1:] if len(out) >= width else ""
                out = overflow + out[len(overflow)*1:width] if len(out) >= width else out
                pos += 1
                print(f'{out}', end="\r", flush=True)
                sleep(0.09)
                print("\033[2K", end='\r', flush=True)
            except Exception as exc:
                print("\033[1A\033[2K", end='', flush=True)
                # print(f"{type(exc).__name__}: {str(exc)}")
                break
            except KeyboardInterrupt:
                print("\033[1A\033[2K", end="", flush=True)
                break

@arg("text", help="Text to marquee")
def main(text: str):
    Marquee(text).mainloop()

if __name__ == "__main__":
    parser = ArghParser()
    parser.set_default_command(main)
    parser.dispatch()
