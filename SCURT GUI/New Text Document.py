def events(self):
    self.updated = False
    action = None

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game(self)
        # keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                quit_game(self)
            if event.key == pg.K_DOWN:
                action = 'down'
            if event.key == pg.K_UP:
                action = 'up'
            if event.key == pg.K_RETURN:
                action = 'enter'
        # mouse
        if event.type == pg.MOUSEMOTION:
            self.mousex, self.mousey = pg.mouse.get_pos()
            for i in range(len(self.menu_rects.items())):
                if self.menu_rects[i].collidepoint(self.mousex, self.mousey):
                    self.menu['selected_option'] = i
                    self.updated = True
                    break
        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(len(self.menu_rects.items())):
                if self.menu_rects[i].collidepoint(self.mousex, self.mousey):
                    action = 'enter'
                    break
        # joystick
        if event.type == pg.JOYBUTTONDOWN:
            if event.button == J_BUTTONS['A']:
                action = 'enter'
        if event.type == pg.JOYAXISMOTION:
            if event.dict['axis'] == 1:
                if time.time() >= self.last_axis_motion + 0.3:
                    if event.dict['value'] < -JOYSTICK_THRESHOLD:
                        action = 'up'
                        self.last_axis_motion = time.time()
                    elif event.dict['value'] > JOYSTICK_THRESHOLD:
                        action = 'down'
                        self.last_axis_motion = time.time()

    if action == 'down':
        self.menu["selected_option"] += 1
        self.menu["selected_option"] %= len(self.menu["options"])
        self.updated = True
    elif action == 'up':
        self.menu["selected_option"] -= 1
        self.menu["selected_option"] %= len(self.menu["options"])
        self.updated = True
    elif action == 'enter':
        self.menu["options"][self.menu["selected_option"]]["func"](self)
