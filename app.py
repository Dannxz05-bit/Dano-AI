import streamlit as st
from google import genai

st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# CSS para el fondo oscuro
st.markdown("<style>.stApp { background-color: #000408; }</style>", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# CANVAS DE PARTÍCULAS (Potencia visual máxima)
st.components.v1.html("""
<canvas id="canvas" style="width: 100%; height: 300px;"></canvas>
<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = 600; canvas.height = 300;
let particles = [];
class Particle {
    constructor() {
        this.x = canvas.width/2; this.y = canvas.height/2;
        this.size = Math.random() * 3 + 1;
        this.speedX = Math.random() * 4 - 2;
        this.speedY = Math.random() * 4 - 2;
        this.color = '#00f2ff';
    }
    update() { this.x += this.speedX; this.y += this.speedY; }
    draw() { ctx.fillStyle = this.color; ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI*2); ctx.fill(); }
}
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if(particles.length < 50) particles.push(new Particle());
    particles.forEach((p, i) => {
        p.update(); p.draw();
        if(p.x < 0 || p.x > canvas.width || p.y < 0 || p.y > canvas.height) particles.splice(i, 1);
    });
    requestAnimationFrame(animate);
}
animate();
</script>
""", height=300)

# Lógica IA
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
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
""", unsafe_allow_html=True)
