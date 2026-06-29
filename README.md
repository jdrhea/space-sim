# Space Sim

A lightweight gravity simulation built with Python and Pygame. The project models a central body and several orbiting planets using Newtonian gravity, letting you explore orbital motion and add your own planets interactively.

## Overview

Space Sim is a small educational project that visualizes gravitational attraction between bodies in a 2D environment. It starts with a central massive body and a few orbiting planets, then allows you to:

- observe how gravity influences motion,
- inspect planet data such as position, mass, velocity, and acceleration,
- place additional planets into the simulation with a right click.

## Features

- Real-time 2D gravitational simulation
- Central star with orbiting planets
- Interactive planet placement
- On-screen information panel for selected bodies
- Simple, dependency-light setup

## Requirements

- Python 3.8+
- Pygame

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jdrhea/space-sim.git
   cd space-sim
   ```

2. Install the Python dependency:

   ```bash
   pip install pygame
   ```

## Running the Simulation

Start the program with:

```bash
python3 space-sim.py
```

If you are using a different Python launcher, replace `python3` with the version you use locally.

## Controls

- Left-click a planet to display its current statistics in the information panel.
- Right-click anywhere in the simulation window to create a new randomly colored planet.
- Close the window to exit the program.

## What the Simulation Shows

The script uses a simplified gravity model where each body accelerates toward other bodies based on mass and distance. The simulation calculates:

- gravitational acceleration,
- velocity changes over time,
- orbital motion around the central body,
- basic orbital properties for the selected planet.

## Project Structure

- [space-sim.py](space-sim.py) — the main simulation script
- [LICENSE](LICENSE) — Apache License 2.0

## Customization Ideas

You can experiment with the simulation by changing values in the script, such as:

- the central body's mass,
- initial planet speeds,
- the playback speed,
- the scale of the simulation window.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
