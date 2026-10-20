import argparse
import logging
import os
from pathlib import Path

import qrcode


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code for a URL.")
    parser.add_argument(
        "--url",
        default=os.getenv("QR_URL", "https://www.njit.edu"),
        help="URL to encode in the QR code",
    )
    args = parser.parse_args()

    output_dir = Path(os.getenv("QR_OUTPUT_DIR", "qr_codes"))
    log_dir = Path(os.getenv("LOG_DIR", "logs"))

    output_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_dir / "app.log", encoding="utf-8"),
        ],
    )

    try:
        image = qrcode.make(args.url)
        output_file = output_dir / "qr_code.png"
        image.save(output_file)
        logging.info("QR code generated for %s", args.url)
        logging.info("QR code saved to %s", output_file)
    except Exception:
        logging.exception("QR code generation failed")
        raise


if __name__ == "__main__":
    main()