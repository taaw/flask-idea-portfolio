"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

p4_monkeymath_bp = Blueprint(
    'p4_monkeymath_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view
