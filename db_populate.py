from app import db, models

aBCorganization = models.Centre(centre_id="123xxx",
                                name="Abc organization",
                                address="123 dyanand vihar",
                                pincode=110095,
                                phone=222667999,
                                email_address="123Abc@gmail.com",
                                contactname="Bhanu Prasad",
                                password="xxx")
db.session.add(aBCorganization)  # can teh first alphabet be in Caps?
db.session.commit()

dEForganization = models.Centre(centre_id="21yhhxxx",
                                name=" DEF organization",
                                address="13 anand vihar",
                                pincode=110075,
                                phone=222000999,
                                email_address="13DEFc@gmail.com",
                                contactname="hanu Prahlad",
                                password="xxx")
db.session.add(dEForganization)
db.session.commit()

gHIorganization = models.Centre(centre_id="21GhhKxxx",
                                name=" GHI organization",
                                address="13 andParbat delhi",
                                pincode=110067,
                                phone=2229900999,
                                email_address="1GHIc@gmail.com",
                                contactname="Prahlad Dhingra",
                                password="xxx")
db.session.add(gHIorganization)
db.session.commit()

xYZorganization = models.Centre(centre_id="21XYZKxxx",
                                name=" XYZ organization",
                                address="131 Parbat vihar noida",
                                pincode=110087,
                                phone=222990000,
                                email_address="1parbatc@gmail.com",
                                contactname="Sakshi Bhnagra",
                                password="xxx")
db.session.add(xYZorganization)
db.session.commit()

# TO SEE a list of all models.Centre we can do
#db.session.query(Centre).all()
models.Centre.query.all()

# creating users

ram = models.User(user_id="ram@gmail.com",
                  name="Ram Kapppor",
                  password="ram)2016")
db.session.add(ram)
db.session.commit()

rama = models.User(user_id="rama22@gmail.com",
                   name="Rama Narang",
                   password="rama_2016")
db.session.add(rama)
db.session.commit()

shayma = models.User(user_id="rshyma122@gmail.com",
                     name="Shyama Sharma",
                     password="shyama_2016")
db.session.add(shayma)
db.session.commit()


krishna = models.User(user_id="rishna122@gmail.com",
                      name="Krisshna Sharma",
                      password="Krsihna9_2016")
db.session.add(krishna)
db.session.commit()


# Making new BOOKS by models.Books class

book_one = models.Books(book_id=1222222,
                        title="I am book one",
                        author="David Willimans",
                        description="This is the first Book",
                        number=11,
                        centre_id="21GhhKxxx")
db.session.add(book_one)
db.session.commit()

book_two = models.Books(book_id=10012,
                        title="I am book two",
                        author="Suuny Willimans",
                        description="This is the second Book",
                        number=10,
                        centre_id="123xxx")
db.session.add(book_two)
db.session.commit()

book_three = models.Books(book_id=12666222,
                          title="I am book three",
                          author="Sarah lee",
                          description="This is the third Book",
                          number=3,
                          centre_id="21yhhxxx")
db.session.add(book_three)
db.session.commit()

book_four = models.Books(book_id=23366222,
                         title="I am book four",
                         author="Thomas Jane lee",
                         description="This is the fourth Book",
                         number=9,
                         centre_id="123xxx")
db.session.add(book_four)
db.session.commit()


book_five = models.Books(book_id=43366222,
                         title="I am book five",
                         author="Marshal lee",
                         description="This is the fifth Book",
                         number=4,
                         centre_id="21XYZKxxx")
db.session.add(book_four)
db.session.commit()

# TO SEE a list of all models.Books we can do
#db.session.query(models.Books).all()
models.Books.query.all()


# Making new Book&centres by models.CentreBooks class

# first = models.CentreBooks(centre=aBCorganization,
#                            books=book_five)
# db.session.add(first)
# db.session.commit()
#
# second = models.CentreBooks(centre=aBCorganization,
#                             books=book_two)
# db.session.add(second)
# db.session.commit()
#
# third = models.CentreBooks(centre=xYZorganization,
#                            books=book_five)
# db.session.add(third)
# db.session.commit()
#
# fourth = models.CentreBooks(centre=xYZorganization,
#                             books=book_three)
# db.session.add(fourth)
# db.session.commit()
#
# fifth = models.CentreBooks(centre=gHIorganization,
#                            books=book_three)
# db.session.add(fifth)
# db.session.commit()
#
# sixth = models.CentreBooks(centre=dEForganization,
#                            books=book_three)
# db.session.add(sixth)
# db.session.commit()
#
# seventh = models.CentreBooks(centre=xYZorganization,
#                              books=book_one)
# db.session.add(seventh)
# db.session.commit()
#
# eighth = models.CentreBooks(centre=xYZorganization,
#                             books=book_one)
# db.session.add(eighth)
# db.session.commit()
#

