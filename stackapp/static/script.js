// Get the canvas element
const canvas = document.getElementById('cubeCanvas');
canvas.width = canvas.clientWidth;
canvas.height = canvas.clientHeight;

// Create a Three.js scene
const scene = new THREE.Scene();

// Create a camera and position it
//const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 5);
//camera.position.z = 2;

const camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 50);
camera.position.z = 2;


// Create a WebGL renderer
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });

// Set canvas background color to white
renderer.setClearColor(0xffffff);

// Create a cube and add it to the scene
const geometry = new THREE.BoxGeometry(1, 1, 1, 128, 128, 128);
const material = new THREE.MeshBasicMaterial({ color: 0x44aa88 });
//const cube = new THREE.Mesh(geometry, material);

// Create an array to store materials for each face
const materials = [
    new THREE.MeshBasicMaterial({ color: 0x44aa88 }), // Default color
    new THREE.MeshBasicMaterial({ color: 0x44aa88 }),
    new THREE.MeshBasicMaterial({ color: 0x44aa88 }),
    new THREE.MeshBasicMaterial({ color: 0x44aa88 }),
    new THREE.MeshBasicMaterial({ color: 0x44aa88 }),
    new THREE.MeshBasicMaterial({ color: 0x44aa88 }),
];

// Apply materials to the cube's geometry
const cube = new THREE.Mesh(geometry, materials);

// Set the cube's position to center it within the canvas
cube.position.set(0, 0, 0);

scene.add(cube);

// Function to update the cube's color
function updateCubeColor() {
    const color1 = document.getElementById('wall1-color').value;
    const color2 = document.getElementById('wall2-color').value;
    const color3 = document.getElementById('wall3-color').value;
    const color4 = document.getElementById('wall4-color').value;
    const color5 = document.getElementById('wall5-color').value;
    const color6 = document.getElementById('wall6-color').value;

    const colors = [color1, color2, color3, color4, color5, color6];

    // Set cube material colors
    colors.forEach((color, index) => {
        materials[index].color.set(color);
    });
}

// Add event listener to the "Change Digits" button
document.getElementById('changeDigits').addEventListener('click', () => {
    updateCubeColor();
});

// Function to animate the cube
function animate() {
    requestAnimationFrame(animate);

    // Rotate the cube
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    // Render the scene with the camera
    renderer.render(scene, camera);
}

// Call the animate function to start the animation loop
animate();
