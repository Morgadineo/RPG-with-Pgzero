import pygame
from pgzero.actor import Actor
from core.utils import tint_actor_red, reset_actor_tint


class CombatScene:
    """Manages turn-based combat between player and enemy actors.
    
    This class handles the combat logic, animations, and state transitions for a 
    turn-based battle system. It supports player attacks (via spacebar) and 
    automatic enemy attacks, with visual feedback for damage.
    
    States:
        - IDLE: Waiting for player input or enemy turn decision
        - ANIMATING: Playing damage/hurt animation
        - RESOLVING: Processing queued actions
    
    Attributes:
        STATE_IDLE (str): State when waiting for input or turn transition.
        STATE_ANIMATING (str): State during damage animation.
        STATE_RESOLVING (str): State when resolving queued actions.
        ACTION_PLAYER_ATTACK (str): Identifier for player attack action.
        ACTION_ENEMY_ATTACK (str): Identifier for enemy attack action.
        
        player (Actor): The player character actor.
        enemy (Actor): The enemy character actor.
        enemy_base_surf (Surface): Original enemy surface for tint reset.
        width (int): Screen width.
        height (int): Screen height.
        turn (str): Current turn ('player' or 'enemy').
        finished (bool): Whether combat has concluded.
        winner (str): Winner of combat ('player' or 'enemy').
        state (str): Current state machine state.
        anim_timer (float): Timer for animations and delays.
        ANIM_HURT_TIME (float): Duration of hurt animation in seconds.
        TURN_DELAY (float): Delay between turns in seconds.
        action_queue (list[str]): Queue of actions to be resolved.
    """
    
    # Estados internos
    STATE_IDLE = "idle"
    STATE_ANIMATING = "animating"
    STATE_RESOLVING = "resolving"

    # Ações possíveis
    ACTION_PLAYER_ATTACK = "player_attack"
    ACTION_ENEMY_ATTACK = "enemy_attack"

    def __init__(self, player, enemy, screen_size):
        """Initializes the combat scene with player and enemy.
        
        Args:
            player (Actor): Player character with health and attack attributes.
            enemy (Actor): Enemy character with health attribute.
            screen_size (tuple): (width, height) of the game screen.
        """
        self.player = player
        self.enemy = enemy
        self.enemy_base_surf = enemy._surf

        self.width, self.height = screen_size

        self.turn = "player"
        self.finished = False
        self.winner = None

        self.state = self.STATE_IDLE
        self.anim_timer = 0.0
        self.ANIM_HURT_TIME = 0.4
        self.TURN_DELAY = 0.2

        self.action_queue: list[str] = []

    # ------------------------------------------------------------------
    # DRAW
    # ------------------------------------------------------------------

    def draw(self, screen):
        """Draws all combat scene elements to the screen.
        
        Renders player and enemy actors, health displays, and turn indicator.
        
        Args:
            screen (pygame.Surface): The screen surface to draw onto.
        """
        self.player.draw()
        self.enemy.draw()

        screen.draw.text(
            f"Player HP: {self.player.health}",
            topleft=(20, 20),
            fontsize=32
        )

        screen.draw.text(
            f"Enemy HP: {self.enemy.health}",
            topright=(self.width - 20, 20),
            fontsize=32
        )

        screen.draw.text(
            f"Turn: {self.turn.upper()}",
            center=(self.width // 2, 20),
            fontsize=32
        )

    # ------------------------------------------------------------------
    # INPUT
    # ------------------------------------------------------------------

    def on_key_down(self, keyboard):
        """Handles keyboard input for player actions.
        
        Only processes input during player turn when in idle state and combat
        is not finished. Spacebar triggers player attack.
        
        States:
            - Only processes input in IDLE state
            - Ignores input if combat is FINISHED
            - Only accepts input during player turn
        
        Args:
            keyboard: Pygame Zero keyboard input object.
        """
        if self.finished or self.state != self.STATE_IDLE:
            return

        if self.turn == "player" and keyboard.space:
            self._enqueue_player_attack()

    # ------------------------------------------------------------------
    # ACTION QUEUE
    # ------------------------------------------------------------------

    def _enqueue_player_attack(self):
        """Queues a player attack action.
        
        States:
            - Changes state from IDLE to RESOLVING
        
        Side Effects:
            - Adds ACTION_PLAYER_ATTACK to action_queue
            - Sets state to STATE_RESOLVING
        """
        self.action_queue.append(self.ACTION_PLAYER_ATTACK)
        self.state = self.STATE_RESOLVING

    def _enqueue_enemy_attack(self):
        """Queues an enemy attack action.
        
        Called automatically during enemy turn. Changes state to RESOLVING.
        
        States:
            - Changes state from IDLE to RESOLVING
        
        Side Effects:
            - Adds ACTION_ENEMY_ATTACK to action_queue
            - Sets state to STATE_RESOLVING
        """
        self.action_queue.append(self.ACTION_ENEMY_ATTACK)
        self.state = self.STATE_RESOLVING

    # ------------------------------------------------------------------
    # ACTION RESOLUTION
    # ------------------------------------------------------------------

    def _resolve_next_action(self):
        """Processes the next action in the queue.
        
        Pops and executes the next action. Returns to IDLE state if queue is empty.
        Actions trigger corresponding hurt animations.
        
        States:
            - RESOLVING -> IDLE (if queue empty)
            - RESOLVING -> ANIMATING (if action processed)
        
        Side Effects:
            - Calls _start_enemy_hurt() or _start_player_hurt()
            - May change state to ANIMATING
            - May change state to IDLE
        """
        if not self.action_queue:
            self.state = self.STATE_IDLE
            return

        action = self.action_queue.pop(0)

        if action == self.ACTION_PLAYER_ATTACK:
            self._start_enemy_hurt()

        elif action == self.ACTION_ENEMY_ATTACK:
            self._start_player_hurt()

    # ------------------------------------------------------------------
    # ANIMATION STARTERS
    # ------------------------------------------------------------------

    def _start_enemy_hurt(self):
        """Executes player attack against enemy.
        
        Reduces enemy health by player's attack value, applies visual tint,
        and starts hurt animation. Ends combat if enemy health reaches zero.
        
        States:
            - RESOLVING -> ANIMATING
        
        Side Effects:
            - Reduces enemy.health
            - Applies red tint to enemy
            - Sets anim_timer to ANIM_HURT_TIME
            - May set finished=True and winner="player"
        """
        self.enemy.health -= self.player.attack
        tint_actor_red(self.enemy)

        self.anim_timer = self.ANIM_HURT_TIME
        self.state = self.STATE_ANIMATING

        if self.enemy.health <= 0:
            self.finished = True
            self.winner = "player"

    def _start_player_hurt(self):
        """Executes enemy attack against player.
        
        Calls player's get_hit method, changes to hurt sprite, and starts
        animation. Ends combat if player health reaches zero.
        
        States:
            - RESOLVING -> ANIMATING
        
        Side Effects:
            - Calls player.get_hit(enemy)
            - Changes player sprite to hurt image
            - Sets anim_timer to ANIM_HURT_TIME
            - May set finished=True and winner="enemy"
        """
        self.player.get_hit(self.enemy)

        self.player.__hurt_image__()

        self.anim_timer = self.ANIM_HURT_TIME
        self.state = self.STATE_ANIMATING

        if self.player.health <= 0:
            self.finished = True
            self.winner = "enemy"

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------

    def update(self, dt):
        """Updates combat logic, animations, and state transitions.
        
        Manages the state machine and coordinates all combat flow.
        
        States:
            - FINISHED: No updates if combat finished
            - RESOLVING: Calls _resolve_next_action()
            - ANIMATING: Updates timer, calls _end_animation() when expired
            - IDLE (enemy turn): Queues enemy attack
        
        Args:
            dt (float): Delta time in seconds since last update.
        """
        if self.finished:
            return

        if self.state == self.STATE_RESOLVING:
            self._resolve_next_action()
            return

        if self.state == self.STATE_ANIMATING:
            self.anim_timer -= dt

            if self.anim_timer <= 0:
                self._end_animation()
            return

        if self.state == self.STATE_IDLE and self.turn == "enemy":
            self._enqueue_enemy_attack()

    # ------------------------------------------------------------------
    # ANIMATION END
    # ------------------------------------------------------------------

    def _end_animation(self):
        """Completes animation cycle and transitions to next turn.
        
        Resets actor visuals to normal, applies turn delay, and swaps turns.
        
        States:
            - ANIMATING -> IDLE (with turn delay)
        
        Side Effects:
            - Resets enemy tint to original
            - Changes player sprite to stand image
            - Sets anim_timer to TURN_DELAY
            - Swaps turn between 'player' and 'enemy'
        """
        self.enemy._surf = self.enemy_base_surf
        self.player.__stand_image__()

        self.state = self.STATE_IDLE
        self.anim_timer = self.TURN_DELAY

        self.turn = "enemy" if self.turn == "player" else "player"
