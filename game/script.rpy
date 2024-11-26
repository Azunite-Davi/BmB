# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Erin")
define m = Character(("Miq"), color="#ffc400", image="miq")
define n = Character(("Nemmi"), color="#a80000", image="nemmi")

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

layeredimage nemmi:
    zoom 0.35
    group body:
        attribute body default:
            "sprites/nemmi/nemmibody.png"

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
            "sprites/nemmi/9 eyes/Normal.webp"
        attribute angry:
            "sprites/nemmi/9 eyes/Angry.webp"
        attribute sad:
            "sprites/nemmi/9 eyes/Sad.webp"
        attribute happy:
            "sprites/nemmi/9 eyes/Happy.webp"
        attribute surprised:
            "sprites/nemmi/9 eyes/Surprise.webp"

    group m_expressions:
        attribute normal:
            "sprites/nemmi/8 muzzle/Neutral.webp"
        attribute angry:
            "sprites/nemmi/8 muzzle/Angry.webp"
        attribute sad:
            "sprites/nemmi/8 muzzle/Sad.webp"
        attribute happy:
            "sprites/nemmi/8 muzzle/Happy.webp"
        attribute talk:
            "sprites/nemmi/8 muzzle/Talk.webp"
        attribute scared:
            "sprites/nemmi/8 muzzle/Scared.webp"
        attribute surprised:
            "sprites/nemmi/8 muzzle/Surprise.webp"
image Crayon_village = "bg/Crayon Village Slope.png" 
image library = "bg/library.jpg" 
image living_room = "bg/Living Room.png" 
image moutain = "bg/Mountain Day.png" 
"bg/NovemBEAR Splash Screen.png" 
image landscape = "bg/Abstract landscape.png" 
image bedroom = "bg/Bedroom.png"
image dream = "bg/mountain_dream.png"
