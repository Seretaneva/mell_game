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
    style.andrei_what.color = "#ffffff"
    style.andrei_what.size = 35
    style.andrei_what.slow_cps = 25
    style.andrei_what.outlines = [(2, "#000000", 0, 0)]
    style.andrei_what.top_margin = 30

    # nou:
    style.andrei_what.justify = True      # întinde rândurile până la marginea dreaptă
    style.andrei_what.text_align = 0.0    # păstrează începutul la stânga (implicit)

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
  # ajustează în funcție de lățimea totală a ecranului




init python:
    # Padding în textbox
    style.window.left_padding = 30
    style.window.right_padding = 30
    style.window.top_padding = 65
    style.window.bottom_padding = 30

#----------------CHARACTERS------------------------------------------------------------
# Leagă naratorul de stilul cu scriere lentă
define e = Character(None, what_style="narr_what")
define m = Character("Андрей", what_style="andrei_what", who_style="andrei_who")
define f = Character("Брат",what_style="andrei_what", who_style="andrei_who")
define me = Character("Mellstroy", what_style="andrei_what", who_style="andrei_who")
define C = Character("Чат", color="#9fff9f", what_style="andrei_what")
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
#-------------------------------------------------------
# STATS & FLAGS (NEW)
# =========================
default REP = 12
default CASH = 250
default CTRL = 6

default FLAG_CASINO = False      # серая интеграция активна
default FLAG_CONFLICT = False    # был острый конфликт «на камеру»
default FLAG_MEDIA = False       # появился интерес медиа/журнала
default FLAG_NEIGHBORS = False   # соседи/управляющая компания давят
default FLAG_VIRAL = False       # нарезка с вечеринки ушла в вирал

# =========================
# HUD (NEW)
# =========================
screen statbar():
    frame:
        align (0.02, 0.02)
        has hbox
        spacing 18
        frame:
            padding (10,6)
            text "Репутация: [REP]" size 28
        frame:
            padding (10,6)
            text "Деньги: [CASH]₽" size 28
        frame:
            padding (10,6)
            text "Контроль: [CTRL]" size 28

# Mic utilitar (opțional): limitează stats 0..99
init python:
    def clamp_stats():
        global REP, CASH, CTRL
        REP = max(0, min(99, REP))
        CASH = max(0, min(999999, CASH))
        CTRL = max(0, min(99, CTRL))

# =========================
# SFX helpers (opțional)
# =========================
define s_knock = "audio/knock_heavy.mp3"
define s_notify = "audio/notify.mp3"
define s_click  = "audio/click.wav"

# =========================================
# CONTINUAREA — după label choice_final_3_1
# =========================================
#----------------------------------------------------------------------------
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
define audio.click = "audio/click.mp3"
define audio.baclajan = "audio/baclajan.mp3"
define audio.badlo = "audio/badlo.mp3"
define audio.dictuesh = "audio/dictuesh.mp3"
define audio.patzan = "audio/patzan.mp3"
define audio.krasnii = "audio/krasnii.mp3"
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

    with moveinleft

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

        with moveinleft

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
    play sound suka
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
        play sound krasnii
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
         $ renpy.movie_cutscene("videos/crug.webm")
         play sound am fadein 0.70
         $ REP += 2
         jump choice_final_3_1

    label choice_final_3_1:
  #------------------------------------------------------------------------------------------------

    # dacă a fost show dur sau glumă: setăm un „impuls” și mergem mai departe
        if not FLAG_VIRAL:
            $ FLAG_VIRAL = True
            $ REP += 2
            $ CASH += 120
            $ clamp_stats()
            C "КЛИПАЙ! КЛИПАЙ! Это разлетится!"


        stop music fadeout 1.0
        play sound s_knock

    e "Глухой, настойчивый стук в дверь. Музыка будто сама стихает, камеры продолжают писать."
    m "Кто там, мать его?.."
    C "ОТКРОЙ! ОТКРОЙ!"

    e "Как Андрей действует?"
    menu:
            "Открыть на стриме — показать силу и контроль (риск)":
                $ REP += 1
                $ CTRL -= 1
                $ FLAG_CONFLICT = True
                $ clamp_stats()
                jump door_public

            "Выключить эфир, решить тихо":
                $ CTRL += 2
                $ REP += 1
                $ clamp_stats()
                jump door_private

            "Позвонить промоутеру за «помощью»":
                if FLAG_CASINO:
                    $ CASH -= 50
                    $ CTRL += 1
                    $ REP -= 1
                    $ clamp_stats()
                    jump door_handler
                else:
                    "Андрей набирает номер... но вспоминает — {i}он отказался от сделки{/i}."
                    jump door_private

