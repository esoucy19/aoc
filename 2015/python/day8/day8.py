import codecs
import functools
import string

from dataclasses import dataclass

example = r'''"""abc""aaa\"aaa""\x27"'''


@dataclass
class Scanner:
    in_str: str  # string to scan
    out_str: str = ""  # resulting string
    tok: str = ""  # token being scanned
    pos: int = 0  # position of the scanner
    crs: int = 0  # position of the forward cursor

    @property
    def current(self) -> str:
        return self.in_str[self.pos]

    def consume_token(self) -> None:
        self.pos = self.crs + 1
        self.crs = self.pos
        self.out_str += self.tok
        self.tok = ""

    def peek(self, n: int = 1, advance: bool = False) -> str | None:
        next_crs = self.crs + n
        if next_crs >= self._l:
            res = None
        else:
            res = self.in_str[self.crs + 1 : next_crs + 1]
            if advance:
                self.crs = next_crs
        return res

    def advance(self, n: int = 1) -> str | None:
        return self.peek(n=n, advance=True)

    @functools.cached_property
    def _l(self) -> int:
        return len(self.in_str)

    def reset(self) -> None:
        self.out_str = ""
        self.tok = ""
        self.pos = 0
        self.crs = 0
        self._l = len(self.in_str)

    def scan(self) -> None:
        self.reset()
        while self.pos < self._l:
            cur = self.current
            match cur:
                case "\\":
                    nxt = self.advance()
                    match nxt:
                        case "\\":
                            self.tok = "\\"
                        case '"':
                            self.tok = '"'
                        case "x":
                            hex = self.advance(n=2)
                            if hex is None:
                                raise RuntimeError(
                                    "reached end of line while parsing token"
                                )
                            else:
                                is_hex = all(h in string.hexdigits for h in hex)
                                if is_hex:
                                    self.tok = chr(int(f"0x{hex}", 16))
                                else:
                                    raise ValueError(
                                        "unrecognized escape sequence `\\x" + hex + "`"
                                    )
                        case None:
                            raise RuntimeError(
                                "reached end of line while parsing token"
                            )
                        case _:
                            raise ValueError(
                                "unrecognized escape sequence `" + nxt + "`"
                            )
                case '"':
                    self.tok = ""
                case _:
                    self.tok = cur
            self.consume_token()

    def encode(self) -> None:
        self.reset()
        self.out_str += '"'
        while self.pos < self._l:
            cur = self.current
            match cur:
                case "\\":
                    self.tok = "\\\\"
                case '"':
                    self.tok = '\\"'
                case _:
                    self.tok = cur
            self.consume_token()
        self.out_str += '"'


if __name__ == "__main__":
    with open("./day8/input.txt") as f:
        lines = f.read().splitlines()
        total = 0
        for line in lines:
            if line:
                scanner = Scanner(line)
                scanner.encode()
                print()
                print(scanner.in_str)
                print(scanner.out_str)
                total += len(scanner.out_str) - len(scanner.in_str)
        print()
        print(total)
