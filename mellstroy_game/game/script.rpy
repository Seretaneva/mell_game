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
        align (0.02, 0.05)
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
define audio.money = "audio/money.mp3"
define audio.dovlenie = "audio/dovlenie.mp3"
define audio.punch = "audio/punch.mp3"
define audio.romantic = "audio/romantic.mp3"
define audio.girl_laugh = "audio/girl_laugh.mp3"
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
    show screen statbar
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
            $ CTRL -= 1
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
        $REP +=1
        hide mellstroy
        with moveoutleft

        stop sound fadeout 0.5
        stop music fadeout 1.0

        show screen statbar
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
    $ CTRL -=1

    m "Да бля... серьёзно?"

    e"Он чувствует раздражение, и в голове проскальзывает мысль сказать что-то жёсткое."
    e "Как поступит Андрей?"
    menu:

            "Сдержаться и не ругаться":
                jump choice_2_2_1
                $CTRL +=2
                $REP -=1
            "Сорваться и высказать всё":
                play sound money
                $REP +=2
                $CTRL -=1
                $CASH +=100
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
        play sound money
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
                $REP +=2
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
    hide screen statbar
    scene black with fade
    centered "{size=70}{=centered_narr}Глава I — завершена{/centered_narr}{/size}"
    #------------------------------------------CAP2

    scene black
    show text _("{size=70}{=centered_narr}Глава II — Игра началась{/=centered_narr}{/size}") at truecenter
    with fade
    pause 2
    hide text
    show screen statbar
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
                $REP +=2
                play sound money
                $CASH +=200
                $CTRL -=1
                jump choice_3_3_1
            "Ты можешь, пожалуйста, снять спасательный круг, блядь?":
                jump choice_3_3_2
                $REP +=3
                play sound money

    label choice_3_3_1:
         me "Я слышал от подписчиков, что ты — шлюха, да?"
         show botox2 at right:
            xysize (700, 700)
         with moveinright
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
         hide botox2

         with moveoutright
         me "Охрана! Выведите эту шлюху из дома!"
         play sound laugh fadein 0.5
         jump choice_final_3_1

    label choice_3_3_2:
         $ renpy.movie_cutscene("videos/crug.webm")
         play sound am fadein 0.70
         $ REP += 2
         $CASH +=500
         jump choice_final_3_1

    label choice_final_3_1:
  #------------------------------------------------------------------------------------------------

    # dacă a fost show dur sau glumă: setăm un „impuls” și mergem mai departe
        if not FLAG_VIRAL:
            $ FLAG_VIRAL = True
            $ REP += 2
            play sound money
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
        play sound patzan fadein 0.5
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
            hide mell_vshoke3
            hide mell_y
            with moveoutleft

            show mell_y_3 at left:
                xysize (1400, 900)
            with moveinleft
            me "Ты чё несёшь, бл**? Это мою хату и эфир трогать нельзя, понял ?"
            stop sound


            "Сосед" "Ты на кого голос поднимаешь? Сейчас полицию вызову, понял?!"
            me "Давай, зови! Мне скрывать нечего. Только потом не ной, когда сам на стрим попадёшь!"
            stop sound

            C "ЩАС БУДЕТ!"
            hide neighbor
            jump post_door

