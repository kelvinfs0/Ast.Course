import sys
import random
import math

import pygame


def clamp(v, a, b):
    return max(a, min(b, v))


def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("小球小游戏")
    clock = pygame.time.Clock()

    # 玩家小球
    player = {
        'x': WIDTH // 2,
        'y': HEIGHT // 2,
        'r': 16,
        'speed': 5,
        'color': (50, 150, 255),
    }

    # 目标小球（吃到得分并重生）
    def spawn_target():
        margin = 20
        return {
            'x': random.randint(margin, WIDTH - margin),
            'y': random.randint(margin, HEIGHT - margin),
            'r': 10,
            'color': (255, 90, 90),
        }

    target = spawn_target()
    score = 0

    font = pygame.font.SysFont(None, 28)

    instructions = [
        "方向键移动小球",
        "按 Esc 或关闭窗口退出",
        "吃到红球得分，得分会刷新红球位置",
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1

        # 归一化移动，避免对角线加速
        if dx != 0 or dy != 0:
            length = math.hypot(dx, dy)
            dx = dx / length
            dy = dy / length

        player['x'] += dx * player['speed']
        player['y'] += dy * player['speed']
        player['x'] = clamp(player['x'], player['r'], WIDTH - player['r'])
        player['y'] = clamp(player['y'], player['r'], HEIGHT - player['r'])

        # 碰撞检测
        dist = math.hypot(player['x'] - target['x'], player['y'] - target['y'])
        if dist <= player['r'] + target['r']:
            score += 1
            target = spawn_target()

        # 绘制
        screen.fill((30, 30, 30))
        # 目标
        pygame.draw.circle(screen, target['color'], (int(target['x']), int(target['y'])), target['r'])
        # 玩家
        pygame.draw.circle(screen, player['color'], (int(player['x']), int(player['y'])), player['r'])

        # UI
        score_surf = font.render(f"得分: {score}", True, (240, 240, 240))
        screen.blit(score_surf, (10, 10))
        for i, t in enumerate(instructions):
            surf = font.render(t, True, (200, 200, 200))
            screen.blit(surf, (10, 40 + i * 22))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


if __name__ == '__main__':
    main()
