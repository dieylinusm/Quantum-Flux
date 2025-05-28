# Quantum Flux

Quantum Flux is a unique puzzle game where players manipulate quantum particles (Electrons, Protons, and Neutrons) on a grid to achieve quantum entanglement. The goal is to arrange particles by swapping adjacent ones to create balanced configurations, progressing through increasingly challenging levels.

## Features
- **Dynamic Gameplay**: Swap particles to balance quantum states on a 5x5 grid.
- **Progressive Difficulty**: Levels increase in complexity with more particles as you advance.
- **Minimalist Design**: Clean visuals with Pygame for smooth browser-based performance.
- **Scoring System**: Earn points for swaps and level completions.

## Installation
1. Ensure Python 3.8+ and Pygame are installed:
   ```bash
   pip install pygame
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/quantum-flux.git
   ```
3. Run the game:
   ```bash
   python quantum_flux.py
   ```

## How to Play
- **Objective**: Arrange particles so each type (Electron, Proton, Neutron) has an even number on the grid.
- **Controls**:
  - Click a particle to select it, then click an adjacent particle to swap.
  - Adjacent means one cell up, down, left, or right.
- **Scoring**:
  - 10 points per swap.
  - 100 points for completing a level.
- **Game Over**: Press 'R' to restart if you want to try again.

## Browser Compatibility
This game is built with Pyodide compatibility for browser-based execution. No local file I/O or network calls are used, ensuring smooth performance in web environments.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure code follows PEP 8 guidelines and includes relevant tests.

## Sponsor
Support the development of Quantum Flux by becoming a GitHub Sponsor! Your contributions help maintain and improve this unique game.

[Become a Sponsor](https://github.com/sponsors/yourusername)

## License
MIT License. See [LICENSE](LICENSE) for details.