# ---------- 2) PRIVATE (де-эскалация) ----------
    label door_private:
        play sound click

        scene room4 at truecenter:
            xysize (1920, 1080)
        with fade

        show mell_y_3 at left:
            xysize (1400, 800)
        with moveinleft
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
        play sound money
        $ CASH += 200
        $ FLAG_MEDIA = True
        $ clamp_stats()
    elif CTRL <= 3:
        e  "В телеграм-чатах дома начинается обсуждение: скрины, теги, угрозы жалоб."
        $ REP -= 1
        $ clamp_stats()

    # Короткая сцена послевкусия
    play music sad1 fadein 0.8
    show mell_y_3 at left:
            xysize (1400, 800)
    e  "Квартира затихает. Пластик стаканов, запах сладкой колы и дешёвых духов. Андрей сидит напротив чёрного монитора."
    me "Заебало всё, хочу больше денег!."
    if FLAG_VIRAL:
        C "НАРЕЗКИ В ТРЕНДАХ! «Момент с дверью» — ТОП!"
        $ REP += 1
        $ clamp_stats()

    # Клиффхэнгер к следующей главе
    play sound ring
    e "Телефон вибрирует. Номер неизвестен."
    stop sound
    "Голос" "Привет, Андрей. Видели твой эфир. Есть предложение. Не телик, не радио. Крупнее. Встретимся?"
    me "Что за хуй?"
    stop music fadeout 1.3

    scene black with fade
    centered "{size=70}{=centered_narr}Глава II — завершена{/centered_narr}{/size}"
    $ persistent.REP_ch2 = REP
    $ persistent.CASH_ch2 = CASH
    $ persistent.CTRL_ch2 = CTRL

    hide screen statbar   # =========================
# ГЛАВА III — «Цена шума»-----------------------------------------------------------------------------------
# Сильная слава → срыв → последствия
# =========================

# Новые флаги для сюжета
default FLAG_LEGAL = False        # пошёл юридический процесс
default FLAG_APOLOGY = False      # сделал извинение
default FLAG_BAN = False          # платформа/площадки ввели ограничения
default FLAG_BREAK = False        # объявил паузу/рефлексии

