import math

def sample_hitbox(frames, t):
    """按时间采样 hitbox。"""
    raise NotImplementedError("TODO: sample_hitbox")

def align_snapshot(client_time, lag):
    """快照对齐。"""
    raise NotImplementedError("TODO: align_snapshot")

def prediction_authority(is_prediction):
    """预测权威性。"""
    raise NotImplementedError("TODO: prediction_authority")

def fire_interval(tick_rate, per_tick):
    """射速间隔。"""
    raise NotImplementedError("TODO: fire_interval")

def recoil_authoritative(local, server):
    """后坐力权威。"""
    raise NotImplementedError("TODO: recoil_authoritative")

def pellet_seed(server_seed):
    """pellet 种子。"""
    raise NotImplementedError("TODO: pellet_seed")

def resolve_damage(damage, shield):
    """护盾结算。"""
    raise NotImplementedError("TODO: resolve_damage")

def swept_hit(start, end, point, radius):
    """扫掠命中。"""
    raise NotImplementedError("TODO: swept_hit")

def dedupe_hits(ids):
    """命中去重。"""
    raise NotImplementedError("TODO: dedupe_hits")

def rollback_window(max_lag, margin):
    """回滚窗口。"""
    raise NotImplementedError("TODO: rollback_window")

def tick_for_time(time, tick_rate):
    """时间转 tick。"""
    raise NotImplementedError("TODO: tick_for_time")

def interpolate(a, b, t):
    """插值。"""
    raise NotImplementedError("TODO: interpolate")

def hitbox_scale(scale, box):
    """判定盒缩放。"""
    raise NotImplementedError("TODO: hitbox_scale")

def authoritative_position(client, server):
    """服务器位置。"""
    raise NotImplementedError("TODO: authoritative_position")

def lag_id(seed, index):
    """延迟补偿 id。"""
    raise NotImplementedError("TODO: lag_id")
