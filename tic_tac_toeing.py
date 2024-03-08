import numpy as np
import scipy.signal as sig

class TicTacToe:
    def __init__(self, size: int) -> None:
        self.size = size
        self.grid = np.zeros(shape=(3,3))
        self.turn = 1
        self.winner = None
        self.game_in_progress = True
        self.verification_kernels = []
        self.generate_verification_kernels()

    def update_grid(self, row, col):
        self.grid[row, col] = 1 if self.turn == 1 else -1
        self.turn = 2 if self.turn == 1 else 1
        self.check_grid_state()

    def generate_verification_kernels(self):
        empty_kernel = np.zeros(self.size, self.size)
        horizontal_kernel = empty_kernel[0, :] = 1
        self.verification_kernels.append(horizontal_kernel)
        vertical_kernel = empty_kernel[:, 0]
        self.verification_kernels.append(vertical_kernel)
        diag_kernel1 = np.eye
        diag_kernel2 = np.flip(np.eye, axis=0)
        self.verification_kernels.append(diag_kernel1, diag_kernel2)

    def check_grid_state(self):
        padded_matrix = np.pad(self.grid, pad_width=2, mode='constant', constant_values=0)
        for kernel in self.verification_kernels:
            result = sig.convolve(padded_matrix, kernel)
            if result == 3:
                self.winner = 'Player 1'
                self.game_in_progress = False
                return 'Player 1 won'
            elif result == -3:
                self.winner = 'Player 2'
                self.game_in_progress = False
                return  'Player 2 won'
        else:
            if any(self.grid == 0):
                return 0
            else:
                self.game_in_progress = False
                return 'Stalemate you duckers'