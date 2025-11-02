label splashscreen:
    $ _preferences.language = "russian"
    return

init python:
    # Font global + contur
    style.default.font = "fonts/DejaVuSans.ttf"
    style.default.outlines = [(2, "#000000", 0, 0)]

    # Stil narațiune (e) cu scriere treptată
    style.narr_what = Style(style.default)
    style.narr_what.size = 40
    style.narr_what.slow_cps = 25
    style.narr_what.slow_abortable = True
    style.narr_what.outlines = [(2, "#000000", 0, 0)]

    # Stilurile lui Андрей
    style.andrei_who = Style(style.say_label)
    style.andrei_who.color = "#8de0ff"    # aceeași culoare la nume
    style.andrei_who.size = 40
    style.andrei_who.bold = True
    # atenție: poziția namebox-ului se face prin gui.name_*, nu aici

    style.andrei_what = Style(style.say_dialogue)
    style.andrei_what.color = "#ffffff"   # culoarea replicilor
    style.andrei_what.size = 40
    style.andrei_what.outlines = [(2, "#000000", 0, 0)]
    style.andrei_what.top_margin = 30     # „mai jos” față de namebox

    # Titluri centrate
    style.centered_narr = Style(style.default)
    style.centered_narr.font = "fonts/cyrillic-old.otf"
    style.centered_narr.size = 92
    style.centered_narr.color = "#FFFFFF"
    style.centered_narr.text_align = 0.5
    style.centered_narr.xalign = 0.5
    style.centered_narr.yalign = 0.5

# Viteză text implicită
define config.default_text_cps = 25

# =========================================
# LAYOUT TEXTBOX (GLOBAL)
# =========================================
# namebox deasupra textboxului și aliniere cu textul
define gui.name_xpos = 210
define gui.name_ypos = -60
define gui.name_xalign = 0.0

# replicile (what) pe aceeași coloană cu numele, dar mai jos
define gui.dialogue_xpos = 200
define gui.dialogue_ypos = 50     # coboară textul în box

init python:
    # Padding în textbox
    style.window.left_padding = 30
    style.window.right_padding = 30
    style.window.top_padding = 65
    style.window.bottom_padding = 30


# Leagă naratorul de stilul cu scriere lentă
define e = Character(None, what_style="narr_what")
define m = Character("Андрей", what_style="andrei_what", who_style="andrei_who")
define f = Character("Брат",what_style="andrei_what", who_style="andrei_who")
define me = Character("Mellstroy", what_style="andrei_what", who_style="andrei_who")

# Viteză de text de siguranță (în caz că jucătorul are „Instant”)
define config.default_text_cps = 25

# =========================================================
# CANALE & AUDIO
# =========================================================

init python:
    renpy.music.register_channel(
        "narration",   # numele canalului tău
        "voice",       # tipul canalului => folosește aceleași setări ca Voice
        loop=False,
        tight=False,   # pentru voice-over narațiune lungă
        buffer_queue=True
    )
init python:
    # Padding pentru textbox
    style.window.left_padding = 70      # spațiu de la marginea stângă
    style.window.right_padding = 30     # spațiu de la marginea dreaptă
    style.window.top_padding = 65       # spațiu sus
    style.window.bottom_padding = 30

# Aliasuri audio (pune fișierele în game/audio/)
define audio.bg_m1    = "audio/bg_m1.ogg"
define audio.bg2 = "audio/bg2.mp3"
define audio.audio1nr = "audio/audio1nr.ogg"
define audio.audio2nr = "audio/audio2nr.ogg"
define audio.audio3nr = "audio/audio3nr.ogg"
define audio.audio4nr = "audio/audio4nr.ogg"
define audio.audio5nr = "audio/audio5nr.ogg"
define audio.bayyagali = "audio/mellstroy-bayyagali.mp3"
define audio.yeah = "audio/yeah.mp3"
define audio.cool = "audio/cool_music.mp3"
define audio.comp_s1 = "audio/comp_s1.mp3"
define audio.comp_m1 = "audio/comp_m1.mp3"
define audio.stop = "audio/stop-stop.mp3"
define audio.laugh = "audio/laugh.mp3"
define audio.sad1 = "audio/sad1.mp3"
define audio.ring = "audio/ring.mp3"
define audio.party_music = "audio/party_music.mp3"
define audio.am = "audio/am.mp3"
# =========================================================
# TRANZIȚII
# =========================================================
define slow_dissolve = Dissolve(1.0)

