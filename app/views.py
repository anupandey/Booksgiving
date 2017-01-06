from flask import Flask, render_template, request, redirect, url_for, flash
from flask.ext.login import login_required

from app import app, db, login_manager
from models import Centre, Books, BorrowingDetails, DonationDetails, User

# FOR ALL USERS

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)

@app.route('/')
@app.route('/home')
def homePage():
    # if username present display username at corner, near signup
    return render_template('home.html')

@app.route('/home1')
def homePage1():
    # if username present display username at corner, near signup
    return render_template('home_test.html')

@app.route('/about')
def about():
    # if username present display username at corner, near signup
    return render_template('about.html')
    #"This is the about page for HappyBooksgivings!"

@app.route('/signupUser')
def signupPage():
    # if username present display username at corner, near signup
    return render_template('signupUser.html')


@app.route('/borrowLink')
def borrowLink():
    return render_template('borrowLink.html')
    #"This is the page that links to the borrow page!"


@app.route('/donateLink')
# @login_required
def donateLink():
    return render_template('donateLink.html')
    # "This is the page that links to the donate page!"


@app.route('/partnerorganisations')
def partnerorganisations():
    return render_template('partnerorganisations.html')

    # new code to test today


@app.route('/centres')
def showCentres():
    centres = Centre.query.all()
    return render_template('showCentres.html', centres=centres)


@app.route('/centres/<centre_id>')
def centreInfo(centre_id):
    centre = Centre.query.filter_by(centre_id=centre_id).one()
    return render_template('showCentre.html', centre=centre)
    # for an individual user to acess its own details and with provisons to
    # edit details


@app.route('/centres/<centre_id>/books',  methods= ['GET','POST'])
def showBooksInCentre(centre_id):
    if request.method == 'POST':
        centre = Centre.query.filter_by(centre_id=centre_id).one()
        book_id = request.form['book_id']
        try:
            searchbook = Books.query.filter_by(book_id = book_id).one()
            if searchbook.centre_id == centre_id:
                centre = Centre.query.filter_by(centre_id=centre_id).one()
                return render_template('searchbook.html', searchbook=searchbook, centre=centre)
        except:
                pass
        return render_template('searchbook.html', centre=centre)
    else:
        centre = Centre.query.filter_by(centre_id=centre_id).one()
        books = Books.query.filter_by(centre_id=centre_id)
        return render_template('showBooksInCentre.html', centre=centre, books=books)


@app.route('/centres/new' ,  methods= ['GET','POST'])
def newCentre():
    if request.method == 'POST':
        newcentre = Centre(
                name=request.form['name'],
                centre_id=request.form['centre_id'],
                pincode=request.form['pincode'],
                address=request.form['address'],
                phone=request.form['phone'],
                email_address=request.form['email_address'],
                contactname=request.form['contactname'],
                password=request.form['password'])
        db.session.add(newcentre)
        db.session.commit()
        return redirect(url_for('showCentres'))
    else:
        return render_template('signupCentre.html')


@app.route('/centres/<centre_id>/edit' , methods= ['GET', 'POST'])
def editCentre(centre_id):
    editedcentre = Centre.query.filter_by(centre_id=centre_id).one()
    if request.method == 'POST':
        if request.form['email_address']:
                editedcentre.email_address = request.form['email_address']

        if request.form['phone']:
                editedcentre.phone = request.form['phone']

        if request.form['contactname']:
                editedcentre.contactname = request.form['contactname']

        db.session.add(editedcentre)
        db.session.commit()
        flash("Your centre details have been edited!")
        return redirect(url_for('centreInfo', centre_id=centre_id))
    else:
        return render_template(
            'editCentre.html', centre_id=centre_id, centre=editedcentre)


