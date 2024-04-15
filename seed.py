from app import app, db
from models.comment_model import CommentModel
from models.footballer_model import FootballerModel
from models.user_model import UserModel

with app.app_context():

    try:
        print("creating the db")
        db.drop_all()
        db.create_all()

        print("seeding")
        user = UserModel(
            email="jamie@jamie.com", username="jamie", password="Hello123!"
        )
        user.save()

        mo_salah = FootballerModel(
            user_id=1,
            name="Mo Salah",
            position="Forward",
            shirt_number=11,
            nationality="Egyptian",
            club="Liverpool",
            career_goals=286,
            career_appearances=592,
            foot="left",
            image="https://cdn.britannica.com/91/200591-050-95794068/Mohamed-Salah-Egyptian-skills-English-Premier-League-2018.jpg",
            bio="Mohamed Salah (born 15 June 1992), known as Mohamed Salah or Mo Salah, is an Egyptian professional footballer who plays as a right winger or forward for Premier League club Liverpool and captains the Egypt national team. Regarded as one of the best players of his generation and among the greatest African players of all time, he is known for his clinical finishing, dribbling and speed",
            admin_id=1,
        )
        mo_salah.save()

        comment = CommentModel(content="What a player!", footballer_id=1, user_id=1)
        comment.save()

        print("database seeded!")
    except Exception as e:
        print(e)
