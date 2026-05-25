import streamlit as st
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="wide")

# 2. CSS "Bomba Nuclear" (Fuerza el fondo y el Canvas al fondo de todo)
st.markdown("""
    <style>
    /* Fondo oscuro absoluto */
    .stApp { background-color: #000408 !important; }
    
    /* El contenedor del canvas siempre al fondo */
    #background-canvas {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: -1 !important;
        background-color: #000408 !important;
    }
    
    .chat-container { 
        position: relative; z-index: 1; 
        max-width: 800px; margin: auto;
        padding-top: 100px;
    }
    h1 { color: #00f2ff; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# 3. Canvas forzado
st.components.v1.html("""
<canvas id="background-canvas"></canvas>
<script>
const canvas = document.getElementById('background-canvas');
const ctx = canvas.getContext('2d');
function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
window.addEventListener('resize', resize);
resize();

let particles = [];
class Particle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 2 + 1;
        this.speedX = (Math.random() - 0.5) * 0.3;
        this.speedY = (Math.random() - 0.5) * 0.3;
    }
    update() { this.x += this.speedX; this.y += this.speedY; }
    draw() { ctx.fillStyle = '#00f2ff'; ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI*2); ctx.fill(); }
}
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if(particles.length < 100) particles.push(new Particle());
    particles.forEach((p, i) => {
        p.update(); p.draw();
        if(p.x < 0 || p.x > canvas.width || p.y < 0 || p.y > canvas.height) particles.splice(i, 1);
    });
    requestAnimationFrame(animate);
}
animate();
</script>
""", height=0)

# 4. Chat
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("💠 DANO AI - REACTOR UNIT")
# ... (resto de tu lógica de chat igual que antes)
