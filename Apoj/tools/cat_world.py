# -*- coding: utf-8 -*-
from catalog_helper import make_song

WORLD_SONGS = [
    make_song(
        id="world_queen_bohemian_rhapsody",
        title="Bohemian Rhapsody",
        artist="Queen",
        category="world",
        year="1975",
        durationSec=16.0,
        melodyNotes=[65, 64, 62, 60, 62, 65, 69, 67, 65, 64],
        segments_text=[
            ("Mama just killed a man", "Mama just killed a man..."),
            ("Put a gun against his head", "Put a gun against his head pulled my trigger now he's dead..."),
            ("Mama life had just begun", "Mama life had just begun..."),
            ("And now I've gone and thrown it all away", "Thrown it all away!")
        ],
        options_text=[
            ("Bohemian Rhapsody («Mama, just killed a man...»)", True),
            ("We Are the Champions («We are the champions, my friends...»)", False),
            ("Don't Stop Me Now («Tonight I'm gonna have myself a real good time...»)", False),
            ("Radio Ga Ga («All we hear is radio ga ga...»)", False)
        ],
        difficulty="MEDIUM"
    ),
    make_song(
        id="world_queen_we_will_rock_you",
        title="We Will Rock You",
        artist="Queen",
        category="world",
        year="1977",
        durationSec=15.0,
        melodyNotes=[64, 64, 64, 64, 62, 60, 64, 64, 62, 60],
        segments_text=[
            ("Buddy you're a boy make a big noise", "Buddy you're a boy make a big noise..."),
            ("Playing in the street gonna be a big man someday", "Playing in the street gonna be a big man someday..."),
            ("You got mud on your face", "You got mud on your face big disgrace..."),
            ("We will we will rock you", "We will we will rock you!")
        ],
        options_text=[
            ("We Will Rock You («We will, we will rock you!»)", True),
            ("We Are the Champions («We are the champions...»)", False),
            ("Another One Bites the Dust («And another one gone...»)", False),
            ("I Want to Break Free («I want to break free...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_imagine_dragons_believer",
        title="Believer",
        artist="Imagine Dragons",
        category="world",
        year="2017",
        durationSec=15.5,
        melodyNotes=[60, 63, 67, 65, 63, 60, 63, 67, 70, 67],
        segments_text=[
            ("First things first", "First things first I'mma say all the words inside my head..."),
            ("I'm fired up and tired of the way", "I'm fired up and tired of the way that things have been..."),
            ("Pain! You made me a you made me a believer", "Pain! You made me a believer believer..."),
            ("Pain! You break me down", "Pain! You break me down and build me up!")
        ],
        options_text=[
            ("Believer («Pain! You made me a, you made me a believer...»)", True),
            ("Radioactive («I'm waking up to ash and dust...»)", False),
            ("Demons («When the days are cold and the cards all fold...»)", False),
            ("Thunder («Thunder, feel the thunder...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_michael_jackson_billie_jean",
        title="Billie Jean",
        artist="Michael Jackson",
        category="world",
        year="1982",
        durationSec=15.2,
        melodyNotes=[66, 64, 62, 64, 66, 64, 62, 59, 62, 64],
        segments_text=[
            ("She was more like a beauty queen", "She was more like a beauty queen from a movie scene..."),
            ("I said don't mind but what do you mean", "I said don't mind but what do you mean I am the one..."),
            ("Billie Jean is not my lover", "Billie Jean is not my lover..."),
            ("She's just a girl who claims that I am the one", "The kid is not my son!")
        ],
        options_text=[
            ("Billie Jean («Billie Jean is not my lover...»)", True),
            ("Beat It («Just beat it, beat it...»)", False),
            ("Thriller («Cause this is thriller, thriller night...»)", False),
            ("Smooth Criminal («Annie, are you ok?..»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_beatles_yesterday",
        title="Yesterday",
        artist="The Beatles (Paul McCartney)",
        category="world",
        year="1965",
        durationSec=15.0,
        melodyNotes=[65, 64, 62, 60, 62, 64, 65, 64, 62, 60],
        segments_text=[
            ("Yesterday", "Yesterday all my troubles seemed so far away..."),
            ("Now it looks as though they're here to stay", "Now it looks as though they're here to stay..."),
            ("Oh I believe in yesterday", "Oh I believe in yesterday..."),
            ("Suddenly I'm not half the man I used to be", "I believe in yesterday!")
        ],
        options_text=[
            ("Yesterday («Yesterday, all my troubles seemed so far away...»)", True),
            ("Let It Be («When I find myself in times of trouble...»)", False),
            ("Hey Jude («Hey Jude, don't make it bad...»)", False),
            ("Help! («Help, I need somebody...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_beatles_yellow_submarine",
        title="Yellow Submarine",
        artist="The Beatles",
        category="world",
        year="1966",
        durationSec=14.8,
        melodyNotes=[67, 67, 65, 64, 62, 60, 64, 67, 69, 67],
        segments_text=[
            ("We all live in a yellow submarine", "We all live in a yellow submarine..."),
            ("Yellow submarine yellow submarine", "Yellow submarine yellow submarine..."),
            ("We all live in a yellow submarine", "We all live in a yellow submarine..."),
            ("Yellow submarine", "Yellow submarine!")
        ],
        options_text=[
            ("Yellow Submarine («We all live in a yellow submarine...»)", True),
            ("Yesterday («Yesterday, all my troubles...»)", False),
            ("All You Need Is Love («All you need is love...»)", False),
            ("Come Together («Here come old flat top...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_abba_dancing_queen",
        title="Dancing Queen",
        artist="ABBA",
        category="world",
        year="1976",
        durationSec=15.4,
        melodyNotes=[64, 67, 71, 72, 71, 69, 67, 64, 62, 64],
        segments_text=[
            ("You can dance you can jive", "You can dance you can jive..."),
            ("Having the time of your life", "Having the time of your life..."),
            ("See that girl watch that scene", "See that girl watch that scene..."),
            ("Dig in the dancing queen", "Dig in the dancing queen!")
        ],
        options_text=[
            ("Dancing Queen («You can dance, you can jive...»)", True),
            ("Mamma Mia («Mamma mia, here I go again...»)", False),
            ("Gimme! Gimme! Gimme! («A man after midnight...»)", False),
            ("Waterloo («Waterloo, couldn't escape if I wanted to...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_bon_jovi_its_my_life",
        title="It's My Life",
        artist="Bon Jovi",
        category="world",
        year="2000",
        durationSec=15.5,
        melodyNotes=[60, 63, 65, 67, 65, 63, 60, 63, 65, 67],
        segments_text=[
            ("It's my life", "It's my life..."),
            ("It's now or never", "It's now or never..."),
            ("I ain't gonna live forever", "I ain't gonna live forever..."),
            ("I just want to live while I'm alive", "It's my life!")
        ],
        options_text=[
            ("It's My Life («It's my life, it's now or never...»)", True),
            ("Livin' on a Prayer («Woah, we're halfway there...»)", False),
            ("Always («And I will love you, baby, always...»)", False),
            ("You Give Love a Bad Name («Shot through the heart...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_nirvana_smells_like_teen_spirit",
        title="Smells Like Teen Spirit",
        artist="Nirvana (Kurt Cobain)",
        category="world",
        year="1991",
        durationSec=15.8,
        melodyNotes=[65, 65, 68, 68, 66, 66, 63, 63, 65, 65],
        segments_text=[
            ("With the lights out it's less dangerous", "With the lights out it's less dangerous..."),
            ("Here we are now entertain us", "Here we are now entertain us..."),
            ("I feel stupid and contagious", "I feel stupid and contagious..."),
            ("A mulatto an albino a mosquito my libido", "Yeah!")
        ],
        options_text=[
            ("Smells Like Teen Spirit («Here we are now, entertain us...»)", True),
            ("Come As You Are («Come as you are, as you were...»)", False),
            ("Lithium («I'm so happy 'cause today I found my friends...»)", False),
            ("The Man Who Sold the World («We passed upon the stair...»)", False)
        ],
        difficulty="MEDIUM"
    ),
    make_song(
        id="world_acdc_highway_to_hell",
        title="Highway to Hell",
        artist="AC/DC",
        category="world",
        year="1979",
        durationSec=15.0,
        melodyNotes=[64, 67, 69, 67, 64, 62, 64, 67, 69, 67],
        segments_text=[
            ("Living easy living free", "Living easy living free..."),
            ("Season ticket on a one-way ride", "Season ticket on a one-way ride..."),
            ("I'm on the highway to hell", "I'm on the highway to hell..."),
            ("Highway to hell", "Highway to hell!")
        ],
        options_text=[
            ("Highway to Hell («I'm on the highway to hell...»)", True),
            ("Back in Black («Back in black, I hit the sack...»)", False),
            ("Thunderstruck («Thunder, thunder... Thunderstruck!»)", False),
            ("TNT («Cause I'm T.N.T., I'm dynamite...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_linkin_park_in_the_end",
        title="In the End",
        artist="Linkin Park (Chester Bennington)",
        category="world",
        year="2000",
        durationSec=15.5,
        melodyNotes=[63, 66, 65, 63, 61, 59, 61, 63, 66, 65],
        segments_text=[
            ("It starts with one thing I don't know why", "It starts with one thing I don't know why..."),
            ("It doesn't even matter how hard you try", "It doesn't even matter how hard you try..."),
            ("I tried so hard and got so far", "I tried so hard and got so far..."),
            ("But in the end it doesn't even matter", "It doesn't even matter!")
        ],
        options_text=[
            ("In the End («I tried so hard and got so far...»)", True),
            ("Numb («I've become so numb, I can't feel you there...»)", False),
            ("Faint («I am a little bit of loneliness...»)", False),
            ("Crawling («Crawling in my skin...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_coldplay_viva_la_vida",
        title="Viva La Vida",
        artist="Coldplay",
        category="world",
        year="2008",
        durationSec=15.0,
        melodyNotes=[65, 68, 70, 72, 70, 68, 65, 63, 65, 68],
        segments_text=[
            ("I used to rule the world", "I used to rule the world..."),
            ("Seas would rise when I gave the word", "Seas would rise when I gave the word..."),
            ("Now in the morning I sleep alone", "Now in the morning I sleep alone..."),
            ("Sweep the streets I used to own", "Sweep the streets I used to own!")
        ],
        options_text=[
            ("Viva La Vida («I used to rule the world...»)", True),
            ("Yellow («Look at the stars, look how they shine for you...»)", False),
            ("The Scientist («Nobody said it was easy...»)", False),
            ("Clocks («Lights go out and I can't be saved...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_aha_take_on_me",
        title="Take On Me",
        artist="a-ha",
        category="world",
        year="1985",
        durationSec=15.2,
        melodyNotes=[62, 62, 69, 66, 62, 64, 67, 66, 64, 62],
        segments_text=[
            ("Talking away", "Talking away I don't know what I'm to say..."),
            ("I'll say it anyway", "I'll say it anyway today's another day to find you..."),
            ("Take on me", "Take on me take on me..."),
            ("Take me on", "I'll be gone in a day or two!")
        ],
        options_text=[
            ("Take On Me («Take on me, take me on...»)", True),
            ("The Sun Always Shines on T.V. («Touch me, how can it be...»)", False),
            ("Hunting High and Low («Here I am and facing rain...»)", False),
            ("Stay on These Roads («Cold has found a home...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_adele_rolling_in_the_deep",
        title="Rolling in the Deep",
        artist="Adele",
        category="world",
        year="2010",
        durationSec=15.4,
        melodyNotes=[60, 63, 65, 67, 65, 63, 60, 63, 65, 67],
        segments_text=[
            ("There's a fire starting in my heart", "There's a fire starting in my heart..."),
            ("Reaching a fever pitch and it's bringing me out the dark", "Reaching a fever pitch..."),
            ("We could have had it all", "We could have had it all..."),
            ("Rolling in the deep", "Rolling in the deep!")
        ],
        options_text=[
            ("Rolling in the Deep («We could have had it all...»)", True),
            ("Someone Like You («Never mind, I'll find someone like you...»)", False),
            ("Set Fire to the Rain («But I set fire to the rain...»)", False),
            ("Hello («Hello from the other side...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_survivor_eye_of_the_tiger",
        title="Eye of the Tiger",
        artist="Survivor (к/ф «Рокки 3»)",
        category="world",
        year="1982",
        durationSec=15.0,
        melodyNotes=[60, 60, 58, 60, 60, 58, 60, 63, 62, 60],
        segments_text=[
            ("Rising up back on the street", "Rising up back on the street..."),
            ("Did my time took my chances", "Did my time took my chances..."),
            ("It's the eye of the tiger", "It's the eye of the tiger it's the thrill of the fight..."),
            ("Rising up to the challenge of our rival", "And the last known survivor!")
        ],
        options_text=[
            ("Eye of the Tiger («It's the eye of the tiger, it's the thrill of the fight...»)", True),
            ("The Final Countdown («It's the final countdown...»)", False),
            ("We Will Rock You («We will, we will rock you...»)", False),
            ("Gonna Fly Now («Theme from Rocky»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_eagles_hotel_california",
        title="Hotel California",
        artist="Eagles",
        category="world",
        year="1976",
        durationSec=16.0,
        melodyNotes=[66, 64, 62, 61, 59, 57, 59, 61, 62, 64],
        segments_text=[
            ("On a dark desert highway", "On a dark desert highway cool wind in my hair..."),
            ("Warm smell of colitas", "Warm smell of colitas rising up through the air..."),
            ("Welcome to the Hotel California", "Welcome to the Hotel California..."),
            ("Such a lovely place", "Such a lovely place!")
        ],
        options_text=[
            ("Hotel California («Welcome to the Hotel California...»)", True),
            ("Desperado («Desperado, why don't you come to your senses...»)", False),
            ("Take It Easy («Take it easy, take it easy...»)", False),
            ("One of These Nights («One of these nights...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_george_michael_careless_whisper",
        title="Careless Whisper",
        artist="George Michael (Wham!)",
        category="world",
        year="1984",
        durationSec=15.0,
        melodyNotes=[62, 65, 69, 67, 65, 64, 62, 60, 62, 65],
        segments_text=[
            ("I'm never gonna dance again", "I'm never gonna dance again..."),
            ("Guilty feet have got no rhythm", "Guilty feet have got no rhythm..."),
            ("Though it's easy to pretend", "Though it's easy to pretend..."),
            ("I know you're not a fool", "Careless whisper!")
        ],
        options_text=[
            ("Careless Whisper («I'm never gonna dance again, guilty feet...»)", True),
            ("Last Christmas («Last Christmas I gave you my heart...»)", False),
            ("Faith («Cause I gotta have faith...»)", False),
            ("Wake Me Up Before You Go-Go («Don't leave me hanging on...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="world_ed_sheeran_shape_of_you",
        title="Shape of You",
        artist="Ed Sheeran",
        category="world",
        year="2017",
        durationSec=15.0,
        melodyNotes=[61, 64, 66, 68, 66, 64, 61, 64, 66, 68],
        segments_text=[
            ("The club isn't the best place to find a lover", "The club isn't the best place to find a lover..."),
            ("So the bar is where I go", "So the bar is where I go..."),
            ("I'm in love with the shape of you", "I'm in love with the shape of you..."),
            ("We push and pull like a magnet do", "I'm in love with your body!")
        ],
        options_text=[
            ("Shape of You («I'm in love with the shape of you...»)", True),
            ("Perfect («Baby, I'm dancing in the dark...»)", False),
            ("Bad Habits («My bad habits lead to late nights...»)", False),
            ("Thinking Out Loud («When your legs don't work...»)", False)
        ],
        difficulty="EASY"
    )
]