label chapter4:

    scene black
    show text _("{size=70}{=centered_narr}Глава III — Цена шума{/=centered_narr}{/size}") at truecenter
    with fade
    pause 2
    hide text

    # Он уже «на вершине»
    scene big_party at truecenter:
        xysize (1920,1080)
    play music party_music fadein 1.0
    show screen statbar

    e "Вечер. Онлайны бьют рекорды. Комната — как студия: свет, камеры, люди. Донаты летят, чат трещит."
    $CASH +=20000
    show mel6 at left:
        xysize (1000, 1000)
    with moveinleft
    C "ГОСТЕЙ БОЛЬШЕ! ДВИЖ!"
    C "ТОП МОМЕНТЫ, ПОГНАЛИ!"
    play sound laugh
    me "Бляяя. Сейчас будет весело, нахуй!"
    show alena at right:
         xysize (1400, 800)
    with moveinright
    # Разгон — напряжение растёт
    "Гость" "Покажи, что ты топчик!?"
    play sound krasnii
    menu:
        "Не сдержаться и ударить (риск последствий)":

            jump ch4_choice_attack


        "Сдержаться и отпустить (держать линию)":
            jump ch4_choice_resist


        "Выключить стрим прямо сейчас":
            jump ch4_choice_off

    label ch4_choice_attack:
        # Резкая сцена — без графических подробностей, с чёрной перебивкой
        stop music fadeout 0.5
        play sound "audio/stop-stop.mp3"
        scene black with hpunch
        play sound dovlenie
        e "Вспышка. Руки дрожат. Комната замолкает на долю секунды, а потом взрывается шумом."
        C "ЭЭЭ! ТЫ ЧЁ?!"
        scene big_party at truecenter:
            xysize (1920,1080)
        with Fade(2.5, 1.0, 1.0)
        e "Камера дёрнулась. Чат лихорадит, донаты летят — но воздух стал тяжёлым."

        $ REP -= 4
        $ CTRL -= 3
        $ CASH += 300
        $ FLAG_LEGAL = True # запускаем юридические последствия
        $ FLAG_VIRAL = True # момент уходит в вирал
        $ clamp_stats()

        show vah at left:
            xysize (1400, 800)
        with moveinleft
        play sound suka
        me "…Бля. Перегнул."
        play music sad1 fadein 0.8
        jump ch4_afterchoice




    label ch4_choice_resist:
        # Спокойная деэскалация в кадре

        me "Пошла нахуй отсюда!"
        play sound punch
        hide alena
        with moveoutright
        e "Он делает шаг назад и опускает руки. Сцена сдувается, но в комнате становится легче дышать."
        $ CTRL += 3
        $ REP += 1
        $ CASH -= 50
        $ clamp_stats()


        C "ВОТ ЭТО КОНТРОЛЬ!"
        play sound "audio/click.mp3"
        jump ch4_afterchoice

    label ch4_choice_off:
        # Моментальное выключение эфира
        stop music fadeout 0.7
        play sound "audio/click.mp3"
        scene room4 at truecenter:
             xysize (1920,1080)
        with fade
        e "Экран гаснет. Свет камер тухнет. В квартире — только тишина и короткое эхо шагов."
        $ CTRL += 4
        $ REP -= 1
        $ CASH -= 200
        $ FLAG_BREAK = True # объявил паузу
        $ clamp_stats()
        show mell_y_3 at left:
            xysize (1400, 800)
        with moveinleft
        me "Эфир — стоп. Разберёмся без шоу."
        play music sad1 fadein 0.8
        jump ch4_afterchoice

    label ch4_afterchoice:

    if FLAG_LEGAL:
        play sound "audio/ring.mp3"
        e "Телефон звонит без пауз. Сообщения от юриста, метки знакомых, сухие формулировки в почте."
        me "Игру подорожали. Теперь каждый шаг — чек."
        $ CASH -= 2000
        $ CTRL += 1
        $ clamp_stats()

    if FLAG_VIRAL:
        C "КЛИПЫ В ТРЕНДАХ! МОМЕНТ РАЗЛЕТЕЛСЯ!"

        $ REP += 1
        $ clamp_stats()


    if FLAG_BREAK:
        e "Он пишет короткий пост: «Нужна пауза. Пересобираю формат. Возвращусь с правилами»."
        $ CTRL += 1
        $ clamp_stats()


        # Мягкая вилка следующего шага
        e "Что дальше?"
    menu:
        "Публично извиниться и пересобрать формат (реабилитация)":
            $ REP += 1
            $ CTRL += 2
            $ CASH -= 1000
            $ FLAG_APOLOGY = True
            $ clamp_stats()
            me "Я перегнул. Извиняюсь. Пересоберём правила — границы есть."
            jump ch4_outro


        "Сделать камбэк‑стрим по правилам (риск, но шанс вернуть онлайн)":
            $ REP += 2
            $ CTRL -= 1
            $ CASH += 150
            $ clamp_stats()
            me "Один вечер. Жёсткий, но по правилам. Без срывов. Погнали."
            jump ch4_outro


        "Уйти в серые интеграции, закрыть дыры деньгами (удар по репутации)":
            $ CASH += 6000
            $ REP -= 2
            $ FLAG_CASINO = True
            $ clamp_stats()
            me "Ладно. Да и похуй вообще. Сама виновата."
            jump ch4_outro

    label ch4_outro:
        stop music fadeout 1.0
        scene black with fade
        centered "{size=64}{=centered_narr}Глава IV — завершена{/centered_narr}{/size}"
        $ persistent.REP_ch4 = REP
        $ persistent.CASH_ch4 = CASH
        $ persistent.CTRL_ch4 = CTRL
        hide screen statbar
