import pygame
import time
import math
from gtts import gTTS
from io import BytesIO
from pygame_emojis import load_emoji

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)
EMOJI_SIZE = (50, 50)

# Initialize pygame and audio
pygame.mixer.pre_init(frequency=44100, buffer=4096)
pygame.init()
pygame.mixer.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Abenteuer im Dungeon")
font = pygame.font.SysFont(None, 36)
font_background = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()

# Load emojis
tree = load_emoji('🌲', EMOJI_SIZE)
temple = load_emoji('🏛️', EMOJI_SIZE)

# Game state
tts_enabled = True
info_screen_active = False

background = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "                                                                                                                                           I - Info",
    "",
    "                      Python 3.12                                               WS 2024/2025 | Yannick Simon Streule",
    ""]

actions = {
    1: {"text": "Du bist ein Abenteurer, auf der Suche nach dem sagen- umwobenen Artefakt der Macht. Nachdem du den Eingang eines Dschungeltempels entdeckt hast, stehst du vor drei Wegen.",
        "options": ["Den rechten Gang nehmen.", "Den linken Gang betreten.", "Die versteckte Treppe hinuntersteigen."],
        "targets": [2, 3, 4]},
    2: {"text": "Der rechte Gang führt zu einer Halle mit einem steinernen Wächter, der vor sich hin knurrt.",
        "options": ["Den Wächter angreifen.", "Dich verstecken.", "Einen Stein werfen, um ihn abzulenken."],
        "targets": [5, 6, 7]},
    3: {"text": "Du folgst dem linken Gang und erreichst eine Weggabelung.",
        "options": ["Dem schmalen Pfad folgen.", "Den breiten Pfad nehmen."],
        "targets": [8, 9]},
    4: {"text": "Die versteckte Treppe führt in eine Kammer, in der das Artefakt von einer riesigen Schlange bewacht wird.",
        "options": ["Die Schlange betäuben.", "Um die Schlange schleichen."],
        "targets": [10, 11]},
    5: {"text": "Nach einem langen Kampf gegen den Wächter entdeckst du einen geheimen Korridor.",
        "options": ["Dem Korridor folgen.", "Zurück zum Eingang."],
        "targets": [12, 1]},
    6: {"text": "Hinter einer versteckten Tür findest du eine Vorratskammer mit alten Schätzen.",
        "options": ["Die Schätze durchsuchen.", "Den Raum verlassen."],
        "targets": [13, 2]},
    7: {"text": "Du erreichst eine große Halle mit mehreren steinernen Statuen.",
        "options": ["Die Statuen untersuchen.", "Schnell hindurchgehen."],
        "targets": [14, 15]},
    8: {"text": "Ein schmaler Weg führt zu einem Wasserfall, der eine versteckte Tür verbirgt.",
        "options": ["Durch die Tür gehen.", "Zurück zur Weggabelung."],
        "targets": [16, 3]},
    9: {"text": "Der breite Gang führt dich in eine alte Bibliothek voller mystischer Bücher.",
        "options": ["In den Büchern lesen.", "Die Bibliothek durchqueren."],
        "targets": [17, 18]},
    10: {"text": "Die Schlange schläft ein, und du nimmst das Artefakt.",
         "options": ["Das Artefakt genauer untersuchen.", "Den Raum schnell verlassen."],
         "targets": [19, 11]},
    11: {"text": "Du hast das Artefakt der Macht erfolgreich gefunden und es sicher aus dem Tempel herausgebracht. Dein Abenteuer könnte hier enden, oder du könntest den Tempel weiter erkunden.",
         "options": ["Das Abenteuer beenden.", "Den Tempel weiter erkunden."],
         "targets": [0, 12],
         "onexit": ["Herzlichen Glückwunsch! Du hast das Artefakt sicher aus dem Tempel gebracht und das Abenteuer erfolgreich beendet!"]},
    12: {"text": "Der Korridor führt zu einer geheimen Kammer, in der eine alte Kriegerstatue steht.",
         "options": ["Die Statue untersuchen.", "Weitergehen."],
         "targets": [20, 21]},
    13: {"text": "Hinter den Schätzen verbirgt sich ein Geheimgang.",
         "options": ["Den Geheimgang betreten.", "Den Schatz nehmen."],
         "targets": [22, 23]},
    14: {"text": "Die Statuen erwachen und beginnen sich zu bewegen.",
         "options": ["Kämpfen.", "Fliehen."],
         "targets": [24, 7]},
    15: {"text": "Am anderen Ende der Halle findest du einen Brunnen mit magischem Wasser.",
         "options": ["Vom Wasser trinken.", "Den Brunnen ignorieren."],
         "targets": [25, 18]},
    16: {"text": "Hinter der verborgenen Tür findest du einen uralten Schatz.",
         "options": ["Den Schatz nehmen.", "Den Raum durchsuchen."],
         "targets": [26, 27]},
    17: {"text": "In den Büchern entdeckst du einen Hinweis auf das Versteck des Artefakts.",
         "options": ["Dem Hinweis folgen.", "Weiter in der Bibliothek suchen."],
         "targets": [28, 18]},
    18: {"text": "Am Ausgang der Bibliothek entdeckst du eine verborgene Tür.",
         "options": ["Die Tür öffnen.", "Zurück zur Weggabelung."],
         "targets": [29, 3]},
    19: {"text": "Das Artefakt beginnt zu leuchten und enthüllt geheime Inschriften.",
         "options": ["Die Inschriften lesen.", "Das Artefakt schnell verstauen und fliehen."],
         "targets": [30, 11]},
    20: {"text": "Die Statue gibt dir Hinweise auf den Ausgang des Tempels.",
         "options": ["Den Hinweisen folgen.", "Die Statue unbeachtet lassen und weitergehen."],
         "targets": [11, 21]},
    21: {"text": "Der Gang führt zu einer alten, verborgenen Grabkammer.",
         "options": ["Die Grabkammer betreten.", "Zurück zur Statue."],
         "targets": [0, 20],
         "onexit": ["Ein Fluch trifft dich, und du erstarrst. Dein Abenteuer endet hier."]},
    22: {"text": "Im Geheimgang findest du alte Zeichnungen, die den Tempelplan zeigen.",
         "options": ["Den Plan studieren.", "Den Gang weiter erkunden."],
         "targets": [18, 23]},
    23: {"text": "Die Schatzkammer enthält das Artefakt der Macht, von leuchtenden Kristallen umgeben.",
         "options": ["Das Artefakt nehmen.", "Die Kristalle untersuchen."],
         "targets": [11, 0],
         "onexit": ["", "Die Kristalle aktivieren eine Falle. Dein Abenteuer endet hier."]},
    24: {"text": "Nach dem Kampf öffnet sich ein geheimes Tor.",
         "options": ["Durch das Tor gehen.", "Zurückgehen."],
         "targets": [11, 7]},
    25: {"text": "Die magische Kraft des Wassers heilt deine Wunden und gibt dir neue Energie.",
         "options": ["Weitergehen.", "Am Brunnen ausruhen."],
         "targets": [15, 0],
         "onexit": ["", "Ein lautes Knurren ertönt. Dein Abenteuer endet hier."]},
    26: {"text": "Der Schatz enthält antike Artefakte, die magische Kräfte verbergen.",
         "options": ["Die Artefakte untersuchen.", "Den Raum verlassen."],
         "targets": [30, 16]},
    27: {"text": "Die Karte enthüllt eine versteckte Treppe, die dich weiter führt.",
         "options": ["Die Treppe hinuntergehen.", "Zurück zur Kammer."],
         "targets": [16, 3]},
    28: {"text": "Ein Raum mit seltsamen Runen erscheint vor dir.",
         "options": ["Die Runen lesen.", "Den Raum schnell verlassen."],
         "targets": [29, 11]},
    29: {"text": "Eine große Schatzkammer voller goldener Artefakte liegt vor dir.",
         "options": ["Einen Schatz mitnehmen.", "Weitergehen."],
         "targets": [11, 12]},
    30: {"text": "Der Talisman verleiht dir die Kraft, den Tempel zu verlassen.",
         "options": ["Den Talisman aktivieren.", "Den Tempel erkunden."],
         "targets": [0, 11],
         "onexit": ["Du verlässt den Tempel als Held mit unermesslichem Reichtum!"]}}


