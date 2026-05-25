import streamlit as st
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="wide")

# 2. CSS optimizado para pantalla completa y fluidez
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    [data-testid="stAppViewContainer"] { padding: 0 !important; }
    #canvas { 
        position: fixed; top: 0; left: 0; 
        width: 100vw; height: 100vh; 
        z-index: 0; 
    }
    .chat-container { 
        position: relative; z-index: 1; 
        max-width: 800px; margin: auto;
        padding-top: 50px;
    }
    h1 { color: #00f2ff; text-align: center; text-shadow: 0 0 10px #00f2ff; }
    </style>
""", unsafe_allow_html=True)

# 3. Canvas con velocidad reducida (más lento y elegante)
st.components.v1.html("""
<canvas id="canvas"></canvas>
<script>
const canvas = document.getElementById('canvas');
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
        // VELOCIDAD REDUCIDA (0.5 hace que se muevan suavemente)
        this.speedX = (Math.random() - 0.5) * 0.5;
        this.speedY = (Math.random() - 0.5) * 0.5;
    }
    update() { this.x += this.speedX; this.y += this.speedY; }
    draw() { ctx.fillStyle = '#00f2ff'; ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI*2); ctx.fill(); }
}
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if(particles.length < 80) particles.push(new Particle());
    particles.forEach((p, i) => {
        p.update(); p.draw();
        // Eliminar si salen de pantalla
        if(p.x < 0 || p.x > canvas.width || p.y < 0 || p.y > canvas.height) particles.splice(i, 1);
    });
    requestAnimationFrame(animate);
}
animate();
</script>
""", height=0)

# 4. Interfaz de Chat
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("💠 DANO AI - REACTOR UNIT")

try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configura tu GOOGLE_API_KEY")
    st.stop()

if "messages" not in st.session_state: st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if prompt := st.chat_input("Dano AI escuchando..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
st.markdown('</div>', unsafe_allow_html=True)
