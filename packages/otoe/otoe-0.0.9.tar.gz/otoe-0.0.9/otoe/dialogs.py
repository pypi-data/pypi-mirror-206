from rich import print


def confirmation_dialog_factory(text, positive='yes', negative='no'):
    def dialog(**kwargs) -> bool:
        print(text.format(**kwargs))
        print(f'[{positive}/{negative}]')
        confirm = input()
        if confirm == positive:
            return True
        return False

    return dialog


override_target_dir_dialog = confirmation_dialog_factory(
    'Directory "{dir}" already exists. Do you want to override it?'
)


ensure_ready = confirmation_dialog_factory(
    'Make sure you have made a backup of your notes. Do you want to continue?'
)
