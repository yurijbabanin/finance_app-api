from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get_revenue/<id>')
def get_revenue(id):
    resp = [
        {'id': 1, 'u_id': 1, 'mouth': '02/23', 'sum': 50000, 'curence': 'RUB'},
        {'id': 2, 'u_id': 1, 'mouth': '02/23', 'sum': 25000, 'curence': 'RUB'},
        {'id': 3, 'u_id': 1,'mouth': '02/23', 'sum': 11529, 'curence': 'RUB'}
    ]
    return jsonify(
        id=1,
        u_id=1
    )

@app.route('/get_cost/<id>')
def get_cost(id):
    return 'get_cost for id: ' +id

@app.route('/get_financial_cushion/<id>')
def financial_cushion(id):
    return 'financial_cushion for id: ' +id

@app.route('/get_spend/<id>')
def get_spend(id):
    return 'get_spend for id: ' +id

@app.route('/create_spend/<u_id>/<date>/<desc>/<category>/<spend>')
def create_spend(u_id, date, desc, category, spend):
    return jsonify(
        u_ud = u_id,
        date = date,
        desc = desc,
        category = category,
        spend = spend
    )

if __name__ == '__main__':
    app.run()
