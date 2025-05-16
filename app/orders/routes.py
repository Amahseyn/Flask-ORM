# app/orders/routes.py
from flask import Blueprint, request, jsonify
from app.orders.models import db, Order
from flask_login import login_required, current_user

orders_bp = Blueprint('orders', __name__)

# Create Order
@orders_bp.route('/create', methods=['POST'])
@login_required
def create_order():
    data = request.get_json()
    order = Order(total_amount=data['total_amount'], user_id=current_user.id)
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order created successfully"}), 201

# Get Order by ID
@orders_bp.route('/<int:order_id>', methods=['GET'])
@login_required
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify({"id": order.id, "total_amount": order.total_amount, "user_id": order.user_id}), 200