@app.route('/centres/<centre_id>/delete', methods= ['GET', 'POST'])
def deleteCentre(centre_id):
    centreToDelete = Centre.query.filter_by(centre_id=centre_id).one()
    if request.method == 'POST':
        db.session.delete(centreToDelete)
        db.session.commit()
        flash("Your centre details have been deleted!")
        return redirect(url_for('showCentres'))
    else:
        return render_template(
            'deleteCentre.html', centre_id = centre_id, centre = centreToDelete)


@app.route('/centres/<centre_id>/books/new', methods = ['GET', 'POST'])
def addBook(centre_id):
    if request.method == 'POST':
        newBook = Books(title = request.form['title'],
                        book_id = request.form['book_id'],
                        author = request.form['author'],
                        description = request.form['description'],
                        number = request.form['number'],
                        centre_id = centre_id)
        db.session.add(newBook)
        db.session.commit()
        flash("Your book has been added sucessfully!")
        return redirect(url_for('showBooksInCentre', centre_id = centre_id))
    else:
        return render_template('addDonationDetails.html', centre_id = centre_id )

@app.route('/centres/<centre_id>/books/<int:book_id>/edit', methods=['GET', 'POST'])
def editBook(centre_id, book_id):
    editedBook = Books.query.filter_by(book_id=book_id).one()
    if request.method == 'POST':
        if request.form['title']:
            editedBook.title = request.form['title']

        if request.form['author']:
            editedBook.author = request.form['author']

        if request.form ['description']:
            editedBook.description = request.form['description']

        if request.form ['number']:
            editedBook.number = request.form['number']

        db.session.add(editedBook)
        db.session.commit()
        flash("Your book details have been edited")
        return redirect(url_for('showBooksInCentre', centre_id=centre_id))
    else:
        return render_template('editBook.html', centre_id=centre_id, book_id =  book_id, book=editedBook)

@app.route('/centres/<centre_id>/books/<int:book_id>/delete' , methods=['GET', 'POST'] )
def deleteBook(centre_id, book_id):
    bookToDelete = Books.query.filter_by(book_id=book_id).one()
    if request.method == 'POST':
        db.session.delete(bookToDelete)
        db.session.commit()
        return redirect(url_for('showBooksInCentre', centre_id=centre_id))
    else:
        return render_template('deleteBook.html', book=bookToDelete)
    #"allows centres to delete books in their respective  centres"

@app.route('/centres/<centre_id>/books/addBook', methods=['GET', 'POST'])
def addBookNew(centre_id):
    if request.method == 'POST':
        book_id = request.form['book_id']
        try:
            addbook = Books.query.filter_by(book_id = book_id).one()
            if addbook.centre_id == centre_id:
                return redirect(url_for('addBookNew2', centre_id = centre_id, book_id=book_id))
            else:
                return render_template('addDonationDetails.html', centre_id = centre_id)
        except:
            return render_template('addDonationDetails.html', centre_id = centre_id)
    else:
        return render_template('addBookNew.html', centre_id=centre_id)


@app.route('/centres/<centre_id>/books/addBookNew/<int:book_id>', methods=['GET', 'POST'])
def addBookNew2(centre_id, book_id):
    book = Books.query.filter_by(book_id = book_id).one()
    if request.method == 'POST':
        book.number += int(request.form['number'])
        print book.number
        # db.session.add(book)
        db.session.commit()
        flash("Your book has been added")
        return redirect(url_for('showBooksInCentre', centre_id=centre_id))
    else:
        return render_template('addBookNew2.html', centre_id=centre_id, book=book)


@app.route('/centres/<centre_id>/donations')
def donation(centre_id):
    centre = Centre.query.filter_by(centre_id=centre_id).one()
    donation_details = DonationDetails.query.filter_by(centre_id = centre_id)
    if donation_details:
        return render_template('detailsofdonation.html',centre=centre, donation_details = donation_details)
    else:
        return render_template('notransaction.html', centre_id=centre_id)

