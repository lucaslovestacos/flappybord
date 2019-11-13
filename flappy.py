app.stepsPerSecond = 60
app.background = gradient('lightBlue', 'white', start='bottom')

bg = Image('https://github.com/lucaslovestacos/flappybord/blob/master/birdbg4.png?raw=true', 0, 0)

bird = Image('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/sprites/yellowbird-midflap.png', 190, 200)

bird.Speed = 0
app.score = 0
app.die = 1

app.badDeathCounter = 0

cheatbutton = Rect(0, 0, 50, 20, fill=rgb(78, 192, 202))

pipe1 = Image('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/sprites/pipe-green.png', 400, -150, rotateAngle=180)
pipe2 = Image('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/sprites/pipe-green.png', 400, pipe1.centerY+275, align='top')

ground = Image('https://github.com/sourabhv/FlapPyBird/blob/master/assets/sprites/base.png?raw=true', 0, 400-50, width=430)

name = app.getTextInput("What's your name?")

namelabel = Label(name, 200, 375, fill='white', border='black', borderWidth=1, bold=True, size=30)

spacelabel = Label('Press R or Click to try again!', 200, 250, size=28, fill='white', border='black', bold=True, visible=False, borderWidth=1)
winlabel = Label('You Died!', 200, 200, size=70, border='black', fill='white', bold=True, visible=False)
scorelabel = Label(app.score, 200, 50, fill='white', border='black', bold=True, size=50)
velocitylabel = Label(bird.Speed, 50, 50, visible=False)
positionlabel = Label(bird.centerY, 50, 100, visible=False)

app.scorecheck = 0

pointsound = Sound('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/audio/point.ogg')
jumpsound = Sound('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/audio/wing.ogg')
losesound = Sound('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/audio/hit.ogg')
songsound = Sound("https://github.com/lucaslovestacos/flappybord/blob/master/'.wav?raw=true")

startlabel = Group(Label('Press R or Click to Start!', 200, 250, size=25, border='black', fill='white', bold=True, borderWidth=1), Label('Use Up, Space, or Click to jump!', 200, 300, size=25, border='black', fill='white', bold=True, borderWidth=1))

app.music = 1
app.sfx = 1

musicon = Image('https://github.com/lucaslovestacos/flappybord/blob/master/flappy%20music.png?raw=true', 350, 10)
sfxon = Image('https://github.com/lucaslovestacos/flappybord/blob/master/flappy%20sfx.png?raw=true', 350, 40)

musiccross = Image('https://github.com/lucaslovestacos/flappybord/blob/master/flappy%20music%20off.png?raw=true', 350, 10, visible=False)
sfxcross = Image('https://github.com/lucaslovestacos/flappybord/blob/master/flappy%20sfx%20off.png?raw=true', 350, 40, visible=False)

highscoretext = Label('Your Highscore:', 200, 100, size=25, fill='white', border='black', borderWidth=1, bold=True, visible=False)
highscorelabel = Label(0, 200, 140, size=30,fill='white', border='black', borderWidth=1, bold=True, visible=False)

app.highscore = 0

#cheatcode checks
app.invincibird = 0
app.superjump = 0
app.debugcheck = 0
app.speedypipes = 0
app.inverse = 0
app.antigravity = 0
app.supergravity = 0

def jump():
    if (app.sfx == 1):
        if (app.die == 0):
            jumpsound.play(restart=True)
    else:
        pass
    if (app.superjump == 0):
        if (app.inverse == 0):
            bird.Speed = -8
        else:
            bird.Speed = 8
    else:
        if (app.inverse == 0):
            bird.Speed = -16
        else:
            bird.Speed = 16

def cheatCall(message):
    
    cheat = app.getTextInput(message)
    scorelabel.fill='red'
    if (cheat == 'invincibird'):
        app.invincibird = 1
    elif (cheat == 'superjump'):
        app.superjump = 1
    elif (cheat == 'debug'):
        app.debugcheck = 1
    elif (cheat == 'speedypipes'):
        app.speedypipes = 1
    elif (cheat == 'inverse'):
        if (app.inverse == 0):
            app.inverse = 1
        else:
            app.inverse = 0
    elif (cheat == 'resetbird'):
        bird.centerY = 200
        bird.Speed = 0
    elif (cheat == 'antigravity'):
        app.supergravity = 0
        app.antigravity = 1
    elif (cheat == 'supergravity'):
        app.supergravity = 1
        app.antigravity = 0
    elif (cheat == 'clear'):
        app.invincibird = 0
        app.superjump = 0
        app.debugcheck = 0
        app.speedypipes = 0
        app.inverse = 0
        app.antigravity = 0
        app.supergravity = 0
    elif (cheat == 'kill'):
        lose()
    elif (cheat == ''):
        pass
    else:
        cheatCall('Invalid Cheat Code:')
        
