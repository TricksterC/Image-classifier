import os
import time
import cv2
from picamera2 import Picamera2


def main():
    save_dir = "dataset"
    print("Rpi Image Dataset collector!")
    class_name = input("Enter the label class name: ").strip().lower()

    if not class_name:
        print("Class name cannot be empty. Exiting :/")
        return

    target_path = os.path.join(save_dir, class_name)
    os.makedirs(target_path, exist_ok=True)

    print("\nChoose capture mode:")
    print("1. Manual capture (press SPACE to save)")
    print("2. Interval capture (automatic every X seconds)")
    mode = input("Select mode: (1 or 2): ").strip()

    interval = 1.0
    if mode == "2":
        interval = float(input("Enter time interval between shots in seconds (eg 1.5): "))

    picam2 = Picamera2()
    config = picam2.create_still_configuration(
        main={"size": (1280, 720)}
    )

    picam2.configure(config)
    picam2.start()

    time.sleep(2)

    existing = [
        f for f in os.listdir(target_path)
        if f.endswith(".jpg")
    ]
    img_counter = len(existing)

    print(f"\nSaving images to {target_path}")

    try:
        if mode == "1":
            while True:
                cmd = input(
                    "\nPress ENTER to capture "
                    "(q + ENTER to quit): "
                )

                if cmd.lower() == "q":
                    break

                frame = picam2.capture_array()
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                filename = os.path.join(
                    target_path,
                    f"{class_name}_{img_counter:04d}.jpg"
                )

                cv2.imwrite(filename, frame)
                print(f"Saved {filename}")
                img_counter += 1

        else:
            print("\nPress Ctrl + C to stop\n")

            while True:
                frame = picam2.capture_array()
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                filename = os.path.join(
                    target_path,
                    f"{class_name}_{img_counter:04d}.jpg"
                )

                cv2.imwrite(filename, frame)
                print(f"Saved {filename}")
                img_counter += 1
                time.sleep(interval)

    except KeyboardInterrupt:
        pass

    finally:
        picam2.stop()

    print(f"\nCollected {img_counter} images.")


if __name__ == "__main__":
    main()
