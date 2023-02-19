from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

app = Flask(__name__)
CORS(app, resources=r'/*')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_app-api.db'
db = SQLAlchemy(app)


class Spand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, nullable=False)
    date_d = db.Column(db.String, nullable=False)
    date_m = db.Column(db.String, nullable=False)
    date_y = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    spend = db.Column(db.Integer, nullable=False)

    # def __init__(self, date, desc, category, spend):
    #     self.date = date
    #     self.desc = desc
    #     self.category = category
    #     self.spend = spend

    def __repr__(self):
        return '<Spend %r>' % self.id

class Revenue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, nullable=False)
    date_m = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    sum = db.Column(db.Integer, nullable=False)

    # def __init__(self, date, desc, category, spend):
    #     self.date = date
    #     self.desc = desc
    #     self.category = category
    #     self.spend = spend

    def __repr__(self):
        return '<Revenue %r>' % self.id

class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, nullable=False)
    date_m = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    sum = db.Column(db.Integer, nullable=False)

    # def __init__(self, date, desc, category, spend):
    #     self.date = date
    #     self.desc = desc
    #     self.category = category
    #     self.spend = spend

    def __repr__(self):
        return '<Cost %r>' % self.id

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String, nullable=False)

    # def __init__(self, date, desc, category, spend):
    #     self.date = date
    #     self.desc = desc
    #     self.category = category
    #     self.spend = spend

    def __repr__(self):
        return '<Category %r>' % self.id

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    # def __init__(self, date, desc, category, spend):
    #     self.date = date
    #     self.desc = desc
    #     self.category = category
    #     self.spend = spend

    def __repr__(self):
        return '<Users %r>' % self.id

def check_db():
    check_spends = Spand.query.order_by(Spand.id).all()
    check_revenue = Revenue.query.order_by(Revenue.id).all()
    check_cost = Cost.query.order_by(Cost.id).all()
    check_category = Category.query.order_by(Category.id).all()
    check_users = Users.query.order_by(Users.id).all()
    return {
         "id": check_spends.id
    }
    # db.create_all()


@app.route('/get_revenue/<u_id>/<date_m>')
def get_revenue(u_id, date_m):
    revenue = Revenue.query.filter(and_((Revenue.date_m == date_m), (Revenue.u_id == u_id))).all()
    return render_template('get_revenue.html', revenue=revenue), {'Content-Type': 'application/json'}


@app.route('/get_cost/<u_id>/<date_m>')
def get_cost(u_id, date_m):
    cost = Cost.query.filter(and_((Cost.date_m == date_m), (Cost.u_id == u_id))).all()
    return render_template('get_cost.html', cost=cost), {'Content-Type': 'application/json'}
@app.route('/get_profit_per_month/<u_id>/<date_m>')
def get_profit_per_month(u_id, date_m):
    get_all_revenue_by_m = Revenue.query.filter(and_((Revenue.date_m == date_m), (Revenue.u_id == u_id))).all()
    get_all_cost_by_m = Cost.query.filter(and_((Cost.date_m == date_m), (Cost.u_id == u_id))).all()
    return render_template('get_profit.html', get_all_revenue_by_m=get_all_revenue_by_m, get_all_cost_by_m=get_all_cost_by_m),{'Content-Type': 'application/json'}

@app.route('/get_financial_cushion/<u_id>')
def financial_cushion(u_id):
    return jsonify(financial_cushion=26854) #Для примера, потом сделаю


@app.route('/get_spend/<u_id>', methods = ['GET'])
def get_spend(u_id):
    spends = Spand.query.order_by(Spand.id).all()
    return render_template('get_spend.html', spends=spends), {'Content-Type': 'application/json'}


@app.route('/create_spend/<u_id>/<date_d>/<date_m>/<date_y>/<desc>/<category>/<spend>')
def create_spend(u_id, date_d, date_m, date_y, desc, category, spend):
    # db.create_all()
    spend = Spand(u_id=u_id, date_d=date_d, date_m=date_m, date_y=date_y, desc=desc, category=category,spend=spend)
    db.session.add(spend)
    db.session.commit()
    return jsonify(status="success")

@app.route('/create_revenue/<u_id>/<date_m>/<desc>/<sum>')
def create_revenue(u_id, date_m, desc, sum):
    # db.create_all()
    revenue = Revenue(u_id=u_id, date_m=date_m, desc=desc, sum=sum)
    db.session.add(revenue)
    db.session.commit()
    return jsonify(status="success")

@app.route('/create_cost/<u_id>/<date_m>/<desc>/<sum>')
def create_cost(u_id, date_m, desc, sum):
    # db.create_all()
    cost = Cost(u_id=u_id, date_m=date_m, desc=desc, sum=sum)
    db.session.add(cost)
    db.session.commit()
    return jsonify(status="success")

@app.route('/create_category/<u_id>/<desc>/')
def create_category(u_id, desc):
    # db.create_all()
    cost = Cost(u_id=u_id, desc=desc)
    db.session.add(cost)
    db.session.commit()
    return jsonify(status="success")

if __name__ == '__main__':
    app.run()