@app.route('/centres/<centre_id>/borrowings')
def borrowing(centre_id):
    centre = Centre.query.filter_by(centre_id=centre_id).one()
    borrowing_details = BorrowingDetails.query.filter_by(centre_id = centre_id)
    if borrowing_details:
        return render_template('detailsofborrowing.html',centre=centre , borrowing_details = borrowing_details)
    else:
        return render_template('notransaction.html', centre_id=centre_id)

@app.route('/signupUser' ,  methods= ['GET','POST'])
def signupUser():
    if request.method == 'POST':
        newuser = User(
                name=request.form['name'],
                user_id=request.form['email_address'],
                password=request.form['password'])
        db.session.add(newuser)
        db.session.commit()
        #flash('User successfully registered')
        return redirect(url_for('signupThankyou'))
    else:
        return render_template('signupUser.html')

@app.route('/signupUser/thankyou')
def signupThankyou():
    return render_template('signupUserThankyou.html')

@app.route('/loginUser',methods=['GET','POST'])
def loginUser():
    if request.method == 'POST':
        entered_id = request.form['userid']
        entered_password = request.form['password']
        user = User.query.filter_by(user_id = entered_id).one()
        if user:
            if user.password == entered_password:
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return render_template('home.html')
            else:
                flash("Sorry, Password match is invalid")
                return render_template('loginUser.html')
        else:
            flash("Sorry, Username Password match is invalid")
            return render_template('loginUser.html')
    else:
        return render_template('loginUser.html')

# @app.route('/centres/<centre_id>/donations')
# def donation(centre_id):
#     centre = Centre.query.filter_by(centre_id=centre_id).one()
#     donation_details = DonationDetails.query.filter_by(centre_id = centre_id)
#     if donation_details:
#         return render_template('detailsofdonation.html',centre=centre, donation_details = donation_details)
#     else:
#         return render_template('notransaction.html', centre_id=centre_id)

@app.route('/borrowLink/findbook', methods=["GET", "POST"])
def findbook():
    if request.method == 'POST':
        book_id = request.form['text']
        searchBooks = Books.query.filter_by(book_id=book_id)
        return render_template('borrowSearchResults.html', searchBooks=searchBooks)
    else:
        return render_template('searchBookToBorrow.html')

@app.route('/searchBookToDonate', methods=["GET", "POST"])
def findCentres():
    centres = Centre.query.all()
    return render_template('allCentres.html', centres=centres)


@app.route('/centres/<centre_id>/books/search', methods=["GET", "POST"])
def searchBook(centre_id):
    if request.method == 'POST':
        book_id = request.form['book_id']
        try:
            searchbook = Books.query.filter_by(book_id = book_id).one()
            if searchbook.centre_id == centre_id:
                return redirect(url_for('searchbook.html', centre_id = centre_id))
            else:
                return render_template('searchbook.html')
        except:
                return render_template('searchbook.html')
    else:
        return redirect(url_for('showBooksInCentre', centre_id = centre_id))


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """For GET requests, display the login form. For POSTS, login the current user
#     by processing the form."""
#     if request.method == 'POST':
#         entered_id = request.form['userid']
#         entered_passowrd = request.form['passowrd']
#         try:
#             user = User.query.filter_by(user_id = entered_id).one()
#             if user.password = entered_password:
#                 user.authenticated = True
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user, remember=True)
#                 return
#             else:
#                 return
#         except:
#             return
#     else:
#         return render_template("loginCentre.html")
#
#
#
#
#
#         if form.validate_on_submit():
#         user = User.query.get(form.email.data)
#         if user:
#             if bcrypt.check_password_hash(user.password, form.password.data):
#                 user.authenticated = True
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user, remember=True)
#                 return redirect(url_for("bull.reports"))
#     return render_template("login.html", form=form)
#
# @bull.route("/logout", methods=["GET"])
# @login_required
# def logout():
#     """Logout the current user."""
#     user = current_user
#     user.authenticated = False
#     db.session.add(user)
#     db.session.commit()
#     logout_user()
#     return render_template("logout.html")
