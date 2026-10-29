"""google.colab.files 대체: 로컬 파일은 이미 접근 가능하므로 경로 기반으로 동작."""
import os


def upload(*paths):
    """Colab처럼 {파일명: bytes} 딕셔너리를 반환한다.

    인자를 주면 해당 경로의 파일을 읽고, 없으면 파일명을 입력받는다.
    """
    if not paths:
        names = input("업로드할 파일 경로(여러 개는 쉼표로 구분): ")
        paths = [p.strip().strip('"') for p in names.split(",") if p.strip()]
    result = {}
    for p in paths:
        with open(p, "rb") as f:
            result[os.path.basename(p)] = f.read()
    return result


def download(filename):
    """로컬에서는 다운로드가 필요 없으므로 파일 위치만 알려준다."""
    print(f"[colab_shim] 파일은 로컬에 있습니다: {os.path.abspath(filename)}")
