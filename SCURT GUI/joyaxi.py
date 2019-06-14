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