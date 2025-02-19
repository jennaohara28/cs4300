def favorite_books():
    return [
            ("Zodiac Academy: The Awakening", "Caroline Peckham and Susanne Valenti"),
            ("Zodiac Academy: Ruthless Fae", "Caroline Peckham and Susanne Valenti"),
            ("Zodiac Academy: The Reckoning", "Caroline Peckham and Susanne Valenti"),
            ("Zodiac Academy: The Elementals", "Caroline Peckham and Susanne Valenti"),
            ("Zodiac Academy: The Prophecy", "Caroline Peckham and Susanne Valenti"),
    ]

def first_three_fave_books():
    return favorite_books()[:3]

def student_database():
    return {
        "Aname": 100001,
        "Bname": 100002,
        "Cname": 100003,
    }

def test_favorite_books():
    books = favorite_books()
    assert books[0] == ("Zodiac Academy: The Awakening", "Caroline Peckham and Susanne Valenti")
    assert books[1] == ("Zodiac Academy: Ruthless Fae", "Caroline Peckham and Susanne Valenti")
    assert books[2] == ("Zodiac Academy: The Reckoning", "Caroline Peckham and Susanne Valenti")
    assert books[3] == ("Zodiac Academy: The Elementals", "Caroline Peckham and Susanne Valenti")
    assert books[4] == ("Zodiac Academy: The Prophecy", "Caroline Peckham and Susanne Valenti")

def test_first_three_fave_books():
    books = first_three_fave_books()
    assert books[0] == ("Zodiac Academy: The Awakening", "Caroline Peckham and Susanne Valenti")
    assert books[1] == ("Zodiac Academy: Ruthless Fae", "Caroline Peckham and Susanne Valenti")
    assert books[2] == ("Zodiac Academy: The Reckoning", "Caroline Peckham and Susanne Valenti")

def test_student_database():
    students = student_database()
    assert isinstance(students, dict)
    assert "Aname" in students and students["Aname"] == 100001
    assert "Bname" in students and students["Bname"] == 100002
    assert "Cname" in students and students["Cname"] == 100003