from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

datasets = {
    "Dataset 1": [30, 40, 20, 10],
    "Dataset 2": [10, 20, 30, 40],
    "Dataset 3": [15, 25, 35, 25]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_url = None
    if request.method == 'POST':
        selected_dataset = request.form['dataset']
        selected_chart = request.form['chart_type']
        data = datasets[selected_dataset]

        plt.figure(figsize=(5, 4))
        if selected_chart == "Bar Chart":
            plt.bar(range(len(data)), data, color='blue')
        elif selected_chart == "Line Chart":
            plt.plot(range(len(data)), data, marker='o', linestyle='-', color='green')
        elif selected_chart == "Pie Chart":
            plt.pie(data, labels=range(len(data)), autopct='%1.1f%%', startangle=90)

        plt.title(f"{selected_chart} for {selected_dataset}")

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        chart_url = base64.b64encode(img.getvalue()).decode()
        plt.close()

    return render_template('index.html', chart_url=chart_url)

if __name__ == '__main__':
    app.run(debug=True)
