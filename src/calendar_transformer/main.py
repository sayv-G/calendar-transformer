import sys

from .calendar_io import load_calendar, save_calendar
from .config import load_yaml
from .processor import transform_calendar


def main():
    if len(sys.argv) != 3:
        print("Verwendung:")
        print("python main.py <input.ics> <output.ics>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    subjects = load_yaml("subjects.yaml")
    teachers = load_yaml("teachers.yaml")

    calendar = load_calendar(input_file)

    count = transform_calendar(
        calendar,
        subjects,
        teachers,
    )

    save_calendar(calendar, output_file)

    print(f"✅ {count} Termine verarbeitet.")
    print(f"💾 Gespeichert: {output_file}")


if __name__ == "__main__":
    main()