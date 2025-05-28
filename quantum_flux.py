import asyncio
import platform
import pygame
import random
import numpy as np

# Game constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 5
CELL_SIZE = 100
GRID_OFFSET_X = (WIDTH - GRID_SIZE * CELL_SIZE) // 2
GRID_OFFSET_Y = (HEIGHT - GRID_SIZE * CELL_SIZE) // 2
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
RED = (255, 64, 64)
GREEN = (64, 255, 64)

# Particle types
PARTICLE_TYPES = ["Electron", "Proton", "Neutron"]

class QuantumFlux:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Quantum Flux")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected = None
        self.level = 1
        self.score = 0
        self.game_over = False
        self.setup_level()

    def setup_level(self):
        # Clear grid
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        
        # Place particles randomly
        num_particles = self.level + 2
        for _ in range(num_particles):
            while True:
                x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
                if self.grid[y][x] is None:
                    self.grid[y][x] = random.choice(PARTICLE_TYPES)
                    break

    def check_win_condition(self):
        # Win if all particles are paired (simplified quantum entanglement simulation)
        particle_counts = {"Electron": 0, "Proton": 0, "Neutron": 0}
        for row in self.grid:
            for cell in row:
                if cell:
                    particle_counts[cell] += 1
        
        # Win condition: even number of each particle type
        return all(count % 2 == 0 for count in particle_counts.values())

    def swap_particles(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        self.grid[y1][x1], self.grid[y2][x2] = self.grid[y2][x2], self.grid[y1][x1]

    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw grid
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(
                    GRID_OFFSET_X + x * CELL_SIZE,
                    GRID_OFFSET_Y + y * CELL_SIZE,
                    CELL_SIZE - 5,
                    CELL_SIZE - 5
                )
                pygame.draw.rect(self.screen, WHITE, rect, 1)
                
                if self.grid[y][x]:
                    color = BLUE if self.grid[y][x] == "Electron" else RED if self.grid[y][x] == "Proton" else GREEN
                    pygame.draw.circle(
                        self.screen,
                        color,
                        rect.center,
                        CELL_SIZE // 3
                    )
                    text = self.font.render(self.grid[y][x][0], True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

        # Draw score and level
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))

        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to Restart", True, WHITE)
            self.screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))

        pygame.display.flip()

    def update_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                pos = pygame.mouse.get_pos()
                grid_x = (pos[0] - GRID_OFFSET_X) // CELL_SIZE
                grid_y = (pos[1] - GRID_OFFSET_Y) // CELL_SIZE
                if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                    if self.selected is None:
                        if self.grid[grid_y][grid_x] is not None:
                            self.selected = (grid_x, grid_y)
                    else:
                        # Check if adjacent
                        sx, sy = self.selected
                        if (abs(sx - grid_x) + abs(sy - grid_y)) == 1:
                            self.swap_particles(self.selected, (grid_x, grid_y))
                            self.score += 10
                            if self.check_win_condition():
                                self.level += 1
                                self.score += 100
                                self.setup_level()
                        self.selected = None
            elif event.type == pygame.KEYDOWN and self.game_over:
                if event.key == pygame.K_r:
                    self.__init__()

        self.draw()

async def main():
    game = QuantumFlux()
    while not game.game_over:
        game.update_loop()
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