# ---------- 1) PUBLIC (шоу) ----------
    label door_public:
        play music party_music fadein 0.7
        show neighbor at right:
             xysize (500, 800)
        with moveinright

        e "Ты распахиваешь дверь. На пороге стоит сосед — злой, в халате, с телефоном в руке."
        $ FLAG_NEIGHBORS = True
        play sound baclajan fadein 0.5
        "Сосед" "Вы что, бл**? Ночь на дворе! Это что за цирк, мать вашу?!"



        C "ООООО! ЖЕСТЬ ПРИШЛА!"
        # mini-choice în fața publicului
    menu:
        "Держать рамку, предложить компромисс.":
            $ CTRL += 2
            $ CASH -= 100
            $ REP += 1
            $ clamp_stats()
            me "Так, бл**, хватит кипеть. Музыку убавлю, людей разгоню — всё, вопрос решён."
            "Сосед" "Ладно... только чтоб без этого больше."
            me "Будет тихо. Не кипятись, живём рядом — без цирка."
            "Сосед" "Окей..."
            e "Сосед уходит, дверь захлопывается. В квартире снова гул и свет ламп."
            hide neighbor
            jump post_door


        "Резко отвечать, давить статусом (риск скандала)":
            $ REP += 2
            $ CTRL -= 2
            $ clamp_stats()

            play sound badlo fadein 0.5
            me "Ты чё несёшь, бл**? Это мою хату и эфир трогать нельзя, понял ?"
            stop sound

            play sound patzan fadein 0.5
            "Сосед" "Ты на кого голос поднимаешь? Сейчас полицию вызову, понял?!"
            me "Давай, зови! Мне скрывать нечего. Только потом не ной, когда сам на стрим попадёшь!"
            stop sound

            C "ЩАС БУДЕТ!"
            hide neighbor
            jump post_door

# ---------- 2) PRIVATE (де-эскалация) ----------
    label door_private:
        play sound click
        e "Ты тихо отключаешь стрим. Экран гаснет, лампа мерцает."
        play sound knock_heavy
        e "Стук в дверь. За порогом слышен раздражённый голос."
        show neighbor at right:
             xysize (500, 800)
        with moveinright
        play sound patzan fadein 0.5
        "Сосед" "Эй, ты там! Полночь, бл**! Музыку прикрути уже!"

        me "Успокойся, сосед. Всё, тише делаем, люди уходят."
        "Сосед" "Каждую ночь одно и то же! Мы тебе не клуб под окном держим!"
        me "Я понял, бл**, хватит орать. Всё, вопрос закрыт. Иди спи спокойно."
        $ CTRL += 1
        $ CASH -= 80
        $ REP += 1
        $ clamp_stats()
        hide neighbor
        jump post_door

# ---------- 3) HANDLER (серый компромисс) ----------
    label door_handler:
        e "Ты шепотом даёшь сигнал промоутеру. Через десять минут подъезжает «решала»."
        "Решала" "Сейчас разберёмся. Официально — вы талант, не проблема. Неофициально — вот купоны на такси для подъезда, извиняемся."
        $ CASH -= 150
        $ CTRL += 1
        $ REP -= 1
        $ clamp_stats()
        show neighbor at right:
             xysize (500, 800)
        with moveinright
        "Сосед" "Ладно. Только если сегодня — конец."
        hide neighbor
        jump post_door

