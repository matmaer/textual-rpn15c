#!/usr/bin/env python3

"""
A visual implementation of a classic 15c RPN calculator.
see [https://en.wikipedia.org/wiki/HP-15C]
or [https://www.hpmuseum.org/forum/archive/index.php?thread-19260.html]
looks like a real calculator.
"""

from textual import events, on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, Grid
from textual.reactive import var
from textual.widgets import Button, Digits, Label, Static

class HP_Button( Button ):
    def __init__(self, *args, **kwargs):
        super().__init__( id=kwargs["id"] )
        self.label = args[0]
        self.border_title = args[1]
        self.border_subtitle = args[2]



class RPN_CalculatorApp(App):
    """A working TUI calculator."""
    CSS_PATH = "rpn_15c.tcss"

    def compose(self) -> ComposeResult:
        """Add our buttons."""
        with Container(id="calculator"):
            with Horizontal(id="upper"):
                with Vertical(id="bezel"):
                    yield Digits("-8,8,8,8,8,8,8,8,8,8,", id="numbers", classes="lcd")
                    with Horizontal(id="status", classes="lcd"):
                        yield Label( "USER", id="user-state", classes="lcd")
                        yield Label( "f", id="f-shift-state", classes="lcd")
                        yield Label( "g", id="g-shift-state", classes="lcd")
                        yield Label( "BEGIN", id="begin-state", classes="lcd")
                        yield Label( "GRAD", id="grad-state", classes="lcd")
                        yield Label( "DMY", id="dmy-state", classes="lcd")
                        yield Label( "C", id="c-state", classes="lcd")
                        yield Label( "PRGM", id="prgm-state", classes="lcd")
                with Vertical(id="logo"):
                    yield Label("help", id="rpn-help")
                    yield Label("15C", id="rpn-model")
            calc_buttons =  Grid(id="buttons")
            calc_buttons.border_subtitle = "H E W L E T T • P A C K A R D"
            #calc_buttons.border_subtitle = "L A U T X E T • B A C K W A R D"
            with calc_buttons:
                yield HP_Button("√x", "A", "  x²   ", id="sqrt-x")
                yield HP_Button("eˣ", "B", "  LN   ", id="exp-x")
                yield HP_Button("10ˣ", "C", "  LOG  ", id="ten-x")
                yield HP_Button(" yˣ", "D", "   %   ", id="wye-x")
                yield HP_Button("1/x", "E", "  Δ%   ", id="inverse-x")
                yield HP_Button("CHS", " MATRIX", "  ABS  ", id="chs")
                yield HP_Button("7", "FIX", "  DEG  ", id="digit-7")
                yield HP_Button("8", "SCI", "  RAD  ", id="digit-8")
                yield HP_Button("9", "ENG", "  GRD  ", id="digit-9")
                yield HP_Button("÷", "SOLVE", "  x≤y  ", id="division")
                yield HP_Button("SST", "LBL", "  BST  ", id="sst")
                yield HP_Button("GTO", "HYP", " HYP⁻¹ ", id="gto")
                yield HP_Button("SIN", "DIM", " SIN⁻¹ ", id="sin")
                yield HP_Button("COS", "(i)", " COS⁻¹ ", id="cos")
                yield HP_Button("TAN", "I", " TAN⁻¹ ", id="tan")
                yield HP_Button("EEX", " RESULT", "   π   ", id="eex")
                yield HP_Button("4", "x ≷", "  S F  ", id="digit-4")
                yield HP_Button("5", "DSE", "  C F  ", id="digit-5")
                yield HP_Button("6", "ISG", "  F ?  ", id="digit-6")
                yield HP_Button("×", "∫ᵧˣ", "  x=0  ", id="multiplication")
                yield HP_Button("R/S", "PSE", "  P/R  ", id="rtos")
                yield HP_Button("GSB", "Σ", "  RTN  ", id="gsb")
                yield HP_Button("R↓", "PRGM", "  R↑  ", id="r-down")
                yield HP_Button("x ≷ y", "REG", "  RND  ", id="x-swap-y")
                yield HP_Button("←", " PREFIX", "  CLx  ", id="backspace")
                yield HP_Button("E\nN\nT\nE\nR", " RAN # ", " LSTx  ", id="enter")
                yield HP_Button("1", "→ R", "  → P  ", id="digit-1")
                yield HP_Button("2", "→H.MS", "  → H  ", id="digit-2")
                yield HP_Button("3", "→RAD", " →DEG  ", id="digit-3")
                yield HP_Button("−", "Re ≷ Im", "  TEST ", id="subtraction")
                yield HP_Button("ON", "", "", id="on")
                yield HP_Button("f", "", "       ", id="shift-f")
                yield HP_Button("g", "", "       ", id="shift-g")
                yield HP_Button("STO", " FRAC", "  INT  ", id="sto")
                yield HP_Button("RCL", " USER", "  MEM  ", id="rcl")
                yield HP_Button("0", "x!", "   x̄   ", id="digit-0")
                yield HP_Button("•", "s", "  ŷ,r  ", id="decimal")
                yield HP_Button("Σ+", "L.R.", "  Σ-   ", id="sum")
                yield HP_Button("+", "Py,x", " Cy,x  ", id="addition")

    def on_mount(self) -> None:
        self.query_one("#enter")

if __name__ == "__main__":
    RPN_CalculatorApp().run()
