# game_of_stacks
A web game, where the player can add his one and only cube to the stack. Choose whisely.


Game under construction. The plan is:

-build a Flask app with a backend with game data and logic
-add javascript canvas with 3d representation of the tower (stack)
-add simple tower-scrolling, according to the tower floor.


Rules:
One player (registered by email) can add only one cube.
The player can customize each wall of the cube and decide its position on the stack floor.
The cube is always added on top of the stack.
Once the cube is placed, it stays there forever.
Stack is 2 x 2 cubes big on the floor plan. Height is unlimited. One cube is one floor of the stack.
After the placing of the cube into the stack, a few things happen:
1. The player gets notified about his stack neighbors. His neighbors also get the notification.
2. A wall of a cube that is touching a neighboring cube is only visible to the neighbor and vice versa.
3. If the cube is the first on the floor, all the walls, apart from the bottom one, are visible to everybody until the other cubes appear.
4. When the next floor is built, only two walls of the cube are visible to the world, the rest are secrets that only neighbors know.
The player can visit any floor of the stack at any time and from any angle.
The player cannot change his cube.
The player can open and view the hidden walls of his neighbors.
The player can watch the stack grow.


Cube rules:
-wall of the cube can be either text in a 40x40 field or an icon of 256x256 pixels. app will offer conversions from image to icon at some point.
-cube colors will be picked out of the palette.
-text color will be picked either as black, white, or in opposition to cub's color.
-special gold cubes, double the size, will be offered randomly or to specific users.
