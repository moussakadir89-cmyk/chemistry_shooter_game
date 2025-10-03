import pygame
import sys
import random

# --- Initialize Pygame ---
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English Learning Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_GREEN = (0, 150, 0)
PURPLE = (128, 0, 128)

# Fonts
font = pygame.font.SysFont(None, 28)
large_font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

# Player settings
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# King settings
king_pos = [WIDTH // 2 - 50, 50]
king_size = 100
king_hp = 50
max_king_hp = 50

# Score
score = 0
streak = 0

# English Learning Data with Difficulty Levels
vocabulary_sets = {
    "synonyms": {
        "beginner": [
            {"question": "What is a synonym for 'HAPPY'?", "options": ["Sad", "Joyful", "Angry", "Tired"], "correct": 1, "damage": 6, "definition": "Joyful means feeling great happiness"},
            {"question": "What is a synonym for 'BIG'?", "options": ["Small", "Tiny", "Large", "Narrow"], "correct": 2, "damage": 6, "definition": "Large means of great size"},
            {"question": "What is a synonym for 'FAST'?", "options": ["Quick", "Slow", "Heavy", "Light"], "correct": 0, "damage": 6, "definition": "Quick means moving at high speed"},
            {"question": "What is a synonym for 'SMART'?", "options": ["Dumb", "Clever", "Lazy", "Mean"], "correct": 1, "damage": 6, "definition": "Clever means having intelligence"},
        ],
        "intermediate": [
            {"question": "What is a synonym for 'BEAUTIFUL'?", "options": ["Ugly", "Plain", "Gorgeous", "Simple"], "correct": 2, "damage": 8, "definition": "Gorgeous means extremely beautiful"},
            {"question": "What is a synonym for 'ANGRY'?", "options": ["Happy", "Furious", "Calm", "Sleepy"], "correct": 1, "damage": 8, "definition": "Furious means extremely angry"},
            {"question": "What is a synonym for 'TIRED'?", "options": ["Energetic", "Exhausted", "Alert", "Active"], "correct": 1, "damage": 8, "definition": "Exhausted means extremely tired"},
        ],
        "advanced": [
            {"question": "What is a synonym for 'ELOQUENT'?", "options": ["Articulate", "Clumsy", "Silent", "Confused"], "correct": 0, "damage": 12, "definition": "Articulate means expressing oneself clearly"},
            {"question": "What is a synonym for 'METICULOUS'?", "options": ["Careless", "Precise", "Random", "Hasty"], "correct": 1, "damage": 12, "definition": "Precise means exact and accurate"},
        ]
    },
    "antonyms": {
        "beginner": [
            {"question": "What is the OPPOSITE of 'HOT'?", "options": ["Warm", "Cold", "Cool", "Mild"], "correct": 1, "damage": 7, "definition": "Cold is the complete opposite of hot"},
            {"question": "What is the OPPOSITE of 'UP'?", "options": ["Down", "High", "Over", "Above"], "correct": 0, "damage": 7, "definition": "Down is the opposite direction of up"},
            {"question": "What is the OPPOSITE of 'LOVE'?", "options": ["Like", "Hate", "Care", "Want"], "correct": 1, "damage": 7, "definition": "Hate is the strongest opposite of love"},
        ],
        "intermediate": [
            {"question": "What is the OPPOSITE of 'LIGHT' (weight)?", "options": ["Bright", "Heavy", "White", "Clear"], "correct": 1, "damage": 10, "definition": "Heavy is the opposite of light in weight"},
            {"question": "What is the OPPOSITE of 'FIRST'?", "options": ["Second", "Last", "Middle", "Next"], "correct": 1, "damage": 10, "definition": "Last is the final position, opposite of first"},
        ],
        "advanced": [
            {"question": "What is the OPPOSITE of 'BENEVOLENT'?", "options": ["Malevolent", "Kind", "Generous", "Helpful"], "correct": 0, "damage": 15, "definition": "Malevolent means having evil intentions"},
            {"question": "What is the OPPOSITE of 'ABUNDANT'?", "options": ["Plentiful", "Scarce", "Multiple", "Various"], "correct": 1, "damage": 15, "definition": "Scarce means existing in small quantities"},
        ]
    },
    "spelling": {
        "beginner": [
            {"question": "Which word is spelled CORRECTLY?", "options": ["Frend", "Friend", "Freind", "Frien"], "correct": 1, "damage": 8, "definition": "Friend: a person you like and trust"},
            {"question": "Which word is spelled CORRECTLY?", "options": ["Scool", "School", "Shool", "Skool"], "correct": 1, "damage": 8, "definition": "School: a place of learning"},
        ],
        "intermediate": [
            {"question": "Which word is spelled CORRECTLY?", "options": ["Recieve", "Receive", "Receve", "Receeve"], "correct": 1, "damage": 12, "definition": "Receive: to get or accept something"},
            {"question": "Which word is spelled CORRECTLY?", "options": ["Seperate", "Separate", "Seprate", "Separete"], "correct": 1, "damage": 12, "definition": "Separate: to divide or keep apart"},
        ],
        "advanced": [
            {"question": "Which word is spelled CORRECTLY?", "options": ["Definately", "Definatly", "Definitely", "Definetly"], "correct": 2, "damage": 15, "definition": "Definitely: without doubt or certainly"},
            {"question": "Which word is spelled CORRECTLY?", "options": ["Occured", "Occurred", "Occurd", "Ocurred"], "correct": 1, "damage": 15, "definition": "Occurred: happened or took place"},
        ]
    },
    "grammar": {
        "beginner": [
            {"question": "Choose the correct verb: 'She ___ to school every day.'", "options": ["go", "goes", "going", "gone"], "correct": 1, "damage": 9, "definition": "Goes is correct for third person singular present tense"},
            {"question": "Choose the correct article: '___ apple a day keeps the doctor away.'", "options": ["A", "An", "The", "Some"], "correct": 1, "damage": 9, "definition": "An is used before words starting with vowel sounds"},
        ],
        "intermediate": [
            {"question": "Choose the correct tense: 'I ___ this book yesterday.'", "options": ["read", "reads", "reading", "will read"], "correct": 0, "damage": 12, "definition": "Read (past tense) is correct for actions completed yesterday"},
            {"question": "Choose the correct pronoun: 'The gift is for you and ___.'", "options": ["I", "me", "my", "mine"], "correct": 1, "damage": 12, "definition": "Me is the correct object pronoun"},
        ],
        "advanced": [
            {"question": "Choose the correct form: 'If I ___ rich, I would travel the world.'", "options": ["am", "was", "were", "will be"], "correct": 2, "damage": 18, "definition": "Were is used in hypothetical conditional statements"},
            {"question": "Choose the correct word: 'The effect of the medicine ___ immediate.'", "options": ["was", "were", "are", "been"], "correct": 0, "damage": 18, "definition": "Was agrees with the singular subject 'effect'"},
        ]
    },
    "definitions": {
        "beginner": [
            {"question": "What does 'BRAVE' mean?", "options": ["Scared", "Courageous", "Weak", "Tired"], "correct": 1, "damage": 7, "definition": "Courageous means showing courage in the face of danger"},
            {"question": "What does 'ANCIENT' mean?", "options": ["New", "Modern", "Very old", "Recent"], "correct": 2, "damage": 7, "definition": "Ancient means belonging to the very distant past"},
        ],
        "intermediate": [
            {"question": "What does 'PERSEVERE' mean?", "options": ["Give up", "Continue trying", "Start over", "Avoid"], "correct": 1, "damage": 11, "definition": "Persevere means to continue despite difficulties"},
            {"question": "What does 'SKEPTICAL' mean?", "options": ["Trusting", "Doubtful", "Certain", "Happy"], "correct": 1, "damage": 11, "definition": "Skeptical means having doubts about something"},
        ],
        "advanced": [
            {"question": "What does 'UBIQUITOUS' mean?", "options": ["Rare", "Present everywhere", "Ancient", "Expensive"], "correct": 1, "damage": 16, "definition": "Ubiquitous means existing or being everywhere"},
            {"question": "What does 'EPHEMERAL' mean?", "options": ["Permanent", "Brief", "Large", "Expensive"], "correct": 1, "damage": 16, "definition": "Ephemeral means lasting for a very short time"},
        ]
    },
    "sentence_completion": {
        "beginner": [
            {"question": "Complete: 'The cat is ___ the table.'", "options": ["in", "on", "at", "by"], "correct": 1, "damage": 8, "definition": "On is used for surfaces like tables"},
            {"question": "Complete: 'I am ___ homework.'", "options": ["make", "making", "do", "doing"], "correct": 3, "damage": 8, "definition": "Doing homework is the correct phrase"},
        ],
        "intermediate": [
            {"question": "Complete: 'The movie was so boring that I fell ___.'", "options": ["sleep", "asleep", "sleeping", "slept"], "correct": 1, "damage": 13, "definition": "Fell asleep is the correct phrasal verb"},
            {"question": "Complete: 'She has been working here ___ five years.'", "options": ["since", "for", "during", "from"], "correct": 1, "damage": 13, "definition": "For is used with periods of time"},
        ],
        "advanced": [
            {"question": "Complete: 'Had I known about the traffic, I ___ earlier.'", "options": ["left", "would leave", "would have left", "will leave"], "correct": 2, "damage": 17, "definition": "Would have left is correct for past unreal conditionals"},
        ]
    },
    "rhyming": {
        "beginner": [
            {"question": "Which word RHYMES with 'CAT'?", "options": ["Dog", "Hat", "Car", "Run"], "correct": 1, "damage": 6, "definition": "Hat rhymes with cat (both end in -at)"},
            {"question": "Which word RHYMES with 'TREE'?", "options": ["Free", "Tall", "Green", "Wood"], "correct": 0, "damage": 6, "definition": "Free rhymes with tree (both end in -ee)"},
        ],
        "intermediate": [
            {"question": "Which word RHYMES with 'ORANGE'?", "options": ["Purple", "Door-hinge", "Yellow", "Apple"], "correct": 1, "damage": 14, "definition": "Door-hinge is one of the few words that rhymes with orange"},
            {"question": "Which word RHYMES with 'LAUGHTER'?", "options": ["Happy", "After", "Loud", "Funny"], "correct": 1, "damage": 14, "definition": "After rhymes with laughter"},
        ]
    },
    "plurals": {
        "beginner": [
            {"question": "What is the plural of 'CHILD'?", "options": ["Childs", "Children", "Childes", "Child"], "correct": 1, "damage": 9, "definition": "Children is the irregular plural of child"},
            {"question": "What is the plural of 'MOUSE'?", "options": ["Mouses", "Mice", "Mouse", "Mousies"], "correct": 1, "damage": 9, "definition": "Mice is the irregular plural of mouse"},
        ],
        "intermediate": [
            {"question": "What is the plural of 'GOOSE'?", "options": ["Gooses", "Geese", "Goose", "Geeses"], "correct": 1, "damage": 13, "definition": "Geese is the irregular plural of goose"},
            {"question": "What is the plural of 'FOOT'?", "options": ["Foots", "Feets", "Feet", "Foot"], "correct": 2, "damage": 13, "definition": "Feet is the irregular plural of foot"},
        ]
    }
}

# Current game state
current_question = None
game_mode = "synonyms"  # Can be "synonyms", "antonyms", "spelling", "grammar", "definitions", "sentence_completion", "rhyming", "plurals"
difficulty_level = "beginner"  # "beginner", "intermediate", "advanced"
bullets = []
feedback_message = ""
feedback_timer = 0
definition_message = ""
definition_timer = 0

# Power-up system
player_health = 100
max_player_health = 100
power_up_active = False
power_up_timer = 0
power_up_type = ""
double_damage_streak = 5
current_power_streak = 0

# Progress tracking
category_scores = {mode: 0 for mode in ["synonyms", "antonyms", "spelling", "grammar", "definitions", "sentence_completion", "rhyming", "plurals"]}
total_questions_answered = 0
correct_answers = 0

# Clock
clock = pygame.time.Clock()

# --- Functions ---
def get_random_question():
    if game_mode in vocabulary_sets and difficulty_level in vocabulary_sets[game_mode]:
        questions = vocabulary_sets[game_mode][difficulty_level]
        return random.choice(questions)
    else:
        # Fallback to beginner level if advanced questions don't exist
        fallback_level = "beginner" if "beginner" in vocabulary_sets[game_mode] else list(vocabulary_sets[game_mode].keys())[0]
        questions = vocabulary_sets[game_mode][fallback_level]
        return random.choice(questions)

def draw_player():
    player_color = BLUE
    if power_up_active:
        if power_up_type == "double_damage":
            player_color = YELLOW
        elif power_up_type == "rapid_fire":
            player_color = GREEN
    
    pygame.draw.rect(screen, player_color, (*player_pos, player_size, player_size))
    
    # Draw player health bar
    health_bar_width = 150
    health_bar_height = 15
    health_bar_x = player_pos[0] - 50
    health_bar_y = player_pos[1] + player_size + 10
    
    # Background
    pygame.draw.rect(screen, WHITE, (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
    
    # Health fill
    health_fill_width = (player_health / max_player_health) * health_bar_width
    health_color = GREEN if player_health > max_player_health * 0.5 else RED
    pygame.draw.rect(screen, health_color, (health_bar_x, health_bar_y, health_fill_width, health_bar_height))

def draw_king():
    # Draw king
    pygame.draw.rect(screen, RED, (*king_pos, king_size, king_size))
    
    # Draw HP bar
    hp_bar_width = 200
    hp_bar_height = 20
    hp_bar_x = king_pos[0] - 50
    hp_bar_y = king_pos[1] - 40
    
    # Background of HP bar
    pygame.draw.rect(screen, WHITE, (hp_bar_x, hp_bar_y, hp_bar_width, hp_bar_height))
    
    # HP fill
    hp_fill_width = (king_hp / max_king_hp) * hp_bar_width
    color = GREEN if king_hp > max_king_hp * 0.3 else RED
    pygame.draw.rect(screen, color, (hp_bar_x, hp_bar_y, hp_fill_width, hp_bar_height))
    
    # HP text
    hp_text = font.render(f"Boss HP: {king_hp}/{max_king_hp}", True, WHITE)
    screen.blit(hp_text, (hp_bar_x, hp_bar_y - 25))

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, bullet["rect"])

def fire_bullet(damage):
    bullet_rect = pygame.Rect(player_pos[0] + player_size//2 - 5, player_pos[1], 10, 20)
    bullets.append({"rect": bullet_rect, "damage": damage})

def display_question_and_options():
    if current_question is None:
        return
    
    # Display question
    question_text = large_font.render(current_question["question"], True, WHITE)
    question_rect = question_text.get_rect(center=(WIDTH//2, HEIGHT - 180))
    screen.blit(question_text, question_rect)
    
    # Display options
    for idx, option in enumerate(current_question["options"]):
        option_text = font.render(f"{idx+1}: {option}", True, WHITE)
        x_pos = 50 + idx * 200
        y_pos = HEIGHT - 140
        
        # Highlight correct answer after selection
        if feedback_timer > 0 and idx == current_question["correct"]:
            pygame.draw.rect(screen, DARK_GREEN, (x_pos-10, y_pos-5, 180, 35))
        
        screen.blit(option_text, (x_pos, y_pos))

def display_game_info():
    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))
    
    # Streak
    streak_color = YELLOW if streak >= double_damage_streak else WHITE
    streak_text = font.render(f"Streak: {streak}", True, streak_color)
    screen.blit(streak_text, (20, 50))
    
    # Game mode and difficulty
    mode_text = font.render(f"Mode: {game_mode.capitalize()}", True, WHITE)
    screen.blit(mode_text, (20, 80))
    
    difficulty_text = font.render(f"Level: {difficulty_level.capitalize()}", True, WHITE)
    screen.blit(difficulty_text, (20, 110))
    
    # Accuracy
    accuracy = (correct_answers / total_questions_answered * 100) if total_questions_answered > 0 else 0
    accuracy_text = font.render(f"Accuracy: {accuracy:.1f}%", True, WHITE)
    screen.blit(accuracy_text, (20, 140))
    
    # Power-up status
    if power_up_active:
        power_text = font.render(f"POWER-UP: {power_up_type.replace('_', ' ').upper()}", True, YELLOW)
        screen.blit(power_text, (20, 170))
    
    # Instructions
    instruction_text = small_font.render("1-4: Answer | M: Mode | D: Difficulty | R: Reset | H: Heal", True, WHITE)
    screen.blit(instruction_text, (20, HEIGHT - 30))

def display_feedback():
    if feedback_timer > 0 and feedback_message:
        feedback_color = GREEN if "Correct" in feedback_message else RED
        feedback_surface = font.render(feedback_message, True, feedback_color)
        feedback_rect = feedback_surface.get_rect(center=(WIDTH//2, HEIGHT - 100))
        screen.blit(feedback_surface, feedback_rect)
    
    # Display word definition
    if definition_timer > 0 and definition_message:
        definition_surface = small_font.render(definition_message, True, LIGHT_BLUE)
        definition_rect = definition_surface.get_rect(center=(WIDTH//2, HEIGHT - 70))
        screen.blit(definition_surface, definition_rect)

def change_game_mode():
    global game_mode, current_question
    modes = list(vocabulary_sets.keys())
    current_index = modes.index(game_mode)
    game_mode = modes[(current_index + 1) % len(modes)]
    current_question = get_random_question()

def change_difficulty():
    global difficulty_level, current_question
    difficulties = ["beginner", "intermediate", "advanced"]
    current_index = difficulties.index(difficulty_level)
    difficulty_level = difficulties[(current_index + 1) % len(difficulties)]
    current_question = get_random_question()

def activate_power_up(power_type):
    global power_up_active, power_up_timer, power_up_type
    power_up_active = True
    power_up_timer = 300  # 5 seconds at 60 FPS
    power_up_type = power_type

def heal_player():
    global player_health
    if streak >= 3:  # Requires 3+ streak to heal
        player_health = min(max_player_health, player_health + 20)
        return True
    return False

def reset_game():
    global king_hp, score, streak, current_question, bullets, feedback_message, feedback_timer
    global player_health, power_up_active, power_up_timer, power_up_type, current_power_streak
    global category_scores, total_questions_answered, correct_answers, definition_message, definition_timer
    global difficulty_level
    
    king_hp = max_king_hp
    score = 0
    streak = 0
    current_question = get_random_question()
    bullets = []
    feedback_message = ""
    feedback_timer = 0
    player_health = max_player_health
    power_up_active = False
    power_up_timer = 0
    power_up_type = ""
    current_power_streak = 0
    category_scores = {mode: 0 for mode in category_scores.keys()}
    total_questions_answered = 0
    correct_answers = 0
    definition_message = ""
    definition_timer = 0
    difficulty_level = "beginner"

# Initialize first question
current_question = get_random_question()

def main():
    """Main function to start the game."""
    global running, current_question
    
    # Initialize first question
    current_question = get_random_question()
    
    # --- Game Loop ---
    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # Answer questions
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    selected_option = event.key - pygame.K_1
                    total_questions_answered += 1
                    
                    if selected_option == current_question["correct"]:
                        # Correct answer
                        correct_answers += 1
                        damage = current_question["damage"]
                        
                        # Apply power-ups
                        if power_up_active and power_up_type == "double_damage":
                            damage *= 2
                        
                        # Streak bonus damage
                        if streak >= double_damage_streak:
                            damage = int(damage * 1.5)
                            if not power_up_active:
                                activate_power_up("double_damage")
                        
                        fire_bullet(damage)
                        score += damage
                        streak += 1
                        current_power_streak += 1
                        category_scores[game_mode] += damage
                        
                        feedback_message = f"Correct! +{damage} damage!"
                        
                        # Show definition
                        if "definition" in current_question:
                            definition_message = current_question["definition"]
                            definition_timer = 180  # 3 seconds
                        
                        # Auto-increase difficulty based on performance
                        if streak > 0 and streak % 7 == 0:
                            if difficulty_level == "beginner":
                                difficulty_level = "intermediate"
                                feedback_message += " Level up to Intermediate!"
                            elif difficulty_level == "intermediate" and streak % 14 == 0:
                                difficulty_level = "advanced"
                                feedback_message += " Level up to Advanced!"
                                
                    else:
                        # Wrong answer
                        streak = 0
                        current_power_streak = 0
                        player_health -= 10  # Take damage for wrong answers
                        feedback_message = f"Wrong! Correct answer: {current_question['options'][current_question['correct']]}"
                        
                        # Show definition for wrong answers too
                        if "definition" in current_question:
                            definition_message = current_question["definition"]
                            definition_timer = 240  # 4 seconds for wrong answers
                    
                    feedback_timer = 120  # Show feedback for 2 seconds at 60 FPS
                    
                # Change game mode
                elif event.key == pygame.K_m:
                    change_game_mode()
                    feedback_message = f"Mode changed to: {game_mode.capitalize()}"
                    feedback_timer = 60
                    
                # Change difficulty
                elif event.key == pygame.K_d:
                    change_difficulty()
                    feedback_message = f"Difficulty changed to: {difficulty_level.capitalize()}"
                    feedback_timer = 60
                    
                # Heal player
                elif event.key == pygame.K_h:
                    if heal_player():
                        feedback_message = "Healed! (-3 streak required)"
                        feedback_timer = 60
                    else:
                        feedback_message = "Need 3+ streak to heal!"
                        feedback_timer = 60
                    
                # Reset game
                elif event.key == pygame.K_r:
                    reset_game()
                    feedback_message = "Game Reset!"
                    feedback_timer = 60
        
        # Update feedback timer
        if feedback_timer > 0:
            feedback_timer -= 1
            if feedback_timer == 0:
                # Get new question when feedback ends
                current_question = get_random_question()
        
        # Update definition timer
        if definition_timer > 0:
            definition_timer -= 1
        
        # Update power-up timer
        if power_up_timer > 0:
            power_up_timer -= 1
            if power_up_timer == 0:
                power_up_active = False
                power_up_type = ""
        
        # Move bullets
        for bullet in bullets[:]:
            bullet["rect"].y -= 8
            
            # Remove bullets that go off screen
            if bullet["rect"].y < 0:
                bullets.remove(bullet)
                continue
                
            # Collision with king
            king_rect = pygame.Rect(*king_pos, king_size, king_size)
            if bullet["rect"].colliderect(king_rect):
                king_hp -= bullet["damage"]
                bullets.remove(bullet)
                
                if king_hp <= 0:
                    king_hp = 0
                    feedback_message = "🎉 Victory! Boss defeated! Press R to play again."
                    feedback_timer = 300  # Show victory message longer
        
        # Draw everything
        draw_player()
        draw_king()
        draw_bullets()
        display_question_and_options()
        display_game_info()
        display_feedback()
        
        # Check win condition
        if king_hp <= 0:
            win_text = large_font.render("🎉 VICTORY! 🎉", True, YELLOW)
            win_rect = win_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(win_text, win_rect)
            
            # Show final stats
            stats_text = font.render(f"Final Score: {score} | Accuracy: {(correct_answers/total_questions_answered*100):.1f}%", True, WHITE)
            stats_rect = stats_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))
            screen.blit(stats_text, stats_rect)
        
        # Check game over condition
        elif player_health <= 0:
            game_over_text = large_font.render("GAME OVER", True, RED)
            game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(game_over_text, game_over_rect)
            
            restart_text = font.render("Press R to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))
            screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()