# ---------- POST DOOR: финальная раздача и хук ----------
    label post_door:
        stop music fadeout 1.0
        scene room4 at truecenter:
            xysize (1920, 1080)
    with fade
    # Бонус/штраф в зависимости de cum a mers
    if REP >= 15 and CTRL >= 7:
        e "На утро сторис у местных пабликов: «Как провести вечеринку и не поссориться со всем домом»."
        $ CASH += 200
        $ FLAG_MEDIA = True
        $ clamp_stats()
    elif CTRL <= 3:
        e  "В телеграм-чатах дома начинается обсуждение: скрины, теги, угрозы жалоб."
        $ REP -= 1
        $ clamp_stats()

    # Короткая сцена послевкусия
    play music sad1 fadein 0.8

    e  "Квартира затихает. Пластик стаканов, запах сладкой колы и дешёвых духов. Андрей сидит напротив чёрного монитора."
    me "Всё это похоже на контроль. Но на самом деле — это тонкая грань. Один неверный шаг — и ты просто шум."
    if FLAG_VIRAL:
        C "НАРЕЗКИ В ТРЕНДАХ! «Момент с дверью» — ТОП!"
        $ REP += 1
        $ clamp_stats()

    # Клиффхэнгер к следующей главе
    play sound ring
    e "Телефон вибрирует. Номер неизвестен."
    stop sound
    "Голос" "Привет, Андрей. Видели твой эфир. Есть предложение. Не телик, не радио. Крупнее. Встретимся?"
    me "(внутри) Игра становится дороже. Вопрос — кто платит чек."
    stop music fadeout 1.3

    scene black with fade
    centered "{size=70}{=centered_narr}Глава III — завершена{/centered_narr}{/size}"
    $ persistent.REP_ch2 = REP
    $ persistent.CASH_ch2 = CASH
    $ persistent.CTRL_ch2 = CTRL

    # =========================
# ГЛАВА IV — «Цена шума»-----------------------------------------------------------------------------------
# Сильная слава → срыв → последствия
# =========================

# Новые флаги для сюжета
default FLAG_LEGAL = False        # пошёл юридический процесс
default FLAG_APOLOGY = False      # сделал извинение
default FLAG_BAN = False          # платформа/площадки ввели ограничения
default FLAG_BREAK = False        # объявил паузу/рефлексии

label chapter4:

    scene black
    show text _("{size=70}{=centered_narr}Глава IV — Цена шума{/=centered_narr}{/size}") at truecenter
    with fade
    pause 2
    hide text

    # Он уже «на вершине»
    scene party at truecenter:
        xysize (1920,1080)
    play music party_music fadein 1.0
    show screen statbar

    e "Вечер. Онлайны бьют рекорды. Комната — как студия: свет, камеры, люди. Донаты летят, чат трещит."
    C "ГОСТЕЙ БОЛЬШЕ! ДВИЖ!"
    C "ТОП МОМЕНТЫ, ПОГНАЛИ!"
    me "Сегодня делаем громче. Вы хотели шоу — получите. Без тормозов."

    # Разгон — напряжение растёт
    "Гость" "Ну что, ставки? Танец, челлендж, импров?"
    me "Делаем импров. Кто не тянет — уходит из кадра. Всё честно."
    e "Смех, толчки локтями, телефоны, вспышки. Ритм ускоряется. Андрей на грани — энергетика давит изнутри."

    # Точка срыва — БЕЗ графики: перебивка/чёрный экран + звук/чат
    stop music fadeout 0.5
    play sound "audio/stop-stop.mp3"
    e "Мгновение — и всё идёт не так. Слова — острые, как стекло. Сцена ломается."
    scene black with hpunch
    e "Камера дёргается. Кадр рвётся. Чат взрывается."
    C "ЭЭЭ! ЧТО ЭТО БЫЛО?!"
    C "ПЕРЕШЁЛ ГРАНЬ!"
    play sound "audio/laugh.mp3"
    e "Смех где-то сбоку переходит в гул. Кто-то кричит «Вырубай!»"

    # Постфактум: последствия
    scene dark_room with slow_dissolve
    play music sad1 fadein 0.8
    e "Тишина наступает резко. Монитор горит холодным светом. Кто-то закрывает дверь."
    me "(тяжело дышит) …Чёрт. Это было лишнее."
    $ REP -= 3
    $ CTRL -= 2
    $ CASH -= 100
    $ FLAG_LEGAL = True
    $ clamp_stats()

    # Реакция вокруг
    C "КЛИПЫ УЖЕ В СЕТИ!"
    C "ВСЁ, ЕГО ОТМЕНЯТ!"
    C "ЗВОНИ ПРЕДСТАВИТЕЛЮ!"
    e "Телефон вибрирует без остановки. Сообщения, метки, «обсуждают все»."
    e "Как Андрей реагирует?"
    # Выбор стратегии: отрицать/извиниться/уйти на паузу
    menu:

            "Отрицать: «Вы всё переврали!» (риск эскалации)":
                $ REP -= 2
                $ CTRL -= 1
                $ FLAG_BAN = True
                $ clamp_stats()
                me "Вы вообще видели контекст? Вы всё перегнули! Ничего криминального!"
                C "ФУ! НЕ ВЕРИМ!"
                e "Площадки начинают ставить ограничения. Новостные паблики берут тему."
                jump ch4_afterchoice

            "Извиниться публично: коротко и чётко (снижение огня)":
                $ REP += 1
                $ CTRL += 2
                $ CASH -= 50
                $ FLAG_APOLOGY = True
                $ clamp_stats()
                me "Я перегнул. Это неправильно. Извиняюсь. Видео сниму, эфиры пересоберу. Грань — есть грань."
                C "ПРИНЯЛ. СЛЕДИ ЗА СЛОВАМИ!"
                e "Часть аудитории выдыхает. СМИ фиксируют извинение."
                jump ch4_afterchoice

            "Уйти на паузу: выключить эфиры, взять ответственность (дорого, но взросло)":
                $ CTRL += 3
                $ REP -= 1
                $ CASH -= 300
                $ FLAG_BREAK = True
                $ clamp_stats()
                me "Стоп. Беру паузу. С командой разберём формат, пересмотрим правила. Я отвечаю за то, что делаю."
                C "ДА, ТАК НАДО… НО БОЛЬНО!"
                e "Шум слегка стихает. Появляется пространство для хода дальше."
                jump ch4_afterchoice

