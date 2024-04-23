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
            club="Liverpool",
            position="Forward",
            shirt_number=11,
            nationality="Egyptian",
            career_goals=286,
            career_appearances=592,
            foot="Left",
            image="https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2149164666.jpg?c=16x9&q=h_833,w_1480,c_fill",
            bio="Mohamed Salah (born 15 June 1992), known as Mohamed Salah or Mo Salah, is an Egyptian professional footballer who plays as a right winger or forward for Premier League club Liverpool and captains the Egypt national team. Regarded as one of the best players of his generation and among the greatest African players of all time, he is known for his clinical finishing, dribbling and speed",
        )

        mac_allister = FootballerModel(
            user_id=1,
            name="Alexis Mac Allister",
            club="Liverpool",
            position="Midfielder",
            shirt_number=10,
            nationality="Argentine",
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
            shirt_number=66,
            nationality="English",
            club="Liverpool",
            career_goals=18,
            career_appearances=303,
            foot="Right",
            image="https://library.sportingnews.com/styles/twitter_card_120x120/s3/2024-01/Trent%20Alexander-Arnold%20Liverpool%20010924.jpg?itok=Oz6LhHO2",
            bio="Trent John Alexander-Arnold (born 7 October 1998) is an English professional footballer who plays as a right-back or midfielder for Premier League club Liverpool and the England national team. Considered one of the best right-backs in the world, he is known for his range of passing, crossing and assists. Owing to such capabilities, he has also occasionally been deployed as a midfielder for both club and country",
        )

        virgil_van_dijk = FootballerModel(
            user_id=1,
            name="Virgil Van Dijk",
            position="Defender",
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
            shirt_number=1,
            nationality="Brazilian",
            club="Liverpool",
            career_goals=1,
            career_appearances=421,
            foot="Right",
            image="https://static.independent.co.uk/2023/02/05/13/d58cdb59f5db42c199cdeb368676b73dY29udGVudHNlYXJjaGFwaSwxNjc1Njg5MjA3-2.70435116.jpg?quality=75&width=640&crop=3%3A2%2Csmart&auto=webp",
            bio="Álisson Ramsés Becker (born 2 October 1992), known as Alisson Becker or simply Alisson, is a Brazilian professional footballer who plays as a goalkeeper for Premier League club Liverpool and the Brazil national team. Regarded as one of the best goalkeepers in the world,[4] he is renowned for his immense shot stopping, distribution and ability in one-on-one situations.",
        )
        ederson = FootballerModel(
            user_id=1,
            name="Ederson",
            position="Goalkeeper",
            shirt_number=1,
            nationality="Brazilian",
            club="Manchester City",
            career_goals=0,
            career_appearances=480,
            foot="Right",
            image="https://i2-prod.manchestereveningnews.co.uk/sport/football/football-news/article27515888.ece/ALTERNATES/s1200b/1_GettyImages-1612548204.jpg",
            bio="Ederson Santana de Moraes (born 17 August 1993), simply known as Ederson,is a Brazilian professional footballer who currently plays as a goalkeeper for Premier League club Manchester City and the Brazil national team. Widely regarded as one of the best goalkeepers in the world, he is known for his reflexes, physical strength, and shot-stopping ability",
        )
        john_stones = FootballerModel(
            user_id=1,
            name="John Stones",
            position="Defender",
            shirt_number=5,
            nationality="English",
            club="Manchester City",
            career_goals=8,
            career_appearances=378,
            foot="Right",
            image="https://e0.365dm.com/24/03/1600x900/skysports-john-stones-man-city_6478805.jpg?20240304203052",
            bio="John Stones (born 28 May 1994) is an English professional footballer who plays as a centre-back or defensive midfielder for Premier League club Manchester City and the England national team. Widely regarded as one of the best defenders in the world, Stones is known for his technical ability and his physical presence on the field.",
        )
        phil_foden = FootballerModel(
            user_id=1,
            name="Phil Foden",
            position="Midfielder",
            shirt_number=47,
            nationality="English",
            club="Manchester City",
            career_goals=82,
            career_appearances=264,
            foot="Left",
            image="https://www.mancity.com/features/phil-foden-one-of-our-own/assets/VNxkiCqskG/phil-foden-one-of-our-own-2560x1440.jpg",
            bio="Philip Walter Foden (born 28 May 2000) is an English professional footballer who plays as a midfielder for Premier League club Manchester City and the England national team.",
        )
        kevin_de_bruyne = FootballerModel(
            user_id=1,
            name="Kevin De Bruyne",
            position="Midfielder",
            shirt_number=17,
            nationality="Belgian",
            club="Manchester City",
            career_goals=148,
            career_appearances=604,
            foot="Right",
            image="https://www.coachesvoice.com/wp-content/uploads/2021/10/DeBruyneMobile.jpg",
            bio="Kevin De Bruyne (born 28 June 1991) is a Belgian professional footballer who plays as a midfielder for and captains both Premier League club Manchester City and the Belgium national team. He is widely regarded as one of the greatest players of his generation, as well as one of the best midfielders in the world. Pundits have described him as a complete footballer.",
        )
        erling_haaland = FootballerModel(
            user_id=1,
            name="Erling Haaland",
            position="Forward",
            shirt_number=9,
            nationality="Norwegian",
            club="Manchester City",
            career_goals=238,
            career_appearances=292,
            foot="Right",
            image="https://upload.wikimedia.org/wikipedia/commons/6/6e/Erling_Haaland_2023_%28cropped-v2%29.jpg",
            bio="Erling Braut Haaland (born 21 July 2000) is a Norwegian professional footballer who plays as a striker for Premier League club Manchester City and the Norway national team. Considered one of the best players in the world, he is known for his speed, strength, positioning, and finishing inside the box. In his debut Premier League season, Haaland broke the record for the most goals scored by a player in a single season, with 36.",
        )
        ramsdale = FootballerModel(
            user_id=1,
            name="Aaron Ramsdale",
            position="Goalkeeper",
            shirt_number=1,
            nationality="English",
            club="Arsenal",
            career_goals=0,
            career_appearances=215,
            foot="Right",
            image="https://media.cnn.com/api/v1/images/stellar/prod/230804092833-02-aaron-ramsdale.jpg?c=original",
            bio="Aaron Christopher Ramsdale (born 14 May 1998) is an English professional footballer who plays as a goalkeeper for Premier League club Arsenal and the England national team.",
        )
        saliba = FootballerModel(
            user_id=1,
            name="William Saliba",
            position="Defender",
            shirt_number=2,
            nationality="French",
            club="Arsenal",
            career_goals=6,
            career_appearances=193,
            foot="Right",
            image="https://assets.goal.com/images/v3/blt28eeb5c0c27c75ce/GOAL_-_Blank_WEB_-_Facebook_-_2023-09-12T131353.608.png?auto=webp&format=pjpg&width=3840&quality=60",
            bio="William Alain André Gabriel Saliba (born 24 March 2001) is a French professional footballer who plays as a centre-back for Premier League club Arsenal and the France national team. He is considered by many to be one of the best centre-backs in world football.",
        )
        rice = FootballerModel(
            user_id=1,
            name="Declan Rice",
            position="Midfielder",
            shirt_number=41,
            nationality="English",
            club="Arsenal",
            career_goals=21,
            career_appearances=294,
            foot="Right",
            image="https://i2-prod.mirror.co.uk/incoming/article31031024.ece/ALTERNATES/n615/0_GettyImages-1692793263.jpg",
            bio="Declan Rice (born 14 January 1999) is an English professional footballer who plays as a defensive midfielder for Premier League club Arsenal and the England national team.",
        )
        odegaard = FootballerModel(
            user_id=1,
            name="Martin Ødegaard",
            position="Midfielder",
            shirt_number=8,
            nationality="Norwegian",
            club="Arsenal",
            career_goals=71,
            career_appearances=380,
            foot="Right",
            image="https://d2x51gyc4ptf2q.cloudfront.net/content/uploads/2023/01/02114755/Martin-Odegaard-Arsenal-F365-10.jpg",
            bio="Martin Ødegaard (born 17 December 1998) is a Norwegian professional footballer who plays as a midfielder for and captains both Premier League club Arsenal and the Norway national team. Considered one of the best midfielders in the world, he is known for his technique, dribbling ability, vision and range of passing.",
        )
        saka = FootballerModel(
            user_id=1,
            name="Bukayo Saka",
            position="Foward",
            shirt_number=7,
            nationality="English",
            club="Arsenal",
            career_goals=57,
            career_appearances=226,
            foot="Right",
            image="https://assets.goal.com/images/v3/bltd56c89691e495897/saka_arsenal.jpg?auto=webp&format=pjpg&width=3840&quality=60",
            bio="Bukayo Ayoyinka Temidayo Saka (born 5 September 2001) is an English professional footballer who plays as a right winger for Premier League club Arsenal and the England national team. He is regarded as one of the best wingers in the world",
        )

        mo_salah.save()
        mac_allister.save()
        alexander_arnold.save()
        virgil_van_dijk.save()
        allison_becker.save()
        ederson.save()
        john_stones.save()
        phil_foden.save()
        kevin_de_bruyne.save()
        erling_haaland.save()
        ramsdale.save()
        saliba.save()
        rice.save()
        odegaard.save()
        saka.save()

        comment = CommentModel(content="What a player!", footballer_id=1, user_id=1)
        comment.save()

        print("database seeded!")
    except Exception as e:
        print(e)