#---------------------------------------------------------------CAP 4 --------------------------------------------
    label chapter5:

        scene black
        show text _("{size=70}{=centered_narr}Глава IV — После шума{/=centered_narr}{/size}") at truecenter
        with fade
        pause 2
        hide text

        play music sad1 fadein 1.0

        scene room6 at truecenter:
            xysize (1920,1080)
        with fade
        show screen statbar
        e "Прошло два года. Сцены сменились, но Мелстрой всё реже включает камеру."
        e "Квартира больше похожа на музей успеха: бутылки, пыль, сувениры и мониторы без сигнала."
        show mell_y_3 at left:
            xysize (1400,800)
        with moveinleft
        me "Столько шума... ради чего?"
        e "Телефон молчит. Иногда он включает стрим, но уже без драйва. Зрители видят усталость."
        e "Однажды он просыпается и думает — {i}или поменять жизнь, или закончить всё.{/i}"
        e "Что он выберет?"
    # Ultima alegere – influențează subtil статистики și servește ca punte narativă
        e "Перед ним — телефон, старый микрофон и комната, где от эха когда-то кружилась голова."

    menu:
        "Ответить на внезапный звонок и выйти из дома":
            $ last_step = "call"
            play sound ring
            $ REP += 2
            $ CTRL += 1
            $ CASH -= 100
            $ clamp_stats()
            e "Он берёт трубку: на линии — тишина, короткие гудки срываются."
            scene gomel_13 at truecenter:
                xysize (1920,1080)
            with fade
            e "Он всё равно выходит. Холодный воздух бьёт в лицо, город шумит ровно и спокойно."
            e "Где-то внутри загорается тонкая искра — не из-за звонка, а потому что он, наконец, сделал шаг."

        "Отключить телефон и закрыть шторы":
            $ last_step = "shut"
            play sound "audio/click.mp3"
            $ CTRL -= 1
            $ REP -= 1
            $ clamp_stats()
            e "Экран гаснет. Шторы ложатся плотной складкой, комната уменьшается."
            scene room4 at truecenter:
                xysize (1920,1080)
            with fade
            e "На тумбочке мигнёт уведомление, но он не смотрит. В тишине слышно, как тикнет часы и как дышит дом."

        "Включить камеру и записать честное обращение к себе":
            $ last_step = "record"
            play sound "audio/yeah.mp3"
            $ CTRL += 2
            $ REP += 1
            $ clamp_stats()
            e "Красный огонёк камеры мигает. Он говорит не зрителям — себе, без монтажа и масок."
            e "Видео остаётся в черновиках. Но впервые за долгое время он слышит свой настоящий голос."
            $ renpy.movie_cutscene("videos/sud.webm")

    # Mică tranziție coerentă înainte de verdict
    if last_step == "call":
        e "Он идёт без цели: витрины, редкие прохожие, запах кофе на углу. В голове собирается план — ещё не чёткий."
    elif last_step == "shut":
        e "Он садится на пол, прислоняется к стене. Мысли тяжелеют. За дверью кто-то смеётся — и смех уходит вдалеке."
    elif last_step == "record":
        e "Он просматривает черновик ещё раз. Там — усталость и честность. Из таких вещей строят что-то новое."

    # -------------------------------
    # DECIZIE AUTOMATĂ A FINALULUI (în funcție de statistici)
    # -------------------------------
    $ _alone_score  = (CASH >= 15000)*2 + (CTRL <= 5)*2 + (REP <= 8)
    $ _love_score   = (REP >= 16)*2   + (CTRL >= 8)*2   + (CASH <= 8000)
    $ _reb_score    = (CTRL >= 10)*2  + (REP >= 12)     + (CASH >= 5000)

    if CASH >= 15000 and CTRL <= 5 and REP < 15:
        jump ch5_path_alone
    elif REP >= 16 and CTRL >= 8:
        jump ch5_path_love
    elif CTRL >= 10 or (REP >= 12 and CASH >= 5000):
        jump ch5_path_rebuild
    else:
        if _reb_score >= _love_score and _reb_score >= _alone_score:
            jump ch5_path_rebuild
        elif _love_score >= _alone_score:
            jump ch5_path_love
        else:
            jump ch5_path_alone


    label ch5_path_alone:
        play sound "audio/stop-stop.mp3"
        if last_step == "shut":
            e "Телефон молчит, шторы закрыты. Его решение стать тише оказалось слишком громким."
        elif last_step == "call":
            e "Он возвращается домой ближе к ночи. Шаг сделал — но сил не хватило сделать второй."
        else:
            e "Черновик так и остаётся в папке. Без отправки, без ответа."

        with fade
        e "Снаружи город шумит, а внутри — только эхо старых фраз и донатов."
        me "Да и похуй. Всё равно все были временные."
        play sound "audio/dovlenie.mp3"
        e "Он перестаёт выходить. Друзья исчезают, комната темнеет."
        stop music fadeout 2
        play music "audio/sad1.mp3" fadein 2
        e "Иногда он включает старый стрим, слушает себя. И улыбается, но глаза пустые."
        me "Меня больше ничего не радует. Девушки, деньги, алкоголь — пиздец. Ничего уже не имеет смысла. Всё одно и то же."
        me "Отца нет..."
        centered "{size=60}{b}ФИНАЛ I — ПУСТОТА{/b}{/size}"
        $ persistent.ENDING = "alone"
        return


    label ch5_path_love:
        play sound ring
        if last_step == "call":
            e "Тот самый номер перезванивает уже на улице. На этот раз — живой голос."
            "Голос" "Ты, кажется, забыл, как жить, Мелстрой. Выйди на свежий воздух, просто пройдись."
        elif last_step == "record":
            scene room6 at truecenter:
                xysize (1920,1080)
            e "На честный черновик приходит ответ: «Спасибо, что сказал это вслух. Выйди, подыши, посмотри вокруг»."
        else:  # shut
            show mell_y_3 at left:
                xysize (900,900)
        with moveinleft
        scene gomel_13 at truecenter:
                xysize (1920,1080)
        e "Он всё же выходит за хлебом среди ночи. Просто чтобы пройтись, успокоить мысли."
        stop sound

        play music "audio/romantic.mp3" fadein 1.5
        scene park at truecenter:
            xysize (1920,1080)
        with slow_dissolve
        show mell_y_3 at left:
            xysize (1500,800)
        with moveinleft
        e "Воздух другой. Небо будто чище, чем обычно. Он идёт, глядя в телефон, проверяя ленту, забыв про всё вокруг."
        e "И вдруг — лёгкий удар, почти неслышный."
        play sound "audio/bump.mp3"
        e "Телефон чуть не падает из рук. Перед ним — девушка, растерянная, с термосом кофе и тёплой улыбкой."

        show blonde at right:
            xysize (550,800)
        with moveinright

        "Девушка" "Ой! Прости, я не смотрела..."
        me "Нет, это я... засмотрелся в экран, как идиот."
        e "Они оба смеются. Неловкость рассеивается, как туман после дождя."

        "Девушка" "Я Аня."
        me "Я — просто парень, который слишком долго не поднимал голову от телефона."
        play sound girl_laugh
        e "Она улыбается."

        "Аня" " Такое бывает, у всех бывают трудные периоды в жизни."
        e "И так, среди утреннего шума города, начинается история, которая могла случиться только в тишине."
        e "Он идёт рядом, чувствуя, что впервые за долгое время — живой."

        play sound "audio/money.mp3"
        $ REP += 3
        $ CTRL += 3
        $ CASH -= 500
        $ clamp_stats()

    centered "{size=60}{b}ФИНАЛ II — ЛЮБОВЬ{/b}{/size}"
    $ persistent.ENDING = "love"
    return



    label ch5_path_rebuild:
        if last_step == "record":
            e "Из честного черновика рождается план. Не хайп — структура."
        elif last_step == "call":
            e "Прогулка без цели даёт ему идею. Не возвращаться в старый формат — построить новый."
        else: # shut
            e "В темноте приходит мысль: если не можешь выключить шум, измени правила."
        play music "audio/party_music.mp3" fadein 1.0
        e "Он снова включает камеры. Но теперь — не ради донатов."
        e "Проект называется {b}«MELLSTROY.GAME»{/b}."
        play sound "audio/yeah.mp3"
        C "СТАРЫЙ МЕЛСТРОЙ ВЕРНУЛСЯ, НО ДРУГОЙ!"
        hide mell_y_3
        show mell_y2 at left:
            xysize (1200,800)
        with moveinleft
        me "Если я могу менять себя — значит, можно менять систему."
        e "Под его руководством рождается новая волна. Чат гудит, но теперь — с уважением."
        play sound "audio/money.mp3"
        $ REP += 5
        $ CTRL += 4
        $ CASH += 10000
        $ clamp_stats()
        e "Он улыбается. На этот раз — честно."
        centered "{size=60}{b}ФИНАЛ III — ПЕРЕРОЖДЕНИЕ{/b}{/size}"
        $ persistent.ENDING = "rebuild"
        return









