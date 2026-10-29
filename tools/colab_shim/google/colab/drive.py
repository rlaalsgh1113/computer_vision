"""google.colab.drive 대체: 마운트 경로에 로컬 폴더를 연결."""
import os


def mount(mountpoint, force_remount=False, **kwargs):
    """마운트 대신 폴더만 만든다. Colab 경로(/content/drive)는 현재 폴더 아래로 바꾼다."""
    path = mountpoint
    if path.startswith("/content"):
        path = os.path.join(os.getcwd(), path.lstrip("/"))
    os.makedirs(path, exist_ok=True)
    print(f"[colab_shim] Google Drive 마운트는 로컬에서 지원되지 않습니다. 로컬 폴더 사용: {path}")


def flush_and_unmount(*args, **kwargs):
    pass
