from app import db


class Centre(db.Model):
    __tablename__ = 'centre'

    centre_id = db.Column(db.String(25), primary_key=True,
                          nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(250), nullable=False,  unique=True)
    pincode = db.Column(db.Integer, nullable=False)
    # can we specify a format here? 011-22116269
    phone = db.Column(db.Integer, nullable=False,  unique=True)
    # is the string length ok?
    email_address = db.Column(db.String(30), nullable=False,  unique=True)
    contactname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)


class User(db.Model):
    __tablename__ = 'user'

    # non-organisation/individual users only
    # user email is the user id. is the string length ok?
    user_id = db.Column(db.String(30), nullable=False,
                        primary_key=True, unique=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.user_id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False



class Books(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    description = db.Column(db.String(200))
    # image = Column() #what type of variable is this?
    number = db.Column(db.Integer, nullable=False)
    centre_id = db.Column(db.String(25), db.ForeignKey('centre.centre_id'))
    #centre = db.relationship(Centre)

class BorrowingDetails(db.Model):
    __tablename__ = 'borrowing_details'

    borrowing_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    date = db.Column(db.String(8), nullable=False)
    user_id = db.Column(db.String(30), db.ForeignKey('user.user_id'))
    #user = db.relationship(User)

    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    #books = db.relationship(Books)

    centre_id = db.Column(db.String(25), db.ForeignKey('centre.centre_id'))
    #centre = db.relationship(Centre)


class DonationDetails(db.Model):
    __tablename__ = 'donation_details'
    donation_id = db.Column(db.Integer, primary_key=True,
                            nullable=False, unique=True)
    date = db.Column(db.String(8), nullable=False)

    user_id = db.Column(db.String(30), db.ForeignKey('user.user_id'))
    #user = db.relationship(User)

    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    #books = db.relationship(Books)

    centre_id = db.Column(db.String(25), db.ForeignKey('centre.centre_id'))
    #centre = db.relationship(Centre)

# class CentreBooks(db.Model):
#     __tablename__ = 'centre_books'
#
#     centre_id = db.Column(db.String(25), db.ForeignKey('centre.centre_id'))
#     centre = db.relationship(Centre)
#
#     book_id =  db.Column(db.Integer, db.ForeignKey('books.book_id'))
#     books = db.relationship(Books)
#
#
# # class CentreBooks(db.Model):
#     __tablename__ = 'centre_books'
#
#     centre_id = db.Column(db.String(25))
#     book_id = db.Column(db.Integer)
#     __table_args__ = (ForeignKeyConstraint(['centre_id', 'book_id'],
#                                            ['centre.centre_id', 'books.book_id']),
#                       {})
#
#     books = db.relationship(Books)
#     centre = db.relationship(Centre)
#
#     total_books = db.Column(db.Integer, nullable = False)
#
#     # cb_id = Column(Integer, nullable = False, primary_key = True)
#
