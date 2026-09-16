# -*- coding: utf-8 -*-
from catalog_helper import make_song

MEMES_SONGS = [
    make_song(
        id="memes_yagoda_malinka",
        title="Ягода Малинка",
        artist="Хабиб",
        category="memes",
        year="2020",
        durationSec=15.0,
        melodyNotes=[67, 65, 64, 62, 60, 64, 67, 69, 67, 64],
        segments_text=[
            ("Ягода малинка оп-оп-оп", "Ягода малинка оп-оп-оп..."),
            ("Крутит головой залетает в топ", "Крутит головой залетает в топ..."),
            ("Такая ты грустинка холоднее льда", "Такая ты грустинка холоднее льда..."),
            ("Но улыбка твоя это просто пушка", "Просто пушка!")
        ],
        options_text=[
            ("Ягода Малинка («Ягода малинка оп-оп-оп, крутит головой...»)", True),
            ("Малинки («Малинки, малинки, такие вечеринки...»)", False),
            ("Венера-Юпитер («Ты Венера, я Юпитер...»)", False),
            ("Любимка («Время пострелять, между нами пальба...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_matushka_zemlya",
        title="Матушка Земля",
        artist="Татьяна Куртукова",
        category="memes",
        year="2024",
        durationSec=15.5,
        melodyNotes=[60, 64, 67, 69, 72, 69, 67, 64, 62, 60],
        segments_text=[
            ("Матушка земля белая березонька", "Матушка земля белая березонька..."),
            ("Для меня святая Русь для других занозонька", "Для меня святая Русь для других занозонька..."),
            ("Матушка земля белая березонька", "Матушка земля белая березонька..."),
            ("Для меня святая Русь", "Святая Русь!")
        ],
        options_text=[
            ("Матушка Земля («Матушка земля, белая березонька...»)", True),
            ("Я русский («Я русский, я иду до конца...»)", False),
            ("По полюшку («По полюшку, по полюшку иду к тебе...»)", False),
            ("Русский вальс («Легкий школьный вальс...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_skibidi",
        title="Skibidi",
        artist="Little Big",
        category="memes",
        year="2018",
        durationSec=14.8,
        melodyNotes=[60, 60, 63, 65, 60, 60, 63, 65, 67, 65],
        segments_text=[
            ("Skibidi wap-pa-pa", "Skibidi wap-pa-pa..."),
            ("Skibidi wap-pa-pa-pa-pa", "Skibidi wap-pa-pa-pa-pa..."),
            ("Skibidi wap-pa-pa", "Skibidi wap-pa-pa..."),
            ("Skibidi boom boom", "Skibidi boom boom!")
        ],
        options_text=[
            ("Skibidi («Skibidi wap-pa-pa, skibidi boom boom...»)", True),
            ("UNO («Uno, uno, dos, cuatro...»)", False),
            ("Faradenza («Uno uno uno esta corazon...»)", False),
            ("Hypnodancer («I'm a hypnodancer...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_uno",
        title="UNO",
        artist="Little Big",
        category="memes",
        year="2020",
        durationSec=15.0,
        melodyNotes=[62, 65, 67, 69, 67, 65, 62, 65, 67, 69],
        segments_text=[
            ("Uno uno uno dos cuatro", "Uno uno uno dos cuatro..."),
            ("All I have is only one pair of shoes", "All I have is only one pair of shoes..."),
            ("It's gonna be a night to remember", "It's gonna be a night to remember..."),
            ("Are you ready", "Uno dos tres quatro!")
        ],
        options_text=[
            ("UNO («Uno, uno, dos, cuatro...»)", True),
            ("Skibidi («Skibidi wap-pa-pa...»)", False),
            ("Go Bananas («I'm OK, I'm not alcoholic...»)", False),
            ("Tacos («Tacos tacos, burrito burrito...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_venera_yupiter",
        title="Венера-Юпитер",
        artist="Ваня Дмитриенко",
        category="memes",
        year="2020",
        durationSec=15.2,
        melodyNotes=[64, 67, 69, 72, 71, 69, 67, 64, 62, 60],
        segments_text=[
            ("Ты Венера я Юпитер", "Ты Венера я Юпитер..."),
            ("Ты Москва я Питер", "Ты Москва я Питер..."),
            ("Люди помогите дышать", "Люди помогите дышать..."),
            ("Ты Венера я Юпитер", "Ты Венера я Юпитер!")
        ],
        options_text=[
            ("Венера-Юпитер («Ты Венера, я Юпитер, ты Москва, я Питер...»)", True),
            ("Лего («Мы как конструктор Лего...»)", False),
            ("31-я весна («Это 31-я весна...»)", False),
            ("Юпитер («Далеко во тьме летит Юпитер...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_lyubimka",
        title="Любимка",
        artist="NILETTO",
        category="memes",
        year="2019",
        durationSec=15.0,
        melodyNotes=[60, 64, 67, 65, 64, 62, 60, 64, 62, 60],
        segments_text=[
            ("Время пострелять между нами пальба", "Время пострелять между нами пальба..."),
            ("Пау-пау па-па-па", "Пау-пау па-па-па..."),
            ("Попадаешь в сердце остаешься там", "Попадаешь в сердце остаешься там..."),
            ("Любимка", "Любимка!")
        ],
        options_text=[
            ("Любимка («Время пострелять, между нами пальба...»)", True),
            ("Краш («Ты мой краш, либо дура, либо дашь...»)", False),
            ("Fly 2 («Полетели высоко...»)", False),
            ("Ты такая красивая («Ты такая красивая, как звезда...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_malinovy_zakat",
        title="Малиновый закат",
        artist="Макс Корж",
        category="memes",
        year="2017",
        durationSec=15.4,
        melodyNotes=[60, 62, 64, 67, 65, 64, 62, 60, 62, 64],
        segments_text=[
            ("Малиновый закат стекает по стене", "Малиновый закат стекает по стене..."),
            ("И я опять один на этой стороне", "И я опять один на этой стороне..."),
            ("Малиновый закат", "Малиновый закат..."),
            ("Стекает по стене", "Стекает по стене!")
        ],
        options_text=[
            ("Малиновый закат («Малиновый закат стекает по стене...»)", True),
            ("Жить в кайф («Небо поможет нам, небо поможет нам...»)", False),
            ("Малый повзрослел («Малый повзрослел, малый повзрослел...»)", False),
            ("Пьяный дождь («И пусть капает капает дождь...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_siniy_traktor",
        title="Едет трактор (Синий трактор)",
        artist="Артем Колпаков",
        category="memes",
        year="2016",
        durationSec=14.5,
        melodyNotes=[60, 64, 67, 65, 64, 62, 60, 64, 62, 60],
        segments_text=[
            ("По полям по полям синий трактор едет к нам", "По полям по полям синий трактор едет к нам..."),
            ("У него в прицепе кто-то песенку поет", "У него в прицепе кто-то песенку поет..."),
            ("А ну малыш давай попробуй отгадай", "А ну малыш давай попробуй отгадай..."),
            ("Кто же кто же кто же песенку поет", "Кто же песенку поет!")
        ],
        options_text=[
            ("Синий трактор («По полям, по полям синий трактор едет к нам...»)", True),
            ("Черепаха («Черепаха по имени Натаха...»)", False),
            ("Акуленок («Baby shark doo doo doo...»)", False),
            ("Бибика («Колесики, колесики и красивый руль...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_po_baram",
        title="По барам",
        artist="ANNA ASTI",
        category="memes",
        year="2022",
        durationSec=15.0,
        melodyNotes=[65, 69, 72, 70, 69, 67, 65, 64, 62, 65],
        segments_text=[
            ("По барам по барам", "По барам по барам..."),
            ("Пьяная в дым угара", "Пьяная в дым угара..."),
            ("Я так хотела забыть тебя", "Я так хотела забыть тебя..."),
            ("Но не забыла", "По барам!")
        ],
        options_text=[
            ("По барам («По барам, по барам, пьяная в дым угара...»)", True),
            ("Царица («Мальчик поплыл, мальчик плачет...»)", False),
            ("Феникс («Из пепла возродится птица...»)", False),
            ("Ночью на кухне («Ночью на кухне горит огонек...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_malchik_na_devyatke",
        title="Мальчик на девятке",
        artist="DEAD BLONDE",
        category="memes",
        year="2020",
        durationSec=15.0,
        melodyNotes=[67, 65, 64, 62, 60, 64, 67, 69, 67, 64],
        segments_text=[
            ("Мальчик на девятке мчится по проспекту", "Мальчик на девятке мчится по проспекту..."),
            ("Музыка в колонках глушит весь район", "Музыка в колонках глушит весь район..."),
            ("Он такой крутой и смотрит на меня", "Он такой крутой и смотрит на меня..."),
            ("Мальчик на девятке", "Мальчик на девятке!")
        ],
        options_text=[
            ("Мальчик на девятке («Мальчик на девятке мчится по проспекту...»)", True),
            ("Бесприданница («Я не бесприданница, просто так сложилось...»)", False),
            ("Банкомат («Банкомат выдает мне рубли...»)", False),
            ("Вишневая семерка («Вишневая семерка, неоновые фары...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_gangnam_style",
        title="Gangnam Style",
        artist="PSY",
        category="memes",
        year="2012",
        durationSec=15.2,
        melodyNotes=[60, 60, 60, 63, 65, 67, 65, 63, 60, 60],
        segments_text=[
            ("Oppan Gangnam Style", "Oppan Gangnam Style..."),
            ("Gangnam Style", "Gangnam Style..."),
            ("Eh Sexy Lady", "Eh Sexy Lady..."),
            ("Oppan Gangnam Style", "Op-op-op-op oppan Gangnam Style!")
        ],
        options_text=[
            ("Gangnam Style («Oppan Gangnam Style! Eh, Sexy Lady...»)", True),
            ("Gentleman («I'm a mother father gentleman...»)", False),
            ("Haru Haru («Listen to my heart...»)", False),
            ("Fantastic Baby («Boom shakalaka...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_crazy_frog",
        title="Axel F",
        artist="Crazy Frog",
        category="memes",
        year="2005",
        durationSec=14.8,
        melodyNotes=[62, 65, 62, 62, 67, 62, 60, 62, 69, 62],
        segments_text=[
            ("Ring ding ding ding", "Ring ding ding ding baa aramba baa..."),
            ("Bomba baa barooumba", "Bomba baa barooumba..."),
            ("Wh-wh-what's going on-on", "Wh-wh-what's going on-on..."),
            ("Ding ding ding", "Ding ding ding ding ding!")
        ],
        options_text=[
            ("Axel F («Ring ding ding ding baa aramba... Crazy Frog»)", True),
            ("Popcorn («Popcorn remix...»)", False),
            ("We Are the Champions (Frog) («We are the champions...»)", False),
            ("Gummy Bear («I am a gummy bear...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_plachu_na_tehno",
        title="Плачу на техно",
        artist="Cream Soda & ХЛЕБ",
        category="memes",
        year="2020",
        durationSec=15.0,
        melodyNotes=[60, 64, 67, 69, 72, 69, 67, 64, 62, 60],
        segments_text=[
            ("Я плачу на техно", "Я плачу на техно..."),
            ("Я плачу на техно", "Я плачу на техно..."),
            ("Ты не со мной слезы текут на рейве", "Ты не со мной слезы текут на рейве..."),
            ("Плачу на техно", "Плачу на техно!")
        ],
        options_text=[
            ("Плачу на техно («Я плачу на техно, ты не со мной...»)", True),
            ("Никаких больше вечеринок («Никаких больше вечеринок...»)", False),
            ("Сердце лед («Мое сердце лед, никто не растопит...»)", False),
            ("Розовый фламинго («Розовый фламинго дитя заката...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_ugonschitsa",
        title="Угонщица",
        artist="Ирина Аллегрова",
        category="memes",
        year="1994",
        durationSec=15.2,
        melodyNotes=[64, 67, 69, 72, 71, 69, 67, 64, 62, 64],
        segments_text=[
            ("Угнала тебя угнала", "Угнала тебя угнала..."),
            ("Ну и что же здесь криминального", "Ну и что же здесь криминального..."),
            ("Я полюбила тебя на глазах у всех", "Я полюбила тебя на глазах у всех..."),
            ("Угонщица", "Угонщица!")
        ],
        options_text=[
            ("Угонщица («Угнала тебя, угнала, ну и что же тут криминального...»)", True),
            ("Младший лейтенант («Младший лейтенант, мальчик молодой...»)", False),
            ("Фотография 9х12 («Фотография 9 на 12 с наивной подписью на память...»)", False),
            ("Шальная императрица («Гуляй, шальная императрица...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_dip_haus",
        title="Увезите меня на Дип-хаус",
        artist="GAYAZOV$ BROTHER$",
        category="memes",
        year="2019",
        durationSec=15.0,
        melodyNotes=[60, 64, 67, 65, 64, 62, 60, 64, 67, 72],
        segments_text=[
            ("Увезите меня на Дип-хаус", "Увезите меня на Дип-хаус..."),
            ("Я надену самый лучший костюм", "Я надену самый лучший костюм..."),
            ("И пускай весь мир подождет", "И пускай весь мир подождет..."),
            ("Увезите меня на Дип-хаус", "Увезите меня на Дип-хаус!")
        ],
        options_text=[
            ("Увезите меня на Дип-хаус («Я надену самый лучший костюм...»)", True),
            ("Малиновая Лада («Малиновая Лада, малиновый закат...»)", False),
            ("Пошла жара («Пошла жара, огонь на танцполе...»)", False),
            ("Кредо («Мое кредо — быть первым...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_chastushki_sektor",
        title="Частушки",
        artist="Сектор Газа (Юрий Хой)",
        category="memes",
        year="1993",
        durationSec=14.5,
        melodyNotes=[67, 67, 65, 64, 62, 60, 64, 67, 72, 67],
        segments_text=[
            ("Эх гармошка заиграла", "Эх гармошка заиграла весело и звонко..."),
            ("Выходи плясать народ", "Выходи плясать народ собирай девчонок..."),
            ("Частушки запевай", "Частушки запевай..."),
            ("Громче подпевай", "Громче подпевай!")
        ],
        options_text=[
            ("Частушки («Эх, гармошка заиграла...»)", True),
            ("Пора домой («Вечером на лавочке...»)", False),
            ("Туман («Ядреный туман...»)", False),
            ("Демобилизация («Скоро дембель, поезд мчит домой...»)", False)
        ],
        difficulty="EASY"
    ),
    make_song(
        id="memes_dymok",
        title="Дымок",
        artist="Ицык Цыпер & Игорь Цыба",
        category="memes",
        year="2023",
        durationSec=15.0,
        melodyNotes=[57, 60, 64, 62, 60, 59, 57, 60, 64, 67],
        segments_text=[
            ("Дымок пошел по комнате", "Дымок пошел по комнате..."),
            ("Кругом туман и тишина", "Кругом туман и тишина..."),
            ("А мы сидим вдвоем с тобой", "А мы сидим вдвоем с тобой..."),
            ("Дымок", "Дымок!")
        ],
        options_text=[
            ("Дымок («Дымок пошел по комнате, кругом туман...»)", True),
            ("По барам («По барам, по барам...»)", False),
            ("Ягода Малинка («Оп-оп-оп, крутит головой...»)", False),
            ("Матушка Земля («Белая березонька...»)", False)
        ],
        difficulty="EASY"
    )
]
