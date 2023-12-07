from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_palette')
def generate_palette():
    colors = generate_colors()
    return {'colors': colors}

def generate_colors():
    # Gere aqui suas cores de forma aleatória ou seguindo alguma lógica específica
    # Vou gerar 5 cores aleatórias como exemplo
    num_colors = 5
    colors = ['#%06x' % random.randint(0, 0xFFFFFF) for _ in range(num_colors)]
    return colors

if __name__ == '__main__':
    app.run(debug=True)
