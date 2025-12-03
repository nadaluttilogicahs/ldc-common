#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path
import sys
import os

@dataclass
class Paths:
    work_dir: Path
    work_dir_name: str
    root_dir: Path
    rollback_dir: Path
    download_dir: Path
    usb_dir: Path
    certs_dir: Path
    dev_info_dir: Path
    db_set: Path
    db_rtd: Path
    db_arc_dir: Path
    db_lan: Path
    db_prg: Path

def _compute_paths() -> Paths:
    if getattr(sys, "frozen", False):
        exe_folder = Path(sys.executable).parent
    else:
        exe_folder = Path(__file__).resolve().parent

    work_dir = exe_folder.parent
    root_dir = work_dir.parent

    return Paths(
        work_dir=work_dir,
        work_dir_name=work_dir.name,
        root_dir=root_dir,
        rollback_dir=root_dir / "rollback",
        download_dir=Path("/opt/updates/download"),
        usb_dir=Path("/opt/updates/usb"),
        certs_dir=Path("/opt/aws-iot/certs"),
        dev_info_dir=Path("/opt/aws-iot/device-info"),
        db_set=Path("/data/settings.db"),
        db_rtd=Path("/data/rtd.db"),
        db_arc_dir=Path("/data/"),
        db_lan=Path("/data/language.db"),
        db_prg=Path("/data/prg.db"),
    )

PATHS = _compute_paths()


# if getattr(sys, 'frozen', False):
#     # Se compilato con PyInstaller, sys.executable è il percorso dell'eseguibile.
#     exe_folder = os.path.dirname(sys.executable)
# else:
#     # Se eseguito normalmente, usa __file__.
#     exe_folder = os.path.dirname(os.path.abspath(__file__))

# work_dir = os.path.dirname(exe_folder)      # ex. "/home/lg58/LDC-100"
# work_dir_name = os.path.basename(work_dir)  # ex. "LDC-100"
# root_dir = os.path.dirname(work_dir)        # ex. "/home/lg58"
# rollback_dir = f'{root_dir}/rollback'       # ex. "/home/lg58/rollback"
# download_dir = "/opt/updates/download"
# usb_dir = "/opt/updates/usb"


# certs_dir = "/opt/aws-iot/certs"
# dev_info_dir = "/opt/aws-iot/device-info"


# DB_SET_D = "/data/settings.db"  # r"/home/lg58/LDC-100/data/settings.db"
# DB_RTD_D = "/data/rtd.db"       # r"/home/lg58/LDC-100/data/rtd.db"
# DB_ARC_D = "/data/"             # r"/home/lg58/LDC-100/data/"

# DB_LAN_D = "/data/language.db"  # r"/home/lg58/LDC-100/data/language.db"
# DB_PRG_D = "/data/prg.db"       # r"/home/lg58/LDC-100/data/prg.db"