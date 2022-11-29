# eafit uni map • ![GitHub top language](https://img.shields.io/github/languages/top/LuisForPresident/eafit-uni-map?style=plastic) ![GitHub](https://img.shields.io/github/license/LuisForPresident/eafit-uni-map?style=plastic) ![GitHub Release Date](https://img.shields.io/github/release-date/LuisForPresident/eafit-uni-map?style=plastic) ![Project for uni](https://img.shields.io/badge/project-for%20uni-yellow?style=plastic)

A command-line program that gives you a list of directions between places located in the campus of the Universidad EAFIT.

## Screenshot

![A screen capture of the main menu of the program.](./images/screenshot.png)

## Features
- Get directions from one place to another
- Choose destination from your favorite places
- See steps and time estimates for the trip
- Edit your favorite places (add or remove)
- See all-time stats (steps and time)

## Contributing
I'd appreciate critical feedback. Leave an issue (if I have not archived the repo) or… hmm… see if I've added an email address to my GitHub profile yet.

## Reason for being
As _the_ project for the practical course "Principles of Software Development" (ST0243).

Taught at EAFIT University (Medellín, Colombia).

By professor [Paola A. Vallejo-Correa](https://scholar.google.com/citations?user=S8xNhVoAAAAJ).

## Requirements
### System
Haven't tested yet… Works best on macOS and _probably_ Linux.

### Dependencies
1. `pick` for the "curses based interactive selection list in the terminal" ![PyPI - License](https://img.shields.io/pypi/l/pick?style=flat)

2. `networkx` for [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) ![PyPI - License](https://img.shields.io/pypi/l/networkx?style=flat)

## Authors
1. [Luis M. Torres-Villegas](https://www.github.com/LuisForPresident)
2. [Miguel Suárez-Obando](https://www.github.com/MSO2023)

## Run
1. Download the project
    ```shell
    git clone https://github.com/LuisForPresident/eafit-uni-map
    ```

2. Change directory
    ```shell
    cd eafit-uni-map
    ```

3. Install dependencies
    ```shell
    pip install -r requirements.txt
    ```

4. Change directory (again)
    ```shell
    cd eafit-uni-map
    ```

5. Run
    ```shell
    python3 main.py
    ```

## Caveats
- The file paths are relative. So you working directory must be `eafit-uni-map/eafit-uni-map`. Else, the files won't be found.
- The font size is small.
- Probably doesn't work well in Windows.
- While changing `curses` screens, the terminal is visible.
- `KeyboardInterrupt` errors are not accounted for, i.e., `Ctrl-C` exits the program.
- There is no option to reset stats to 0.

## Graph
![A colored version of the graph, generated with graphonline.ru/en](./images/colored-graph.png)

## License
Released under the BSD 3-Clause license.

## GitHub repo
https://github.com/LuisForPresident/eafit-uni-map/

## Related
- [Adrephos/EAFIT-maps](https://github.com/Adrephos/EAFIT-maps) (2021) [Java, JavaScript, Node.js, React]

- [sicomEAFIT/CampusMovil-EAFIT](https://github.com/sicomEAFIT/CampusMovil-EAFIT) (2015) [Objective-C, Java, Ruby]

## Thanks
- [Wang Dàpéng](https://github.com/wong2) for the [`pick`](https://pypi.org/project/pick/) module

- [Viviana Hoyos-Sierra](https://github.com/Vivi-Hoyos2710) (TA) for the initial implementation of Dijkstra’s algorithm

- [Alejandro Ríos-Muñoz](https://github.com/alejoriosm04) for his helpful advice
