import cx_Freeze
executables = [cx_Freeze.Executable("game.py")]
cx_Freeze.setup(
    name="Jet Game",    # Voce pode colocar outro nome para seu jogo
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": [
                            'sounds', 'sprites'
                            # Nome do arquivo ou arquivos de imagens, sons, etc, separados por virgula
                            # Exemplo "racecar.png"
                           ]}},
    executables=executables
)