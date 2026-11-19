from pathlib import Path

from llama_cpp import Llama

from linea.cli import _Silencio

for ruta in sorted(Path("/modelos").glob("*.gguf")):
    with _Silencio():
        m = Llama(model_path=str(ruta), vocab_only=True, verbose=False)
    print(f"{ruta.name:38s} {str(m.metadata.get('general.name')):28s} licencia={m.metadata.get('general.license', 'NO LO DICE')}")