# =========================================================
# SCENĂ
# =========================================================
label start:

    $ renpy.music.set_volume(0.5, channel='music')
    stop music fadeout 2
    scene black
    with fade
    window hide

    # TITLU
    show text _("{size=70}{=centered_narr}ПУТЬ МЕЛЛСТРОЯ{/=centered_narr}{/size}") at truecenter
    with fade
    pause 2
    hide text with fade
    pause 1

    # INTRO NARAȚIUNE + MUZICĂ

    play music bg2 fadein 1.0
    play narration audio1nr

    show text _("{size=40}{color=#FFFFFF}{=centered_narr}Каждый город хранит свои истории.{/=centered_narr}{/color}{/size}") at truecenter
    with fade
    pause 2
    hide text

    show text _("{size=40}{color=#CCCCCC}{=centered_narr}Одни забываются вместе с пылью улиц...{/=centered_narr}{/color}{/size}") at truecenter
    with fade
    pause 4
    hide text

    show text _("{size=40}{color=#FFFFFF}{=centered_narr}Но эта история — о парне, который не боялся мечтать.{/=centered_narr}{/color}{/size}") at truecenter
    with fade
    pause 3
    hide text
    stop narration fadeout 0.5

    # SCENE 1
    scene gomel_10 at truecenter:
        xysize (1920, 1080)
    with fade

    play narration audio2nr
    show text _("{size=58}{=centered_narr}Иногда путь к вершине начинается не с громких слов и не с денег.{/=centered_narr}{/size}") at truecenter
    pause 5
    hide text
    stop narration fadeout 0.5

    # SCENE 2
    scene gomel_4 at truecenter:
        xysize (1920, 1080)
    with slow_dissolve

    play narration audio3nr
    show text _("{size=58}{=centered_narr}Он начинается с мечты. Маленькой, почти незаметной, но живой.{/=centered_narr}{/size}") at truecenter
    pause 6.5
    hide text
    stop narration fadeout 0.5

    # SCENE 3
    scene gomel_9 at truecenter:
        xysize (1920, 1080)
    with fade

    play narration audio4nr
    show text _("{size=58}{=centered_narr}В глубине белорусского города, где зимы долгие, а улицы тихие, жил парень по имени Андрей.{/=centered_narr}{/size}") at truecenter
    pause 6
    hide text
    stop narration fadeout 0.5

    # SCENE 4
    scene gomel_12 at truecenter:
        xysize (1920, 1080)
    with fade

    play narration audio5nr
    show text _("{size=58}{=centered_narr}Его дом был обычным, жизнь — скромной, но внутри горел огонь, который не гасили ни бедность, ни одиночество.{/=centered_narr}{/size}") at truecenter
    pause 6.5
    hide text

    stop music fadeout 1.0
    stop narration fadeout 1.0
