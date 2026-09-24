# 🎀 PetalPop — Python Flask Photobooth

A pink, mobile-friendly photobooth website powered by **Python Flask + Pillow**, with browser-based HTML/CSS/JavaScript camera controls. Photos remain in the browser until the user clicks **Download**, when the final decorated PNG is sent to the Python server for 300-DPI PNG processing; the server does **not** save images.

## Run in VS Code (Windows)

1. Install Python 3.10+ and open this folder in VS Code.
2. Open the VS Code terminal in this folder.
3. Install dependencies: `py -m pip install -r requirements.txt`
4. Start the server: `py server.py`
5. Open **http://localhost:5000** in Chrome or Edge and allow camera access.

On macOS/Linux use `python3 -m pip install -r requirements.txt` and `python3 server.py`.

You can also double-click `run_windows.bat` after installing Python; it installs requirements and starts Flask.

## Open on a phone

Deploy the **whole Flask project** to a Python-compatible HTTPS host. For example, a host supporting Flask/WSGI can run `gunicorn server:app` (install `gunicorn` there). Your phone can then open its HTTPS URL and allow camera access. **Do not** use ordinary HTTP LAN URLs (`http://192.168...`) for phone camera testing; most mobile browsers require HTTPS. Camera permission is requested when the shooting page is opened.

## Features

- Welcome screen; eight layouts (1×4, 2×4, 2×3, 1×3, 2×2, 3×3, 1×2, 3×2).
- Customizable frame color, spacing and caption.
- Manual shutter or 10-second timer; front/back camera switch where supported.
- Retakes proportional to layout size; choose photos per print slot.
- Eight filters, movable/resizable emoji stickers.
- Download PNG through the Python Pillow endpoint with 300-DPI metadata; browser print dialog.

## Important notes

The Python backend serves the website and processes the final PNG. The browser must use JavaScript for phone camera access, stickers, preview and print dialog. The site does not automatically connect to a physical printer; a configured printer and browser print permission are required. 300-DPI metadata does not guarantee a particular physical print size; set paper size and scale in your print dialog. Google fonts require internet, but fallback fonts work offline.
\n## Rear flash and automatic timer\nOn supported rear cameras, tap **Flash off** to enable the hardware torch. Hardware flash depends on the phone, browser and camera capabilities; unsupported devices show Flash unavailable. With the 3-, 5- or 10-second timer, one tap of **Take photo** automatically captures all remaining slots, counting down before each photo. Manual mode takes one photo per tap.\n
### Flash On / Off
Choose **Off** or **On** from the Flash dropdown in the camera. It is available for supported rear cameras only. Some phones and browsers do not expose hardware torch control; on those devices the selector is disabled.

## Flash on both cameras
Flash On/Off is available for the front camera as a white **screen flash** during each capture. Web browsers cannot activate a hardware LED on the front camera. On the back camera, the selector activates the real LED torch when supported by the phone/browser; otherwise it is disabled. Selfie screen flash brightens the preview but may not illuminate the person's face as strongly as a full-screen white display. Timer automatic capture still works.
