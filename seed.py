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
        user = UserModel(
            email="della@della.com", username="della", password="Hello123!"
        )
        user.save()

        mo_salah = FootballerModel(
            user_id=1,
            name="Mo Salah",
            team="Liverpool",
            position="Forward",
            shirt_number=11,
            nationality="Egyptian",
            club="Liverpool",
            career_goals=286,
            career_appearances=592,
            foot="Left",
            image="https://cdn.britannica.com/91/200591-050-95794068/Mohamed-Salah-Egyptian-skills-English-Premier-League-2018.jpg",
            bio="Mohamed Salah (born 15 June 1992), known as Mohamed Salah or Mo Salah, is an Egyptian professional footballer who plays as a right winger or forward for Premier League club Liverpool and captains the Egypt national team. Regarded as one of the best players of his generation and among the greatest African players of all time, he is known for his clinical finishing, dribbling and speed",
        )

        mac_allister = FootballerModel(
            user_id=1,
            name="Alexis Mac Allister",
            team="Liverpool",
            position="Midfield",
            shirt_number=10,
            nationality="Argentine",
            club="Liverpool",
            career_goals=40,
            career_appearances=252,
            foot="Right",
            image="https://tmssl.akamaized.net/images/foto/galerie/alexis-mac-allister-fc-liverpool-2023-1693910962-115929.jpg?lm=1693910988",
            bio="Alexis Mac Allister (born 24 December 1998) is an Argentine professional footballer who plays as a midfielder for Premier League club Liverpool and the Argentina national team.",
        )

        alexander_arnold = FootballerModel(
            user_id=1,
            name="Trent Alexander-Arnold",
            position="Defender",
            team="Liverpool",
            shirt_number=66,
            nationality="English",
            club="Liverpool",
            career_goals=18,
            career_appearances=303,
            foot="Right",
            image="https://library.sportingnews.com/styles/twitter_card_120x120/s3/2024-01/Trent%20Alexander-Arnold%20Liverpool%20010924.jpg?itok=Oz6LhHO2",
            bio="Trent John Alexander-Arnold (born 7 October 1998) is an English professional footballer who plays as a right-back or midfielder for Premier League club Liverpool and the England national team. Considered one of the best right-backs in the world, he is known for his range of passing, crossing and assists.[4][5][6][7][8] Owing to such capabilities, he has also occasionally been deployed as a midfielder for both club and country",
        )

        virgil_van_dijk = FootballerModel(
            user_id=1,
            name="Virgil Van Dijk",
            position="Defender",
            team="Liverpool",
            shirt_number=4,
            nationality="Dutch",
            club="Liverpool",
            career_goals=52,
            career_appearances=524,
            foot="Right",
            image="https://i2-prod.football.london/arsenal-fc/news/article28615283.ece/ALTERNATES/s1200c/0_liverpool-captain-virgil-van-dijk-intends-to-enjoy-the-ride-of-the-premier-league-title-race-with-manchester-city-tim.jpg",
            bio="Virgil van Dijk (born 8 July 1991) is a Dutch professional footballer who plays as a centre-back for Premier League club Liverpool and the Netherlands national team. Widely regarded as one of the best defenders of his generation, he is known for his strength, leadership, speed and aerial ability.",
        )

        allison_becker = FootballerModel(
            user_id=1,
            name="Alisson Becker",
            position="Goalkeeper",
            team="Liverpool",
            shirt_number=1,
            nationality="Brazilian",
            club="Liverpool",
            career_goals=1,
            career_appearances=421,
            foot="Right",
            image="https://static.independent.co.uk/2023/02/05/13/d58cdb59f5db42c199cdeb368676b73dY29udGVudHNlYXJjaGFwaSwxNjc1Njg5MjA3-2.70435116.jpg?quality=75&width=640&crop=3%3A2%2Csmart&auto=webp",
            bio="Álisson Ramsés Becker (born 2 October 1992), known as Alisson Becker or simply Alisson, is a Brazilian professional footballer who plays as a goalkeeper for Premier League club Liverpool and the Brazil national team. Regarded as one of the best goalkeepers in the world,[4] he is renowned for his immense shot stopping, distribution and ability in one-on-one situations.",
        )
        mo_salah.save()
        mac_allister.save()
        alexander_arnold.save()
        virgil_van_dijk.save()
        allison_becker.save()

        comment = CommentModel(content="What a player!", footballer_id=1, user_id=1)
        comment.save()

        print("database seeded!")
    except Exception as e:
        print(e)