def start():
    
    startlabel.visible = False
    
    #cheatcode checks
    app.invincibird = 0
    app.superjump = 0
    app.debugcheck = 0
    app.speedypipes = 0
    app.inverse = 0
    app.antigravity = 0
    app.supergravity = 0
    
    bird.Speed = 0
    app.score = 0
    app.die = 0
    
    highscoretext.visible=False
    highscorelabel.visible=False
    
    app.scorecheck = 0
    
    bird.centerY = 200
    pipe1.centerX = 400
    pipe2.centerX = 400
    
    winlabel.visible = False
    spacelabel.visible = False
    
    scorelabel.fill = 'white'
    
    if (app.music == 0):
        pass
    else:
        songsound.play(restart=True, loop=True)

pass

def lose():
    if (app.sfx == 1):
        losesound.play()
    spacelabel.visible = True
    
    if (app.score <= 10):
        app.badDeathCounter += 1
        print(app.badDeathCounter)
    else:
        app.badDeathCounter = 0
        print(app.badDeathCounter)
    
    if (app.badDeathCounter > 9):
        winlabel.value = 'You Suck!'
        winlabel.visible = True
    else:
        winlabel.value = 'You Died!'
        winlabel.visible = True
    
    app.die = 1
    songsound.pause()
    
    highscoretext.visible=True
    highscorelabel.visible=True

pass

def onStep():
    
    bird.rotateAngle = bird.Speed*4
    
    scorelabel.value = app.score
    
    if (app.die == 0):
        if (app.speedypipes == 0):
            bg.centerX -= 1 + (app.score*.02)
            ground.centerX -= 2.5 + (app.score*.02) 
            pipe1.centerX -= 2.5 + (app.score*.02)
            pipe2.centerX -= 2.5 + (app.score*.02)
        else:
            bg.centerX -= 2 + (app.score*.04)
            ground.centerX -= 5 + (app.score*.04)
            pipe1.centerX -= 5 + (app.score*.04)
            pipe2.centerX -= 5 + (app.score*.04)
        
        if (bird.hitsShape(pipe1) or bird.hitsShape(pipe2) or bird.centerY < 0 or ground.hitsShape(bird)):
            if (app.invincibird == 0):
                lose()
            else:
                pass
        
        namelabel.value = name
        
        if (app.inverse == 0):
            if (app.antigravity == 0 and app.supergravity == 0):
                bird.Speed +=.5
            elif (app.antigravity == 1):
                bird.Speed += .1
            else:
                bird.Speed += 1
        else:
            if (app.antigravity == 0 and app.supergravity == 0):
                bird.Speed -=.5
            elif (app.antigravity == 1):
                bird.Speed -= .1
            else:
                bird.Speed -= 1
    
        bird.centerY += bird.Speed
        
        if (pipe1.centerX < -26):
            
            pipe1.centerX = 426
            pipe2.centerX = 426
            
            app.scorecheck = 0
            
            pipe1.top = randrange(-275, -120)
            pipe2.top = pipe1.centerY+275
            
        if (pipe1.centerX < 200):
            if (app.scorecheck == 0):
                if (app.sfx == 1): 
                    pointsound.play()
                app.score += 1
                app.scorecheck = 1
                if (app.score > app.highscore):
                    if (scorelabel.fill != 'red'):
                        app.highscore = app.score
                        highscorelabel.value = app.highscore
        
        if (app.debugcheck == 1):
            velocitylabel.visible = True
            velocitylabel.value = rounded(bird.Speed)
            positionlabel.visible = True
            positionlabel.value = rounded(bird.centerY)
            
        if (ground.left <= -30):
            ground.left = 0
            
        if (bg.left <= -416):
            bg.left = 0
            
    else:
        pass

def onKeyPress(key):
    
    if (key == 'up' or key == 'space'):
        jump()
    
    if (key == 'r'):
        if (app.die == 1):
            start()
    
    if (key == 'c'):
        cheatCall('Input Cheat Code:')

def onMousePress(mouseX, mouseY):
    if ((musicon.contains(mouseX, mouseY) or sfxon.contains(mouseX, mouseY)) != True):
        jump()
    
    if (app.die == 1):
        if ((musicon.contains(mouseX, mouseY) or sfxon.contains(mouseX, mouseY)) != True):
            start()
        
    if (cheatbutton.hits(mouseX, mouseY)):
        cheatCall('Input Cheat Code:')
    
    if (musicon.contains(mouseX, mouseY)):
        if (app.music == 1):
            musiccross.visible = True
            songsound.pause()
            app.music = 0
        else:
            musiccross.visible = False
            songsound.play(loop=True)
            app.music = 1
    elif (sfxon.contains(mouseX, mouseY)):
        if (app.sfx == 1):
            sfxcross.visible = True
            app.sfx = 0
        else:
            sfxcross.visible = False
            app.sfx = 1
