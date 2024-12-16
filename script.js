// Create the game container
const body = document.body;
const gameContainer = document.createElement("div");
gameContainer.style.display = "grid";
gameContainer.style.gridTemplateColumns = "200px 200px 200px";
gameContainer.style.gap = "5px";
body.appendChild(gameContainer);

// Game variables
const board = Array(9).fill(null); // Array to store X and O values
let currentPlayer = "X"; // Tracks the current player
let gameActive = true;

// Create the game cells
for (let i = 0; i < 9; i++) {
  const cell = document.createElement("div");
  cell.style.width = "200px";
  cell.style.height = "200px";
  cell.style.border = "4px solid black";
  cell.style.display = "flex";
  cell.style.justifyContent = "center";
  cell.style.alignItems = "center";
  cell.style.fontSize = "70px";
  cell.style.cursor = "pointer";
  cell.dataset.index = i; // Set the index for each cell

  cell.addEventListener("click", () => handleCellClick(cell));
  gameContainer.appendChild(cell);
}

// Function to handle cell click
function handleCellClick(cell) {
  const index = cell.dataset.index;

  // Check if the cell is already filled or if the game is inactive
  if (board[index] || !gameActive) return;

  // Update board state and UI
  board[index] = currentPlayer;
  cell.textContent = currentPlayer;

  // Check if the current player wins
  if (checkWinner()) {
    alert(`${currentPlayer} wins!`);
    gameActive = false;
    return;
  }

  // Check if it's a draw
  if (board.every((cell) => cell)) {
    alert("It's a draw!");
    gameActive = false;
    return;
  }

  // Switch player
  currentPlayer = currentPlayer === "X" ? "O" : "X";
}

// Function to check for a winner
function checkWinner() {
  const winningCombinations = [
    [0, 1, 2], // Top row
    [3, 4, 5], // Middle row
    [6, 7, 8], // Bottom row
    [0, 3, 6], // Left column
    [1, 4, 7], // Middle column
    [2, 5, 8], // Right column
    [0, 4, 8], // Diagonal from top-left
    [2, 4, 6], // Diagonal from top-right
  ];

  // Check if any winning combination is satisfied
  return winningCombinations.some((combo) =>
    combo.every((index) => board[index] === currentPlayer)
  );
}

// Add a reset button
const resetButton = document.createElement("button");
resetButton.textContent = "Reset Game";
resetButton.style.marginTop = "20px";
body.appendChild(resetButton);

resetButton.addEventListener("click", () => {
  // Reset game state
  board.fill(null);
  currentPlayer = "X";
  gameActive = true;

  // Clear all cells
  Array.from(gameContainer.children).forEach((cell) => {
    cell.textContent = "";
  });
});