label ch4_afterchoice:

    # Юридический хвост
    if FLAG_LEGAL:
        play sound "audio/ring.mp3"
        e "Звонок от юристов. Сухие фразы, ссылки на статьи, «нужна встреча»."
        me "(в сторону) Игра подорожала. Теперь каждый шаг — чек."
        $ CASH -= 200
        $ CTRL += 1
        $ clamp_stats()

    # Короткий прессинг медиа/площадок
    if FLAG_BAN:
        e "Одна из платформ пишет: «Временное ограничение эфиров». Несколько брендов ставят паузу."
        $ REP -= 1
        $ clamp_stats()
    elif FLAG_APOLOGY:
        e "Несколько пабликов отмечают извинение. Волна негатива не уходит, но острота падает."
        $ REP += 1
        $ clamp_stats()

    # Мини-арка «безумия от славы и денег» — внутренний кризис
    scene loft_empty with slow_dissolve
    e "Комната, ещё вчера полная людей, теперь кажется слишком большой. Деньги есть, шум был, но пустота только громче."
    me "Вам всем шоу нужно, да? А мне — чтоб не превратиться в шум и тень."
    if CTRL <= 3:
        me "(сжимает кулак) Ещё чуть-чуть — и я сам себе враг."
    else:
        me "(ровно) Держу линию. Любой ценой."
    e "Что дальше?"
    # Ход вперёд: три дорожки на следующую главу
    menu:

            "Собрать новый «белый» формат: правила, контракт с медиаплощадкой (курс на реабилитацию)":
                $ CTRL += 2
                $ REP += 1
                $ clamp_stats()
                $ persistent.path_rebuild = True
                jump ch4_outro
            "Сделать «камбэк-ночь»: один эфир, но по правилам (риск, шанс вернуть онлайн)":
                $ REP += 2
                $ CTRL -= 1
                $ CASH += 150
                $ clamp_stats()
                $ persistent.path_comeback = True
                jump ch4_outro
            "Уйти в «серые» интеграции: быстро закрыть дыры деньгами (удар по репутации)":
                $ CASH += 600
                $ REP -= 2
                $ FLAG_CASINO = True
                $ clamp_stats()
                $ persistent.path_grey = True
                jump ch4_outro

label ch4_outro:
    stop music fadeout 1.0
    scene black with fade
    centered "{size=64}{b}Глава IV — завершена{/b}{/size}"
    $ persistent.REP_ch4 = REP
    $ persistent.CASH_ch4 = CASH
    $ persistent.CTRL_ch4 = CTRL
    return


    return


