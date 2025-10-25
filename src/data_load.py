import fastf1
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "cache"
CACHE_DIR.mkdir(exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))

def load_fastf1_session(year:int, grand_prix: str, session: str):
    session = fastf1.get_session(year, grand_prix, session)
    session.load()
    return session

def get_fastest_lap_telemetry(session, driver_code: str):
    lap = session.laps.pick_driver(driver_code).pick_fastest()
    telemetry = lap.get_car_data().add_distance()
    return telemetry