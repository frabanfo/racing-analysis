from src.data_load import load_fastf1_session, get_fastest_lap_telemetry
from src.viz import plot_speed_distance

def main():
    year = 2024
    gp = "Monaco"
    driver = "VER"

    print(f"Loading session {year} {gp} ...")
    session = load_fastf1_session(year, gp, "R")
    print("Session loaded.")
    tel = get_fastest_lap_telemetry(session, driver)
    print("Telemetry loaded. Plotting...")
    plt = plot_speed_distance(tel, title=f"{driver} fastest lap {gp} {year}")
    plt.show()

if __name__ == "__main__":
    main()