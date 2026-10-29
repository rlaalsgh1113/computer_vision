"""google.colab.output 대체: 로컬 Jupyter는 커스텀 위젯을 기본 지원하므로 아무 동작도 하지 않음."""


def enable_custom_widget_manager():
    pass


def disable_custom_widget_manager():
    pass


def clear(*args, **kwargs):
    from IPython.display import clear_output
    clear_output()