def print_start_screen():
    """Displays the start screen with a pulsating 'Press Enter' prompt and a green title.
    Returns True if Enter is pressed to continue."""
    running = True
    base_font_size = 36
    title_font_size = 54
    animation_speed = 3

    title_font = pygame.font.Font(None, title_font_size)
    title_surface = title_font.render("Abenteuer im Dungeon", True, GREEN)
    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

    while running:
        screen.fill(BLACK)

        current_time = time.time()
        scale_factor = 1 + 0.2 * math.sin(animation_speed * current_time)
        animated_font_size = int(base_font_size * scale_factor)

        font = pygame.font.Font(None, animated_font_size)
        text_surface = font.render("Drücke die Eingabetaste", True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        screen.blit(title_surface, title_rect)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_RETURN:
                    return True


def draw_info_screen():
    """Draws the info screen."""
    global tts_enabled
    info_background = pygame.Surface((SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100))
    info_background.set_alpha(200)
    info_background.fill((50, 50, 50))

    screen.blit(info_background, (50, 50))

    info_text = [
        "Abenteuer im Dungeon - Info",
        "",
        "Steuerung:",
        "",
        "- Pfeiltasten: Optionen auswählen",
        "- Eingabetaste: Auswahl bestätigen",
        "- S: Sprachausgabe an/aus",
        "- ESC: Spiel beenden",
        "- Leertaste: Schreibanimation überspringen",
        "",
        "Sprachausgabe:",
        f"Status: {'Aktiviert' if tts_enabled else 'Deaktiviert'}"
        "",
        "",
        "",
        "                                            I: Info-Bildschirm verstecken",]

    for i, line in enumerate(info_text):
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (75, 75 + i * 30))

    pygame.display.flip()