#--------------------------------------------------------------------------------------------CAP1
    # INTERTITLU
    scene black
    show text _("{size=70}{=centered_narr}Глава I — С нижних этажей к вершинам шума{/=centered_narr}{/size}") at truecenter
    with fade
    pause 2
    hide text

    # NARAȚIUNE ÎN TEXTBOX (scriere treptată)
    window show
    scene gomel_13 at truecenter:
        xysize (1920, 1080)
    play music sad1 fadein 1.0

    e "{cps=25}Холодный вечер. Гомель утопает в лёгком тумане, фонари отражаются в лужах, словно тысячи маленьких солнц.{/cps}"
    e "{cps=25}Андрей идёт по пустой улице вместе с друзьями. Смех, запах дешёвых сигарет, пульсирующий бит из телефона.{/cps}"
    e "{cps=25}Но его мысли — далеко.{/cps}"

    show mell_y_3 at left:
        xalign 0.05
        yalign 1.0
    play sound "suka.mp3"
    m "{cps=25}«Чёрт... так дальше нельзя»{/cps}"
    m "{cps=25}«Каждый день — одно и то же. Болтовня, показуха, ни хрена не меняется.»{/cps}"

    e "Андрей возвращается домой — с пустыми руками и тяжёлой головой."


    e "Панельный дом, облезшая дверь, запах сырости и старой мебели. Всё, как всегда."
    e "Он открывает дверь в свою комнату — и замирает."


    scene room1 at truecenter:
        xysize (1920, 1080)
    with fade


    e "На кровати стояла коробка."

    hide mell_y_3
    with moveoutleft

    show mellstroy at left:
        xysize (800, 1000)
        linear 1.0 xalign 0.05
    with move

    m "Кто поставил сюда коробку?"

    menu:
        "Позвонить брату.":
            jump choice_1_1
        "Открыть коробку.":
            jump choice_1_2

    label choice_1_1:
        $ menu_flag = True
        e "Он звонит своему брату и спрашивает его:"
        m "Что за коробка у меня на кровати?"
        f "Давай быстрее, глянь, что там!"
        hide mellstroy
        with moveoutleft

        show mel5 at left:
            xysize (800, 600)
            xalign 0.05 yalign 0.5
        jump choice_final_1

    label choice_1_2:
        $ menu_flag = False
        e "Андрей не медлит — вскрывает коробку."
        jump choice_final_1

    label choice_final_1:
        play music cool fadein 1
        play sound yeah
        e "Внутри — новый, но простой компьютер. Без подсветки, без наворотов, обычный системник с недорогим монитором."
        m "Ахуеть..."
        hide mellstroy
        with moveoutleft

        stop sound fadeout 0.5
        stop music fadeout 1.0
    #-----------------------------------------CAP2
        scene black
        show text _("{size=70}{=centered_narr}Глава II — Первый стрим{/=centered_narr}{/size}") at truecenter
        with fade
        pause 2
        hide text

        scene dark_room at truecenter:
            xysize (1920, 1080)
        with fade
        e "Вечер. Комната полутёмная, только свет из монитора освещает стены."

        show mellstroy at left:
            xysize (800, 1000)
            linear 1.0 xalign 0.05
        with moveoutleft

    play sound comp_s1 fadein 1

    e "Андрей подключает провода, шумит кулер, вебка мигает красным глазом."
    e "Монитор моргнул, показал рабочий стол. Всё заработало."

    pause 1.0

    m "Ну... понеслась."

    play music cool_music fadein 2

    e"На экране пустое окно стрима. Ноль зрителей, ноль сообщений. Только он и его отражение в углу камеры."

    m "Если кто-то слышит... привет, я Андрей. Можете звать меня Меллстрой."

    e"Он запускает Dota 2. Первые минуты тихие, зрителей нет."

    m "Так... играем, как есть."
    play sound yeah
    e"Через несколько минут он проигрывает катку."


    m "Да бля... серьёзно?"

    e"Он чувствует раздражение, и в голове проскальзывает мысль сказать что-то жёсткое."
    e "Как поступит Андрей?"
    menu:

            "Сдержаться и не ругаться":
                jump choice_2_2_1
            "Сорваться и высказать всё":
                jump choice_2_2_2

    label choice_2_2_1:
         m "Ладно, спокойно... первая катка, фигня вопрос."
         e "Он продолжает играть, стараясь не показать эмоции."
         e "Стрим идёт спокойно, но зрителей почти нет."
         m "Скучно пиздец... нужно что-то замутить."
         jump choice_final_2_2

    label choice_2_2_2:
        play sound stop
        m "Да что за хуйня?!"
        e "Он срывается, ударяет по столу. В чате — первый донат."
        m "Эм... донат? За эту хуйню?!.."
        play sound laugh
        e "Андрей замечает, что после вспышки злости зрителей стало больше."
        m "Похоже, людям нравится, когда я психую..."
        m "Ну ладно, тогда получите шоу."
        jump choice_final_2_2

    label choice_final_2_2:
    e "Поздно вечером он сидит, усталый, но довольный. Это только начало."
    e "Что Андрей решит дальше?"
    menu:

            "Позвать друзей, чтобы стрим был веселее":
                jump choice_2_1

            "Продолжить один, чтобы выработать свой стиль":
                e "Нет, пока сам. Хочу понять, кто я и что делаю."
                jump choice_2_2
    label choice_2_1:

        hide mellstroy
        with moveoutleft

        show mell_money:
            xysize (700, 600)
            xalign 0.001 yalign 0.42
        with moveinleft
        play sound ring
        m "Надо звать пацанов. Вместе хоть повеселимся."
        e  "Он пишет друзьям, договаривается на завтра."
        stop sound fadeout 1
        jump choice_final_2
    label choice_2_2:
        e "Экран тускнеет. Андрей выключает комп и садится в тишине."
        jump choice_final_2

    label choice_final_2:
        m "Если людям нравится бардак... значит, я устрою им шоу. Настоящее."
    stop music fadeout 2

    #------------------------------------------CAP3
    scene black
    show text _("{size=70}{=centered_narr}Глава III — Игра началась{/=centered_narr}{/size}") at truecenter
    with fade
    pause 2
    hide text
    scene party at truecenter:
            xysize (1920, 1080)
    with fade
    play music party_music fadein 1
    play sound bayyagali fadein 0.5

    e "Прошло несколько месяцев."
    e "Имя Мелстроя знают все. Его стримы — шум, алкоголь, смех и постоянный хаос."
    e  "Он зовёт к себе популярных стримеров, блогеров, музыкантов. Каждый вечер — шоу без сценария."
    show mell_y at left:
            xysize (800, 1000)
            linear 1.0 xalign 0.05
    with moveinleft
    me "Ну что, народ, сегодня будет жара!"
    e "Комната забита людьми, гремит музыка, бутылки звенят, микрофон ловит крики и смех."
    e "Все хотят попасть к нему в эфир, даже если знают, чем это может закончиться."
    e  "В чате тысячи зрителей, донаты летят один за другим."
    e "Во время одной из трансляций рядом с ним стояла некая конкретная девушка."
    e "Он смотрит на девушку и говорит:"
    menu:

            "Я слышал от подписчиков, что ты — шлюха, да?":
                jump choice_3_3_1
            "Ты можешь, пожалуйста, снять спасательный круг, блядь?":
                jump choice_3_3_2

    label choice_3_3_1:
         me "Я слышал от подписчиков, что ты — шлюха, да?"
         e "Девушка смотрит на него и отвечает:"
         e"Ты чё, ахуел, так со мной разговаривать?"
         play sound yeah fadein 0.5

         hide mell_y
         with moveoutleft

         show mell_vshoke3 at left:
             xysize (1000, 800)
             linear 1.0 xalign 0.05
         with moveinleft

         me "Это ты охуела!"
         me "Охрана! Выведите эту шлюху из дома!"
         play sound laugh fadein 0.5
         jump choice_final_3_1

    label choice_3_3_2:
         e "Девушка с выражением недоумения: "
         e "— Что ты имеешь в виду?"
         play sound am fadein 0.70
         me "— Да я сам с собой разговариваю, успокойся нахуй."
         jump choice_final_3_1

    label choice_final_3_1:
         


    return