# creating new models.BorrowingDetails
# would it show error if i enter a book which is not in a centre as per
# the models.CentreBooks class
borrow_one = models.BorrowingDetails(borrowing_id=123,
                                    user_id="ram@gmail.com",
                                    book_id=12666222,
                                    centre_id="123xxx",
                                    date=12032012)  # how to add date as in the format or should I remove date nullable = false
db.session.add(borrow_one)
db.session.commit()

borrow_two = models.BorrowingDetails(borrowing_id=143,
                                    user_id="ram@gmail.com",
                                    book_id=10012,
                                    centre_id="21XYZKxxx",
                                    date=12032012)
db.session.add(borrow_two)
db.session.commit()

borrow_three = models.BorrowingDetails(borrowing_id=243,
                                      user_id="rshyma122@gmail.com",
                                      book_id=43366222,
                                      centre_id="21GhhKxxx",
                                      date=12032012)
db.session.add(borrow_three)
db.session.commit()

borrow_four = models.BorrowingDetails(borrowing_id=567,
                                     user_id="rishna122@gmail.com",
                                     book_id=23366222,
                                     centre_id="21XYZKxxx",
                                     date=12032012)
db.session.add(borrow_four)
db.session.commit()

borrow_five = models.BorrowingDetails(borrowing_id=343,
                                     user_id="ram@gmail.com",
                                     book_id=43366222,
                                     centre_id="21yhhxxx",
                                     date=12032012)

db.session.add(borrow_five)
db.session.commit()

# borrow_six = models.BorrowingDetails(borrowing_id=346,
#                                     user=rama,
#                                     books=book_five,
#                                     centre=dEForganization)
#
# db.session.add(borrow_six)
# db.session.commit()
#
# borrow_seven = models.BorrowingDetails(borrowing_id=3431,
#                                       user=rama,
#                                       books=book_one,
#                                       centre_id="1parbatc@gmail.com")
#
# db.session.add(borrow_seven)
# db.session.commit()

# creating new models.DonationDetails
# would it show error if i enter a book which is not in a centre as per the models.CentreBooks class
# can the id be the same as/clash with the borroeing details
donate_one = models.DonationDetails(donation_id=123,
                                   user_id="ram@gmail.com",
                                   book_id=10012,
                                   centre_id="123xxx",
                                   date=12032012)
db.session.add(donate_one)
db.session.commit()

donate_two = models.DonationDetails(donation_id=163,
                                   user_id="rshyma122@gmail.com",
                                   book_id=12666222,
                                   centre_id="21XYZKxxx",
                                   date=12032012)
db.session.add(donate_two)
db.session.commit()

donate_three = models.DonationDetails(donation_id=243,
                                     user_id="rishna122@gmail.com",
                                     book_id=43366222,
                                     centre_id="21XYZKxxx",
                                     date=12032012)
db.session.add(donate_three)
db.session.commit()

donate_four = models.DonationDetails(donation_id=567,
                                    user_id="rishna122@gmail.com",
                                    book_id=23366222,
                                    centre_id="21GhhKxxx",
                                    date=12032012)
db.session.add(donate_four)
db.session.commit()

donate_five = models.DonationDetails(donation_id=343,
                                    user_id="ram@gmail.com",
                                    book_id=43366222,
                                    centre_id="21yhhxxx",
                                    date=12032012)

db.session.add(donate_five)
db.session.commit()

# donate_six = models.DonationDetails(donation_id=346,
#                                    user=rama,
#                                    books=book_five,
#                                    centre=dEForganization)
#
# db.session.add(donate_six)
# db.session.commit()
#
# donate_seven = models.DonationDetails(donation_id=3431,
#                                      user=krishna,
#                                      books=book_one,
#                                      centre_id="1parbatc@gmail.com")
#
# db.session.add(donate_seven)
# db.session.commit()
#
# donate_eight = models.DonationDetails(donation_id=3431,
#                                      user=krishna,
#                                      books=book_two,
#                                      centre_id="1parbatc@gmail.com")
#
# db.session.add(donate_eight)
# db.session.commit()
#
# donate_nine = models.DonationDetails(donation_id=3431,
#                                     user=krishna,
#                                     books=book_four,
#                                     centre_id="1parbatc@gmail.com")
#
# db.session.add(donate_ninen)
# db.session.commit()
#
# donate_ten = models.DonationDetails(donation_id=3431,
#                                    user=krishna,
#                                    books=book_six,
#                                    centre_id="1parbatc@gmail.com")
#
# db.session.add(donate_ten)
# db.session.commit()