def loading_screen():
    """Displays a loading screen with a rotating symbol and gradually added dots."""
    symbols = ["|", "/", "-", "\\"]
    symbol_index = 0
    dot_count = 0
    max_dots = 3
    frame_counter = 0
    loading_duration = 30
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)

        loading_symbol = symbols[symbol_index]
        symbol_surface = font.render(loading_symbol, True, WHITE)
        screen.blit(symbol_surface, ((SCREEN_WIDTH - symbol_surface.get_width()) // 2, SCREEN_HEIGHT // 2 - 50))

        loading_text = "Lade das Abenteuer" + "." * dot_count
        text_surface = font.render(loading_text, True, WHITE)
        screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, SCREEN_HEIGHT // 2 + 10))

        pygame.display.flip()

        symbol_index = (symbol_index + 1) % len(symbols)

        if frame_counter % 10 == 0:
            dot_count = (dot_count + 1) % (max_dots + 1)

        if dot_count == max_dots and frame_counter >= loading_duration - 1:
            time.sleep(1)
            running = False

        time.sleep(0.1)
        frame_counter += 1
        clock.tick(10)


def draw_background():
    """Draws the background."""
    screen.fill(BLACK)
    for i, line in enumerate(background):
        text_surface = font_background.render(line, True, WHITE)
        screen.blit(text_surface, (10, 10 + i * 20))
    screen.blit(temple, (45, 530))
    screen.blit(tree, (25, 530))
    screen.blit(tree, (65, 530))


def draw_text(text, x, y, color=WHITE):
    """Draws text on the screen with dynamic line wrapping."""
    words = text.split()
    current_line = ''
    line_height = 30
    for word in words:
        test_line = current_line + word + ' '
        text_width = font.size(test_line)[0]
        if text_width > SCREEN_WIDTH - 2 * x:
            current_line = current_line.rsplit(' ', 1)[0]
            screen.blit(font.render(current_line + " " * 200, True, color, BLACK), (x, y))
            current_line = word + ' '
            y += line_height
        else:
            current_line = test_line
    if current_line:
        screen.blit(font.render(current_line, True, color, BLACK), (x, y))


def typing_effect(text, start_x=50, start_y=50, delay=0.065):
    """Displays the text with a typing effect, including line breaks and an option to toggle TTS."""
    draw_background()
    pygame.display.flip()

    current_text = ""
    y_offset = start_y
    global tts_enabled
    skip_animation = False

    for char in text:
        if skip_animation:
            break

        if char == '\n':
            draw_text(current_text, start_x, y_offset)
            y_offset += 30
            current_text = ""
            continue

        current_text += char
        draw_text(current_text, start_x, y_offset)
        pygame.display.flip()

        time.sleep(delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_s:
                    tts_enabled = not tts_enabled
                    if not tts_enabled:
                        pygame.mixer.music.stop()
                    else:
                        mp3_fp = BytesIO()
                        tts = gTTS(text=text, lang="de", slow=False)
                        tts.write_to_fp(mp3_fp)
                        mp3_fp.seek(0)
                        pygame.mixer.music.load(mp3_fp)
                        pygame.mixer.music.play()
                elif event.key not in (pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_s):
                    skip_animation = True

    if current_text or skip_animation:
        draw_text(text, start_x, y_offset)


def handle_choice(text, options):
    """Handles the player's input for selecting options using arrow keys or numbers."""
    choice_index = 0
    choice_made = False
    global tts_enabled, info_screen_active

    while not choice_made:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_UP:
                    choice_index = (choice_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    choice_index = (choice_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    choice_made = True
                    return choice_index
                elif event.key == pygame.K_s:
                    tts_enabled = not tts_enabled
                    if not tts_enabled:
                        pygame.mixer.music.stop()
                    else:
                        mp3_fp = BytesIO()
                        tts_text = f"{text} Was möchtest du tun? {format_options_for_speech(options)}"
                        tts = gTTS(text=tts_text, lang="de", slow=False)
                        tts.write_to_fp(mp3_fp)
                        mp3_fp.seek(0)
                        pygame.mixer.music.load(mp3_fp)
                        pygame.mixer.music.play()
                elif event.key == pygame.K_i:
                    info_screen_active = not info_screen_active

        screen.fill(BLACK)
        if info_screen_active:
            draw_info_screen()
        else:
            draw_background()
            draw_text(text, 50, 50)
            draw_text(f"Was möchtest du tun? [{' / '.join(str(i + 1) for i in range(len(options)))}]", 50, 300)
            for i, option in enumerate(options):
                color = GREEN if i == choice_index else WHITE
                draw_text(f"{i + 1}. {option}", 50, 330 + i * 30, color)
            pygame.display.flip()


def show_text(text, options=None):
    """Displays the text with line breaks and optional questions."""
    typing_effect(text)


def format_options_for_speech(options):
    """Formats the options for more natural-sounding speech output."""
    if len(options) == 2:
        return f"{options[0]} oder {options[1]}"
    elif len(options) > 2:
        return ", ".join(options[:-1]) + f" oder {options[-1]}"
    else:
        return options[0]


def countdown_before_exit(last_message):
    """Displays the countdown before the game window closes."""
    for i in range(3, 0, -1):
        screen.fill(BLACK)
        draw_background()
        draw_text(last_message, 50, 50)
        countdown_text = f"Dieses Fenster schließt sich in {i}..."
        countdown_surface = font.render(countdown_text, True, WHITE)
        screen.blit(countdown_surface, (50, SCREEN_HEIGHT - 160))
        pygame.display.flip()
        time.sleep(1)
    pygame.quit()
    quit()


def game_engine():
    current_step = 1
    global tts_enabled

    while current_step > 0:
        current_action = actions[current_step]
        options_text = format_options_for_speech(current_action["options"])

        if tts_enabled:
            mp3_fp = BytesIO()
            tts_text = f"{current_action['text']} Was möchtest du tun? {options_text}"
            tts = gTTS(text=tts_text, lang="de", slow=False)
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            pygame.mixer.music.load(mp3_fp)
            pygame.mixer.music.play()

        show_text(current_action["text"], current_action["options"])

        choice = handle_choice(current_action["text"], current_action["options"])
        current_step = current_action["targets"][choice]

        if current_step == 0 and "onexit" in current_action:
            last_message = current_action["onexit"][choice]
            if tts_enabled:
                mp3_fp = BytesIO()
                tts = gTTS(text=last_message, lang="de", slow=False)
                tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0)
                pygame.mixer.music.load(mp3_fp)
                pygame.mixer.music.play()

            show_text(last_message)
            countdown_before_exit(last_message)


def main():
    print_start_screen()
    loading_screen()
    game_engine()


main()
