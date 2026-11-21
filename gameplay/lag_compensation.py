import math


def sample_hitbox(frames, t):
    """按时间采样 hitbox。

    回滚时不能只取当前 hitbox，而是在历史帧中找到时间戳不晚于 t 的
    最新一帧；t 早于首帧则取首帧，晚于末帧则取末帧。
    """
    if not frames:
        return None
    ordered = sorted(frames, key=lambda f: f[0])
    sampled = ordered[0]
    for frame in ordered:
        if frame[0] <= t:
            sampled = frame
        else:
            break
    return sampled[1]


def align_snapshot(client_time, lag):
    """快照对齐。

    插值位置必须对齐快照时间戳：服务器回放时间 = 客户端时间 - 网络延迟，
    不能出现负时间。
    """
    return max(0, client_time - lag)


def prediction_authority(is_prediction):
    """预测权威性。

    客户端预测只用于本地表现，永远不作为命中事实上报，服务器不承认
    任何预测结果。
    """
    return False


def fire_interval(tick_rate, per_tick):
    """射速间隔。

    射速由服务器 tick 驱动，与客户端帧率无关：
    间隔（秒）= 每次开火占用 tick 数 / tick 速率，保留 6 位小数。
    """
    return round(per_tick / tick_rate, 6)


def recoil_authoritative(local, server):
    """后坐力权威。

    后坐力只认服务器计算结果，客户端本地那一套仅用于表现，不参与弹道。
    """
    return server


def pellet_seed(server_seed):
    """pellet 种子。

    霰弹每个 pellet 的随机种子由服务器统一下发，客户端与服务器用同一
    种子，保证两边命中数一致。
    """
    return server_seed


def resolve_damage(damage, shield):
    """护盾结算。

    固定结算顺序：先扣护盾，护盾被打穿后溢出的伤害才进入血量。
    返回 (进入血量的伤害, 剩余护盾值)。
    """
    absorbed = min(damage, shield)
    remaining_shield = shield - absorbed
    health_damage = damage - absorbed
    return (health_damage, remaining_shield)


def swept_hit(start, end, point, radius):
    """扫掠命中。

    高速投射物对 start->end 的整个线段做扫掠，而不是只测两个端点：
    目标点到线段的最短距离不超过判定半径即命中（可穿过薄目标）。
    """
    sx, sy = start
    ex, ey = end
    px, py = point
    dx, dy = ex - sx, ey - sy
    length_sq = dx * dx + dy * dy
    if length_sq == 0.0:
        closest_x, closest_y = sx, sy
    else:
        u = ((px - sx) * dx + (py - sy) * dy) / length_sq
        u = max(0.0, min(1.0, u))
        closest_x = sx + u * dx
        closest_y = sy + u * dy
    dist_sq = (px - closest_x) ** 2 + (py - closest_y) ** 2
    return dist_sq <= radius * radius


def dedupe_hits(ids):
    """命中去重。

    每发子弹带唯一序号，丢包重传导致的重复上报按序号去重，
    返回去重后的命中数量，防止伤害翻倍。
    """
    return len(set(ids))


def rollback_window(max_lag, margin):
    """回滚窗口。

    回滚窗口按延迟上限收紧，取延迟上限与允许余量中的较小值，
    避免静止靶被长时间追着打。
    """
    return min(max_lag, margin)


def tick_for_time(time, tick_rate):
    """时间转 tick。"""
    return round(time * tick_rate)


def interpolate(a, b, t):
    """插值。"""
    return a + (b - a) * t


def hitbox_scale(scale, box):
    """判定盒缩放。"""
    return tuple(dim * scale for dim in box)


def authoritative_position(client, server):
    """服务器位置。

    位置以服务器快照为准，客户端预测位置在判定时被服务器值覆盖。
    """
    return server


def lag_id(seed, index):
    """延迟补偿 id。"""
    return f"{seed}:{index}"
