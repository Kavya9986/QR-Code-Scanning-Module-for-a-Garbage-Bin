# Project Title: QR Code Scanning Module for a Garbage Bin

This project is a Python-based QR code scanning module designed to encourage users to participate in waste management by incentivizing them with rewards. The system allows users to scan their unique QR codes using a camera, and in return, they earn "coins" for their contributions.

## Requirements

- Python
- OpenCV (`cv2` module)
- PyZbar (`pyzbar` module)
- NumPy
- CSV file: `USERID.csv`

## How It Works

1. Users run the script (`p9.py`) to start the QR code scanning module.
2. The camera is activated, and users present their QR codes in front of it.
3. The system decodes the QR code to extract the user's ID and displays it on the screen with the corresponding "coins" earned.
4. Users can press `Ctrl-M` to log their rewards in the `USERID.csv` file.
5. Additionally, there's a graphical user interface (GUI) application that allows users to check their reward points by entering their USER ID.

## Getting Started

1. Clone the repository to your local machine.
2. Ensure you have the necessary Python libraries (`cv2`, `pyzbar`, NumPy).
3. Run the main script (`p9.py`) to start the QR code scanning module.
4. Show your QR code in front of the camera until your user ID and coins earned appear on the screen.
5. Press `Ctrl-M` to log your rewards.
6. To check your reward points later, use the graphical user interface (`GUI.py`) application.

## User Guide

1. Run the script (`p9.py`) and activate your camera.
2. Show your unique QR code to the camera until your user ID and coins appear.
3. Press `Ctrl-M` to log your rewards.
4. To check your reward points later, use the `GUI.py` application and enter your USER ID.
5. Note: The log of user activity is maintained in the `USERID.csv` file.

## Author

This project is developed by Kavya S Jain.

Feel free to contribute to the project or report any issues you encounter.

Happy waste management! ♻️🌍

_*Note: Ensure you have the necessary permissions and access to run the camera and read/write files on your system.*_

