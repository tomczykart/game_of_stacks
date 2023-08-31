// Get the canvas element
const canvas = document.getElementById('cubeCanvas');
canvas.width = canvas.clientWidth;
canvas.height = canvas.clientHeight;


// Sizes
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
};

// Update window size
window.addEventListener('resize', () => {
    sizes.width = window.innerWidth;
    sizes.height = window.innerHeight;
    camera.updateProjectionMatrix()
    camera.aspect = sizes.width / sizes.height;
    renderer.setSize(sizes.width, sizes.height)
})

// Create a Three.js scene
const scene = new THREE.Scene();

// Create a camera and position it
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 50);
// camera.position.z = 4;
camera.position.set(1,0,4);

// Create light
const light = new THREE.PointLight(0xffffff, 1, 100)
light.position.set(0, 10, 15)
scene.add(light)

// Create a WebGL renderer
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });

// Set renderer size
renderer.setSize(sizes.width, sizes.height)

// Set canvas background color to white
renderer.setClearColor(0xffffff);


// Load textures
const loader = new THREE.TextureLoader();
const texture = loader.load("https://threejs.org/examples/textures/floors/FloorsCheckerboard_S_Diffuse.jpg");
//  const texture = loader.load(texture1Url);
// const texture = loader.load(tex);
texture.colorSpace = THREE.SRGBColorSpace;
 
// Create a cube and add it to the scene
const geometry = new THREE.BoxGeometry(1, 1, 1, 128, 128, 128);

// Create an array to store materials for each face
const materials = [
    new THREE.MeshStandardMaterial({ color: 0x44aa88, map: texture, }), // Default color
    new THREE.MeshStandardMaterial({ color: 0x44aa88 }),
    new THREE.MeshStandardMaterial({ color: 0x44aa88 }),
    new THREE.MeshStandardMaterial({ color: 0x44aa88 }),
    new THREE.MeshStandardMaterial({ color: 0x44aa88 }),
    new THREE.MeshStandardMaterial({ color: 0x44aa88 }),
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
    cube.rotation.z += 0.01;

    // Render the scene with the camera
    renderer.render(scene, camera);
}

// Call the animate function to start the animation loop
animate();
