import itertools

def generate_all_possible_rows():
    """Generates all possible rows for the 6x6 board with 2x1 dominos."""
    # All combinations of three dominos in a row (3*2 squares)
    dominos = ['00', '11']
    all_rows = [''.join(p) for p in itertools.product(dominos, repeat=3)]
    return all_rows

def is_valid_board(board):
    """Check if the board is a valid configuration."""
    for i in range(5):
        # Check if two adjacent rows have the same pattern at the same place
        for j in range(6):
            if board[i][j] == board[i + 1][j]:
                return False
    return True

def check_all_boards():
    """Check all possible boards for a fault line."""
    all_rows = generate_all_possible_rows()
    valid_boards_with_fault_lines = 0
    total_valid_boards = 0

    for board_rows in itertools.product(all_rows, repeat=6):
        board = np.array([list(row) for row in board_rows], dtype=int)
        if is_valid_board(board):
            total_valid_boards += 1
            if has_fault_line(board):
                valid_boards_with_fault_lines += 1

    return valid_boards_with_fault_lines, total_valid_boards

# Check all boards (Note: This can be very time-consuming)
valid_boards_with_fault_lines, total_valid_boards = check_all_boards()
valid_boards_with_fault_lines, total_valid_boards
