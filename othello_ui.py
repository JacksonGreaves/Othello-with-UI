# Jackson Greaves jdgreave

import tkinter
import othello_setup

DEFAULT_FONT = ('Helvetica', 18)

class GameSpecifications:
    def __init__(self):

        self._spec_inputs = tkinter.Tk()

        self._spec_inputs.attributes('-topmost', True)
        
        front_label = tkinter.Label(
            master = self._spec_inputs,
            text = "OTHELLO SPECIFICATIONS\n(press 'OK' when done)",
            font = DEFAULT_FONT)
        
        front_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)

        col_label = tkinter.Label(
            master = self._spec_inputs,
            text = 'Number of Cols \n(even number 4-16)', font = DEFAULT_FONT)
        
        col_label.grid(
            row = 1, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._col_entry = tkinter.Entry(
            master = self._spec_inputs, width = 5, font = DEFAULT_FONT)

        self._col_entry.grid(
            row = 1, column = 1, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)

        row_label = tkinter.Label(
            master = self._spec_inputs,
            text = 'Number of Cols \n(even number 4-16)', font = DEFAULT_FONT)

        row_label.grid(
            row = 2, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._spec_inputs, width = 5, font = DEFAULT_FONT)

        self._row_entry.grid(
            row = 2, column = 1, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)

        first_move_label = tkinter.Label(
            master = self._spec_inputs,
            text = 'First Move\n(B or W)', font = DEFAULT_FONT)

        first_move_label.grid(
            row = 3, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._first_move_entry = tkinter.Entry(
            master = self._spec_inputs, width = 5, font = DEFAULT_FONT)

        self._first_move_entry.grid(
            row = 3, column = 1, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)

        top_left_label = tkinter.Label(
            master = self._spec_inputs,
            text = 'Top Left Puck\n(B or W)', font = DEFAULT_FONT)

        top_left_label.grid(
            row = 4, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._top_left_entry = tkinter.Entry(
            master = self._spec_inputs, width = 5, font = DEFAULT_FONT)

        self._top_left_entry.grid(
            row = 4, column = 1, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)
 
        win_how_label = tkinter.Label(
            master = self._spec_inputs,
            text = "How to Win\n('>' or '<')", font = DEFAULT_FONT)
        
        win_how_label.grid(
            row = 5, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        self._win_how_entry = tkinter.Entry(
            master = self._spec_inputs, width = 5, font = DEFAULT_FONT)

        self._win_how_entry.grid(
            row = 5, column = 1, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)

        button_frame = tkinter.Button(
            master = self._spec_inputs)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2,
            padx = 5, pady = 5,
            sticky = tkinter.S)

        start_button = tkinter.Button(
            master = button_frame, text = 'START', font = DEFAULT_FONT,
            command = self._on_start_button)

        start_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        self._spec_inputs.columnconfigure(1, weight = 1)
        self._spec_inputs.rowconfigure(5, weight = 1)

        self._start_clicked = False
        self._get_cols = 0
        self._get_rows = 0
        self._get_first_move = ''
        self._get_top_left = ''
        self._get_win_how = ''

    def show(self):
        self._spec_inputs.mainloop()

    def was_start_clicked(self) -> bool:
        return self._start_clicked

    def _get_cols(self):
        return self._cols

    def _get_rows(self):
        return self._rows

    def _get_first_move(self):
        return self._first_move

    def _get_top_left(self):
        return self.get_top_left

    def _get_win_how(self):
        return self._win_how

    def _is_even(self, num: int):
        return num % 2 == 0

    def _is_between(self, num: int):
        return num >= 4 and num <= 16

    def _is_BorW(self, move: str):
        return move == 'B' or move == 'W'

    def _is_g_or_l(self, symbol: str):
        return symbol == '>' or symbol == '<'

    def _on_start_button(self):
        '''
        Takes the values from the tkinter entries and,
           if all the inputs are valid, destroys the
           tkinter window
        '''
        self._start_clicked = True
        self._get_cols = int(self._col_entry.get())
        self._get_rows = int(self._row_entry.get())
        self._get_first_move = self._first_move_entry.get()
        self._get_top_left = self._top_left_entry.get()
        self._get_win_how = self._win_how_entry.get()

        if self._is_even(self._get_cols) and self._is_even(self._get_rows):
            if self._is_between(self._get_cols) and self._is_between(self._get_rows):
                if self._is_BorW(self._get_first_move) and self._is_BorW(self._get_top_left):
                    if self._is_g_or_l(self._get_win_how):
                        self._spec_inputs.destroy()

class GridApplication:
    def __init__(self, game: 'GameState', rows: int, cols: int):
        self.game = game
        self.rows = rows
        self.cols = cols
        
        self.possible_moves = self.game.getMoveCheck()

        self.canvas_width = 600
        self.canvas_height = 650
        
        self.cols_intake = 8
        self.rows_intake = 8
        self.first_move_intake = 'B'
        self.top_left_intake = 'B'
        self.win_how_intake = '>'

        self.winner = None
        
        self.black_pucks = self.game.numColor(rows, cols, 1)
        self.white_pucks = self.game.numColor(rows, cols, 2)

        self._root_window = tkinter.Tk()

        self.pucks_label = tkinter.Label(
            master = self._root_window,
            text = "Black: {} White: {}".format(self.black_pucks, self.white_pucks),
            font = DEFAULT_FONT)
        
        self.pucks_label.grid(
            row = 0, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = self.canvas_width, height = self.canvas_height,
            background = '#009900')
        
        self._canvas.grid(
            row = 1, column = 0, padx = 5, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self.bottom_label = tkinter.Label(
            master = self._root_window,
            text =  "{}'s turn".format(self.game.turnToString()),
            font = DEFAULT_FONT)

        self.bottom_label.grid(
            row = 2, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 0)

    def start(self) -> None:
        self._input_button_text = 'Input Game Specifications to Play!'
        self._game_started = False
        self._root_window.mainloop()

    def _make_fractions(self) -> None:
        '''
        Returns a list containing the total pixel height and
           width, and the fractional pixel height and width
           in a list
        '''
        fractions = []
        
        self.canvas_width = self._canvas.winfo_width()
        self.canvas_height = self._canvas.winfo_height()
        fractions.append(self.canvas_width)
        fractions.append(self.canvas_height)
        
        rowSize = (self.canvas_height / self.rows)
        colSize = (self.canvas_width / self.cols)
        fractions.append(rowSize)
        fractions.append(colSize)

        return fractions
    
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''
        Calls the _make_fractions function and uses
           the _draw_lines function
        '''
        self.possible_moves = self.game.getMoveCheck()
        fractions = self._make_fractions()
        self._draw_lines(fractions)
        self._draw_pucks(fractions)

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''
        Calculates the row and column of a click on the board
            and calls on _check_canvas_input()
        '''
        
        fractions = self._make_fractions()
        click_point = [event.x, event.y]
        for row in range(self.rows):
            for col in range(self.cols):
                if click_point[0] > self._make_xy_vals(fractions, 'X', col):
                    if click_point[0] < self._make_xy_vals(fractions, 'X', col + 1):
                        if click_point[1] > self._make_xy_vals(fractions, 'Y', row):
                            if click_point[1] < self._make_xy_vals(fractions, 'Y', row + 1):
                                self._check_canvas_input([row, col])

    def _check_canvas_input(self, RandC: [int, int]):
        '''
        Takes the row and column of the user's input and
           checks to see if it is in the game's list of possible
           moves; If so, the pucks are flipped, if no moves are left
           for the player, it switches player, and if there are no
           moves for either player, the game ends
        '''
        moves = self.game.getMoveCheck()
        if not self.game.endGame():
            if not self.game.noMoves():
                if self.game.checkBoardMove(RandC):
                    flips = self.game.compileFlips(moves, RandC)
                    self.game.makeFlips(flips)
                    self.game.switchPlayer()
                    if not self.game.areMoves():
                        self.game.switchPlayer()
        self.black_pucks = self.game.numColor(rows, cols, 1)
        self.white_pucks = self.game.numColor(rows, cols, 2)
        moves = self.game.getMoveCheck()
        if len(moves) == 0:
            self.winner = self.game.whoWon()
            self.bottom_label['text'] = '{} Wins!'.format(self.winner)
        else:
            self.bottom_label['text'] = "{}'s turn".format(self.game.turnToString())
        self.pucks_label['text'] = "Black: {} White: {}".format(self.black_pucks, self.white_pucks)
        self._draw_pucks(self._make_fractions())
        

    def _make_xy_vals(self, fractions: [float], xOrY: str, num: int) -> float:
        '''
        Takes the fractional values of the current board, a string
           specifying whether the return will be for an X or Y value,
           and returns the fractional value multiplied by an integer
           for the row/column number
        '''
        if xOrY == 'X':
            return fractions[3] * num
        if xOrY == 'Y':
            return fractions[2] * num

    def _draw_lines(self, fractions: [float]):
        '''
        Deletes everything on the canvas and calls on the
           _make_line() function to create a grid
        '''
        self._canvas.delete(tkinter.ALL)

        for row in range(self.rows - 1):
            self._make_line(fractions, 0, row + 1)
        for col in range(self.cols - 1):
            self._make_line(fractions, 1, col + 1)
        
    def _make_line(self, fractions: [float], rOrC: int, num: int) -> None:
        '''
        Draws a vertical or horizontal line (specified by rOrC,
           0 for horizontal or 1 for vertical)
        '''
        if rOrC == 0:
            self._canvas.create_line(0, self._make_xy_vals(fractions, 'Y', num),
                                     fractions[0],
                                     self._make_xy_vals(fractions, 'Y', num),
                                     fill = 'black')
        elif rOrC == 1:
            self._canvas.create_line(self._make_xy_vals(fractions, 'X', num), 0,
                                     self._make_xy_vals(fractions, 'X', num),
                                     fractions[1],
                                     fill = 'black')

    def _draw_pucks(self, fractions: [float]):
        '''
        Calls on the _make_puck function for all pucks
           in the current board
        '''
        for row in range(self.rows):
            for col in range(self.cols):
                if self.game.board[row][col] == 1:
                    self._make_puck(fractions, 1, [row, col])
                elif self.game.board[row][col] == 2:
                    self._make_puck(fractions, 2, [row, col])
        
    def _make_puck(self, fractions: [float], bOrW: int, xAndY: [int]):
        '''
        Creates a black or white oval on the board
        '''
        if bOrW == 1:
            self._canvas.create_oval(self._make_xy_vals(fractions, 'X', xAndY[1]),
                                 self._make_xy_vals(fractions, 'Y', xAndY[0]),
                                 self._make_xy_vals(fractions, 'X', xAndY[1] + 1),
                                 self._make_xy_vals(fractions, 'Y', xAndY[0] + 1),
                                 outline="black",
                                 fill="black", width=1)
        if bOrW == 2:
            self._canvas.create_oval(self._make_xy_vals(fractions, 'X', xAndY[1]),
                                 self._make_xy_vals(fractions, 'Y', xAndY[0]),
                                 self._make_xy_vals(fractions, 'X', xAndY[1] + 1),
                                 self._make_xy_vals(fractions, 'Y', xAndY[0] + 1),
                                 outline="black",
                                 fill="white", width=1)

if __name__ == '__main__':
    inputs = GameSpecifications()
    inputs.show()
    rows = inputs._get_rows
    cols = inputs._get_cols
    first_move = inputs._get_first_move
    top_left = inputs._get_top_left
    win_how = inputs._get_win_how

    new_game = othello_setup.startGame(rows, cols, first_move,
                                       top_left, win_how)
    
    app = GridApplication(new_game, rows, cols)
    app.start()
