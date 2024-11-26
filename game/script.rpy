# The script of the game goes in this file.
init python:
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Erin")
define m = Character(("Miq"), color="#ffc400", image="miq")
define n = Character("Nemmi", color="#a80000", image="nemmi", cb_name="nemni", callback=speaker("nemmi"))


layeredimage miq:
    zoom 0.35


    group body:
        attribute body default:
            "sprites/miq/b_miq.webp"
    group face:
        attribute face default:
            "sprites/miq/face.webp"

    group shirts:
        attribute WhiteDress:
            "sprites/miq/WhiteDress.webp"
        attribute YellowCasual:
            "sprites/miq/YellowCasual.webp"


    group pants:
        attribute BlackSlacks:
            "sprites/miq/BlackSlacks.webp"
    group undie:
        attribute undie:
            "sprites/miq/Red.webp"

    group e_expressions:
        attribute normal default:
            "sprites/miq/e_normal.webp"
        attribute angry:
            "sprites/miq/e_angry.webp"
        attribute sad:
            "sprites/miq/e_sad.webp"
        attribute happy:
            "sprites/miq/e_happy.webp"
        attribute surprised:
            "sprites/miq/e_surprise.webp"
        attribute thinking:
            "sprites/miq/e_thinking.webp"

    group m_expressions:
        attribute Open:
            "sprites/miq/Open.webp"
        attribute Closed:
            "sprites/miq/Closed.webp"

image nemmi_speaking:
    "sprites/nemmi/8 muzzle/Normal.png"
    0.1
    "sprites/nemmi/8 muzzle/Talk.png"
    repeat

image nemmi_idle:
    "sprites/nemmi/8 muzzle/Normal.png"

layeredimage nemmi:
    zoom 0.35
    group mouth:
        attribute normal default:
            WhileSpeaking("nemmi", "nemmi_speaking", "nemmi_idle")

    group body:
        attribute backhair default:
            "sprites/nemmi/backhair.png"
        attribute body default:
            "sprites/nemmi/nemmibody.png"
        attribute fronthair default:
            "sprites/nemmi/frontHair.png"


    group shirts:
        attribute BlackHoodie:
            "sprites/nemmi/BlackHoodie.webp"
        attribute Tanktop:
            "sprites/nemmi/Tanktop.webp"


    group pants:
        attribute short:
            "sprites/nemmi/GreenShorts.webp"
    group undie:
        attribute undie:
            "sprites/nemmi/WhiteBrief.webp"

    group e_expressions:
        attribute eye_normal default:
            "sprites/nemmi/9 eyes/eyeNormal.png"
        attribute angry:
            "sprites/nemmi/9 eyes/Angry.png"
        attribute sad:
            "sprites/nemmi/9 eyes/eyeSad.png"
        attribute happy:
            "sprites/nemmi/9 eyes/Happy.webp"
        attribute surprised:
            "sprites/nemmi/9 eyes/eyeSurprise.png"
        attribute confused:
            "sprites/nemmi/9 Eyes/eyeConfused.png"

    group m_expressions:
        attribute normal:
            "sprites/nemmi/8 muzzle/Normal.png"
        attribute angry:
            "sprites/nemmi/8 muzzle/Angry.png"
        attribute sad:
            "sprites/nemmi/8 muzzle/Sad.png"
        attribute happy:
            "sprites/nemmi/8 muzzle/Happy.png"
        attribute talk:
            "sprites/nemmi/8 muzzle/Talk.png"
        attribute pout:
            "sprites/nemmi/8 muzzle/Pout.png"
        attribute scared:
            "sprites/nemmi/8 muzzle/Scared.png"
        attribute surprised:
            "sprites/nemmi/8 muzzle/Surprise.png"
        attribute grit:
            "sprites/nemmi/8 muzzle/Grit.png"
image Crayon_village = "bg/Crayon Village Slope.png" 
image library = "bg/library.jpg" 
image living_room = "bg/Living Room.png" 
image moutain = "bg/Mountain Day.png" 
"bg/NovemBEAR Splash Screen.png" 
image landscape = "bg/Abstract landscape.png" 
image bedroom = "bg/Bedroom.png"
image dream = "bg/mountain_dream.png"
