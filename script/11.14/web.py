from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/')
def show_results():
    conn = sqlite3.connect('tictactoe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT winner, COUNT(*) FROM results GROUP BY winner')
    results = cursor.fetchall()
    conn.close()

    html = '''
    <!DOCTYPE html>
    <html lang="hu">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tic Tac Toe Eredmények</title>
        <meta name="description" content="Tic Tac Toe Eredmények">
        <meta name="author" content="Gyuris Dánie">
        <meta name="keywords" content="Tic Tac Toe, Eredmények">
        <meta name="robots" content="index, follow">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #444;
            }
            table {
                width: 50%;
                margin: 0 auto;
                border-collapse: collapse;
            }
            th, td {
                padding: 10px;
                text-align: center;
                border: 1px solid #ddd;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
        </style>
        <script>
            // Frissíti az oldalt minden 10 másodpercben
            setInterval(function() {
                window.location.reload();
            }, 10000);
        </script>
    </head>
    <body>
        <h1>Tic Tac Toe Eredmények</h1>
        <table>
            <tr>
                <th>Játékos</th>
                <th>Győzelmek száma</th>
            </tr>
            {% for winner, count in results %}
            <tr>
                <td>{{ winner }}</td>
                <td>{{ count }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    '''
    return render_template_string(html, results=results)

if __name__ == '__main__':
    app.run(debug=True)