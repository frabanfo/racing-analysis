from src.data_load import load_fastf1_session, get_fastest_lap_telemetry
from src.viz import plot_speed_distance, plot_throttle_distance, plot_brakes_distance
import matplotlib
from pathlib import Path
matplotlib.use('tkagg')   

def main():
    year = 2024
    gp = "Monaco"
    driver = "VER"
    session = load_fastf1_session(year, gp, "R")
    tel = get_fastest_lap_telemetry(session, driver)

    fig = plot_speed_distance(tel, title=f"{driver} fastest lap {gp} {year}")
    fig1 = plot_throttle_distance(tel, title=f"{driver} throttle in fastest lap {gp} {year}")
    fig2 = plot_brakes_distance(tel, title=f"{driver} brakes in fastest lap {gp} {year}")

    out_path = Path.cwd() / "data" / "plots"
    out_path.mkdir(parents=True, exist_ok=True)
    
    file = out_path / "ver_fastest_lap.png"
    file1 = out_path / "ver_throttle_lap.png"
    file2 = out_path / "ver_brakes_lap.png"

    fig.savefig(file, dpi=150)
    fig1.savefig(file1, dpi=150)
    fig2.savefig(file2, dpi=150)
    print(f"Saved plot to {file}")

if __name__ == "__main__":
    main()