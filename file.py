armadilhas = []
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        enemy = hero.findNearestEnemy()
        if hero.distanceTo(enemy) < 10:
            enemy = hero.findNearestEnemy()
            if enemy and hero.isReady("cleave"):
                enemies = hero.findEnemies()
                quantos = 0
                for i in enemies:
                    quantos += 1
                    if quantos <= 3:
                        hero.cleave(enemy)
                    else:
                        pass
                    break
            enemy = hero.findNearestEnemy()
            if enemy and hero.isReady("attack"):
                hero.attack(enemy)
                enemy = hero.findNearestEnemy()
            
            if enemy and hero.isReady("bash"):
                hero.bash(enemy)
                enemy = hero.findNearestEnemy()
            
            else:
                hero.shield()
        elif hero.distanceTo(enemy) < 20:
            x = hero.pos.x
            y = hero.pos.y
            
            enemyX = enemy.pos.x
            enemyY = enemy.pos.y
            
            hero.moveXY(x - (x-enemyX)/32, y - (y-enemyY)/32)
        else:
            enemy = hero.findNearestEnemy()
            for i in armadilhas:
                if i == hero.pos:
                    x = hero.pos.x
                    y = hero.pos.y
                    
                    enemyX = enemy.pos.x
                    enemyY = enemy.pos.y
                    
                    hero.moveXY(x - (x-enemyX)/64, y - (y-enemyY)/64)
                else:
                    hero.buildXY("bear-trap", hero.pos)
            armadilhas.append(hero.pos)
             
    else:
        enemy = hero.findNearestEnemy()
        for i in armadilhas:
            if i == hero.pos:
                x = hero.pos.x
                y = hero.pos.y
                enemy = hero.findNearestEnemy()
                if enemy:
                    enemyX = enemy.pos.x
                    enemyY = enemy.pos.y
                else:
                    break
                
                hero.moveXY(x - (x-enemyX)/64, y - (y-enemyY)/64)
            else:
                hero.buildXY("bear-trap", hero.pos)
            armadilhas.append(hero.pos)
