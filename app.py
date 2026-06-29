from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Danahe's Magical Crafts</title>
        <style>
            :root {
                --lila: #c7a7ff;
                --rosa: #ffd1e8;
                --celeste: #b9ecff;
                --crema: #fff8f0;
                --morado: #6d4c8d;
                --texto: #3b2f4a;
            }

            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                font-family: "Segoe UI", Arial, sans-serif;
                color: var(--texto);
                background:
                    radial-gradient(circle at top left, #ffe1f1 0, transparent 32%),
                    radial-gradient(circle at bottom right, #c7f0ff 0, transparent 34%),
                    linear-gradient(135deg, var(--crema), #fff1fb);
                overflow-x: hidden;
            }

            header {
                padding: 28px 8%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 20px;
            }

            .logo {
                font-size: 28px;
                font-weight: 800;
                color: var(--morado);
                letter-spacing: 0.5px;
            }

            .pill {
                background: white;
                border: 2px solid #f2d9ff;
                border-radius: 999px;
                padding: 10px 18px;
                font-weight: 700;
                box-shadow: 0 10px 25px rgba(109, 76, 141, 0.12);
            }

            .hero {
                width: min(1100px, 92%);
                margin: 30px auto;
                display: grid;
                grid-template-columns: 1.1fr 0.9fr;
                gap: 34px;
                align-items: center;
            }

            .card {
                background: rgba(255, 255, 255, 0.74);
                border: 2px solid rgba(255, 255, 255, 0.9);
                border-radius: 34px;
                padding: 42px;
                box-shadow: 0 25px 60px rgba(109, 76, 141, 0.16);
                backdrop-filter: blur(12px);
            }

            h1 {
                font-size: clamp(40px, 6vw, 72px);
                line-height: 0.95;
                margin: 0 0 20px;
                color: var(--morado);
            }

            .subtitle {
                font-size: 21px;
                line-height: 1.6;
                margin: 0 0 28px;
            }

            .buttons {
                display: flex;
                gap: 14px;
                flex-wrap: wrap;
            }

            .btn {
                display: inline-block;
                text-decoration: none;
                color: white;
                background: linear-gradient(135deg, #b26bff, #ff87c8);
                border-radius: 18px;
                padding: 14px 22px;
                font-weight: 800;
                box-shadow: 0 12px 24px rgba(178, 107, 255, 0.27);
            }

            .btn.secondary {
                color: var(--morado);
                background: white;
                border: 2px solid #ead7ff;
            }

            .showcase {
                display: grid;
                gap: 18px;
            }

            .product {
                background: white;
                border-radius: 28px;
                padding: 22px;
                box-shadow: 0 15px 36px rgba(109, 76, 141, 0.12);
                border: 2px solid #f8eaff;
            }

            .emoji {
                font-size: 48px;
                margin-bottom: 8px;
            }

            .product h3 {
                margin: 0 0 8px;
                color: var(--morado);
                font-size: 24px;
            }

            .product p {
                margin: 0;
                line-height: 1.5;
            }

            .section {
                width: min(1100px, 92%);
                margin: 18px auto 50px;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
            }

            .mini {
                background: rgba(255, 255, 255, 0.78);
                border: 2px solid #fff;
                border-radius: 26px;
                padding: 24px;
                text-align: center;
                box-shadow: 0 12px 28px rgba(109, 76, 141, 0.11);
            }

            .mini strong {
                color: var(--morado);
                font-size: 20px;
            }

            footer {
                text-align: center;
                padding: 28px;
                color: var(--morado);
                font-weight: 700;
            }

            @media (max-width: 820px) {
                header, .hero {
                    grid-template-columns: 1fr;
                }

                header {
                    flex-direction: column;
                }

                .section {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <div class="logo">🌙 Danahe's Magical Crafts</div>
            <div class="pill">Hecho a mano con amor pastel ✨</div>
        </header>

        <main class="hero">
            <section class="card">
                <h1>Detalles mágicos para regalar</h1>
                <p class="subtitle">
                    Amigurumis, pulseras y papercrafts personalizados con estilo kawaii,
                    colores suaves y un toque artesanal que convierte cada pedido en una mini historia.
                </p>
                <div class="buttons">
                    <a class="btn" href="#productos">Ver productos</a>
                    <a class="btn secondary" href="#contacto">Pedir diseño</a>
                </div>
            </section>

            <section class="showcase" id="productos">
                <article class="product">
                    <div class="emoji">🧶</div>
                    <h3>Amigurumis</h3>
                    <p>Personajes, animalitos y figuras tejidas para regalos únicos.</p>
                </article>
                <article class="product">
                    <div class="emoji">📿</div>
                    <h3>Pulseras</h3>
                    <p>Accesorios personalizados con colores, nombres y detalles especiales.</p>
                </article>
                <article class="product">
                    <div class="emoji">🎀</div>
                    <h3>Papercrafts</h3>
                    <p>Diseños de papel decorativos para fechas especiales y sorpresas lindas.</p>
                </article>
            </section>
        </main>

        <section class="section" id="contacto">
            <div class="mini"><strong>Personalizado</strong><br>Elige color, estilo y detalle.</div>
            <div class="mini"><strong>Artesanal</strong><br>Cada pieza se realiza con cuidado.</div>
            <div class="mini"><strong>DevOps</strong><br>Desplegado con Flask, Docker, GHCR y Traefik.</div>
        </section>

        <footer>
            © 2026 Danahe's Magical Crafts · Página de práctica DevOps 🚀
        </footer>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok", "project": "danahe-magical-crafts"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
