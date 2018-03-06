"""A basic model for Member related stuff."""

from flask_demo.models import db


class Member(db.Model):
    """A very basic Member"""
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, server_default=db.func.now())
    update_time = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )
    firstname = db.column(db.String(255))
    lastname = db.column(db.String(255))

    phone_numbers = db.relationship('PhoneNumber', back_populates='phone_number')

    def __repr__(self):
        return '<Member id={}, name={}>'.format(self.id, self.name)

    @property
    def name(self):
        return '{} {}'.format(self.firstname, self.lastname)


class PhoneNumber(db.Model):
    """A basic phone number."""
    __tablename__ = 'phone_number'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, server_default=db.func.now())
    update_time = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )
    firstname = db.column(db.String(20))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)

    member = db.relationship('Member', back_populates='member')
